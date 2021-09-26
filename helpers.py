from xml.etree.ElementTree import Element, SubElement, ElementTree
from TDA import *
from models import *
from graphviz import Graph
import os
import xml.etree.ElementTree as ET


def load_configuration_xml(route):
    tree = ET.parse(route)
    root = tree.getroot()
    prod_lines_am = root.find('CantidadLineasProduccion')
    prod_lines_am = prod_lines_am.text.replace("\n", "").replace(" ", "")
    prod_lines = root.find('ListadoLineasProduccion')
    product_list = root.find('ListadoProductos')
    pll = BasicLinkedList()
    pl = BasicLinkedList()
    for line in prod_lines.findall('LineaProduccion'):
        num = line.find('Numero')
        num = num.text.replace("\n", "").replace(" ", "")
        components_am = line.find('CantidadComponentes')
        components_am = components_am.text.replace("\n", "").replace(" ", "")
        assemble_time = line.find('TiempoEnsamblaje')
        assemble_time = assemble_time.text.replace("\n", "").replace(" ", "")
        p_line = ProductionLine(num, components_am, assemble_time)
        pll.insert(p_line)
        """print(num.text)
        print(components_am.text)
        print(assemble_time.text)"""

    for product in product_list.findall('Producto'):
        name = product.find('nombre')
        name = name.text.replace("\n", "").replace(" ", "")
        instructions = product.find('elaboracion')

        instructions_queue = Queue()
        instructions_list = instructions.text.split(' ')
        for ins in instructions_list:
            if ins != '' and ins != '\n':
                instructions_queue.enqueue(ins)
        prod = Product(name, instructions_queue)
        pl.insert(prod)

    actual_machine = Machine(prod_lines_am, pll, pl)

    return actual_machine


def load_simulation_xml(route):
    tree = ET.parse(route)
    root = tree.getroot()
    names = BasicLinkedList()
    prod_list = BasicLinkedList()
    simulation_list = BasicLinkedList()

    for name in root.findall('Nombre'):
        name = name.text.replace("\n", "").replace(" ", "")
        names.insert(name)

    # Extracts all of the arrays with tags Listado Productos

    for p_list in root.findall('ListadoProductos'):

        product_list = BasicLinkedList()
        # Extracts all of the products contained in the array
        for product in p_list.findall('Producto'):
            text = product.text.replace("\n", "").replace(" ", "")
            product_list.insert(text)

        prod_list.insert(product_list)

    if names.len() != prod_list.len():
        print("No cuadra la cantidad de nombres con listados de productos")
    else:
        for pos in range(names.len()):
            name = names.get(pos)
            name = name.replace("\n", "").replace(" ", "")
            products_list = prod_list.get(pos)
            simulation_list.insert(Simulation(name, products_list))

    return simulation_list


def generate_graph_queue(process_queue, prod_name, simulation_name):
    dot = Graph(f'{simulation_name}-{prod_name}', format='png')
    temp = process_queue
    for i in range(process_queue.length()):
        node = temp.dequeue()
        dot.node(f"node{i}", f"{node.data}", shape="box")
        if i > 0:
            dot.edge(f"node{i-1}", f"node{i}",)

    dot.render(f'{simulation_name}-{prod_name}')
    os.system(f'{simulation_name}-{prod_name}.png')


def generate_production_lines(machine):
    amount_pl = machine.production_lines
    production_lines = machine.lines_list
    products = machine.products_list

    product = products.first
    production_lines_matrix = LinkedList()
    while product.next is not None:
        for i in range(int(amount_pl)):
            assemble_line = DoubleLinkedList()
            production_line = production_lines.get(i)
            for j in range(int(production_line.components_q)):
                assemble_line.insert(Component(False, f"C{j+1}", False))
            production_lines_matrix.insert(assemble_line, f"L{production_line.number}")

        while not product.data.assemble_q.is_empty():
            component = product.data.assemble_q.dequeue()
            split_line = component.data.split('p')
            line = split_line[0]
            component_name = split_line[1]
            component_name = component_name.replace("C", "")
            component_num = int(component_name)
            components = production_lines_matrix.get_by_name(line)
            item = components.get(component_num-1)
            item.to_assembled = True
        product.production_matrix = production_lines_matrix
        product = product.next


def generate_simulation(machine, p_to_simulate):
    products = machine.products_list
    product = products.first
    production_lines = LinkedList()
    while product.next is not None and product.name != p_to_simulate:
        product = product.next
    production_matrix = product.production_matrix
    assemble_queue = product.assemble_q

    time = 1
    while not assemble_queue.is_empty():
        component = assemble_queue.dequeue()
        print(component.name)
