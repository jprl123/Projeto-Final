with open('mapa1.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    f = []
    for linha in linhas:
        f.append(linha[:4*32])
    f = str(f)
    f = f.replace('[', '')
    f = f.replace(']', '')
    f = f.replace("'", '')
    f = f.replace("\\n", '')
    f = f.replace(",", '\n')
    f = f.replace("    ", '')
    f = str(f)
with open('mapa11.txt', 'w') as x:
    x.write(f)