# with open('input.txt'):
#     print(f.read())

# with open('input.txt', 'w') as f: #open w trybie write tworzy plik
#     print(f.read())

# with open('input.txt', 'w+') as f: #dodajemy tryb read
#     print(f.read())

# with open('input.txt', 'r+') as f:
#     print(f.read())

# with open('input.txt', 'r+') as f:
#     print(f.readlines())

# with open('input.txt', 'r+') as f:
#     for line in f.readlines():
#         print(line,end='')

# with open('input.txt', 'r+') as f:
#     print(f.tell()) #mówi o miejscu, gdzie jest kursor
#     content = f.read()
#     print(f.tell())
#     f.write('NOWSZA WARTOSC')

# with open('input.txt', 'r+') as f:
#     print(f.tell()) #mówi o miejscu, gdzie jest kursor
#     content = f.read()
#     print(f.seek(2)) #cofanie kursora na zadaną pozycję
#     f.write('NOWSZA WARTOSC') #zadziała jak insert, podmieni to co było w tym miejscu

with open('input.txt', 'a+') as f:
    print(f.tell()) #przy append kursor ustawia się na końcu
    f.write('+DODANIE NA KONIEC')