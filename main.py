import numpy as np
import matplotlib.pyplot as plt

# Parametri
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 100

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)

    mset = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)
    return mset

def plot_mandelbrotset(xmin, xmax, ymin, ymax, width, height, max_iter):
    mandelbrotimage = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrotimage, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.title("Insieme di Mandelbrot")
    plt.show()

def main():
    plot_mandelbrotset(xmin, xmax, ymin, ymax, width, height, max_iter)

if __name__ == "__main__":
    main()
