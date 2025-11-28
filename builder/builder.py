class Hamburger:
    def __init__(self):
        self.pao = None
        self.carne = None
        self.queijo = None
        self.bacon = False
        self.salada = False
        self.maionese = False

    def __str__(self):
        detalhespedido = [f"Pao: {self.pao}", f"Carne: {self.carne}"]
        if self.queijo: detalhespedido.append(f"Queijo: {self.queijo}")
        if self.bacon: detalhespedido.append("Extra: Bacon")
        if self.salada: detalhespedido.append("Extra: Salada")
        if self.maionese: detalhespedido.append("Extra: Maionese")
        return "\n".join(detalhespedido)

class BuilderHamburger:
    def __init__(self):
        self.hamburger = Hamburger()

    def reset(self):
        self.hamburger = Hamburger()
        return self

    def set_pao(self, tipo):
        self.hamburger.pao = tipo
        return self

    def set_carne(self, tipo):
        self.hamburger.carne = tipo
        return self
    
    def add_queijo(self, tipo):
        self.hamburger.queijo = tipo
        return self

    def add_bacon(self):
        self.hamburger.bacon = True
        return self

    def add_salada(self):
        self.hamburger.salada = True
        return self

    def add_maionese(self):
        self.hamburger.maionese = True
        return self

    def build(self):
        produto = self.hamburger
        self.reset()
        return produto

class Diretor:
    def fazer_xbacon(self, builder):
        builder.reset()
        builder.set_pao("Brioche")
        builder.set_carne("Picanha")
        builder.add_queijo("Cheddar")
        builder.add_bacon()
        builder.add_maionese()

    def fazer_xsalada(self, builder):
        builder.reset()
        builder.set_pao("Integral")
        builder.set_carne("Frango")
        builder.add_queijo("Prato")
        builder.add_salada()
        builder.add_maionese()
