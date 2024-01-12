from flask import Flask,render_template

app = Flask(__name__, template_folder="templates",
            static_folder="static", static_url_path="/static")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')
def index_direct():
    return render_template("index.html")

@app.route('/test')
def test_direct():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)