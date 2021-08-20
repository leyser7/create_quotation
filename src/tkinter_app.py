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
        self.client_name = "Sin Definir"
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, EnterArticle, Page2):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        self.controller = controller
        text = (
            "¡Bienvenido!"
            # "Ahora "
            #     "podras crear tu cotizacion de una "
            #     "manera facil y sencilla.\n"
            #     "Diligencia los siguientes datos."
        )
        label = ttk.Label(self, text=text, font=LARGEFONT)

        # label.configure(anchor="center")
        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, columnspan=2)

        label1 = ttk.Label(self, text="Nombre del cliente: ", font=MEDIUMFONT)
        label1.grid(row=1, column=0, padx=10)

        text_entry = ttk.Entry(self, width=30)
        text_entry.grid(row=1, column=1, padx=10)
        button1 = ttk.Button(
            self,
            text="Siguiente",
            command=lambda: [
                controller.show_frame(EnterArticle),
                self.get_values(text_entry),
            ],
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Salir", command=controller.destroy)

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=0, padx=10, pady=10)

    def get_values(self, text_entry):
        self.controller.client_name = text_entry.get()


# second window frame page1
class EnterArticle(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Ingrese articulo", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        # button to show frame 2 with text

        button1 = ttk.Button(
            self,
            text="Agregar mas articulos",
            command=lambda: [
                controller.show_frame(EnterArticle),
                self.get_values(text_entry),
            ],
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Salir", command=controller.destroy)

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=0, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Continuar",
            command=lambda: controller.show_frame(Page2),
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=1, padx=10, pady=10)

    def get_values(self, text_entry):
        self.controller.client_name = text_entry.get()


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Page 1", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(
            self,
            text="Startpage",
            command=lambda: controller.show_frame(StartPage),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
