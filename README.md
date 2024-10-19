# hackaton_sergio
Hackaton Sergio Arboleda, con Pilar

## Buenas Practicas

Se crea un repositorio publico en GitHub 

## Sala Principal

https://us02web.zoom.us/j/89297610209?pwd=bbG6cDkprwiI3sQzfWRtIfizLCjSje.1

### Funcionamiento

Implemento una REST API basica con Flask, haciendo uso de peticiones para agregar datos a la lista. Usamos el comando *curl* para hacer las peticiones directamente desde la consola sin software adicional.

```sh
curl -v -X POST http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 4.60971, "lon": -74.08175, "material": "Plastico"}'
```

Si posteriormente hago una peticion GET, lo hare asi:


```sh
curl -X GET http://127.0.0.1:5000/api/reportes

```

### Implemento Peticiones POST

se pueden seguir haciendo igualmente con el comando *curl*, y con el nuevo formulario que se implemento en: *http://127.0.0.1:5000/api/reportes*

```py
@app.route('/api/reportes', methods=['POST'])
def crear_reporte():
    global next_id
    if request.form:
        lat = request.form['lat']
        lon = request.form['lon']
        material = request.form['material']
    else:
        data = request.json
        lat = data['lat']
        lon = data['lon']
        material = data['material']

    nuevo_reporte = {
        'id': next_id,
        'lat': lat,
        'lon': lon,
        'material': material
    }
    reportes.append(nuevo_reporte)
    next_id += 1
    return jsonify({'message': 'Reporte creado exitosamente', 'reporte': nuevo_reporte}), 201
```

### Mentoria con Abel n la mañana 

Abel sugiere *https://lookerstudio.google.com/navigation/reporting* para visuabilizar datos