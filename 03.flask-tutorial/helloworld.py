from flask import Flask
app = Flask(__name__) 

@app.route('/')
def welcome():
    return 'Hello World!'

@app.route('/login')
def checkAuthentication():
    return 'You got access'

if __name__ == '__main__':
    app.run(port=1234,debug=True) #it run's the web application, it can various parameters
