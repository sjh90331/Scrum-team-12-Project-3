import pygal
import lxml
import api
import json

data = api.getAndPrint()
jsonData =json.dumps(data)
#print(type(jsonData))
#print
#print(len(data))
#print(jsonData)
print(data['Meta Data'])
for i in data['Meta Data']:
    print(i)
#     print(i)
#     # for metadata in i:
#     #     print(metadata)