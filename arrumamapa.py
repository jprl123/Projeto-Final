with open('mapa33.txt', 'r') as arquivo:
    arquivo = arquivo.readlines()
    for i in arquivo:
        for j in i:
            while len(j) < 32*4:
                j = j.remove(j[-1])
    