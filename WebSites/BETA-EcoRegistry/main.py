from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    especie_1 = db.Column(db.Text, nullable=False)
    descripcion_especie_1 = db.Column(db.Text, nullable=False)
    img_especie_1 = db.Column(db.Text, nullable=False)
    especie_2 = db.Column(db.Text, nullable=False)
    descripcion_especie_2 = db.Column(db.Text, nullable=False)
    img_especie_2 = db.Column(db.Text, nullable=False)
    especie_3 = db.Column(db.Text, nullable=False)
    descripcion_especie_3 = db.Column(db.Text, nullable=False)
    img_especie_3 = db.Column(db.Text, nullable=False)





# Agregar una nueva entrada a la base de datos
@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    img = request.form['img']
    text = request.form['text']
    especie_1 = request.form['especie_1']
    img_especie_1 = request.form['img_especie_1']
    descripcion_especie_1 = request.form['descripcion_especie_1']
    especie_2 = request.form['especie_2']
    img_especie_2 = request.form['img_especie_2']
    descripcion_especie_2 = request.form['descripcion_especie_2']
    especie_3 = request.form['especie_3']
    img_especie_3 = request.form['img_especie_3']
    descripcion_especie_3 = request.form['descripcion_especie_3']
    new_entry = Entry(
        name=name, 
        img=img, 
        text=text, 
        especie_1=especie_1, 
        img_especie_1=img_especie_1, 
        descripcion_especie_1=descripcion_especie_1, 
        especie_2=especie_2, 
        img_especie_2=img_especie_2, 
        descripcion_especie_2=descripcion_especie_2, 
        especie_3=especie_3, 
        img_especie_3=img_especie_3, 
        descripcion_especie_3=descripcion_especie_3
    )
    db.session.add(new_entry)
    db.session.commit()
    return redirect('/')


# Página principal
@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

# Mostrar el formulario para agregar una nueva entrada
@app.route('/new')
def show_new_entry_form():
    return render_template('new_entry.html')

# Mostrar las entradas por nombre (palabra clave)
@app.route('/categoria/<name>')
def show_category(name):
    entries = Entry.query.filter_by(name=name).all()
    return render_template('cate.html', entries=entries)


# Mostrar todas las entradas
@app.route('/all')
def all_entries():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

#Eliminar objeto de la vase de datos
@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = Entry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)


'''
Lo que necesito para crear una base de datos.
Entro de la carpeta M4L1 utilizando el comando cd M4L1.
cd xxxxx
Escribo python
Saldra algo asi:
>>>
Escribo: >>> from main import app, db
Escribo: >>> app.app_context().push()
Escribo: >>> db.create_all()

'''