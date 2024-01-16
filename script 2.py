import requests
import csv

parameters = { "ID" : "id",
            "Titulo" : "title",
            "Contenido" : "body"
} 
f_write = open('test1.csv', 'w')
writer = csv.writer(f_write, delimiter="\t")
saved_keys = list(parameters.keys())
writer.writerow(saved_keys)

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
content = resp.json()
for element in content:
    data = list()
    for key in saved_keys:
        data.append(element.get(parameters.get(key)))
    writer.writerow(data)