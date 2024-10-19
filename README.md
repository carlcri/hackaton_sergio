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

### Reto Menotia 

Abel sugiere *https://lookerstudio.google.com/navigation/reporting* para visuabilizar datos