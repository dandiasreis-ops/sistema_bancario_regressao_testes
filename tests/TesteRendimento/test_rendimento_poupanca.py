import unittest

from source.CodigoBaseRegressao.sistema_bancario_base_regressao import (
    PessoaFisica,
    ContaCorrente
)

class TestRendimentoPoupanca(unittest.TestCase):

    def test_aplicar_rendimento(self):

        #ARRANGE
        cliente = PessoaFisica("Daniel", "123", "01-01-2000", "SP")
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)

        conta.depositar(1000)

        #ACT
        conta.aplicar_rendimento()

        #ASSERT
        self.assertEqual(conta.saldo, 1005.0)

if __name__ == "__main__":
    unittest.main()