#!/usr/bin/python

from flask import Flask
from flask import send_file
import io
import os
from os import listdir
from os.path import isfile, join
from flask import jsonify
from os import path


app = Flask(__name__)

imges_path = '/home/pi/picamera-motion/images_dup'
images_human = '/home/pi/picamera-motion/images_human'

@app.route('/')

def index():

    return 'Hello world' ,200

@app.route('/images')
def list_images():
    
    onlyfiles = [f for f in listdir(imges_path) if isfile(join(imges_path , f))]
    return jsonify(files=onlyfiles)

@app.route('/image/<string:imgname>')
def get_image(imgname=None):
    if path.exists(imges_path+'/'+imgname) :
        return send_file(imges_path+'/'+imgname, mimetype='image/gif')
    else :
        return 'File not found' ,404
    

@app.route('/moveimage/<string:imgname>/<string:human>')
def moveimage(imgname=None, human=None):
    if path.exists(imges_path+'/'+imgname) :
        if human == 'human':
            os.rename(imges_path+'/'+imgname,images_human+'/'+imgname)
        else :
            os.rename(imges_path+'/'+imgname,images_human+'_not/'+imgname)
            #os.remove(imges_path+'/'+imgname)
        return 'Done'
    else :
        return 'File not found' ,404
    
@app.route('/deleteimage/<string:imgname>')
def deleteimage(imgname=None):
    if path.exists(imges_path+'/'+imgname) :
        os.remove(imges_path+'/'+imgname)
        return 'Done'
    else :
        return 'Image File not found' ,404

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
