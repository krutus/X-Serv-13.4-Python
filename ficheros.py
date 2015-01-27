#!/usr/bin/python

fichero = open("/etc/passwd", "r")

lineasfich = fichero.readlines()

dicc = {}

for linea in lineasfich:
    separados = linea.split(':');
    user = separados[0] 
    shell = separados[-1][:-1]
    dicc [user] = shell
    
print dicc
print "Numero de usuarios:" , len(lineasfich)
