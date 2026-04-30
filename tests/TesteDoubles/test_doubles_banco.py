import unittest
from unittest.mock import MagicMock

from source.CodigoBaseRegressao.sistema_bancario_base_regressao import (
    Cliente,
    ContaCorrente
)

class TestTransacaoComDoubles(unittest.TestCase):

    def test_realizar_transacao_com_doubles(self):

        #ARRANGE

        #Dummy - cliente simples
        cliente = Cliente("Endereço fake")

        #Conta real
        conta = ContaCorrente(cliente, 1)

        #Stub - simula uma transação que "sempre funciona"
        class TransacaoStub:
            def registrar(self, conta):
                conta.saldo += 100  #comportamento controlado

        transacao_stub = TransacaoStub()

        #Mock - verificar se foi chamado
        cliente.realizar_transacao = MagicMock()


        #ACT
        cliente.realizar_transacao(conta, transacao_stub)

        #ASSERT

        #Verifica se o método foi chamado (Mock)
        cliente.realizar_transacao.assert_called_once_with(conta, transacao_stub)

        #(Stub não foi executado porque usei mock)

if __name__ == "__main__":
    unittest.main()