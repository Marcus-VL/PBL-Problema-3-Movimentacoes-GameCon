from classes import Participante, Transacao
from funcoes import cadastro, realizar_transacao, cons_historico, cons_qt_trans

operando = True

while operando:
    print("\
    Opções:\" \
  \n 1-Cadastrar Usuário.\
  \n 2- Realizar Transação.\
  \n 3-Consultar Transações.\
  \n 4-Sair.\
    ")
    opcao = int(input("Insira sua opção de escolha: "))

    match opcao:
        case 1:
            #Cadastro
            pass
        case 2:
            #Nova Transação
            pass
        case 3:
            #Consultando
            escolhendo_consulta = True
            while escolhendo_consulta:
                print("\
                Opções de Consulta:\" \
              \n 1 - Histórico de Participante específico.\
              \n 2 - Participantes com determinada quantidade de transações.\
              \n 3 - Retornar ao menu.\
                    ")
                opcao_consulta = int(input("Insira sua opção de escolha: "))
                if opcao_consulta in (1, 2, 3):
                    escolhendo_consulta = False
                else:
                    print("Opção Incorreta")

            match opcao_consulta:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
        case 4:
            print("\nPrograma Encerrado.")
            operando = False
        case _:
            print("Opção Incorreta.")