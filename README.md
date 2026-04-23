# Sistema Bancário com Testes de Regressão
Evolução do sistema bancário base, com a adição de uma nova funcionalidade e validação através de testes de regressão.

## Nova Funcionalidade
- Investimento em poupança com rendimento

## Testes de Regressão
Testes já existentes foram reutilizados para garantir que a nova funcionalidade não afetou o funcionamento do sistema.

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
