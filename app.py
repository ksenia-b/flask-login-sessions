from flask import Flask, render_template, request


app = Flask(__name__)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Oksana', password='password'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username = username]

    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')