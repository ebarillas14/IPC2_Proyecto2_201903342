from xml.etree.ElementTree import Element, SubElement, ElementTree
from TDA import *
from models import *
import xml.etree.ElementTree as ET


def load_configuration_xml(route):
    tree = ET.parse(route)
    root = tree.getroot()
    prod_lines_am = root.find('CantidadLineasProduccion')
    prod_lines = root.find('ListadoLineasProduccion')
    product_list = root.find('ListadoProductos')
    print(prod_lines_am.text)
    pll = pl = BasicLinkedList()
    for line in prod_lines.findall('LineaProduccion'):
        num = line.find('Numero')
        components_am = line.find('CantidadComponentes')
        assemble_time = line.find('TiempoEnsamblaje')
        p_line = ProductionLine(num, components_am, assemble_time)
        pll.insert(p_line)
        print(num.text)
        print(components_am.text)
        print(assemble_time.text)

    for product in product_list.findall('Producto'):
        name = product.find('nombre')
        instructions = product.find('elaboracion')
        # Need to create a instructions queue
        prod = Product(name, instructions)
        pl.insert(prod)
        print(name.text)
        print(instructions.text)

    actual_machine = Machine(prod_lines_am, pll, pl)

    return actual_machine


def load_simulation_xml(route):
    tree = ET.parse(route)
    root = tree.getroot()
    names = prod_list = simulation_list = BasicLinkedList()

    for name in root.findall('Nombre'):
        names.insert(name)

    # Extracts all of the arrays with tags Listado Productos

    for p_list in root.findall('ListadoProductos'):

        product_list = BasicLinkedList()
        # Extracts all of the products contained in the array
        for product in p_list.findall('Producto'):
            product_list.insert(product)

        prod_list.insert(product_list)

    if names.len() != prod_list.len():
        print("No cuadra la cantidad de nombres con listados de productos")
    else:
        for pos in range(names.len()):
            name = names.get(pos)
            products_list = prod_list.get(pos)
            simulation_list.insert(Simulation(name, products_list))

    return simulation_list
