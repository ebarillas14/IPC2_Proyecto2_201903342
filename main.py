from tkinter import *
from tkinter import ttk, filedialog
from helpers import *
from PIL import ImageTk, Image

"""
    The main.py docuement will Handle all the UI for the application
"""


class WindowDesign:

    def __init__(self):
        root = Tk()
        root.title("Proyecto 2 IPC2")
        root.geometry("1080x720")

        self.config_route_c = StringVar()
        self.config_route_s = StringVar()
        tabControl = ttk.Notebook(root)

        tab1 = Frame(tabControl)
        tab1.columnconfigure(0, weight=1)
        tab1.columnconfigure(1, weight=2)
        tab1.columnconfigure(2, weight=1)
        tab1.columnconfigure(3, weight=2)
        tab1.columnconfigure(4, weight=1)
        tab1.columnconfigure(5, weight=2)
        tab1.rowconfigure(0, weight=1)
        tab1.rowconfigure(1, weight=1)
        tab1.rowconfigure(2, weight=1)
        tab1.rowconfigure(3, weight=1)
        Label(tab1, text="Cargar Archivo de Configuración", font='Helvetica 14 bold').grid(column=0, columnspan=2,
                                                                                           row=0)
        Label(tab1, text="Cargar Archivo de Simulacion", font='Helvetica 14 bold').grid(column=2, columnspan=2, row=0)
        Label(tab1, text="Seleccionar Simulación", font='Helvetica 14 bold').grid(column=4, columnspan=2, row=0)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=0, row=1)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=2, row=1)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=4, row=1)
        conf_r = Label(tab1, textvariable=self.config_route_c, font='Helvetica 12', wraplength=100).grid(column=1, row=1)
        Label(tab1, textvariable=self.config_route_s, font='Helvetica 12', wraplength=100).grid(column=3, row=1)
        Label(tab1, text="SmartWatch", font='Helvetica 12').grid(column=5, row=1)

        Button(tab1, text="Seleccionar y Cargar Archivo", command=self.load_configuration).grid(column=0, columnspan=2,
                                                                                                row=2)

        Button(tab1, text="Seleccionar y Cargar Archivo", command=self.load_simulation).grid(column=2, columnspan=2,
                                                                                             row=2)

        ttk.Combobox(tab1, values=["SmartWatch", "February", "March", "April"]).grid(column=4, columnspan=2, row=2)
        Button(tab1, text="Generar Reporte").grid(column=4, columnspan=2, row=3)

        tab2 = Frame(tabControl)
        Label(tab2, text="Aquí debe de ir el resto de la interfaz gráfica xD").grid(column=0, row=0, padx=30, pady=30)

        tab3 = Frame(tabControl)
        tab3.columnconfigure(0, weight=1)
        tab3.columnconfigure(1, weight=1)
        tab3.columnconfigure(2, weight=3)
        tab3.rowconfigure(0, weight=2)
        tab3.rowconfigure(1, weight=1)
        tab3.rowconfigure(2, weight=1)
        tab3.rowconfigure(3, weight=1)
        tab3.rowconfigure(4, weight=1)
        tab3.rowconfigure(5, weight=1)
        tab3.rowconfigure(6, weight=2)
        tab3.rowconfigure(7, weight=1)
        tab3.rowconfigure(8, weight=1)
        img = Image.open("./static/img/eabda.jpg")
        img_resize = img.resize((226, 318), Image.ANTIALIAS)
        img_resized = ImageTk.PhotoImage(img_resize)
        Label(tab3, image=img_resized).grid(column=2, row=2, rowspan=2)
        Label(tab3, text="Contacto del Programador", font='Helvetica 18 bold').grid(column=0, row=0, columnspan=3)
        Label(tab3, text="Primer Nombre", font='Helvetica 12 bold').grid(column=0, row=1, padx=30, pady=30)
        Label(tab3, text="Eduardo").grid(column=1, row=1, padx=30, pady=30)
        Label(tab3, text="Primer Apellido", font='Helvetica 12 bold').grid(column=0, row=2, padx=30, pady=30)
        Label(tab3, text="Barillas").grid(column=1, row=2, padx=30, pady=30)
        Label(tab3, text="Registro Académico", font='Helvetica 12 bold').grid(column=0, row=3, padx=30, pady=30)
        Label(tab3, text="201903342").grid(column=1, row=3, padx=30, pady=30)
        Label(tab3, text="Asignatura", font='Helvetica 12 bold').grid(column=0, row=4, padx=30, pady=30)
        Label(tab3, text="IPC 2 \"C\"").grid(column=1, row=4, padx=30, pady=30)
        Label(tab3, text="Información Extra de uso del programa", font='Helvetica 18 bold').grid(column=0, row=5,
                                                                                                 columnspan=3)
        Label(tab3, text="Documentacion Oficial", font='Helvetica 12 bold').grid(column=0, row=6, padx=30, pady=30)
        Label(tab3, text="LINK GITLAB").grid(column=1, row=6, padx=30, pady=30)
        Label(tab3, text="F.A.Q", font='Helvetica 12 bold').grid(column=0, row=7, padx=30, pady=30)
        Label(tab3, text="ALGO Aqui").grid(column=1, row=7, padx=30, pady=30)

        tabControl.add(tab1, text='Archivo')
        tabControl.add(tab2, text='Reporte')
        tabControl.add(tab3, text='Ayuda')

        tabControl.pack(expand=1, fill="both")

        self.root = root
        self.root.mainloop()

    def load_configuration(self):
        filename = filedialog.askopenfilename(initialdir="./static/", title="Choose a XML File",
                                              filetypes=(("XML Files", "*.xml"), ("All Files", " *.*")))
        self.config_route_c.set(filename)
        load_configuration_xml(filename)

    def load_simulation(self):
        filename = filedialog.askopenfilename(initialdir="./static/", title="Choose a XML File",
                                              filetypes=(("XML Files", "*.xml"), ("All Files", " *.*")))
        self.config_route_s.set(filename)
        load_simulation_xml(filename)


WindowDesign()
