import os

def opening_counter(user_file):
    if os.path.exists(user_file):
        with open(user_file, 'r+') as file:
            counter = file.read()
            counter = int(counter)
            print(f"Plik był otwarty {counter} raz(y)")
            counter += 1
            counter = str(counter)
            file.seek(0)
            file.write(counter)
    else:
        with open(user_file, 'w+') as file:
            counter = "0"
            file.write(counter)
            print("Utworzono nowy plik")
