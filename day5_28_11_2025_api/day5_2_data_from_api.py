## https://petstore.swagger.io/#/pet/getPetById

import requests
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='views')

@app.route('/')
def get_pets():
    URL_GET_PET = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available&status=pending&status=sold'
    pets = requests.get(URL_GET_PET).json()
    print(pets)
    return render_template('index.html', pets=pets)

@app.route('/skasuj_zwierzaka/<id>')
def delete_pet(id):
    URL_TO_DELETE_PET = 'https://petstore.swagger.io/v2/pet/' + id
    requests.delete(URL_TO_DELETE_PET)
    strona_przekierowania = url_for('get_pets')
    return redirect(strona_przekierowania)

@app.route('/skasuj_wszystkie/zwierzaki')
def delete_all_pets():
    URL_GET_PET = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available&status=pending&status=sold'
    pets = requests.get(URL_GET_PET).json()
    for pet in pets:
        URL_TO_DELETE_PET = 'https://petstore.swagger.io/v2/pet/' + str(pet['id'])
        requests.delete(URL_TO_DELETE_PET)

    strona_przekierowania = url_for('get_pets')
    return redirect(strona_przekierowania)

@app.route('/edytuj_zwierzaka/<id>', methods = ['GET', 'POST'])
def edit_pet(id):
    URL_EDIT_PET = 'https://petstore.swagger.io/v2/pet/' + id
    if request.method == 'POST':
        name = request.form['name']
        requests.post(URL_EDIT_PET, data={'name': name})
        return redirect(url_for('get_pets'))

    pet = requests.get(URL_EDIT_PET).json()
    name = pet.get('name', '')
    return render_template('edit.html', pet_name=name)

@app.route('/dodaj_zwierzaka', methods=['GET', 'POST'])
def add_pet():
    URL_ADD_PET = 'https://petstore.swagger.io/v2/pet'

    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']

        # id z formularza – może być puste
        id_str = request.form.get('id', '').strip()

        # jeśli puste → 0, jeśli coś wpisane → próbujemy zamienić na inta
        try:
            pet_id = int(id_str) if id_str else 0
        except ValueError:
            pet_id = 0  # jak user wpisze głupotę, to i tak dajemy 0

        new_pet = {
            "id": pet_id,
            "name": name,
            "photoUrls": [],
            "tags": [],
            "status": status
        }

        requests.post(URL_ADD_PET, json=new_pet)
        return redirect(url_for('get_pets'))

    return render_template('add.html')

app.run(debug=True)