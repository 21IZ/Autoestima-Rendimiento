import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

def plot_autoestima_vs_estudiantes():
    estudiantes = range(1, int(len(data)) + 1)
    puntuaciones_autoestima = [sum(row[2:]) / 10 for row in data]
    plt.subplot(2, 1, 1)
    plt.title("Puntuación Total en el Test de Autoestima vs. Número de Estudiantes")
    plt.xlabel("Número de Estudiantes")
    plt.ylabel("Puntuación Total en el Test de Autoestima")
    plt.ylim(0, 5)
    plt.scatter(estudiantes, puntuaciones_autoestima, marker='o', color=color_palette[0])
    xaxis = plt.gca().xaxis
    xaxis.set_major_locator(ticker.MultipleLocator(1))  # Mostrar todos los números enteros

def plot_calificaciones_vs_estudiantes():
    estudiantes = range(1, int(len(data)) + 1)
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
    plt.subplot(2, 1, 2)
    plt.title("Puntuación de Calificaciones vs. Número de Estudiantes")
    plt.xlabel("Número de Estudiantes")
    plt.ylabel("Puntuación de Calificaciones")
    plt.ylim(0, 5)
    plt.scatter(estudiantes, puntuaciones_calificaciones, marker='o', color=color_palette[1])

    # Agrega esto para mostrar los valores de x en números enteros
    xaxis = plt.gca().xaxis
    xaxis.set_major_locator(ticker.MultipleLocator(1))  # Mostrar todos los números enteros

def calcular_coincidencias():
    coincidencias = 0
    total = len(data)

    puntuaciones_autoestima = [sum(row[2:]) / 10 for row in data]
    calificaciones = [row[1] for row in data]
    calificacion_minima = min(calificaciones)
    calificacion_maxima = max(calificaciones)
    rango_calificaciones = calificacion_maxima - calificacion_minima

    for i in range(total):
        calificacion = calificaciones[i]
        if calificacion >= calificacion_minima and calificacion < calificacion_minima + rango_calificaciones / 4:
            puntuacion_calificacion = 1
        elif calificacion >= calificacion_minima + rango_calificaciones / 4 and calificacion < calificacion_minima + 2 * rango_calificaciones / 4:
            puntuacion_calificacion = 2
        elif calificacion >= calificacion_minima + 2 * rango_calificaciones / 4 and calificacion < calificacion_minima + 3 * rango_calificaciones / 4:
            puntuacion_calificacion = 3
        else:
            puntuacion_calificacion = 4

        puntuacion_autoestima = round(puntuaciones_autoestima[i])

        if puntuacion_calificacion == puntuacion_autoestima:
            coincidencias += 1

    porcentaje_coincidencias = (coincidencias / total) * 100
    print(f"Coincidencias entre puntuaciones de calificaciones y autoestima: {coincidencias}/{total} ({porcentaje_coincidencias:.2f}%)")

if __name__ == "__main__":
    plt.figure(figsize=(25, 8))
    color_palette = ["#26547d", "#ef436b", "#ffce5c", "#05c793", "#fff5eb"]
    plot_autoestima_vs_estudiantes()
    plot_calificaciones_vs_estudiantes()
    plt.tight_layout()
    plt.savefig("Plots.png")
    calcular_coincidencias()