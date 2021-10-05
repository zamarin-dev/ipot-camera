import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage

from picamera import PiCamera
from time import sleep
import datetime

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'zamarin-dev.appspot.com'})

camera = PiCamera()

def getPicture():
    camera.start_preview()
    sleep(1)
    camera.capture('./pic.jpg')
    camera.stop_preview()

def uploadPicture():
    # firebase = pyrebase.initialize_app(firebaseConfig)
    now = datetime.datetime.now()

    photo_path = './pic.jpg'
    uplode_fname = now.strftime("%Y%m%d%H%M")
    filename = './pic.jpg'
    content_type = 'image/png'
    blob = bucket.blob(filename)
    with open(filename, 'rb') as f:
        blob.upload_from_file(f, content_type=content_type)

getPicture()
uploadPicture()