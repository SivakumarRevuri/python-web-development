from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

posts = [
    {
        "title": "python",
        "author": 'Sivakumar',
        'published': datetime.date.today()
    },
    {
        "title": "Django",
        "author": 'Revanuru',
        'published': datetime.date(day=21, month=12, year=2023)
    },
    {
        "title": "MongoDB",
        "author": 'Moksha',
        'published': datetime.date.today()
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True, port=5555)
    