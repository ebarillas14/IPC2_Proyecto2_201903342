class Component:
    def __init__(self, t_b_a, a):
        self.to_assembled = t_b_a
        self.assembled = a


class ProductionLine:
    def __init__(self, number, components_q, assemble_t):
        self.number = number
        self.components_q = components_q
        self.assemble_t = assemble_t


class Product:
    def __init__(self, name, assemble_ins):
        self.name = name
        self.assemble_q = assemble_ins


class Machine:
    def __init__(self, prod_lines_am, prod_lines_list, prod_list):
        self.production_lines = prod_lines_am
        self.lines_list = prod_lines_list
        self.products_list = prod_list


class Simulation:
    def __init__(self, name, products_list):
        self.name = name
        self.prod_list = products_list

    def get_name(self):
        return self.name

    def get_products(self):
        return self.prod_list
