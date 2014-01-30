# TODO's:
# 1. python-dateutil, si tenemos las fechas, sólo es cuestión de que alimentemos el dateutil(tmstring).
# 2. iso8601
# 3. regexp.finditer(line)
# 4. string, n = regexp.subn(line)
# sub(replacement, string, [count=0])
# Consider using replace()
# Consider using translate()

# Iteramos sobre:
# Vector de patrones
# Vector de datos

regexp = re.compile(pattern)
result = regexp.search(line)

import sys
import re
pattern = "Fred"
regexp = re.compile(pattern)
for line in sys.stdin:
	result = regexp.search(line)
	if result:
		sys.stdout.write(line)

import sys
import re
pattern = r'''
^									# inicio de la linea
RUN\
(\d{6})
\ COMPLETED\.\ OUTPUT\ IN\ FILE\
([a-z]+\.dat)
$									# fin de la linea
'''
regexp = re.compile(patter, re.VERBOSE)
for line in sys.stdin:
	result = regexp.search(line)
	if result:
		sys.stdout.writie("%s\t%s\n" % (result.group(1), result.group(2)))

import sys
import re
pattern = "Fred"
regexp = re.compile(pattern)
for line in sys.stdin:
	result = regexp.search(line)
	if result:
		sys.stdout.write(line)

import sys
import re
pattern = r'''
^									# inicio de la linea
RUN\
(\d{6})
\ COMPLETED\.\ OUTPUT\ IN\ FILE\
([a-z]+\.dat)
$									# fin de la linea
'''
regexp = re.compile(patter, re.VERBOSE)
for line in sys.stdin:
	results = regexp.finditer(line)
	for result in results:
		sys.stdout.writie("%s\t%s\n" % (result.group(1), result.group(2)))

>>> import iso8601
>>> iso8601.parse_date("2007-01-25T12:00:00Z")
datetime.datetime(2007, 1, 25, 12, 0, tzinfo=<iso8601.iso8601.Utc ...>)

# Date
\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])T

# Time
^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$

mm/dd/yy
mm/dd/yyyy
dd/mm/yy
dd/mm/yyyy

# Sin ceros
^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$

# Con ceros
^[0-3][0-9]/[0-3][0-9]/(?:[0-9][0-9])?[0-9][0-9]$

m/d/yy
mm/dd/yyyy
Con uno o dos digitos
^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$

mm/dd/yyyy
Con ceros
^(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}$

d/m/yy
dd/mm/yyyy
Con uno o dos digitos para el mes y el día, y dos o cuatro para el año.
^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$

dd/mm/yyyy
Con ceros.
^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$

Cualquier formato, sin necesidad de ceros:
^(?:(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])|(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9]))/(?:[0-9]{2})?[0-9]{2}$

Cualquier formato, con ceros:
^(?:(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])|(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9]))/[0-9]{4}$

re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', text)

from datetime import datetime
>>> import re
>>> dates = []
>>> patn = re.compile(r'\d{2} \w{3} \d{4}')
>>> fh = open('inputfile')
>>> for line in fh:
...   for match in patn.findall(line):
...     try:
...       val = datetime.strptime(match, '%d %b %Y')
...       dates.append(val)
...     except ValueError:
...       pass # ignore, this isn't a date
