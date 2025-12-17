from collections.abc import MutableMapping

class MapaBase(MutableMapping):
    class _Item:
        __slots__ = '_chave', '_valor'
        def __init__(self, k, v):
            self._chave = k
            self._valor = v
        def __eq__(self, outro):
            return self._chave == outro._chave
        def __ne__(self, outro):
            return not (self == outro)
        def __lt__(self, outro):
            return self._chave < outro._chave

class ArvoreBinariaEncadeada:
    class _No:
        __slots__ = '_elemento', '_pai', '_esquerdo', '_direito'
        def __init__(self, elemento, pai=None, esquerdo=None, direito=None):
            self._elemento = elemento
            self._pai = pai
            self._esquerdo = esquerdo
            self._direito = direito

    class Posicao:
        def __init__(self, container, no):
            self._container = container
            self._no = no
        def elemento(self):
            return self._no._elemento
        def __eq__(self, outro):
            return type(outro) is type(self) and outro._no is self._no
        def __ne__(self, outro):
            return not (self == outro)

    def _validar(self, pos):
        if not isinstance(pos, self.Posicao):
            raise TypeError('pos deve ser do tipo Posicao')
        if pos._container is not self:
            raise ValueError('pos não pertence a esta árvore')
        if pos._no._pai is pos._no: 
            raise ValueError('pos não é mais válida')
        return pos._no

    def _criar_posicao(self, no):
        return self.Posicao(self, no) if no is not None else None

    def __init__(self):
        self._raiz = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def raiz(self):
        return self._criar_posicao(self._raiz)

    def pai(self, pos):
        no = self._validar(pos)
        return self._criar_posicao(no._pai)

    def esquerdo(self, pos):
        no = self._validar(pos)
        return self._criar_posicao(no._esquerdo)

    def direito(self, pos):
        no = self._validar(pos)
        return self._criar_posicao(no._direito)

    def num_filhos(self, pos):
        no = self._validar(pos)
        total = 0
        if no._esquerdo is not None: total += 1
        if no._direito is not None: total += 1
        return total

    def _adicionar_raiz(self, e):
        if self._raiz is not None: raise ValueError('Raiz já existe')
        self._tamanho = 1
        self._raiz = self._No(e)
        return self._criar_posicao(self._raiz)

    def _adicionar_esquerdo(self, pos, e):
        no = self._validar(pos)
        if no._esquerdo is not None: raise ValueError('Filho esquerdo já existe')
        self._tamanho += 1
        no._esquerdo = self._No(e, no)
        return self._criar_posicao(no._esquerdo)

    def _adicionar_direito(self, pos, e):
        no = self._validar(pos)
        if no._direito is not None: raise ValueError('Filho direito já existe')
        self._tamanho += 1
        no._direito = self._No(e, no)
        return self._criar_posicao(no._direito)

    def _substituir(self, pos, e):
        no = self._validar(pos)
        antigo = no._elemento
        no._elemento = e
        return antigo

    def _deletar(self, pos):
        no = self._validar(pos)
        if self.num_filhos(pos) == 2: raise ValueError('pos tem dois filhos')
        filho = no._esquerdo if no._esquerdo else no._direito
        if filho is not None:
            filho._pai = no._pai
        if no is self._raiz:
            self._raiz = filho
        else:
            pai = no._pai
            if no is pai._esquerdo:
                pai._esquerdo = filho
            else:
                pai._direito = filho
        self._tamanho -= 1
        no._pai = no
        return no._elemento

    def esta_vazia(self):
        return len(self) == 0
    
    def eh_folha(self, pos):
        return self.num_filhos(pos) == 0

