#!/bin/bash

echo "Seleccione una opción:"
echo "1. Ejecutar Autoestima y Calificaciones"
echo "2. Ejecutar Combinado"
echo "3. Ejecutar Grado"

read option

case $option in
    1)
        cd Autocalif
        echo "Ejecutando Ros.py..."
        py Ros.py
        sleep 1.5 # Espera 3 segundo para generar la imagen
        start Plots.png & # Abre la imagen en una nueva ventana
        ;;
    2)
        cd Combinado
        echo "Ejecutando Comb.py..."
        py Comb.py
        sleep 1.5
        start Plot_Combinado.png &
        ;;
    3)
        cd Grado
        echo "Ejecutando Grado.py..."
        py Grado.py
        sleep 1.5
        start Grado.png &
        ;;
    *)
        echo "Opción inválida"
        ;;
esac