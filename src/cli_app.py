class cliApp:

    # __init__ function for class tkinterApp
    def __init__(self):
        self.client_name = "Sin definir"
        self.description = "Sin descripcion general"
        self.items_n = []
        self.unit_values = []
        self.items_desc = []

    def exec(self):
        self.client_name = input("Por favor ingrese el nombre del cliente: ")
        n = 1
        continue_item = "n"

        while continue_item in ["n", "N"]:
            try:
                self.items_n.append(
                    int(
                        input(
                            "Por favor ingrese la " f"cantidad del item {n}: "
                        )
                    )
                )
                self.unit_values.append(
                    int(
                        input(
                            "Por favor ingrese el valor "
                            f"unitario del item {n}: "
                        )
                    )
                )
                self.items_desc.append(
                    input(
                        "Por favor ingrese la " f"descripcion del item {n}: "
                    )
                )
                continue_item = input(
                    "Presione N para agregar un nuevo item o "
                    "cualquier otra letra para terminar: "
                )
                n += 1
            except ValueError:
                print(
                    "Ingrese un valor numerico para "
                    f"la cantidad y el valor unitario del item {n}"
                )
        self.description = input(
            "Por favor Ingrese una descripcion general o "
            "presione enter para continuar: "
        )
