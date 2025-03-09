from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, GCP App Engine!/n Hello,People just checking whether qapplication running or not!/n Happy Women's Day "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

