class Fibonacci:
    def __iter__(self):
        self.anterior: int = 0
        self.proximo: int = 1
        self.con: int = 1
        self.iteracao = self.iteracao
        self.fibonacci: list = []
        return self


    def __next__(self) -> list:
        self.anterior: int = 0
        self.proximo: int = 1
        self.fibonacci: list = []
        self.con: int = 1
        while True:
            try:
                self.iteracao = int(input("Quantos números na sequência Fibonacci? "))
                break
            except (ValueError, TypeError):
                print('Erro! Por favor, digite um número.')
        if self.iteracao == 0:
            print('O valor recebido foi zero. Operação encerrada.')
        else:
            while self.con <= self.iteracao:
                self.fibonacci.append(self.anterior)
                self.anterior, self.proximo = self.proximo, self.anterior + self.proximo
                self.con += 1
        return self.fibonacci
    def dic_sequencia(self,):
        valor ={k:v for k,v in enumerate(self.fibonacci)}
        return valor


fi = Fibonacci()
next(fi)
fi.dic_sequencia()
