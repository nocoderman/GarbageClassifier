from flask import Flask
from classify import *

api = Flask(__name__)
@api.route('/main')
def main_page():
    response_body={
        "name" : temp()
    }
    return response_body

if __name__ == "__main__":
    api.run(debug=True)