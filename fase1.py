# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Enrique Bonilla & Ernesto Ramírez"
__date__ ="$25-ene-2014 12:36:13$"


import nltk

fecha = "2@/Sept./199o";

tokens = nltk.regexp_tokenize(fecha, '''\W+''')
print tokens

print fecha.split('/')
