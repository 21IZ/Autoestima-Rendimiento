import csv
import matplotlib.pyplot as plt

data = []
preguntas = []

with open('Datos de contacto.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Lee la primera línea completa
    preguntas = headers[2:]  # Array con las preguntas

    for row in reader:
        grado = row[1]  # Grado del estudiante
        respuestas = [4 if x == "Muy de acuerdo" else 3 if x == "De acuerdo" else 2 if x == "En desacuerdo" else 1 if x == "Muy en desacuerdo" else None for x in row[2:]]  # Convierte las respuestas a valores numéricos
        data.append([grado] + respuestas)  # Agrega la fila con el grado y las respuestas a la lista data

def calculate_means():
    grado_scores = {}
    grado_frequencies = {}
    for row in data:
        grado = row[0]
        scores = row[1:]
        if grado in grado_scores:
            grado_scores[grado] += sum(score / 10 for score in scores)
            grado_frequencies[grado] += 1
        else:
            grado_scores[grado] = sum(score / 10 for score in scores)
            grado_frequencies[grado] = 1
    mean_scores = [(grado_scores[grado] / grado_frequencies[grado]) * 1.25 for grado in sorted(grado_frequencies.keys())]
    return mean_scores


def plot_grado_distribution():
    grado_frequencies = {grado: sum(1 for row in data if row[0] == str(grado)) for grado in [10, 11, 12]}
    sizes = [grado_frequencies[grado] for grado in sorted(grado_frequencies.keys())]
    explode = [0, 0, 0]
    explode[max(enumerate(sorted(grado_frequencies.keys())), key=lambda x: grado_frequencies[x[1]])[0]] = 0.1
    plt.subplot(1, 1, 1)
    plt.title("Distribución por Grado")
    plt.pie(sizes, labels=[str(grado) for grado in sorted(grado_frequencies.keys())], explode=explode, autopct="%1.1f%%", colors=color_palette)

if __name__ == "__main__":
    mean_scores = calculate_means()
    plt.figure(figsize=(16, 8))
    plt.suptitle("ESCALA DE AUTOESTIMA DE ROSENBERG (RSE)", fontweight="bold")
    color_palette = ["#26547d", "#ef436b", "#ffce5c", "#05c793", "#fff5eb"]
    plot_grado_distribution()
    plt.tight_layout()
    plt.savefig("Grado.png")