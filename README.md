# Sistema Bancário com Testes de Regressão
Evolução do sistema bancário base, com a adição de uma nova funcionalidade e validação através de testes de regressão.

## Novas Funcionalidades
- Investimento em poupança
- Cálculo de rendimento automático (0,5% sobre o saldo)

## Testes de Regressão
Testes já existentes foram reutilizados para garantir que a nova funcionalidade não afetou o funcionamento do sistema.

## Testes Implementados
- Testes Unitários
- Testes de Integração
- Testes Funcionais
- Testes de Regressão
- Testes com Test Doubles (Dummy, Stub, Mock)
- Teste de rendimento com TDD

## Desenvolvimento Orientado a Testes (TDD)
A funcionalidade de cálculo de rendimento foi desenvolvida utilizando TDD, onde o teste foi implementado antes da lógica de negócio.

## Integração Contínua
Utilização de GitHub Actions para executar automaticamente todos os testes a cada push no repositório.

### Resultados:
- Todos os testes passaram com sucesso
- Nenhuma funcionalidade anterior foi impactada

## Estrutura do Projeto
source/
CodigoBase/
sistema_bancario_base_regressao.py

tests/
TestesUnitarios/test_unitarios_banco.py
TestesIntegracao/test_integracao_banco.py
TestesFuncionais/test_funcionais_banco.py
TesteInvestimento/test_investimento_banco.py

## Como executar
Para rodar os testes:
```bash
python -m unittest discover -s tests
