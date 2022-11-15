import json
from urllib.request import urlopen

import sys
sys.path.insert(0,'/app')

import pyknowledgegraph

urls = open('articles.csv').read().strip().split("\n")[1:]

for url in urls:
    print(url)
    response = urlopen(url)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    content = data_json["content"].strip()
    
    
    
    