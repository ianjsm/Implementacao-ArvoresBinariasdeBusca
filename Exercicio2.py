from Exercicio1 import MapaArvore

class MapaArvoreAVL(MapaArvore):

    class _No(MapaArvore._No):
        __slots__ = '_altura'
        
        def __init__(self, elemento, pai=None, esquerdo=None, direito=None):
            super().__init__(elemento, pai, esquerdo, direito)
            self._altura = 0
        
        def altura_esquerda(self):
            return self._esquerdo._altura if self._esquerdo is not None else 0
        
        def altura_direita(self):
            return self._direito._altura if self._direito is not None else 0

    def _recomputar_altura(self, pos):
        pos._no._altura = 1 + max(pos._no.altura_esquerda(), pos._no.altura_direita())

    def _esta_balanceado(self, pos):
        return abs(pos._no.altura_esquerda() - pos._no.altura_direita()) <= 1

    def _filho_mais_alto(self, pos, pender_esquerda=False):
        if pos._no.altura_esquerda() + (1 if pender_esquerda else 0) > pos._no.altura_direita():
            return self.esquerdo(pos)
        else:
            return self.direito(pos)

    def _neto_mais_alto(self, pos):
        filho = self._filho_mais_alto(pos)
        alinhamento = (filho == self.esquerdo(pos))
        return self._filho_mais_alto(filho, alinhamento)

    def _rebalancear(self, pos):
        while pos is not None:
            altura_antiga = pos._no._altura
            if not self._esta_balanceado(pos):
                pos = self._reestruturar(self._neto_mais_alto(pos))
                self._recomputar_altura(self.esquerdo(pos))
                self._recomputar_altura(self.direito(pos))
            
            self._recomputar_altura(pos)
            
            if pos._no._altura == altura_antiga:
                pos = None
            else:
                pos = self.pai(pos)

    def _rebalancear_insercao(self, pos):
        self._rebalancear(pos)

    def _rebalancear_delecao(self, pos):
        if pos is not None:
            self._rebalancear(pos)