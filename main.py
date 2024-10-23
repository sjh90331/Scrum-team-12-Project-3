import pygal
import lxml
import api
import json

data = api.getAndPrint()
print(type(data))