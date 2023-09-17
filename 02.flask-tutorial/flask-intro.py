from flask import Flask

app = Flask(__name__)#this is need, so Flask knows where it can look for resources 

@app.route("/hello")#to tell Flask, what url should trigger
def hello_world():
    return "<h1><p style='color:red'>Hello, World! congrats it's working</p></h1>"
"""
#run flask application ("py -m flask --app test run")
#here script: file_name.
#to enable debug mode, use the "--debug" option
#py -m flask --app script --debug run
Warning:
    The debugger allows executing arbitrary Python code from the browser. 
    It is protected by a pin, but still represents a major security risk. 
    Do not run the development server or debugger in a production environment.
"""

#HTML Escaping

from markupsafe import escape

@app.route('/<name>') #it takes the input from URL
def wish(name):
    return f'hello, {escape(name)}!'