import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import tkinter as tk

data = pd.read_csv('iris_data.csv')

pairs = [
    ('SepalLengthCm', 'SepalWidthCm'),
    ('SepalLengthCm', 'PetalLengthCm'),
    ('SepalLengthCm', 'PetalWidthCm'),
    ('SepalWidthCm', 'PetalLengthCm'),
    ('SepalWidthCm', 'PetalWidthCm'),
    ('PetalLengthCm', 'PetalWidthCm')
]


def create_plots():
    plt.figure(figsize=(15, 10))

    for i, (x, y) in enumerate(pairs):
        plt.subplot(2, 3, i + 1)
        plt.scatter(data[x], data[y], alpha=0.5)
        plt.title(f'{x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)

        model = LinearRegression()
        model.fit(data[[x]].values, data[y].values)

        intercept = model.intercept_
        slope = model.coef_[0]

        plt.plot(data[[x]], model.predict(data[[x]]), color='red', linewidth=2, label='Линия регрессии')
        plt.legend()
        plt.text(0.05, 0.95, f'y = {slope:.2f}x + {intercept:.2f}', transform=plt.gca().transAxes)

    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("Iris Data Visualization")

plot_button = tk.Button(root, text="Построить графики", command=create_plots)
plot_button.pack(pady=20)

root.mainloop()
