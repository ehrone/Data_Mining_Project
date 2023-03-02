import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import json

def crea_json():
    endpoint_url = "https://query.wikidata.org/sparql"

    query = """SELECT ?gateau ?gateauLabel ?gateauDescription ?image ?origineLabel
    {
    ?gateau wdt:P279/wdt:P31* wd:Q477248; #des pâtisseries
            wdt:P18 ?image; #l'image
            wdt:P495 ?origine. # l'origine du gateau
                
    
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en"}

    }
    LIMIT 1000"""


    def get_results(endpoint_url, query):
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    results = get_results(endpoint_url, query)
    dico_json ={}

    for result in results["results"]["bindings"]:
        #print(result)
        # on récupère le nom du gateau
        gateau = result['gateauLabel']['value']
        # les valeurs qui nous interessent dans notre requête
        dico={}
        for key, val in result.items():
            dico[key]=val['value']
        dico_json[gateau]=dico
        print("\n", gateau,'\n')
        print(dico_json[gateau], '\n')

    #print(' dico json \n')
    #print(dico_json)
    with open('fichier.json', 'w') as fichier :
        json.dump(dico_json, fichier)