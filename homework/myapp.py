from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/end')
def end():
    return render_template('end.html')

# @app.route('/form-demo')
#def form_demo():
#    first_name = request.args.get('first_name')
#    return first_name

@app.route('/users/<string:username>')
def users(username):
    # return "<h1>hello %s</h1>" % username
    return render_template('users.html', uname=username)

if __name__ == '__main__':
    app.run()
