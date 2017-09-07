from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1> Hello World! How are yoiu doing today? </h1>" 

if __name__ == "__main__":
    application.run()
