class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def gravar(self, dados):
        # a é para append
        # r é para read
        # w é write
        with open(self.arquivo, 'a') as file:
            file.write(dados + '\n')

    def ler(self):
        with open(self.arquivo, 'r') as file:
            texto = ""
            for linha in file:
                texto += linha
                print(linha)
        return texto
    
    def lerLinhas(self):
        arq = open(self.arquivo, 'r')
        linhas = arq.readlines()
        arq.close()
        return linhas
    
    def letTudo(self):
        arq = open(self.arquivo, 'r')
        texto = arq.read()
        arq.close()
        return texto
    
    def lerWhile(self):
        linhas = []
        arq = open(self.arquivo, 'r')
        linha = arq.readline()
        while linha:
            linhas.append(linha)
        arq.close()
        return linhas