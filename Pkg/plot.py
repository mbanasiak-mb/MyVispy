from MyVispy.Pkg.package import *


def prepare_data_2d(x, y):
    pa = np.array([
        x, y
    ]).T

    return pa


def make_surface_3d(x, y, func, color='black'):
    xx, yy = np.meshgrid(x, y)
    z = func(xx, yy)

    # TODO: there is bug in SurfacePlot -> colors, this is a workarround
    c = z / abs(np.amax(z))
    c = vispy.color.get_colormap("cool").map(c).reshape(z.shape + (-1,))
    c = c.flatten().tolist()
    c = list(map(lambda x, y, z, w: (x, y, z, w), c[0::4], c[1::4], c[2::4], c[3::4]))

    data = scene.SurfacePlot(color=color)

    data.set_data(
        x=x, y=y, z=z,
    )

    data.mesh_data.set_vertex_colors(c)

    return data


def make_markers_3d(x, y, func, color='black', size=2):
    xx, yy = np.meshgrid(x, y)
    z = func(xx, yy)

    x = np.reshape(xx, (1, -1))[0]
    y = np.reshape(yy, (1, -1))[0]
    z = np.reshape(z, (1, -1))[0]

    pa = np.array([x, y, z]).T

    data = scene.Markers(
        light_color=None,
        antialias=0
    )

    data.set_data(
        pa,  # ndarray: (n, 3)
        face_color=color,
        edge_color=None,
        edge_width=0,
        size=size,
    )

    return data


def make_line_2d(x, y, color: str = "black", width: float = 2):
    pa = prepare_data_2d(x, y)
    data = scene.Line(
        pos=pa,  # ndarray: (n, 2)
        color=color,
        width=width,
        method="agg",  # agg | gl
        antialias=0
    )

    return data


def make_markers_2d(x, y, color: str = "black", size: float = 2.5):
    pa = prepare_data_2d(x, y)
    data = scene.Markers(
        pos=pa,  # ndarray: (n, 2)
        size=size,
        edge_width=0,
        edge_color=None,
        face_color=color,
        light_color=None,
        antialias=0
    )

    return data


def make_view(length, width, title):
    fig = scene.SceneCanvas(
        bgcolor=vispy.color.Color('white'),
        keys='interactive',
        size=(length, width),
        show=False,
        title=title
    )

    grid = fig.central_widget.add_grid()
    view = grid.add_view()

    return fig, view


def make_view_2d(length: int = 500, width: int = 500, title: str = "Title"):
    fig, view = make_view(length, width, title)
    view.camera = 'panzoom'

    return fig, view


def make_view_3d(length: int = 500, width: int = 500, title: str = "Title"):
    fig, view = make_view(length, width, title)
    view.camera = 'turntable'

    return fig, view


def view_set_range(view, rx: tuple[float, float], ry: tuple[float, float], rz: tuple[float, float] = None):
    view.camera.set_range(rx, ry, rz)


def view_autoscale(view):
    view.camera.set_range()


def view_show_grid(view):
    grid_lines = scene.GridLines((1, 1, 0), color=(0, 0, 0, 1))
    grid_lines.set_gl_state('translucent', cull_face=False)
    view.add(grid_lines)
