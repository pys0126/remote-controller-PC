from flask import Flask, render_template, jsonify, abort, request
import pyautogui as auto
import os

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/screen")
def screen():
    return render_template("screen.html")


@app.route("/halt", methods=["POST"])
def halt():
    if request.method == "POST":
        os.system("shutdown -s -t 60")
        return jsonify(code=200, msg="计算机将在1分钟内关机")
    return abort(405)


@app.route("/close", methods=["POST"])
def close():
    if request.method == "POST":
        os.system("shutdown -a")
        return jsonify(code=200, msg="关机已取消")
    return abort(405)


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        auto.press('volumeup')
        return jsonify(code=200, msg="音量增加")
    return abort(405)


@app.route("/min", methods=["POST"])
def minn():
    if request.method == "POST":
        auto.press('volumedown')
        return jsonify(code=200, msg="音量减小")
    return abort(405)


@app.route("/next", methods=["POST"])
def nextto():
    if request.method == "POST":
        auto.hotkey("ctrl", "alt", "right")
        return jsonify(code=200, msg="已切换下一首")
    return abort(405)


@app.route("/back", methods=["POST"])
def back():
    if request.method == "POST":
        auto.hotkey("ctrl", "alt", "left")
        return jsonify(code=200, msg="已返回上一首")
    return abort(405)


@app.route("/or", methods=["POST"])
def orto():
    if request.method == "POST":
        auto.hotkey("ctrl", "alt", "p")
        return jsonify(code=200, msg="已暂停/开始")
    return abort(405)


@app.route("/screenshot", methods=["POST"])
def screenshot():
    if request.method == "POST":
        os.system("nircmd savescreenshot E:\\Code\\python\\项目\\other\\远程控制\\static\\screen.png")
        return jsonify(code=200, msg="已截图")
    return abort(405)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
