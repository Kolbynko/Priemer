#average = x
#pocet cisel = z
z=0
x=0
pokracuj='y'
while pokracuj == 'y':
  a=int(input('Zadaj číslo: '))
  pokracuj=str(input('Chceš pokračovať? y/n: '))
  if pokracuj == 'n':
    print('Priemer čísel je', x/z)
  
  
