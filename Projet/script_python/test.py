import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import functions as f

f.crea_json()
print("Json crée \n")
f.get_imgs()
print('Images recupéréees \n')
