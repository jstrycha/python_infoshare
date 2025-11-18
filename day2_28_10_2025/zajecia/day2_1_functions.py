# name = 'Jola'
#
# def change_name():
#     print(name)
#
# change_name() #tu się wyprintuje Jola

###############################################################################
# name = 'Jola'
#
# def change_name():
#     print(name) #to już nie zadziała - wywali się błąd, bo zmieniamy name poniżej
#     name = 'Teresa'
#
# change_name()

###############################################################################
def display_name(name='Ewa') -> None:
    print(name)

new_display_name = display_name
print(type(new_display_name))

result = display_name('Grażyna')
print(result) #Zwraca None