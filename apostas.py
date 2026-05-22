import hashlib

def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
        valor = [str(a) for a in valor]
        valores = [sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True

apostas_exemplo = [["lakers", 10], ["vasco", 5], ["lakers", 3]]
resultados_exemplo = [["lakers", True], ["vasco", False]]

item_da_primeira_aposta = apostas_exemplo[0][0]
valor_da_primeira_aposta = apostas_exemplo[0][1]
quantas_apostas_marcos = len(apostas_exemplo)
lakers_ganhou = resultados_exemplo[0][1]

ganho_marcos_a_mao = 26

apostas_exemplo = [["lakers", 3], ["vasco", 50], ["vasco", 13]]
ganho_dalva_a_mao = 6

def aposta(saldo, apostas, item, valor):
    apostas.append([item, valor])
    return saldo - valor

def ganhou(item, resultados):
    for resultado in resultados:
        if resultado[0] == item:
            return resultado[1]
    return False

def novo_saldo(saldo, apostas, resultados):
    for ap in apostas:
        if ganhou(ap[0], resultados):
            saldo += ap[1] * 2
    return saldo

def apostas_pendentes(apostas, resultados):
    pendentes = []
    for ap in apostas:
        achou = False
        for res in resultados:
            if ap[0] == res[0]:
                achou = True
                break
        if not achou:
            pendentes.append(ap)
    return pendentes

saldo_marcos = 0
saldo_dalva = 0
apostas_marcos = []
apostas_dalva = []

saldo_marcos = saldo_marcos + 100
saldo_dalva = saldo_dalva + 200

saldo_marcos = aposta(saldo_marcos, apostas_marcos, "lakers", 10)
saldo_marcos = aposta(saldo_marcos, apostas_marcos, "vasco", 5)

saldo_dalva = aposta(saldo_dalva, apostas_dalva, "palmeiras", 30)
saldo_dalva = aposta(saldo_dalva, apostas_dalva, "lakers", 50)

resultados = [["lakers", True], ["palmeiras", False]]

saldo_final_marcos_previsto = 105
saldo_final_dalva_previsto = 220

saldo_marcos = novo_saldo(saldo_marcos, apostas_marcos, resultados)
apostas_marcos = apostas_pendentes(apostas_marcos, resultados)

saldo_dalva = novo_saldo(saldo_dalva, apostas_dalva, resultados)
apostas_dalva = apostas_pendentes(apostas_dalva, resultados)

def main():
    saldo_marcos = 0
    saldo_dalva = 0
    apostas_marcos = []
    apostas_dalva = []

    while True:
        print()
        print("=== APOSTAS ===")
        print(f"saldo Marcos: {saldo_marcos} | apostas: {apostas_marcos}")
        print(f"saldo Dalva:  {saldo_dalva} | apostas: {apostas_dalva}")
        print("1. Marcos deposita")
        print("2. Marcos aposta")
        print("3. Dalva deposita")
        print("4. Dalva aposta")
        print("5. Resolver items")
        print("6. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            valor = int(input("  Valor do deposito: "))
            saldo_marcos = saldo_marcos + valor
        elif opcao == "2":
            item = input("  Item: ")
            valor = int(input("  Valor: "))
            saldo_marcos = aposta(saldo_marcos, apostas_marcos, item, valor)
        elif opcao == "3":
            valor = int(input("  Valor do deposito (Dalva): "))
            saldo_dalva = saldo_dalva + valor
        elif opcao == "4":
            item = input("  Item: ")
            valor = int(input("  Valor: "))
            saldo_dalva = aposta(saldo_dalva, apostas_dalva, item, valor)
        elif opcao == "5":
            resultados = []
            while True:
                item = input("  Item resolvido (ou ENTER para terminar): ")
                if item == "":
                    break
                resultado_str = input(f"    {item} ganhou? (s/n): ")
                resultado = (resultado_str == "s")
                resultados.append([item, resultado])
            
            saldo_marcos = novo_saldo(saldo_marcos, apostas_marcos, resultados)
            apostas_marcos = apostas_pendentes(apostas_marcos, resultados)
            
            saldo_dalva = novo_saldo(saldo_dalva, apostas_dalva, resultados)
            apostas_dalva = apostas_pendentes(apostas_dalva, resultados)
        elif opcao == "6":
            break
        else:
            print("Opcao invalida")
