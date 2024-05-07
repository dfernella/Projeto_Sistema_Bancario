print ("====== Bem-Vindo ao WeBank ======\n")

print ("== Selecione uma opção do menu ==")

menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques alcançado.")
        else:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif valor > 0:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print("Saque realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato:
            for movimento in extrato:
                print(movimento)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")
        print("==========================================")

    elif opcao == "q":
        print("Saindo do programa...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
