#!/usr/bin/python3
from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def main():
    return render_template("index.html", text="Hello, World!")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'uploads/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    filename = upload.filename

    # file support verification
    ext = os.path.splitext(filename)[1]
    if (ext == ".mp3") or (ext == ".ogg") or (ext == ".wav"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400

    # save file
    destination = "/".join([target, filename])
    print("File saved to to:", destination)
    upload.save(destination)




    return render_template("index.html")


@app.route("/test")
def test():
    return "<h1>Hello, World! test123</h1>"

if __name__ == "__main__":
    app.run()
