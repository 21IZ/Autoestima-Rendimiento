import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

data = []
preguntas = []

with open('Datos de contacto.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Lee la primera línea completa
    preguntas = headers[3:]  # Array con las preguntas

    for row in reader:
        grado = row[1]  # Grado del estudiante
        calificacion = float(row[2])  # Promedio de calificación
        respuestas = [4 if x == "Muy de acuerdo" else 3 if x == "De acuerdo" else 2 if x == "En desacuerdo" else 1 if x == "Muy en desacuerdo" else None for x in row[3:]]  # Convierte las respuestas a valores numéricos
        data.append([grado, calificacion] + respuestas)  # Agrega la fila con el grado, calificación y las respuestas a la lista data

def plot_combinado():
    estudiantes = range(1, int(len(data)) + 1)
    puntuaciones_autoestima = [math.ceil(sum(row[2:])) // 10 for row in data]
    calificaciones = [row[1] for row in data]
    calificacion_minima = min(calificaciones)
    calificacion_maxima = max(calificaciones)
    rango_calificaciones = calificacion_maxima - calificacion_minima
    puntuaciones_calificaciones = []
    for calificacion in calificaciones:
        if calificacion >= calificacion_minima and calificacion < calificacion_minima + rango_calificaciones / 4:
            puntuacion = 1
        elif calificacion >= calificacion_minima + rango_calificaciones / 4 and calificacion < calificacion_minima + 2 * rango_calificaciones / 4:
            puntuacion = 2
        elif calificacion >= calificacion_minima + 2 * rango_calificaciones / 4 and calificacion < calificacion_minima + 3 * rango_calificaciones / 4:
            puntuacion = 3
        else:
            puntuacion = 4
        puntuaciones_calificaciones.append(puntuacion)

    plt.figure(figsize=(25, 8))
    plt.title("Puntuaciones de Autoestima y Calificaciones vs. Número de Estudiantes")
    plt.xlabel("Número de Estudiantes")
    plt.ylabel("Puntuaciones")
    plt.ylim(0, 5)

    coincidencias = 0
    for i in range(len(estudiantes)):
        if puntuaciones_autoestima[i] == puntuaciones_calificaciones[i]:
            coincidencias += 1
            plt.scatter(estudiantes[i], puntuaciones_autoestima[i], marker='o', color='#32CD32', label="Coincidencia" if i == 0 else "")
        else:
            plt.scatter(estudiantes[i], puntuaciones_autoestima[i], marker='o', color='#0000FF', label="Autoestima" if i == 0 else "")
            plt.scatter(estudiantes[i], puntuaciones_calificaciones[i], marker='o', color='#FF0000', label="Calificación" if i == 0 else "")

    print(f"Fueron {coincidencias} coincidencias de los {len(estudiantes)} ( {'{:.2f}'.format(coincidencias/len(estudiantes)*100)}% )")
    xaxis = plt.gca().xaxis
    xaxis.set_major_locator(ticker.MultipleLocator(1))  # Mostrar todos los números enteros
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plot_Combinado.png")

if __name__ == "__main__":
    plot_combinado()