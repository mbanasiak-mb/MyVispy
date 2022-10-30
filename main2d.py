from MyVispy.Pkg.plot import *


def func(x):
    y = x ** 2
    return y


x = np.linspace(-2, 2, 1000)
y1 = func(x)
y2 = func(x) - 2

data1 = make_line_2d(x, y1, 'blue')
data2 = make_markers_2d(x, y2, 'red')

fig, view = make_view_2d()
view.add(data1)
view.add(data2)

view_show_grid(view)
view_autoscale(view)

if __name__ == '__main__':
    fig.show()
    app.run()
