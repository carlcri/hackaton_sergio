import os
from flask import Flask, render_template, request, jsonify, abort, redirect
from datetime import datetime
from geopy.geocoders import Nominatim
from funciones.utilidades import buscar_ciudad



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


@app.route('/ecomap')
def ods_bogota():
    return redirect('https://ecomapodsbogota.wixsite.com/inicio')


@app.route('/test')
def test():
    return render_template("test.html")


# Ruta para manejar el formulario
@app.route('/formulario', methods=['GET'])
def formulario():
    return render_template('form.html')



@app.route('/api/reportes', methods=['GET'])
def obtener_reportes():
    return jsonify(reportes)


@app.route('/api/reportes', methods=['POST'])
def crear_reporte():
    global next_id

    timestamp = datetime.now().strftime('%Y-%m-%d')

    if request.form:
        lat = request.form['lat']
        lon = request.form['lon']
        material = request.form['material']
        cantidad = request.form['cantidad']
    else:
        data = request.json
        lat = data['lat']
        lon = data['lon']
        material = data['material']
        cantidad = request.form['cantidad']

    city, country = buscar_ciudad(lat=lat, lon=lon)

    nuevo_reporte = {
        'id': next_id,
        'lat': lat,
        'lon': lon,
        'material': material,
        'estado': 'reportado',
        'creado': timestamp,
        'area': city,
        'country': country,
        'actualizado': timestamp,
        'reciclador': 'sin asignar',
        'cantidad': cantidad,
    }
    reportes.append(nuevo_reporte)
    next_id += 1
    return jsonify({'message': 'Reporte creado exitosamente', 'reporte': nuevo_reporte}), 201





@app.route('/api/reportes/<int:id>', methods=['GET'])
def obtener_reporte(id):
    reporte = next((r for r in reportes if r['id'] == id), None)
    if reporte is None:
        abort(404)
    return jsonify(reporte)