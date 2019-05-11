from flask import Flask, render_template, json, send_from_directory
from flask_restful import Api, Resource, reqparse
import sys
import os
import argparse
import time
from desktopcam import capture

fileExt = ".png"
dataDir = "data"
template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
app.config["CUSTOM_STATIC_PATH"] = "./data/"
api = Api(app)

class Capture( Resource ):
    def captureImg(self):
        fname = str(int(time.time()))
        imageName = fname + fileExt
        filePath = os.path.join(app.root_path, dataDir, imageName)

        '''  ********** CHANGE 8 ************
            Use print function to print filePath
            filePath is a variable defined above

        '''
        # ---Add code below ---

        '''  *********** CHANGE 9 **********
            Call capture function
                Function name: capture
                Argument : filePath
                Return value: ret
            Example:
                Function name: forward
                Argument value: 100
                Return value: ret

                ret = forward(100)
        '''
        # --- Add code below -----

        if ret:
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
    print( "Requesting", filename )
    return send_from_directory(app.config["CUSTOM_STATIC_PATH"], filename )

@app.route("/")
def index():
    return render_template("index.html", message="Engineers For Tomorrow");

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run web server')
    parser.add_argument('--port', type=int, dest='port',
			default=17244, help='port number for the web server')

    args = parser.parse_args()
    # Check if data dir exists or not.
    # This is the directory from where the images are served after capture.
    dataDirPath = os.path.join(os.getcwd(), dataDir)
    if not os.path.exists(dataDirPath):
        os.makedirs(dataDirPath)
    app.run(host="0.0.0.0", port=args.port, debug=True)
