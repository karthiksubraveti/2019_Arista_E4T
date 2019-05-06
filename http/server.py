from flask import Flask, render_template, json, send_from_directory
from flask_restful import Api, Resource, reqparse
import sys
import os
from desktopcam import capture

fileExt = ".png"
dataDir = "data"
template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
app.config["CUSTOM_STATIC_PATH"] = "./data/"
api = Api(app)
i = 1

class Capture( Resource ):
    def captureImg(self):
        global i
        fname = str(i)
        imageName = fname + fileExt
        i += 1
        filePath = os.path.join(app.root_path, dataDir, imageName)
        print "Saving image to ", filePath
        if capture(filePath):
            return {'basedir': dataDir, 'fname': imageName}, 200
        else:
            return "", 404
    def get(self):
        data, code =  self.captureImg()
        return json.dumps(data), code
    def post(self):
        return "", 200

api.add_resource( Capture, '/capture' )

@app.route("/data/<path:filename>")
def getImage(filename):
    print "Requesting", filename
    return send_from_directory(app.config["CUSTOM_STATIC_PATH"], filename )

@app.route("/")
def index():
    return render_template("index.html", message="Engineers For Tomorrow");

if __name__ == '__main__':
    port = sys.argv[1]
    # Check if data dir exists or not.
    # This is the directory from where the images are served after capture.
    dataDirPath = os.path.join(os.getcwd(), dataDir)
    if not os.path.exists(dataDirPath):
        os.makedirs(dataDirPath)
    app.run(port=int(port), debug=True)
