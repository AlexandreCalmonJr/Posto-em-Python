formas_pagamento = {
    "1": {"nome": "Dinheiro", "desconto": True},
    "2": {"nome": "PIX", "desconto": True},
    "3": {"nome": "Cartão de Crédito", "desconto": False},
    "4": {"nome": "Cartão de Débito", "desconto": True}
}


def listarFormasPagamento():
    """Lista todas as formas de pagamento disponíveis"""
    print("=== FORMAS DE PAGAMENTO ===")
    for codigo, dados in formas_pagamento.items():
        desconto_info = "(10% de desconto)" if dados['desconto'] else ""
        print(f"{codigo} - {dados['nome']} {desconto_info}")
    print()


def selecionarFormaPagamento():
    """Permite ao usuário selecionar uma forma de pagamento"""
    listarFormasPagamento()
    
    while True:
        opcao = input("Escolha a forma de pagamento (1-4): ")
        if opcao in formas_pagamento:
            return opcao
        else:
            print("Opção inválida. Tente novamente.\n")


def verificarDesconto(codigo_pagamento):
    """Verifica se a forma de pagamento tem direito a desconto"""
    if codigo_pagamento in formas_pagamento:
        return formas_pagamento[codigo_pagamento]['desconto']
    return False


def obterNomePagamento(codigo_pagamento):
    """Retorna o nome da forma de pagamento"""
    if codigo_pagamento in formas_pagamento:
        return formas_pagamento[codigo_pagamento]['nome']
    return "Desconhecido"
