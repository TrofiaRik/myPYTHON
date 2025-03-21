# coding: utf-8
#let's create a Dict Literals for my bank
bank={}
print("bank{'EUR'}=25000 is an invalid syntax. You must use the same basi syntax for Dict() and {} Dict Lit")
bank={'EUR':25000}
bank['USD']=35425
print(bank)
bank['EUR']=bank['EUR']+25000
bank['EUR']-=32.25
bank['USD']=64500
print(bank)
bank['EUR']=12542
print(bank)
bank['TRY']=448236.25
print(bank)
bank['EUR']+=2000000
print(bank)
bank['EUR']=bank['EUR']+100
dict()
bank2=dict()
bank2['EUR']=500
bank2['USD']=1500
bank2['USD']-=1000
print(bank2)
print(bank)
