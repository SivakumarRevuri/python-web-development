#building url dynamically
#variable rules and url building
from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return 'Welcome to the Jungle!'

@app.route('/login')
def checkAuthentication():
    return 'You got access'

#creating dynamic URL
@app.route('/grade/<int:score>')
def gradeCheck(score):
    return 'You are passed! with score of: '+str(score)

if __name__ == '__main__':
    app.run(debug=True, port=9999)