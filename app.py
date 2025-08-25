from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет"

if __name__ == "__main__":
    # запуск на 0.0.0.0, чтобы контейнер был доступен извне
    app.run(host="0.0.0.0", port=5000)
