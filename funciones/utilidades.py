from geopy.geocoders import Nominatim
from geopy.exc import GeocoderInsufficientPrivileges

import unicodedata

def buscar_ciudad(lat, lon):
    # Inicializar el geocodificador
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Depurando el error cuando no esta disponible el servicio de geolocalizacion:

    try:
        # Geocodificación inversa
        location = geolocator.reverse((lat, lon), language='es')

        # Mostrar ciudad y país
        if location:
            ciudad = location.raw['address'].get('city', 'No disponible')
            pais = location.raw['address'].get('country', 'No disponible')

            # Solucionando Bug de caracteres especiales, 
            # ciudad = ciudad.encode('utf-8').decode('utf-8')
            print(ciudad)
            ciudad = unicodedata.normalize('NFC', ciudad)
            print(ciudad)
            pais = pais.encode('utf-8').decode('utf-8')
        else:
            return 'No disponible', 'No disponible'
        
        return ciudad, pais
    
    except GeocoderInsufficientPrivileges:
        return 'No disponible', 'No disponible'

