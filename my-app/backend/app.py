from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from classify import *
import os
from werkzeug.utils import secure_filename

api = Flask(__name__)
CORS(api)

upload_folder = os.path.join('static', 'uploads')

api.config['UPLOAD'] = upload_folder

@api.route('/upload/', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename("tempFile.png")
    file.save(filename)
    # Get path of the file
    print("filename: ", filename)
    filePath = os.path.join(os.getcwd(), filename)
    print("filePath: ", filePath)
    result = classify(filePath)
    # Do something with the file variable
    return jsonify({"success": True, "result": str(result)})


if __name__ == "__main__":
    api.run(debug=True)