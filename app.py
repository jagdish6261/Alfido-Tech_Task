from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage
items = ["Item 1", "Item 2", "Item 3"]


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_item = request.form.get('item_name')
        if new_item:
            items.append(new_item)
        return redirect(url_for('index'))
    return render_template('add_item.html')


if __name__ == '__main__':
    app.run(debug=True)
