import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello this page has been build using S2I feature of OpenShift! we have dubugged the issue facing yesterday and testing it again! again making changes to get the build runnin. checking it again after adding the branch as main"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
