from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

# class ingredient:
#     name = 'name'
#     quantity = 0
#     weight = 0
#     price = 0

ingredients = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_ingredient = request.form['ingredient']
        ingredients.append(new_ingredient)
        return redirect(url_for('index'))
    return render_template('index.html', ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)