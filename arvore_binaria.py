from pessoa import chave_nome


class NoArvore:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.chave = chave_nome(pessoa.nome)
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, pessoa):
        novo = NoArvore(pessoa)
        self.tamanho += 1
        if self.raiz is None:
            self.raiz = novo
            return
        atual = self.raiz
        while True:
            if novo.chave < atual.chave:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita

    def buscar(self, nome):
        chave = chave_nome(nome)
        atual = self.raiz
        while atual is not None:
            if chave == atual.chave:
                return atual.pessoa
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def remover(self, nome):
        chave = chave_nome(nome)
        pai = None
        atual = self.raiz
        while atual is not None and atual.chave != chave:
            pai = atual
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        if atual is None:
            return None

        removida = atual.pessoa
        if atual.esquerda is not None and atual.direita is not None:
            # dois filhos: o sucessor em ordem (menor da subarvore direita) ocupa o lugar
            pai_sucessor = atual
            sucessor = atual.direita
            while sucessor.esquerda is not None:
                pai_sucessor = sucessor
                sucessor = sucessor.esquerda
            atual.pessoa = sucessor.pessoa
            atual.chave = sucessor.chave
            if pai_sucessor is atual:
                pai_sucessor.direita = sucessor.direita
            else:
                pai_sucessor.esquerda = sucessor.direita
        else:
            filho = atual.esquerda if atual.esquerda is not None else atual.direita
            if pai is None:
                self.raiz = filho
            elif pai.esquerda is atual:
                pai.esquerda = filho
            else:
                pai.direita = filho
        self.tamanho -= 1
        return removida

    def minimo(self):
        atual = self.raiz
        if atual is None:
            return None
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.pessoa

    def maximo(self):
        atual = self.raiz
        if atual is None:
            return None
        while atual.direita is not None:
            atual = atual.direita
        return atual.pessoa

    def em_ordem(self):
        pilha = []
        atual = self.raiz
        while pilha or atual is not None:
            while atual is not None:
                pilha.append(atual)
                atual = atual.esquerda
            atual = pilha.pop()
            yield atual.pessoa
            atual = atual.direita

    def esta_vazia(self):
        return self.raiz is None
