from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('index.html')


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=5002)
