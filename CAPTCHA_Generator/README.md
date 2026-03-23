# CAPTCHA Generator (Flask)

A Flask-based web application that generates CAPTCHA images and validates user input during login to prevent automated access.

## Overview

This project demonstrates how CAPTCHA can be implemented in a web application using Python and Flask.
A random CAPTCHA image is generated using the Pillow library, displayed to the user, and validated using Flask sessions.

## Features

* Random CAPTCHA image generation
* CAPTCHA refresh functionality
* Session-based CAPTCHA validation
* Login form interface
* CAPTCHA noise and distortion for security
* Simple and clean user interface

## Technologies Used

* Python
* Flask
* Pillow (PIL)
* HTML
* CSS
* JavaScript

## How to Run the Project

Install required packages:

```
pip install -r requirements.txt
```

Run the Flask application:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

## Purpose of the Project

This project was developed to demonstrate CAPTCHA generation and validation using Flask.
It can be used as a learning example for implementing basic security features in web applications.
