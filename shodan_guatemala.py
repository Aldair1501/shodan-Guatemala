#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Libreria y importaciones

import shodan
from collections import defaultdict

# === DATOS DEL ESTUDIANTE ===
CARNET = "202012345"
NOMBRE = "Aldair Sinay"
CURSO = "Seguridad Informática"
SECCION = "B"

# === CONFIGURACIÓN DE SHODAN ===
API_KEY = "TU_API_KEY_AQUI"  # Reemplaza con tu clave de Shodan
QUERY = 'country:"GT"'       # Filtra dispositivos en Guatemala

def main():
    # Crear instancia de la API de Shodan
    api = shodan.Shodan(API_KEY)

    try:
        print(f"Ejecutando búsqueda: {QUERY}")
        # Realizar la búsqueda en Shodan
        results = api.search(QUERY)

        # Conjuntos y diccionarios para almacenar información
        total_ips = set()             # Guarda IPs únicas encontradas
        puertos = defaultdict(int)    # Contador de IPs por puerto

      print("\n=== RESULTADOS ENCONTRADOS ===\n")
        for match in results['matches']:
            # Obtener IP, puerto y tipo de transporte
            ip = match.get('ip_str')
            port = match.get('port', 'N/A')
            service = match.get('transport', 'Desconocido')

            # Guardar información para el resumen
            total_ips.add(ip)
            puertos[port] += 1

            # Mostrar cada resultado en consola
            print(f"IP: {ip} | Puerto: {port} | Servicio: {service}")

        # === RESUMEN DE RESULTADOS ===
        print("\n=== RESUMEN ===")
        print(f"Total de direcciones IP: {len(total_ips)}")
        for port, count in puertos.items():
            print(f"Puerto {port}: {count} IPs")

        # === DATOS DEL ESTUDIANTE ===
        print("\n=== DATOS DEL ESTUDIANTE ===")
        print(f"Carnet: {CARNET}")
        print(f"Nombre: {NOMBRE}")
        print(f"Curso: {CURSO}")
        print(f"Sección: {SECCION}")

    except shodan.APIError as e:
        # Captura errores de la API de Shodan
        print(f"Error en la consulta: {e}")

if __name__ == "__main__":
    main()