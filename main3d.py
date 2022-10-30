from MyVispy.Pkg.plot import *


def func(x, y):
    a = y
    b = y
    c = y
    z = a * np.exp(- (x - b) ** 2 / (2 * c ** 2))
    return z


x = np.linspace(-5, 5, 100)
y1 = np.linspace(-5, 5, 100)
y2 = np.linspace(-5, 5, 100)

data1 = make_surface_3d(x, y1, func, (1, 0, 0, 1))
data2 = make_markers_3d(x, y2, func, 'red')

fig, view = make_view_3d()
view_set_range(view, (-10, 10), (-10, 10), (-10, 10))
view.add(data1)
view.add(data2)

view_show_grid(view)

if __name__ == '__main__':
    fig.show()
    app.run()
