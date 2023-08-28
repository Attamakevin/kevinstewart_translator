from flask import Flask

app = Flask(__name__)

@app.route('/')
def  kevinstewart():
    return "<h1>kevinstewart translator web app</h1>" 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15000)

    
    
