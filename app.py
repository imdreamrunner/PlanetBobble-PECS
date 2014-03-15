import os
from flask import Flask, render_template, send_file, abort
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/main.db'
db = SQLAlchemy(app)
# To create database: db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=False)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images/<string:filename>')
def images(filename):
    path = 'images/' + filename
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)


if __name__ == '__main__':
    app.run()