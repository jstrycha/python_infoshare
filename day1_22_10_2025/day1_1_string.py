# print('Arek')
#
# first_name = input('Podaj swoje imię: ')
# print(first_name) #domyslnie na końcu printa jest znak nowej linii
#
# print('Ala', end='?')
# print('ma', end='**')
# print('kota')
# print(1,2,3,'Ala','Gdansk',sep='+++', end='\t') # '\t' -
#
# print(type(first_name))
# print(first_name.upper())
# print(first_name.capitalize())
#
# biale_znaki = "   białe znaki  "
# print(biale_znaki.strip())
# biale_znaki = "zzzbiałe znakizzz"
# print(biale_znaki.strip('z')) #obcina znaki z początku i końca

print ('aa' * 10)

nazwa_jezyka = "Python"
print(nazwa_jezyka[0])
print(nazwa_jezyka[1:3])
print(nazwa_jezyka[1:-2])
print(nazwa_jezyka[::2])
print(nazwa_jezyka[::-1])

name = "abc"
name_len = len(name)
print(name[name_len-1])

# Escapowanie znaków specjalnych
#plik = "c:\dokumenty\nowy_folder\teren_1\tekst.txt" #tak się nie da, bo widzi \n jako znak nowej linii

# raw string - string surowy
plik1 = r"c:\dokumenty\nowy_folder\teren_1\tekst.txt"
print(plik1)

# podwójne backslashe
plik2 = "c:\\dokumenty\\nowy_folder\\teren_1\\tekst.txt"
print(plik2)

#f-stringi
liczba = 12876.34503
moja_liczba = 2
print(f"Wyświetlam f-string oryginalne: {liczba}")
print(f"Wyświetlam f-string wycentrowane: {liczba:-^30}") #całość ma 30 znaków, dopełniamy minusami
print(f"Wyświetlam f-string wycentrowane: {liczba:-<30}")
print(f"Wyświetlam f-string zaokrąglone: {liczba:.2f}")
print(f"Wyświetlam f-string z separatorem: {liczba:,}")
print(f"Wyświetlam f-string z operacją dodatkową: {liczba-1}")

#Równoważne opcje jak f-string (już rzadko używane)
print('Wyświetlam (format): {} i jeszcze jako nazwany argument {moja_liczba}'.format(liczba,moja_liczba=moja_liczba))

print('Wyświetlam (modulo) jako string: %s' % liczba)
print('Wyświetlam (modulo) jako float: %f' % liczba)
print('Wyświetlam (modulo) jako int: %d' % liczba)




