import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 12)
MEDIUMFONT = ("Verdana", 11)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Crear Cotizacion")
        self.client_name = "Sin definir"
        self.description = "Sin descripcion general"
        self.items_n = []
        self.unit_values = []
        self.items_desc = []
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, EnterArticle, EndPage):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth() / 2.5 - windowWidth / 2)
        positionDown = int(self.winfo_screenheight() / 2.5 - windowHeight / 2)
        self.geometry("+{}+{}".format(positionRight, positionDown))

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def create_exit_button(self, frame):
        exit_button = ttk.Button(frame, text="Salir", command=self.destroy)

        # putting the button in its place by
        # using pack
        exit_button.grid(row=5, column=0, padx=10, pady=10, sticky="s")


# first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        self.controller = controller
        texts = [
            "¡Bienvenido!",
            "Ahora podras crear tu cotización",
            "de una forma fácil y sencilla",
        ]
        for i, text in enumerate(texts):
            label = ttk.Label(self, text=text, font=LARGEFONT)
            label.grid(row=i, column=0, columnspan=2, padx=10, pady=10)
        label = ttk.Label(
            self, text="Nombre del cliente: ", font=MEDIUMFONT, width=22
        )
        label.grid(row=3, column=0, padx=10, pady=20)
        text_entry = ttk.Entry(self, width=30)
        text_entry.grid(row=3, column=1, padx=10, pady=20)
        spacer = tk.Label(self, text="")
        spacer.grid(row=4, column=0, columnspan=2, padx=10, pady=20)
        button1 = ttk.Button(
            self,
            text="Siguiente",
            command=lambda: [
                controller.show_frame(EnterArticle),
                self.get_values(text_entry),
            ],
        )
        button1.grid(row=5, column=1, padx=10, pady=10)
        controller.create_exit_button(self)

    def get_values(self, text_entry):
        self.controller.client_name = text_entry.get()


# second window frame enter article
class EnterArticle(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Header
        self.n = 1
        self.text = tk.StringVar()
        self.text.set(f"Ingrese la informacion del articulo {self.n}")
        label = ttk.Label(
            self,
            textvariable=self.text,
            font=LARGEFONT,
        )
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        # Unit value
        vcmd = (
            self.register(self.validate),
            "%P",
        )
        label = ttk.Label(
            self, text="Precio unitario del articulo:", font=MEDIUMFONT
        )
        label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.unit_value_entry = ttk.Entry(
            self, width=30, validate="all", validatecommand=vcmd
        )
        self.unit_value_entry.grid(row=1, column=1, padx=10, pady=10)
        self.unit_value_entry.insert(0, 0)
        # Item n
        label = ttk.Label(self, text="Cantidad de articulos:", font=MEDIUMFONT)
        label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.item_n_entry = ttk.Entry(
            self, width=30, validate="all", validatecommand=vcmd
        )
        self.item_n_entry.grid(row=2, column=1, padx=10, pady=10)
        self.item_n_entry.insert(0, 0)
        # Description
        label = ttk.Label(
            self, text="Descripcion del articulo:", font=MEDIUMFONT
        )
        label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.desc_text = tk.Text(self, width=30, height=3)
        self.desc_text.grid(row=3, column=1, padx=10, pady=10)
        # Add item
        button1 = ttk.Button(
            self,
            text="Agregar mas articulos",
            command=lambda: [
                controller.show_frame(EnterArticle),
                self.get_values(),
            ],
        )
        button1.grid(row=4, column=1, padx=10, pady=10)
        # Next button
        button2 = ttk.Button(
            self,
            text="Siguiente",
            command=lambda: [
                controller.show_frame(EndPage),
                self.get_values(),
            ],
        )
        button2.grid(row=5, column=1, padx=10, pady=10)
        # Exit button
        controller.create_exit_button(self)

    def get_values(self):
        self.controller.items_desc.append(self.desc_text.get("1.0", "end-1c"))
        self.desc_text.delete("1.0", "end-1c")
        self.controller.items_n.append(self.item_n_entry.get())
        self.item_n_entry.delete(0, "end")
        self.item_n_entry.insert(0, 0)
        self.controller.unit_values.append(self.unit_value_entry.get())
        self.unit_value_entry.delete(0, "end")
        self.unit_value_entry.insert(0, 0)
        self.n += 1
        self.text.set(f"Ingrese la informacion del articulo {self.n}")

    def validate(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


# third window frame page2
class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Generar cotización", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        spacer = tk.Label(self, text="")
        spacer.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        # Description
        label = ttk.Label(
            self, text="Descripcion general:", font=MEDIUMFONT, width=22
        )
        label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.desc_text = tk.Text(self, width=30, height=3)
        self.desc_text.grid(row=2, column=1, padx=10, pady=10)
        spacer = tk.Label(self, text="")
        spacer.grid(row=3, column=0, columnspan=2, padx=10, pady=20)
        # Generate
        button2 = ttk.Button(
            self,
            text="Generar",
            command=lambda: [
                self.get_values(),
                controller.destroy(),
            ],
        )
        button2.grid(row=5, column=1, padx=10, pady=10)

    def get_values(self):
        self.controller.description = self.desc_text.get("1.0", "end-1c")
