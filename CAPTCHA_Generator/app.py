import random
import string
from flask import Flask,session,render_template,request
from PIL import Image,ImageDraw,ImageFont

app=Flask(__name__)
app.secret_key = "secret_key"

message="LOGIN SUCCESSFUL"
def generate_captcha():
    random_text = ''.join(random.choices(string.ascii_letters+string.digits,k=6))
    session["captcha_text"]=random_text

    image=Image.new('RGB',(150,70),'white')  #Image Creation
    draw=ImageDraw.Draw(image)  #Draw object
    #Draw captcha text on image
    # Load font
    font_size = random.randint(25, 35)

    font = ImageFont.truetype(
        "arial.ttf",
        font_size
    )

    # Draw characters with spacing
    x_position = 10

    for char in random_text:

        y_position = random.randint(5, 15)

        draw.text(
            (x_position, y_position),
            char,
            font=font,
            fill=(
                random.randint(0,150),
                random.randint(0,150),
                random.randint(0,150)
            )
        )

        x_position += 25

    #Adding Noise
    #Add noise points
    for _ in range(100):
        x=random.randint(0,150)
        y=random.randint(0,70)
        draw.point((x,y),fill='black')
    #add noise lines
    for _ in range(random.randint(0,3)):
        x1=random.randint(0,150)
        y1=random.randint(0,70)
        x2=random.randint(0,150)
        y2=random.randint(0,70)
        draw.line((x1,y1,x2,y2),fill='black')
    

    image.save("static/captcha.png")

@app.route("/",methods=["GET","POST"])
def index():
    message=""
    if request.method=="POST":
        user_input=request.form["captcha"]
        stored_captcha=session.get("captcha_text")
        username=request.form["username"]
        if(user_input==stored_captcha):
            message="LOGIN SUCCESSFUL. HI "+username
        else:
            message="WRONG CAPTCHA!!! PLEASE ENTER AGAIN"
    generate_captcha()
    return render_template("index.html",message=message)

@app.route("/refresh_captcha")
def refresh_captcha():
    generate_captcha()
    return "done"

if __name__ =="__main__":
    app.run(debug=True)
