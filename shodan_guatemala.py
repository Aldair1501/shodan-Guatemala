#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shodan
from collections import defaultdict

# === DATOS DEL ESTUDIANTE ===
CARNET = "202012345"
NOMBRE = "Aldair Sinay"
CURSO = "Seguridad Informática"
SECCION = "B"

# === CONFIGURACIÓN DE SHODAN ===
API_KEY = "ptaqSMfmFM4KbUaXPrEsOTIC97wSyCqq"  # Tu clave gratuita
QUERY = 'country:"GT" port:80'  # Filtro para cuentas gratuitas
LIMIT_RESULTS = 5               # Limitar resultados para evitar 403

def main():
    # Crear instancia de la API de Shodan
    api = shodan.Shodan(API_KEY)

    try:
        print(f"Ejecutando búsqueda: {QUERY}")
        # Realizar la búsqueda con límite de resultados
        results = api.search(QUERY, limit=LIMIT_RESULTS)

        # Conjuntos y diccionarios para almacenar información
        total_ips = set()          # Guarda IPs únicas encontradas
        puertos = defaultdict(int) # Contador de IPs por puerto

        print("\n=== RESULTADOS ENCONTRADOS ===\n")
        for match in results['matches']:
            ip = match.get('ip_str')
            port = match.get('port', 'N/A')
            service = match.get('transport', 'Desconocido')

            total_ips.add(ip)
            puertos[port] += 1

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
        print(f"Error en la consulta: {e}")

if __name__ == "__main__":
    main()
