saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("Menu")
    print("[d] Depósito")
    print("[s] Saque")
    print("[e] Extrato")
    print("[q] Sair")
    print("*" * 30)

    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedidos.")
        else:
            valor_saque = float(input("Informe o valor de saque: "))
            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n****************EXTRATO*****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("********************************************")

    elif opcao == "q":
        print("Obrigado por escolher o 777 Bank.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
