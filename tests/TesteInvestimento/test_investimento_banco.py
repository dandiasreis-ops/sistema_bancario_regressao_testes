import unittest

#importa as classes
from source.CodigoBaseRegressao.sistema_bancario_base_regressao import (
    PessoaFisica,
    ContaCorrente,
    InvestimentoPoupanca
)

class TestInvestimento(unittest.TestCase):

    def test_investimento_poupanca(self):
        cliente = PessoaFisica("Teste", "123", "01-01-2000", "SP")
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)

        conta.depositar(1000)

        investimento = InvestimentoPoupanca(500)
        cliente.realizar_transacao(conta, investimento)

        self.assertEqual(conta.saldo, 1025)

        self.assertEqual(
            conta.historico.transacoes[-1]["tipo"],
            "InvestimentoPoupanca"
        )

if __name__ == "__main__":
    unittest.main()

'''
Os testes unitários, de integração e funcionais previamente implementados foram reutilizados 
como testes de regressão após a adição da funcionalidade de investimento em poupança.

Resultados:
- Todos os testes anteriores passaram com sucesso.
- Nenhuma funcionalidade existente foi afetada.
- A nova funcionalidade de investimento foi validada com sucesso.
'''