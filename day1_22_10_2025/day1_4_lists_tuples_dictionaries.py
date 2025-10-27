#listy
import copy

grill = ['widelce', 'talerzyki', 'kubki', 'chleb', 'kielbaski', 'piwo']
print(grill, end='')

grill.append('noże')
print(grill)

grill.insert(0,'grill')
print(grill)

grill[0] = 'wegiel'
print(grill)

grill.remove('piwo') #po wartościach a nie indeksach
del grill[0] #kasowanie po indeksach
print(grill)

niepotrzebny_zakup = grill.pop(4) #usuwanie elementu z listy wraz z jego zwróceniem
print(niepotrzebny_zakup)
print(grill)

###################################################################################
#tuple (krotki)
zakupy = ('sprite', 'cytryna', 'lód')
print(zakupy)

################################################
# Referencje
a = ['a', 'b', 'c']
b = a
c = a.copy()
a[0] = 'xxx'
print(a,b,c)

a = ['a',
        ['b',
            ['c']
        ]
     ]

b = a
c = a.copy()
d = copy.deepcopy(a)

a[0] = 'xxx'
a[1][0] = 'yyyyyyyy'

print(a, b, c, d)