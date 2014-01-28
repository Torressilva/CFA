# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Enrique Bonilla & Ernesto Ramírez"
__date__ ="$25-ene-2014 12:36:13$"


import nltk

fecha = "2@/Sept./199o";
#fecha = fecha.split('/');
#print fecha

#tokens1 = nltk.regexp_tokenize(fecha, '''\w+''')
#print tokens1

tokens2 = nltk.regexp_tokenize(fecha, '''\W+''')
print tokens2
#print fecha

print fecha.split('/')
#letras = [''.join(c for c in s if c.isalnum()) for s in fecha.split()]
#print letras

#num = [''.join(c for c in s if c.isdigit()) for s in fecha.split()]
#print num
