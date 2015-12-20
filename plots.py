# Dora Jambor
# plots.py
# 05.12.2014

# Plot linear function
def basic_linear():
    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

basic_linear()

# Plot x-es against y-es with red circles
def plot_xy():
    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()

plot_xy()

# Plot values from 0 to 5 by 0.2
def plot_lines():
    import numpy as np
    import matplotlib.pyplot as plt

    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

plot_lines()

# Plot ultiple figures and axes

def multiple_figure():
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

multiple_figure()

# create a historgram

def historgram():
    import numpy as np
    import matplotlib.pyplot as plt
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

historgram()

# Annotate text
def annotate():
    import numpy as np
    import matplotlib.pyplot as plt

    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )

    plt.ylim(-2,2)
    plt.show()

annotate()
