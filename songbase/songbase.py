from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        # return hello GET
        return render_template('form.html')
    if request.method == "POST":
        first_name = request.form["first_name"]
        return "Hi, your name is %s" % first_name

@app.route('/users/<string:username>')
def users(username):
    # return "<h1>hello %s</h1>" % username
    return render_template('user.html', uname=username)

@app.route('/user')
def user():
    return "this is the page for users"

if __name__ == '__main__':
    app.run()
