from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body { font-family: sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #0078d4; }
        </style>
    </head>
    <body>
        <h1>Hello Josh from Flask app!</h1>
        <p>CI/CD & Reverse Proxy Lab Python App</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
