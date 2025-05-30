from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Flask Server is Working!</h1><p>This is a test to verify that Flask can run correctly.</p>"

if __name__ == '__main__':
    # Run on 0.0.0.0 to make it accessible from any network interface
    app.run(debug=True, host='0.0.0.0') 