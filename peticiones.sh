
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



# GET
curl -X GET http://127.0.0.1:5000/api/reportes
