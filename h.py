from flask import Flask, render_template, request


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=["POST"])
def submit():
    name = request.form.get("name")
    establishment = request.form.get("establishment")

    if not name or not establishment:
        error = "Please fill the required field."
        return render_template("fail.html",
                               error=error,
                               name=name,
                               establishment=establishment)
    return render_template("submit.html")
