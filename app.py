from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello_world():
    return 'hello_wrld'

@app.route('/hello/<name1>/<name2>')
def hello_name1_name2(name1, name2):
    return 'hello %s %s' % (name1, name2)

if __name__ == '__main__':
    app.debug = True
    app.run()
