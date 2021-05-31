class Fase():
    def __init__(self):
        self.fase = 0
        self.avancar_fase()
    def avancar_fase(self):
        self.fase += 1 
        self.mapa = self.excel_txt2mapa('mapa{}.txt'.format(self.fase))
        
    def espelha_mapa(self,l):
        l_2 = []
        for i in range(len(l)):
            l_2.append(list(reversed(l[i])))
        for a in range(len(l_2)):
            for b in range(len(l_2[a])):
                if l_2[a][b] == 1:
                    l[a].append(2)
                elif l_2[a][b] == 2:
                    l[a].append(1)
                else:
                    l[a].append(l_2[a][b])
        return l
    # Transforma um excel salvo em txt nas configurações de obstáculos da fase
    def excel_txt2mapa(self,file_name):
        with open(file_name, 'r') as file:
            file = file.readlines()
            f = []
            for linha in range(len(file)):
                f.append([])
                c = 0
                while c < len(file[linha]):
                    if file[linha][c] != '\t':
                        if file[linha][c] != '\n':
                            if file[linha][c] != ' ':
                                if file[linha][c] == '-':
                                    f[linha].append(file[linha][c]+file[linha][c+1])
                                    c += 1
                                else:
                                    f[linha].append(file[linha][c])
                    c += 1
                i = 0
                while i < len(f):
                    if f[i] == []:
                        f.remove(f[i])
                    else:
                        i += 1
        for linha in f:
            for num in range(len(linha)):
                linha[num] = int(linha[num])
        return self.espelha_mapa(f)
        