combustiveis = {}


def cadastrarCombustivel():
    codigo = input("Código do combustível: ")
    nome = input("Nome do combustível (Ex: Gasolina, Etanol, Diesel): ")
    valor_litro = float(input("Valor por litro (R$): "))
    
    combustiveis[codigo] = {
        "nome": nome,
        "valor_litro": valor_litro
    }
    
    print("Combustível cadastrado com sucesso.\n")


def listarCombustiveis():
    if not combustiveis:
        print("Nenhum combustível cadastrado.\n")
        return
    
    print("=== COMBUSTÍVEIS CADASTRADOS ===")
    for codigo, dados in combustiveis.items():
        print(f"Código: {codigo} | Nome: {dados['nome']} | Valor/Litro: R$ {dados['valor_litro']:.2f}")
    print()


def pesquisarCombustivel():
    codigo = input("Informe o código do combustível: ")
    if codigo in combustiveis:
        dados = combustiveis[codigo]
        print(f"Nome: {dados['nome']}")
        print(f"Valor por litro: R$ {dados['valor_litro']:.2f}\n")
        return True
    else:
        print("Combustível não encontrado.\n")
        return False


def alterarCombustivel():
    codigo = input("Informe o código do combustível para alterar: ")
    if codigo in combustiveis:
        nome = input("Novo nome: ")
        valor_litro = float(input("Novo valor por litro (R$): "))
        
        combustiveis[codigo] = {
            "nome": nome,
            "valor_litro": valor_litro
        }
        
        print("Combustível alterado com sucesso.\n")
    else:
        print("Combustível não encontrado.\n")


def excluirCombustivel():
    codigo = input("Informe o código do combustível para excluir: ")
    if codigo in combustiveis:
        confirmacao = input(f"Tem certeza que deseja excluir '{combustiveis[codigo]['nome']}'? (s/n): ").lower()
        if confirmacao == 's':
            del combustiveis[codigo]
            print("Combustível excluído com sucesso.\n")
        else:
            print("Exclusão cancelada.\n")
    else:
        print("Combustível não encontrado.\n")


def obterCombustivel(codigo):
    """Retorna os dados de um combustível pelo código"""
    return combustiveis.get(codigo)
