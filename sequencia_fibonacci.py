class Fibonacci:
    def __iter__(self) -> None:
        self.anterior: int = 0
        self.proximo: int = 1
        self.con: int = 1
        self.iteracao: None = None
        self.fibonacci: list = []


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


fi = Fibonacci()
next(fi)
