'''
Ejemplo sacado de http://www.tostring.es/2015/02/python-con-dropbox.html para obtener de internet la ip en formato JSON'''

import requests

r=requests.get(r'http://jsonip.com')
ip = r.json()['ip']
print (r)
print (ip)