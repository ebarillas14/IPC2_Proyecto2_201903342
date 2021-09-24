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

        self.machine_configuration = None
        self.sim_names = None
        self.config_route_c = StringVar()
        self.config_route_s = StringVar()
        self.simulation_names_list = BasicLinkedList()
        self.simulations = BasicLinkedList()
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
        tab1.rowconfigure(4, weight=1)
        Label(tab1, text="Cargar Archivo de Configuración", font='Helvetica 14 bold').grid(column=0, columnspan=2,
                                                                                           row=0)
        Label(tab1, text="Cargar Archivo de Simulacion", font='Helvetica 14 bold').grid(column=2, columnspan=2, row=0)
        Label(tab1, text="Seleccionar Simulación", font='Helvetica 14 bold').grid(column=4, columnspan=2, row=0)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=0, row=1)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=2, row=1)
        Label(tab1, text="Ruta", font='Helvetica 12 bold').grid(column=4, row=1)
        conf_r = Label(tab1, textvariable=self.config_route_c, font='Helvetica 12', wraplength=100).grid(column=1,
                                                                                                         row=1)
        Label(tab1, textvariable=self.config_route_s, font='Helvetica 12', wraplength=100).grid(column=3, row=1)
        Label(tab1, text="SmartWatch", font='Helvetica 12').grid(column=5, row=1)

        Button(tab1, text="Seleccionar y Cargar Archivo", command=self.load_configuration).grid(column=0, columnspan=2,
                                                                                                row=2)

        Button(tab1, text="Seleccionar y Cargar Archivo", command=self.load_simulation).grid(column=2, columnspan=2,
                                                                                             row=2)
        sim_names = ttk.Combobox(tab1, postcommand=self.update_names)
        sim_names.grid(column=4, columnspan=2, row=2)

        self.sim_names = sim_names

        sim_products = ttk.Combobox(tab1, postcommand=self.update_names_products)
        sim_products.grid(column=4, columnspan=2, row=3)
        self.sim_products = sim_products

        Button(tab1, text="Generar Reporte", command=self.simulate_product).grid(column=4, columnspan=2, row=4)

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
        self.machine_configuration = load_configuration_xml(filename)

    def load_simulation(self):
        filename = filedialog.askopenfilename(initialdir="./static/", title="Choose a XML File",
                                              filetypes=(("XML Files", "*.xml"), ("All Files", " *.*")))
        self.config_route_s.set(filename)
        simulation_list = load_simulation_xml(filename)
        self.simulations = simulation_list
        simulation = simulation_list.first

        simulations = BasicLinkedList()
        while simulation.next is not None:
            sim_data = simulation.data
            simulations.insert(sim_data.name)
            simulation = simulation.next
        sim_data = simulation.data
        simulations.insert(sim_data.name)
        self.simulation_names_list.append(simulations)

    def simulate_product(self):
        name_of_simulation = self.sim_names.get()
        name_of_product = self.sim_products.get()
        machine = self.machine_configuration
        products_list = machine.products_list
        product = products_list.first

        while product.next is not None and product.data.name != name_of_product:
            product = product.next

        q = product.data.assemble_q
        q.show_queue()
        generate_graph_queue(q, name_of_simulation, name_of_product)

    def update_names(self):
        sim = self.simulation_names_list.first
        list_of_names = []
        while sim.next is not None:
            list_of_names.append(sim.data)
            sim = sim.next
        list_of_names.append(sim.data)
        self.sim_names.config("", values=list_of_names)

    def update_names_products(self):
        name_of_simulation = self.sim_names.get()
        simulations = self.simulations
        simulation = simulations.first
        products_list = BasicLinkedList()
        while simulation.next is not None and simulation.data.name != name_of_simulation:
            simulation = simulation.next
        products_list = simulation.data.prod_list
        list_product_names = []

        product = products_list.first
        while product.next is not None:
            list_product_names.append(product.data)
            product = product.next
        list_product_names.append(product.data)
        self.sim_products.config("", values=list_product_names)


WindowDesign()
