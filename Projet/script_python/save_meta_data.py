import csv
import compte_files.py as c
import recup_meta_data.py as recup 

def save_meta_data(path, indice):

    with open('meta_data.csv', 'w') as file:
        writer_obj=csv.writer(file)

        #for i in range(c.count_files('images')):# counting the number of images we have

        dico = recup.recup_matadata_img(path)#getting the meta_datas of the image
        header, values = [], []

        for key, value in dico.items():# the values to write into our csv file
                header.append(key)
                values.append(value)
            
        if indice ==0 :# we set the header of the file if it is the first call 
            writer_obj.writerows([ header, values ])# we save it in the csv file

        else :
            writer_obj.writerow(values)