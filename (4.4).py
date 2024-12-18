import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

data = pd.read_csv('BTC_data.csv')
x = np.arange(len(data))
y = data['Price'].values

def draw_plot():
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Цена биткоина', color='blue')

    z = np.polyfit(x, y, 3)
    p = np.poly1d(z)
    plt.plot(x, p(x), label='Полином 3-й степени', color='red')

    plt.title('Цена биткоина и полиномиальная аппроксимация')
    plt.xlabel('Дни')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.show()

root = tk.Tk()
root.title("Bitcoin Price Visualization")

button = tk.Button(root, text="Построить график", command=draw_plot)
button.pack(pady=20)

root.mainloop()
