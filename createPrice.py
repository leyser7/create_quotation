import os
import sys
import random
import logging
import datetime
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, Alignment
from src.tkinter_app import tkinterApp

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
date = date.strftime("%d/%m/%Y")
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)


def set_border(ws, cell_range):
    rows = ws[cell_range]
    for row in rows:
        for r in row:
            r.border = thin_border


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


config_path = resource_path("config")
image_path = "tarjeta.png"
file_path = "cotizacion.xlsx"
output_file = "output.xlsx"
wb = load_workbook(f"{config_path}/{file_path}")

ws = wb["Hoja1"]  # or wb.active

ws["R4"] = f"A-{random.randint(10150,10300)}"
ws.merge_cells("R4:U4")
set_border(ws, "R4:U4")
ws["R4"].alignment = Alignment(horizontal="center")

app = tkinterApp()
app.mainloop()
print(app.client_name)
"""

ws["D11"] = input("Por favor ingrese el nombre del cliente: ")
ws["M11"] = date
n = 1
continue_item = "n"
while continue_item in ["n", "N"]:
    try:
        ws[f"L{13 + n}"] = int(input(
                                "Por favor ingrese la "
                                f"cantidad del item {n}: "))
        ws[f"O{13 + n}"] = int(input(
                            "Por favor ingrese el valor "
                            f"unitario del item {n}: "))
        ws[f"C{13 + n}"] = input("Por favor ingrese la "
                                 f"descripcion del item {n}: ")
        ws[f"C{13 + n}"].alignment = Alignment(horizontal="center",
                                               wrap_text=True)
        height = len(ws[f"C{13 + n}"].value)/3
        ws.row_dimensions[14+n].height = 13.8 if height < 13.8 else height
        continue_item = input("Presione N para agregar un nuevo item o "
                              "cualquier otra letra para terminar: ")
        n += 1
    except ValueError:
        print("Ingrese un valor numerico para "
              f"la cantidad y el valor unitario del item {n}")
ws["A22"] = input("Por favor Ingrese una descripcion general o "
                  "presione enter para continuar: ")
wb.save(output_file)
os.system("libreoffice --headless --convert-to pdf "
          f"{output_file} >/dev/null 2>&1")
"""
logger.info(f"{output_file} generated")
