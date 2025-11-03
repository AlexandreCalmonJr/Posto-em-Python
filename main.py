import combustivel as cb
import pagamento as pg
import abastecimento as ab


def menuPrincipal():
    """Menu principal do sistema de controle de abastecimento"""
    while True:
        print("="*50)
        print("SISTEMA DE CONTROLE DE ABASTECIMENTO")
        print("="*50)
        print("\n=== MENU DE COMBUSTÍVEIS ===")
        print("1 - Cadastrar Combustível")
        print("2 - Listar Combustíveis")
        print("3 - Pesquisar Combustível")
        print("4 - Alterar Combustível")
        print("5 - Excluir Combustível")
        
        print("\n=== MENU DE ABASTECIMENTO ===")
        print("6 - Realizar Abastecimento")
        print("7 - Histórico de Abastecimentos")
        
        print("\n=== SISTEMA ===")
        print("0 - Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        print()
        
        if opcao == "1":
            cb.cadastrarCombustivel()
        elif opcao == "2":
            cb.listarCombustiveis()
        elif opcao == "3":
            cb.pesquisarCombustivel()
        elif opcao == "4":
            cb.alterarCombustivel()
        elif opcao == "5":
            cb.excluirCombustivel()
        elif opcao == "6":
            ab.realizarAbastecimento()
        elif opcao == "7":
            ab.listarHistorico()
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menuPrincipal()
