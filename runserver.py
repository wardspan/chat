from flask import Flask, render_template
app = Flask(__name__)

#SETTINGS
DEBUG=True

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=DEBUG)