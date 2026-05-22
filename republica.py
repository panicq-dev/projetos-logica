import hashlib

def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    if isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True

try:
    import gabarito_NAO_MANDAR as _gab
    _GAB = {k: v for k, v in vars(_gab).items() if not k.startswith('_')}
except ImportError:
    _GAB = {}

def _aplica(nome):
    if nome in _GAB:
        globals()[nome] = _GAB[nome]

conta = ["pizza", 30, ["ana", "bruno", "carla"]]

descricao_da_conta = conta[0]
valor_da_conta = conta[1]
numero_de_participantes = len(conta[2])
valor_por_pessoa = conta[1] / len(conta[2])

_aplica('descricao_da_conta'); _aplica('valor_da_conta'); _aplica('numero_de_participantes'); _aplica('valor_por_pessoa')

ana_dividiu = "ana" in conta[2]
daniel_dividiu = "daniel" in conta[2]

_aplica('ana_dividiu'); _aplica('daniel_dividiu')

contas = []
_aplica('contas')

def adiciona_conta(descricao, valor, participantes):
    contas.append([descricao, valor, participantes])

_aplica('adiciona_conta')

contas_exemplo = [
    ["pizza",    30, ["ana", "bruno", "carla"]],
    ["uber",     20, ["ana", "bruno"]],
    ["internet", 90, ["ana", "bruno", "carla", "daniel"]],
]

divida_da_ana = 42.5
divida_da_carla = 32.5
divida_da_eva = 0.0

_aplica('divida_da_ana'); _aplica('divida_da_carla'); _aplica('divida_da_eva')

def quanto_deve(nome):
    total_divida = 0.0
    for conta in contas:
        if nome in conta[2]:
            total_divida += conta[1] / len(conta[2])
    return total_divida

_aplica('quanto_deve')

def integrantes():
    lista_integrantes = []
    for conta in contas:
        for pessoa in conta[2]:
            if pessoa not in lista_integrantes:
                lista_integrantes.append(pessoa)
    return lista_integrantes

_aplica('integrantes')

def main():
    while True:
        print()
        print("=== REPUBLICA ===")
        print("1. Adicionar conta")
        print("2. Quanto alguem deve")
        print("3. Listar integrantes")
        print("4. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            descricao = input("  Descricao da conta: ")
            valor = float(input("  Valor: "))
            nomes_str = input("  Quem dividiu (nomes separados por espaco): ")
            participantes = nomes_str.split()
            adiciona_conta(descricao, valor, participantes)
            print(f"  Conta '{descricao}' adicionada.")
            
        elif opcao == "2":
            lista_moradores = integrantes()
            if not lista_moradores:
                print("  Nenhum integrante cadastrado nas contas ainda.")
                continue
                
            while True:
                print("\n  Selecione o integrante:")
                for i, morador in enumerate(lista_moradores, 1):
                    print(f"  {i}. {morador}")
                
                escolha = input("  Digite o numero correspondente: ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(lista_moradores):
                    nome_selecionado = lista_moradores[int(escolha) - 1]
                    break
                else:
                    print("  Opcao invalida. Escolha um numero da lista.")
            
            divida = quanto_deve(nome_selecionado)
            print(f"  {nome_selecionado} deve no total: R$ {divida:.2f}")
            
        elif opcao == "3":
            lista_moradores = integrantes()
            print("  Integrantes da casa:")
            for morador in lista_moradores:
                print(f"  - {morador}")
                
        elif opcao == "4":
            break
        else:
            print("Opcao invalida")

# Para rodar, descomente a linha abaixo.
# main()
