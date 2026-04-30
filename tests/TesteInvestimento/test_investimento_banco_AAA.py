import unittest

from source.CodigoBase.sistema_bancario_base_regressao import (
    PessoaFisica,
    ContaCorrente,
    InvestimentoPoupanca
)

class TestInvestimentoPoupanca(unittest.TestCase):

    def test_investimento_poupanca(self):

        #ARRANGE (Preparação)
        cliente = PessoaFisica("Daniel", "123", "01-01-2000", "SP")
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)

        conta.depositar(1000)  # saldo inicial

        investimento = InvestimentoPoupanca(500)

        #ACT (Ação)
        cliente.realizar_transacao(conta, investimento)

        #ASSERT (Verificação)
        self.assertEqual(conta.saldo, 1025)  # 500 com rendimento de 5%

        self.assertEqual(
            conta.historico.transacoes[-1]["tipo"],
            "InvestimentoPoupanca"
        )

if __name__ == "__main__":
    unittest.main()