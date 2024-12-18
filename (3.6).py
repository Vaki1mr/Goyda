import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def plot_histograms():
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))
    axs = axs.flatten()

    sample_sizes = [100, 1000, 10000, 100000]

    for i, size in enumerate(sample_sizes):
        data = np.random.normal(loc=0, scale=1, size=size)
        axs[i].hist(data, bins=30, density=True, alpha=0.6, color='b')

        mu, std = np.mean(data), np.std(data)
        xmin, xmax = axs[i].get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / std) ** 2)
        axs[i].plot(x, p, 'k', linewidth=2)

        axs[i].set_title(f'Sample Size: {size}')
        axs[i].set_xlabel('Value')
        axs[i].set_ylabel('Density')

    plt.tight_layout()
    return fig


def main():
    root = tk.Tk()
    root.title("Normal Distribution Histograms")

    fig = plot_histograms()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()


if __name__ == "__main__":
    main()
