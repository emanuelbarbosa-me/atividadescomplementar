class Produto:
    gtdprod = 0

    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.gtdprod += 1

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco
        return self.__preco

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo
        return self.__codigo


class GerenciadorProduto:
    def __init__(self):
        self.listProd = []

    def add_produto(self, produto):
        if isinstance(produto, Produto):
            self.listProd.append(produto)
        return self.listProd

    def remove_produto(self, codigo):
        for pro in self.listProd:
            if codigo == pro.get_codigo():
                self.listProd.remove(pro)
                break

    def listar_produtos(self):
        for pro in self.listProd:
            print(f"Código: {pro.get_codigo()}, Preço: {pro.get_preco()}")

    def precototal(listProd):
        precototal = 0 
        for i in self.listaprod:
            if codigo == pro.getcodigo():
                precototal += self.listProd

        for i in self.codigo:
            if listProd == pro.getlistProd:
                precototal += self.codigo
                return precototal
 
p1 = Produto(12, 123)
p2 = Produto(13, 456)
p3 = Produto(16, 789)

gerenciador = GerenciadorProduto()
print(gerenciador.add_produto(p1))
print(gerenciador.add_produto(p2))
print(gerenciador.add_produto(p3))

gerenciador.listar_produtos()

gerenciador.remove_produto(13)
print("Após remover o produto com código 13:")
gerenciador.listar_produtos()

lista = [123, 456, 789]

