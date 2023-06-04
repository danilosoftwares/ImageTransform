from flask import jsonify, request
from PIL import Image
import os

def convert_bytes(num):
    step_unit = 1000.0
    for x in ['bytes','KB','MB','GB','TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit


def upload_file():
    try:
        result = {"status":997,"message":"payload not found"}
        if request.method == 'POST':
            for item in request.files.getlist("file"):
                img_before = "before.jpg"
                item.save(img_before)

                img_after = "after.jpg"
                image_file = Image.open(img_before)
                image_file.save(img_after, quality=60)

                sz_before = f'Before {convert_bytes(os.stat(img_before).st_size)}'
                sz_after = f'After {convert_bytes(os.stat(img_after).st_size)}'

                sz_before_files = f'Before Files {convert_bytes(os.stat(img_before).st_size * 100000000)}'
                sz_after_files = f'After Files {convert_bytes(os.stat(img_after).st_size * 100000000)}'

                result = {"status":0,"message":sz_before+'\r\n'+sz_after+'\r\n'+sz_before_files+'\r\n'+sz_after_files}
    except Exception as e:
        result = {"status":999,"message":str(e)}
    return jsonify(result)
