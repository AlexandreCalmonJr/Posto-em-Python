import combustivel as cb
import pagamento as pg

historico_abastecimentos = []


def calcularValorTotal(litros, valor_por_litro):
    """Calcula o valor total do abastecimento sem desconto"""
    return litros * valor_por_litro


def calcularDesconto(valor_total, percentual=10):
    """Calcula o valor do desconto (padrão 10%)"""
    return valor_total * (percentual / 100)


def realizarAbastecimento():
    """Realiza um novo abastecimento"""
    print("=== NOVO ABASTECIMENTO ===\n")
    
    # Listar combustíveis disponíveis
    cb.listarCombustiveis()
    
    if not cb.combustiveis:
        print("É necessário cadastrar combustíveis antes de abastecer.\n")
        return
    
    # Selecionar combustível
    codigo_combustivel = input("Informe o código do combustível: ")
    combustivel_dados = cb.obterCombustivel(codigo_combustivel)
    
    if not combustivel_dados:
        print("Combustível não encontrado.\n")
        return
    
    # Informar quantidade
    try:
        litros = float(input("Quantidade em litros: "))
        if litros <= 0:
            print("Quantidade deve ser maior que zero.\n")
            return
    except ValueError:
        print("Valor inválido.\n")
        return
    
    # Selecionar forma de pagamento
    codigo_pagamento = pg.selecionarFormaPagamento()
    
    # Calcular valores
    valor_total = calcularValorTotal(litros, combustivel_dados['valor_litro'])
    tem_desconto = pg.verificarDesconto(codigo_pagamento)
    
    if tem_desconto:
        desconto = calcularDesconto(valor_total)
        valor_final = valor_total - desconto
    else:
        desconto = 0
        valor_final = valor_total
    
    # Registrar abastecimento no histórico
    registro = {
        "combustivel": combustivel_dados['nome'],
        "valor_litro": combustivel_dados['valor_litro'],
        "litros": litros,
        "forma_pagamento": pg.obterNomePagamento(codigo_pagamento),
        "valor_total": valor_total,
        "desconto": desconto,
        "valor_final": valor_final
    }
    
    historico_abastecimentos.append(registro)
    
    # Exibir recibo
    exibirRecibo(registro)


def exibirRecibo(registro):
    """Exibe o recibo do abastecimento"""
    print("\n" + "="*50)
    print("--- Registro de Abastecimento ---")
    print(f"Tipo de Combustível: {registro['combustivel']}")
    print(f"Valor por litro: R$ {registro['valor_litro']:.2f}")
    print(f"Quantidade: {registro['litros']:.1f} litros")
    print(f"Forma de pagamento: {registro['forma_pagamento']}")
    
    if registro['desconto'] > 0:
        print(f"Desconto aplicado: R$ {registro['desconto']:.2f}")
    
    print(f"Total a pagar: R$ {registro['valor_final']:.2f}")
    print("="*50 + "\n")


def listarHistorico():
    """Lista o histórico de abastecimentos"""
    if not historico_abastecimentos:
        print("Nenhum abastecimento realizado.\n")
        return
    
    print("=== HISTÓRICO DE ABASTECIMENTOS ===\n")
    
    total_geral = 0
    
    for i, registro in enumerate(historico_abastecimentos, 1):
        print(f"--- Abastecimento #{i} ---")
        print(f"Combustível: {registro['combustivel']}")
        print(f"Litros: {registro['litros']:.1f}")
        print(f"Pagamento: {registro['forma_pagamento']}")
        print(f"Total: R$ {registro['valor_final']:.2f}")
        print()
        
        total_geral += registro['valor_final']
    
    print(f"Total geral de abastecimentos: R$ {total_geral:.2f}\n")
