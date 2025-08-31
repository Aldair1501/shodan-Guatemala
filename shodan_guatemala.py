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