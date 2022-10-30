from MyVispy.Pkg.plot import *


fig, view = make_view_2d()
view_set_range(view, (-2, 0.25), (-2, 2))


x = np.linspace(-2 + 0.01, 0.25 - 0.01, 10000)
y = 0

acc = 50
for n in range(0, acc):
    y = y ** 2 + x

    data = make_markers_2d(x, y, 'blue', size=0.1)
    view.add(data)

view_show_grid(view)


fig.show()
app.run()
