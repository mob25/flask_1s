from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/jeans')
def jeans():
    return render_template("jeans.html")


@app.route('/shoes')
def shoes():
    return render_template("shoes.html")


@app.route('/jackets')
def jackets():
    return render_template("jackets.html")


@app.route('/baasploa')
def baasploa():
    return render_template("baasploa.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
