
# Primer reporte
curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 4.60971, "lon": -74.08175, "material": "Plastico"}'

# Segundo reporte
curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 4.60971, "lon": -74.08175, "material": "Vidrio"}'

# Tercer reporte
curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 4.60971, "lon": -74.08175, "material": "Cobre"}'



# PETICIONES AJUSTADAS CON COORDENADAS

curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 6.25184, "lon": -75.56359, "material": "Plastico"}'


curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 4.60971, "lon": -74.08175, "material": "Vidrio"}'


curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 10.96389, "lon": -74.79636, "material": "Cobre"}'


curl -v http://127.0.0.1:5000/api/reportes \
-H "Content-Type: application/json" \
-d '{"lat": 3.4516, "lon": -76.5319, "material": "Cobre"}'




# GET
curl -X GET http://127.0.0.1:5000/api/reportes
