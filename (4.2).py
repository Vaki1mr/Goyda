import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def draw_charts():
    df = pd.read_csv('iris_data.csv')
    counts = df['Species'].value_counts()

    cond1 = df['PetalLengthCm'] > 1.2
    cond2 = (df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] < 1.5)
    cond3 = df['PetalLengthCm'] > 1.5

    labels = ['> 1.2 см', '1.2 - 1.5 см', '> 1.5 см']
    sizes = [df[cond1].shape[0], df[cond2].shape[0], df[cond3].shape[0]]

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    axs[0].set_title('Виды ирисов')

    axs[1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    axs[1].set_title('Длина лепестка')

    for ax in axs:
        ax.axis('equal')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = tk.Tk()
root.title("Круговые диаграммы")

btn = tk.Button(root, text="Построить диаграммы", command=draw_charts)
btn.pack()

root.mainloop()

