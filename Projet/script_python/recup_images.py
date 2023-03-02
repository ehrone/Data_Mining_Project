# for the json
from pandas import json_normalize
import pandas as pd    
import json
#########################
import requests
import shutil
import os

def download_image(url):

    headers = {"User-Agent": "Mozilla/5.0"}
    request = requests.get(url, allow_redirects=True, headers=headers, stream=True)
    if request.status_code == 200:
        with open(os.path.basename(url), "wb") as image:
            request.raw.decode_content = True
            shutil.copyfileobj(request.raw, image)
    return request.status_code

# the name of the json with all the data
json_path="fichier.json"
# we get the json
json_data = json.load(open(json_path))


for key, info in json_data.items():
    #print('\n', key,'\n', info, '\n')
    name = info['gateauLabel']# the name to save the image
    print(type(download_image(info['image'])))
