from flask import Flask, request, render_template
from flask_cors import CORS
from classify import *
import os
from werkzeug.utils import secure_filename


api = Flask(__name__)
CORS(api)

upload_folder = os.path.join('static', 'uploads')

api.config['UPLOAD'] = upload_folder

@api.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    image_bytes = file.read()
    return image_bytes
    


@api.route('/main')
def main_page():
    result = classify("./banana.png")
    # ../public/banana.png
    response_body={
        "name" : str(result)
    }
    return response_body

if __name__ == "__main__":
    api.run(debug=True)