from flask import Flask, flash, request, redirect, url_for
import sys
app = Flask(__name__)
 
@app.route("/")
def hello():
	print(request, file=sys.stderr)
	print(request.data, file=sys.stderr)
	return "Hello World!"
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True)