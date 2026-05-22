import hashlib

def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
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

# ===== FASE 1 - Aquecimento: lendo uma palavra =====

palavra_exemplo = "banana"

primeira_letra = palavra_exemplo[0]
tamanho_da_palavra = len(palavra_exemplo)
quantas_letras_a = palavra_exemplo.count("a")
tem_z = "z" in palavra_exemplo
reveladas_iniciais = ["_"] * len(palavra_exemplo)

assert verifica(primeira_letra, 'c681e18b81edaf2b66dd22376734dba5992e362bc3f91ab225854c17'), 'primeira_letra incorreta'
assert verifica(tamanho_da_palavra, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'tamanho_da_palavra incorreta'
assert verifica(quantas_letras_a, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'quantas_letras_a incorreta'
assert verifica(tem_z, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'tem_z incorreta'
assert verifica(reveladas_iniciais, 'e3d6140c9c83b4f888489372e0653fd8d7cb9b8462a186016efc1b2e'), 'reveladas_iniciais incorreta'
print('Exercicio lendo uma palavra: OK')

palavra = "abacaxi"
reveladas = ["a", "_", "a", "_", "a", "_", "_"]

quantas_falta_revelar = reveladas.count("_")

assert verifica(quantas_falta_revelar, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'quantas_falta_revelar incorreta'
print('Exercicio calculo a mao: OK')


# ===== FASE 2 - A funcao revela_letra =====

def revela_letra(palavra, reveladas, letra):
    posicoes_reveladas = 0
    for i in range(len(palavra)):
        if palavra[i] == letra:
            reveladas[i] = letra
            posicoes_reveladas += 1
    return posicoes_reveladas

palavra_t = "banana"
reveladas_t = ["_", "_", "_", "_", "_", "_"]
n = revela_letra(palavra_t, reveladas_t, "a")
assert n == 3, f'revela_letra deveria retornar 3 (3 ocorrencias de a), retornou {n}'
assert reveladas_t == ["_", "a", "_", "a", "_", "a"], f'reveladas errado: {reveladas_t}'

n = revela_letra(palavra_t, reveladas_t, "n")
assert n == 2, f'revela_letra deveria retornar 2 (2 ocorrencias de n), retornou {n}'
assert reveladas_t == ["_", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'

reveladas_t = ["_", "_", "_", "_", "_", "_"]
n = revela_letra(palavra_t, reveladas_t, "z")
assert n == 0, f'revela_letra deveria retornar 0 (z nao aparece), retornou {n}'
assert reveladas_t == ["_", "_", "_", "_", "_", "_"], f'z nao deveria mudar reveladas, virou {reveladas_t}'

print('Exercicio revela_letra: OK')


# ===== FASE 3 - A funcao ganhou =====

def ganhou(reveladas):
    for x in reveladas:
        if x == "_":
            return False
    return True

assert ganhou(["_", "a", "_"]) == False, 'ganhou com underscores deveria ser False'
assert ganhou(["b", "a", "n", "a", "n", "a"]) == True, 'ganhou sem underscores deveria ser True'
assert ganhou(["_"]) == False, 'ganhou com so um underscore deveria ser False'
assert ganhou(["a", "_", "a"]) == False, 'ganhou com underscore no meio deveria ser False'

reveladas_antes = ["_", "a", "_"]
reveladas_copia = ["_", "a", "_"]
ganhou(reveladas_antes)
assert reveladas_antes == reveladas_copia, 'ganhou NAO deveria modificar reveladas'

print('Exercicio ganhou: OK')


# ===== FASE 4 - A funcao processa_chutes =====

def processa_chutes(palavra, reveladas, letras_tentadas, vidas, chutes):
    for letra in chutes:
        if letra in letras_tentadas:
            continue
        letras_tentadas.append(letra)
        revelou = revela_letra(palavra, reveladas, letra)
        if revelou == 0:
            vidas = vidas - 1
        if vidas == 0 or ganhou(reveladas):
            break
    return vidas

palavra_t = "banana"
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra=palavra_t, reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["a", "n"])
assert v == 6, f'sem erros, vidas deveria continuar 6, virou {v}'
assert reveladas_t == ["_", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'
assert letras_t == ["a", "n"], f'letras_tentadas errado: {letras_t}'

reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["a", "a", "a"])
assert v == 6, f'letras repetidas nao gastam vida, virou {v}'
assert letras_t == ["a"], f'letra repetida nao deveria entrar 2x in letras_tentadas: {letras_t}'
assert reveladas_t == ["_", "a", "_", "a", "_", "a"], f'reveladas errado: {reveladas_t}'

reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=3, chutes=["z", "x"])
assert v == 1, f'2 erros com 3 vidas deveriam deixar 1, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar (chutes errados): {reveladas_t}'
assert letras_t == ["z", "x"], f'letras_tentadas errado: {letras_t}'

reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=1, chutes=["z", "x", "y"])
assert v == 0, f'1 vida + 1 erro deveria zerar, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar: {reveladas_t}'
assert letras_t == ["z"], f'apos vidas=0, demais chutes deveriam ser ignorados (break): {letras_t}'

letras_t = []
reveladas_t = ["_"] * 6
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["b", "a", "n", "z"])
assert v == 6, f'ganhou sem erros, vidas deveriam continuar 6, virou {v}'
assert reveladas_t == ["b", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'
assert letras_t == ["b", "a", "n"], f'apos ganhar, "z" nao deveria entrar em letras_tentadas: {letras_t}'

reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=[])
assert v == 6, f'chutes vazios nao deveriam mudar vidas, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar (chutes vazios): {reveladas_t}'
assert letras_t == [], f'letras_tentadas nao deveria mudar (chutes vazios): {letras_t}'

print('Exercicio processa_chutes: OK')


# ===== FASE 5 - Simulacao lucas e heloisa =====

palavra_lucas = "banana"
reveladas_lucas = ["_"] * len(palavra_lucas)
letras_lucas = []
vidas_lucas = 6

palavra_heloisa = "abacaxi"
reveladas_heloisa = ["_"] * len(palavra_heloisa)
letras_heloisa = []
vidas_heloisa = 6

vidas_lucas_previsto = 6
vidas_heloisa_previsto = 5
quantas_reveladas_lucas = 5
quantas_reveladas_heloisa = 4

assert verifica(vidas_lucas_previsto, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'vidas_lucas_previsto incorreto'
assert verifica(vidas_heloisa_previsto, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'vidas_heloisa_previsto incorreto'
assert verifica(quantas_reveladas_lucas, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'quantas_reveladas_lucas incorreta'
assert verifica(quantas_reveladas_heloisa, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'quantas_reveladas_heloisa incorreta'
print('Exercicio previsao lucas e heloisa: OK')

vidas_lucas = processa_chutes(palavra=palavra_lucas, reveladas=reveladas_lucas,
                               letras_tentadas=letras_lucas, vidas=vidas_lucas,
                               chutes=["a", "n", "a"])
vidas_heloisa  = processa_chutes(palavra=palavra_heloisa, reveladas=reveladas_heloisa,
                               letras_tentadas=letras_heloisa, vidas=vidas_heloisa,
                               chutes=["a", "x", "z"])

assert vidas_lucas == 6, f'vidas_lucas deveria ser 6 (sem erros), virou {vidas_lucas}'
assert reveladas_lucas == ["_", "a", "n", "a", "n", "a"], f'reveladas_lucas errado: {reveladas_lucas}'
assert letras_lucas == ["a", "n"], f'letras_lucas errado: {letras_lucas}'

assert vidas_heloisa == 5, f'vidas_heloisa deveria ser 5 (1 erro: z), virou {vidas_heloisa}'
assert reveladas_heloisa == ["a", "_", "a", "_", "a", "x", "_"], f'reveladas_heloisa errado: {reveladas_heloisa}'
assert letras_heloisa == ["a", "x", "z"], f'letras_heloisa errado: {letras_heloisa}'

print('Exercicio simulacao lucas e heloisa: OK')
print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== FASE 6 - INTERFACE CLI =====

def main():
    palavra_lucas = "banana"
    reveladas_lucas = ["_"] * len(palavra_lucas)
    letras_lucas = []
    vidas_lucas = 6

    palavra_heloisa = "abacaxi"
    reveladas_heloisa = ["_"] * len(palavra_heloisa)
    letras_heloisa = []
    vidas_heloisa = 6

    while True:
        print()
        print("=== FORCA ===")
        print(f"lucas: {' '.join(reveladas_lucas)}  | vidas: {vidas_lucas} | tentadas: {letras_lucas}")
        print(f"heloisa:  {' '.join(reveladas_heloisa)}  | vidas: {vidas_heloisa} | tentadas: {letras_heloisa}")
        print("1. lucas chuta letra")
        print("2. heloisa chuta letra")
        print("3. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            letra = input("  Letra: ")
            vidas_lucas = processa_chutes(palavra_lucas, reveladas_lucas, letras_lucas, vidas_lucas, [letra])
            if vidas_lucas == 0:
                print(f"  lucas perdeu! A palavra era '{palavra_lucas}'")
                break
            if ganhou(reveladas_lucas):
                print(f"  lucas ganhou! A palavra era '{palavra_lucas}'")
                break
        elif opcao == "2":
            entrada_heloisa = input("  Letras (separadas por espaco): ")
            chutes_heloisa = entrada_heloisa.split()
            vidas_heloisa = processa_chutes(palavra_heloisa, reveladas_heloisa, letras_heloisa, vidas_heloisa, chutes_heloisa)
            if vidas_heloisa == 0:
                print(f"  heloisa perdeu! A palavra era '{palavra_heloisa}'")
                break
            if ganhou(reveladas_heloisa):
                print(f"  heloisa ganhou! A palavra era '{palavra_heloisa}'")
                break
        elif opcao == "3":
            break
        else:
            print("Opcao invalida")

# Para rodar a interface, descomente:
# main()
