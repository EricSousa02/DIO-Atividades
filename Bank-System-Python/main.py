# Inicializa variáveis globais
saldo = 0
limite = 500
extrato_bancario = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para depósito
def depositar(valor):
    global saldo, extrato_bancario
    if valor > 0:
        saldo += valor
        extrato_bancario += f"Depósito : R${valor:.2f}\n"
    else:
        print("O valor fornecido é inválido")

# Função para saque
def sacar(valor):
    global saldo, extrato_bancario, numero_saques
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedidos = numero_saques >= LIMITE_SAQUES

    if saldo_excedido:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif limite_excedido:
        print("Operação falhou! O valor do saque excede o limite.")
    elif saques_excedidos:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato_bancario += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor especificado é inválido.")

# Função para exibir o extrato bancário
def exibir_extrato():
    global saldo, extrato_bancario
    print("EXTRATO BANCÁRIO".center(20, "-"))
    if not extrato_bancario:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato_bancario)
    print(f"\nSaldo: R${saldo:.2f}")

# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Loop principal do menu
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida.")
