from PIL import Image
from PIL.ExifTags import TAGS 

def recup_matadata_img(path):
    dico_metadata ={}
    # the image's path
    #path =""

    # reading the image
    image = Image.open(path)

    #extracting the data
    exifdata = image.getexif()

    # we need the human redeable tags for the data, we get them with the function TAGS.get(id, id)
    for tag_id in exifdata:
        # we get the tag name
        tag = TAGS.get(tag_id, tag_id)# the human redeable tag
        data = exifdata.get(tag_id)# the value of the tag

        # decoding the tags data
        if isinstance(data, bytes):
            data = data.decode()
        
        # we add that into the dictionnary
        dico_metadata[tag]= data

    return dico_metadata