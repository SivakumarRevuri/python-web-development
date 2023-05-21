from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return '<h1>Welcome to Home page </h1>'

@app.route('/about')
def about_page():
    return '<h1>About page goes here.</h1>'

if __name__ == '__main__':
    app.run(debug=True) # enabling the debug mode.
    