class MapaArvore(ArvoreBinariaEncadeada, MapaBase):
    class Posicao(ArvoreBinariaEncadeada.Posicao):
        def chave(self):
            return self.elemento()._chave
        def valor(self):
            return self.elemento()._valor

    def _busca_subarvore(self, pos, k):
        if k == pos.chave():
            return pos
        elif k < pos.chave():
            if self.esquerdo(pos) is not None:
                return self._busca_subarvore(self.esquerdo(pos), k)
        else:
            if self.direito(pos) is not None:
                return self._busca_subarvore(self.direito(pos), k)
        return pos

    def _primeira_posicao_subarvore(self, pos):
        atual = pos
        while self.esquerdo(atual) is not None:
            atual = self.esquerdo(atual)
        return atual

    def _ultima_posicao_subarvore(self, pos):
        atual = pos
        while self.direito(atual) is not None:
            atual = self.direito(atual)
        return atual

    def primeiro(self):
        return self._primeira_posicao_subarvore(self.raiz()) if len(self) > 0 else None

    def ultimo(self):
        return self._ultima_posicao_subarvore(self.raiz()) if len(self) > 0 else None

    def anterior(self, pos):
        self._validar(pos)
        if self.esquerdo(pos):
            return self._ultima_posicao_subarvore(self.esquerdo(pos))
        else:
            atual = pos
            pai_atual = self.pai(atual)
            while pai_atual is not None and atual == self.esquerdo(pai_atual):
                atual = pai_atual
                pai_atual = self.pai(atual)
            return pai_atual

    def proximo(self, pos):
        self._validar(pos)
        if self.direito(pos):
            return self._primeira_posicao_subarvore(self.direito(pos))
        else:
            atual = pos
            pai_atual = self.pai(atual)
            while pai_atual is not None and atual == self.direito(pai_atual):
                atual = pai_atual
                pai_atual = self.pai(atual)
            return pai_atual

    def buscar_posicao(self, k):
        if self.esta_vazia():
            return None
        pos = self._busca_subarvore(self.raiz(), k)
        self._rebalancear_acesso(pos)
        return pos

    def __getitem__(self, k):
        if self.esta_vazia():
            raise KeyError('Erro de Chave: ' + repr(k))
        pos = self._busca_subarvore(self.raiz(), k)
        self._rebalancear_acesso(pos)
        if k != pos.chave():
            raise KeyError('Erro de Chave: ' + repr(k))
        return pos.valor()

    def __setitem__(self, k, v):
        if self.esta_vazia():
            folha = self._adicionar_raiz(self._Item(k, v))
        else:
            pos = self._busca_subarvore(self.raiz(), k)
            if pos.chave() == k:
                pos.elemento()._valor = v
                self._rebalancear_acesso(pos)
                return
            else:
                novo_item = self._Item(k, v)
                if pos.chave() < k:
                    folha = self._adicionar_direito(pos, novo_item)
                else:
                    folha = self._adicionar_esquerdo(pos, novo_item)
        self._rebalancear_insercao(folha)

    def __delitem__(self, k):
        if not self.esta_vazia():
            pos = self._busca_subarvore(self.raiz(), k)
            if k == pos.chave():
                self.deletar(pos)
                return
            self._rebalancear_acesso(pos)
        raise KeyError('Erro de Chave: ' + repr(k))

    def __iter__(self):
        pos = self.primeiro()
        while pos is not None:
            yield pos.chave()
            pos = self.proximo(pos)

    def deletar(self, pos):
        self._validar(pos)
        if self.esquerdo(pos) and self.direito(pos):
            substituto = self._ultima_posicao_subarvore(self.esquerdo(pos))
            self._substituir(pos, substituto.elemento())
            pos = substituto
        
        pai_no = self.pai(pos)
        self._deletar(pos)
        self._rebalancear_delecao(pai_no)

    def _rebalancear_insercao(self, pos): pass
    def _rebalancear_delecao(self, pos): pass
    def _rebalancear_acesso(self, pos): pass

    def _relinkar(self, pai, filho, eh_filho_esquerdo):
        if eh_filho_esquerdo:
            pai._esquerdo = filho
        else:
            pai._direito = filho
        if filho is not None:
            filho._pai = pai

    def _rotacionar(self, pos):
        x = pos._no
        y = x._pai
        z = y._pai
        if z is None:
            self._raiz = x
            x._pai = None
        else:
            self._relinkar(z, x, y == z._esquerdo)
        
        if x == y._esquerdo:
            self._relinkar(y, x._direito, True)
            self._relinkar(x, y, False)
        else:
            self._relinkar(y, x._esquerdo, False)
            self._relinkar(x, y, True)

    def _reestruturar(self, x):
        y = self.pai(x)
        z = self.pai(y)
        if (x == self.direito(y)) == (y == self.direito(z)):
            self._rotacionar(y)
            return y
        else:
            self._rotacionar(x)
            self._rotacionar(x)
            return x

    def imprimir_arvore(self):
        if self.esta_vazia():
            print("Árvore Vazia")
            return
        self._imprimir_subarvore(self.raiz(), 0)

    def _imprimir_subarvore(self, pos, nivel):
        print("  " * nivel + str(pos.chave()))
        if self.esquerdo(pos):
            self._imprimir_subarvore(self.esquerdo(pos), nivel + 1)
        if self.direito(pos):
            self._imprimir_subarvore(self.direito(pos), nivel + 1)