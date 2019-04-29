from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import sys
import os

port = None

class UImage( Resource ):
    def get(self, uid):
        #uid_path = "http://localhost:%s/images/%s.jpg" % (port,uid)
        #return {'uidPath': uid_path }, 200
        pass
    def post(self, uid):
        print "Creating image with the name uid.jpg"
        cmd = "cp ../images/e4t.jpg ../images/%s.jpg" % uid
        os.system(cmd)
        return uid, 201


template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)
api = Api(app)
api.add_resource( UImage, '/uimage/<string:uid>' )

@app.route("/")
def index():
    return render_template("index.html", message="Engineers For Tomorrow");

if __name__ == '__main__':
    port = sys.argv[1]
    app.run(port=int(port), debug=True)
