import os
from flask import Flask, render_template, request, jsonify

def create_app():
    app = Flask(__name__)
#    Bootstrap(app)
    return app

app = create_app() 


reportes = []
next_id = 1  # ID para los reportes

@app.route('/')
def root():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    last_directory = os.path.basename(current_directory)

    return f'Current Project: {last_directory}'


@app.route('/test')
def test():
    return render_template("test.html")



@app.route('/api/reportes', methods=['GET'])
def obtener_reportes():
    return jsonify(reportes)




@app.route('/api/reportes', methods=['POST'])
def crear_reporte():
    global next_id
    data = request.json
    nuevo_reporte = {
        'id': next_id,
        'lat': data['lat'],
        'lon': data['lon'],
        'material': data['material']
    }
    reportes.append(nuevo_reporte)
    next_id += 1
    return jsonify({'message': 'Reporte creado exitosamente', 'reporte': nuevo_reporte}), 201

