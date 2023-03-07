import datetime
import Textos

class BombaCombustivel:

    # Método construtor necessário para iniciar uma bomba, com os argumentos tipo,quantidade de combustível e valor por litro.
    def __init__(self,TipoCombustivel, ValorLitro, QuantidadeDeCombustivel):
        self.TipoCombustivel = TipoCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeDeCombustivel = QuantidadeDeCombustivel

    # Método para mostrar a situação da bomba, em relação ao tipo, quantidade de combustível e o valor por litro.
    def mostrarStatus(self):
        print("Tipo de combustivel: ", self.TipoCombustivel, "\n Valor por litro: R$ ",self.ValorLitro,
              "\n Quantidade de combustivel na bomba: ", self.QuantidadeDeCombustivel, "litros")

    # Metodo para realizar o abastecimento
    def Abastecimento(self):

        tipo = ""

        while tipo != "l" or "v":
            tipo = input("Qual a forma de abastecimento, digite v - para valor, l - para litros ou c - para cancelar: ")

            # Condição quando a referencia para o abastecimento for por valor.
            if tipo == "v":
                valor =float(input("Qual o valor? "))
                litros = valor / self.ValorLitro
                data = datetime.datetime.now()

                # condicional para não permitir abastecer mais do que a bomba tem de combustível disponível
                if litros > self.QuantidadeDeCombustivel:
                    print("Quantidade de combustivel excede o disponível na bomba")
                else:
                    print("Quantidade de combustivel abastecido: ", litros,"litros","\n""Data do abastecimento: ", data.strftime("%x"))
                    print("Obrigado. Volte Sempre!") # Mensagem de despedida
                    self.QuantidadeDeCombustivel = self.QuantidadeDeCombustivel - litros
                    break

            # Condição quando a referencia para o abastecimento for por litros.
            elif tipo == "l":
                litros = float(input("Qual quantidade em litros? "))
                valorAPagar = litros * self.ValorLitro
                data = datetime.datetime.now()

                # condicional para não permitir abastecer mais do que a bomba tem de combustível disponível
                if litros > self.QuantidadeDeCombustivel:
                    print("Quantidade de combustivel excede o disponível na bomba")
                else:
                    print("Valor a pagar R$ ", valorAPagar,"\n""Data do abastecimento: ", data.strftime("%x"))
                    print("Obrigado. Volte Sempre!") # Mensagem de despedida
                    self.QuantidadeDeCombustivel = self.QuantidadeDeCombustivel - litros
                    break
            elif tipo == "c":
                print("Operação cancelada.")
                break
            else:
                print("Informação incorreta.")



    # Metodo para alterar o tipo de combustível da bomba.

    def alterarCombustivel(self, combustivel):
        self.TipoCombustivel = combustivel
        print("Combustivel alterado com sucesso para ",self.TipoCombustivel)

    # Metodo para alterar a quantidade de combustível disponível na bomba.

    def alterarQuantidadeCombustivel(self,quantidade):
         self.QuantidadeDeCombustivel = quantidade
         print("Quantidade de combustivel alterada com sucesso para ", self.QuantidadeDeCombustivel, "litros.")

         # Metodo para alterar a quantidade de combustível disponível na bomba.

    def alterarValorCombustivel(self, valor):
        self.ValorLitro = valor
        print("Valor por litro alterado com sucesso para R$", self.ValorLitro)

class Menu (BombaCombustivel):
    def __init__(self, TipoCombustivel, ValorLitro, QuantidadeDeCombustivel,senha):
        self.senha = senha
        super().__init__(TipoCombustivel, ValorLitro, QuantidadeDeCombustivel)

    # Metodo para cadastrar uma nova senha de administrador
    def cadastrarSenha(self):

        senhaAdm = input("Digite a senha do adminitrador: ")

        if senhaAdm == self.senha:
            senhaAdm = input("Cadastre a sua senha: ")
            self.senha = senhaAdm
            print("Senha alterada com sucesso.","\n")
        else:
            print("Senha incorreta","\n")

    def indice(self):

        num = 0

        while num != 7:
            Textos.menu()
            print("\n")
            num = str(input("Escolha a sua opção: "))
            print("\n")
            if num == "1":
                b1.mostrarStatus()
                print("\n")
            elif num == "2":
                b1.Abastecimento()
                print("\n")
            elif num == "3":
                senhaAdm = input("Digite sua senha de Adm: ")

                if self.senha == senhaAdm:
                    v = input("Digite o nome do novo combustível: ")
                    b1.alterarCombustivel(v)
                    print("\n")
                else:
                    print("Senha incorreta","\n")

            elif num == "4":
                senhaAdm = input("Digite sua senha de Adm: ")

                if self.senha == senhaAdm:
                    q = int(input("Digite a quantidade de combustível disponível na bomba: "))
                    b1.alterarQuantidadeCombustivel(q)
                    print("\n")
                else:
                    print("Senha incorreta","\n")

            elif num == "5":
                senhaAdm = input("Digite sua senha de Adm: ")

                if self.senha == senhaAdm:
                    v = int(input("Digite o novo valor do combustível disponível na bomba: "))
                    b1.alterarValorCombustivel(v)
                    print("\n")
                else:
                    print("Senha incorreta","\n")
            elif num == "6":
                b1.cadastrarSenha()
            elif num == "7":
                break
            else:
                print("Opção inválida","\n")





b1 = Menu("Gasolina",5,1000,"2345")
b1.indice()













