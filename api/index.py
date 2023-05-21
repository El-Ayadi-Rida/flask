from flask import Flask , render_template , Response, request
import cv2

app = Flask(__name__)

camera=cv2.VideoCapture(0)




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about')
def about():
    return 'About'