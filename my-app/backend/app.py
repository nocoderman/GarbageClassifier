from flask import Flask, request
from flask_cors import CORS
from classify import *

api = Flask(__name__)
CORS(api)

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