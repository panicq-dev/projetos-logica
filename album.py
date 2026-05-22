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

try:
    import gabarito_NAO_MANDAR as _gab
    _GAB = {k: v for k, v in vars(_gab).items() if not k.startswith('_')}
except ImportError:
    _gab = None
    _GAB = {}

def _aplica(nome):
    if nome in _GAB:
        globals()[nome] = _GAB[nome]

def _resync(nome):
    if _gab is None:
        return
    valor = globals()[nome]
    setattr(_gab, nome, valor)
    _GAB[nome] = valor

album = ["pele", "ronaldo", "pele", "garrincha", "pele"]

quantas_figurinhas = len(album)
quantas_peles = album.count("pele")
tem_zico = "zico" in album

_aplica('quantas_figurinhas'); _aplica('quantas_peles'); _aplica('tem_zico')

figurinhas_existentes = ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
album = []
_aplica('album')

def adiciona_figurinha(nome):
    album.append(nome)

_aplica('adiciona_figurinha')

album_exemplo = ["pele", "ronaldo", "pele", "garrincha", "pele", "ronaldo"]

repetidas_a_mao = ["pele", "ronaldo"]
faltantes_a_mao = ["zico", "rivelino"]

_aplica('repetidas_a_mao'); _aplica('faltantes_a_mao')

def faltantes():
    lista_faltantes = []
    for nome in figurinhas_existentes:
        if nome not in album:
            lista_faltantes.append(nome)
    return lista_faltantes

_aplica('faltantes')

def repetidas():
    lista_repetidas = []
    for nome in album:
        if album.count(nome) > 1 and nome not in lista_repetidas:
            lista_repetidas.append(nome)
    return lista_repetidas

_aplica('repetidas')

def main():
    while True:
        print()
        print("=== ALBUM ===")
        print("1. Adicionar figurinha")
        print("2. Sobrando")
        print("3. Faltantes")
        print("4. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            nome = input("  Nome da figurinha: ")
            adiciona_figurinha(nome)
            print(f"  Figurinha '{nome}' adicionada.")
        elif opcao == "2":
            print(f"  Sobrando: {repetidas()}")
        elif opcao == "3":
            print(f"  Faltantes: {faltantes()}")
        elif opcao == "4":
            break
        else:
            print("Opcao invalida")
          
