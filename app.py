from flask import Flask
from database import setup
from resources.tasks import tasks_bp 

app = Flask(__name__)   # __name__ --> nos permite saber si el archivo es ejecutado de forma
                        # directa o si es ejecutado desde otro archivo
# creamos la tabla
setup.create_tables()

app.register_blueprint(tasks_bp)


"""Página principal"""
@app.route('/')
def home():
    return 'Que más pues!!!'

# Decimos que si el archivo es ejecutado de manera directa
if __name__=='__main__':
    app.run(debug=True)