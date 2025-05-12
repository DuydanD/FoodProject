from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__, template_folder="templates")

CSV_FILENAME = 'ingredients.csv'

ingredients = []


@app.route("/", methods=['GET', 'POST'])
def index():
    global ingredients
    filepath = os.path.join(os.path.dirname(__file__), CSV_FILENAME)

    if request.method == 'POST':
        new_ingredient = request.form['ingredient']
        cap_ingredient = new_ingredient.capitalize()
        lower_ingredient = cap_ingredient.lower()

        existing_ingredients = []

        try:
            with open(filepath, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        existing_ingredients.append(row[0].lower())
        except FileNotFoundError:
            pass

        if lower_ingredient not in existing_ingredients:
            with open(filepath, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([cap_ingredient])

        return redirect(url_for('index'))
    
    ingredients = []
    if os.path.exists(filepath):
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row: 
                    ingredients.append(row[0])
    
    return render_template('index.html', ingredients=ingredients)

@app.route("/delete_selected", methods=["POST"])
def delete_selected_ingredients():
    filepath = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
    selected_ingredients = request.form.getlist("delete_ingredient")

    all_ingredients = []
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    all_ingredients.append(row[0])
    except FileNotFoundError: 
        all_ingredients = []

    updated_ingredients = []
    for ingredient in all_ingredients:
        if ingredient.lower() not in [selected.lower() for selected in selected_ingredients]:
            updated_ingredients.append(ingredient)

    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ingredient in updated_ingredients:
            writer.writerow([ingredient])
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)