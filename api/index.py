from flask import Flask , render_template
import cv2

app = Flask(__name__)






@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about')
def about():
    return 'About'