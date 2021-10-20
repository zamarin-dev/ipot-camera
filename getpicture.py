import picamera
from time import sleep
import datetime

import firebase_admin
from firebase_admin import credentials
from google.cloud import storage


storage_client = storage.Client.from_service_account_json('key.json')

def getPicture():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        sleep(3) 
        camera.capture('./pic.jpg')
        camera.stop_preview()
        camera.close()


def upload_blob(file_name, data_sorce):
    bucket_name = 'zamarin-dev.appspot.com'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(filename=data_sorce)

    if file_name in bucket.list_blobs():
        print("cloud storage: upload success")
    else:
        print("cloud storage: upload failed")

getPicture()
upload_fname = 'plant_img/'+datetime.datetime.now().strftime("%Y%m%d%H%M")+'.png'
print(upload_fname)

upload_blob(upload_fname, './pic.jpg')