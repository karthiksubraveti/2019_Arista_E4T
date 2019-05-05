from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import sys
import os
import json

port = None

class Capture( Resource ):
    def captureImg(self, fname):
        imagePath = "/images/" + "testfilepath"
        return json.dumps({"url": imagePath })
    def get(self, fname):
        url = self.captureImg(fname)
        print url
        return url, 200
    def post(self, fname):
        return fname, 200


template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
api = Api(app)
api.add_resource( Capture, '/capture/<string:fname>' )

@app.route("/")
def index():
    return render_template("index.html", message="Engineers For Tomorrow");

if __name__ == '__main__':
    port = sys.argv[1]
    app.run(port=int(port), debug=True)
