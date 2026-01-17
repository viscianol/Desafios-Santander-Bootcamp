# Arquitetura AWS – Redução de Custos em Farmácias

## Visão Geral
A arquitetura proposta utiliza serviços gerenciados da AWS com o objetivo de reduzir custos operacionais, aumentar a escalabilidade e eliminar a necessidade de infraestrutura física local.

A solução foi pensada para atender uma farmácia fictícia que possui sistema de vendas, controle de estoque e geração de relatórios.

## Componentes da Arquitetura

### Amazon EC2 com Auto Scaling
Responsável por hospedar o sistema principal da farmácia (vendas e estoque).  
O Auto Scaling ajusta automaticamente a quantidade de instâncias conforme a demanda, evitando custos com servidores ociosos.

### Amazon S3
Utilizado para armazenar:
- Relatórios de vendas
- Notas fiscais
- Dados históricos de estoque

O Amazon S3 oferece baixo custo, alta durabilidade e fácil integração com outros serviços AWS.

### AWS Lambda
Executa funções sob demanda, como:
- Processamento de relatórios diários
- Validação de dados
- Automatização de rotinas simples

Esse modelo elimina a necessidade de servidores dedicados para tarefas pontuais.

## Fluxo de Funcionamento
1. O sistema da farmácia é acessado pelos usuários.
2. As requisições são processadas pelas instâncias EC2.
3. Dados e relatórios são armazenados no Amazon S3.
4. Processos automatizados são executados via AWS Lambda.
5. O Auto Scaling ajusta os recursos conforme a demanda.

## Benefícios da Arquitetura
- Redução de custos operacionais
- Escalabilidade automática
- Alta disponibilidade
- Menor complexidade de manutenção
