# ---- Flask Hello World ---- #
# import the Flask class from the flask package
from flask import Flask
from flask import abort, request
# create the application object
app = Flask(__name__)
# use the decorator pattern to
# link the view function to a url
@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ['172.16.102.117','127.0.0.1']:
        abort(403)  # Forbidden
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "hello   world"
# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='0.0.0.0')
