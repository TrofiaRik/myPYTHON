Python 3.9.2 (default, Dec  1 2024, 12:12:57) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> box=dict()
>>> box['Money, (eur)']=3500
>>> box['Money, (usd)']=15000
>>> box['Money, (tdl)']=125000000
>>> print(box)
{'Money, (eur)': 3500, 'Money, (usd)': 15000, 'Money, (tdl)': 125000000}
>>> print(box['Money, (eur)'])
3500
>>> box['Money, (eur)']=box['Money, (eur)']+27524
>>> print(box['Money, (eur)'])
31024
>>> 