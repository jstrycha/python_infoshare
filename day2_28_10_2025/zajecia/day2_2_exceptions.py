# def display_name(age) -> None:
#     print(age)
#
# age = input('Podaj wiek: ')
#
# try:
#     print(age) #program wykonuje się do 1 wyjątku, więc to się jeszcze wykona
#     age_int = int(age)
#     print('Masz: ' + age + ' lat')
# except:
#     print('Coś poszło nie tak!')

###############################################################################
def display_name(age) -> None:
    print(age)


age = input('Podaj wiek: ')

try:
    age_int = int(age)
    raise NameError() #rzucamy sami errorem żeby wejść w exception - przydaje się do sprawdzenia jak zachowa się kod jak pójdze exception
    print('Masz: ' + age + ' lat')
except NameError as exception: #zapisujemy obiekt NameError jako exception, możemy wywoływać potem na nim różne metody
    print(exception)
    print('Coś poszło nie tak!')

###############################################################################

