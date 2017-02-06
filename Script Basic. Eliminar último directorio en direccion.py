# Quitar de una dirección el último directorio.

dbxpath = "/Prosegur/Nóminas 2015 Prosegur"
print (dbxpath)

list = dbxpath.split('/')
print(list)
list.pop()
dbxpath=""
# ['', 'Prueba', 'directorio', 'pon']
for a in range((len(list))):
    dbxpath = dbxpath+list[a]+'/'
#dbxpath=dbxpath.rstrip('/')
print (dbxpath)
