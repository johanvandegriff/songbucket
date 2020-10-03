#!/usr/bin/python3
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", text="Hello, World!")

@app.route("/test")
def test():
    return "<h1>Hello, World! test123</h1>"

if __name__ == "__main__":
    app.run()
