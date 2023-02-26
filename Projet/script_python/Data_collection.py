import save_meta_data as save_data

#for the images
import matplotlib.image as matplot


# the name of the json with all the data
json_path=""
# we get the json
json_data = json.load(open(json_path))
data = json_normalize(json_data)

# we get the link of the image and save it in a folder image
link_imgs =data["image"]
#we get the name of the cake
cake = data["gateauLabel"]

# we save the pictures
for i in range(len(link_imgs)):

    name = cake[i]# the name to save
    image = matplot.imread(link_imgs[i])# the image, a numpy table
    matplot.imsave(name, image)
    save_data.save_meta_data(link_imgs[i], i)