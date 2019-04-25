#!/usr/bin/python
import os
import glob
from time import sleep
from picamera import PiCamera
import detect_face_aws

class CameraModule( object ):
    def __init__( self, outputDir ):
        self.outputDir = outputDir
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()

        # Camera warm-up time
        self.counter = 0
        fileList = glob.glob( outputDir + "/*" )
        if not fileList:
            self.counter = 0
        else:
            # file - foo.%d.jpg grab the idx
            maxFileIdx = max( [ int( f.split( '.' )[ 1 ] ) for f in fileList ] )
            self.counter = maxFileIdx + 1


        # warmup delay        
        sleep( 2 )
    
    def initializeCounter( self, ):
        pass

    def run( self, ):
        while True:
            fileName = "%s/pic.%d.jpg" % ( self.outputDir, self.counter )
            self.camera.capture( fileName )
            print "capturing ", fileName
            self.counter += 1
			yield fileName


if __name__ == "__main__":
    outputDir = "output"
    try:
        os.mkdir( outputDir )
    except:
        pass

    cameraModule = CameraModule( outputDir=outputDir )
    for imgFileName in cameraModule.run():
		print "detecting face ", imgFileName
		detect_face_aws.run( imgFileName )
		time.sleep( 1 )
