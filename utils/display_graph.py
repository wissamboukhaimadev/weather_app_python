from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_graph(x_coordinate, y_coordinate):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x_coordinate, y_coordinate)  
    ax.set_title("Data display")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.grid(True)
    return fig

def display_graph(container, x_coordinate, y_coordinate):
    fig = create_graph(x_coordinate, y_coordinate)

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)