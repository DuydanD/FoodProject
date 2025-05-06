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

if __name__ == '__main__':
    app.run(debug=True)