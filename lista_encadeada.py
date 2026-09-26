from pessoa import chave_nome


class NoLista:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_final(self, pessoa):
        novo = NoLista(pessoa)
        if self.inicio is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def buscar(self, nome):
        chave = chave_nome(nome)
        atual = self.inicio
        while atual is not None:
            if chave_nome(atual.pessoa.nome) == chave:
                return atual.pessoa
            atual = atual.proximo
        return None

    def quantidade(self):
        return self.tamanho

    def pessoas(self):
        atual = self.inicio
        while atual is not None:
            yield atual.pessoa
            atual = atual.proximo
