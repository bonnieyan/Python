from flask import Flask

# 传入模块名字
app = Flask(__name__)

# 路由


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/hello')
def hello():
    return 'Hello'


if __name__ == "__main__":
    app.run()