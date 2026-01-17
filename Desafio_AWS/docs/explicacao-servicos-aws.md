# Explicação dos Serviços AWS Utilizados

Este documento apresenta uma descrição dos serviços AWS utilizados no projeto de redução de custos em uma farmácia fictícia.

---

## Amazon EC2 com Auto Scaling

O Amazon EC2 (Elastic Compute Cloud) permite a criação de servidores virtuais sob demanda, eliminando a necessidade de infraestrutura física local.

### Benefícios:
- Pagamento conforme uso
- Escalabilidade automática
- Alta disponibilidade

### Impacto na redução de custos:
Com o uso do Auto Scaling, a farmácia evita manter servidores ativos durante períodos de baixa demanda, reduzindo custos com infraestrutura ociosa.

---

## Amazon S3

O Amazon S3 (Simple Storage Service) é um serviço de armazenamento de objetos altamente durável e de baixo custo.

### Benefícios:
- Baixo custo de armazenamento
- Alta durabilidade dos dados
- Facilidade de acesso e integração

### Impacto na redução de custos:
Substitui servidores locais e sistemas de armazenamento físico, reduzindo gastos com manutenção e expansão de hardware.

---

## AWS Lambda

O AWS Lambda permite a execução de código sem a necessidade de provisionar ou gerenciar servidores.

### Benefícios:
- Execução sob demanda
- Cobrança apenas pelo tempo de execução
- Integração nativa com outros serviços AWS

### Impacto na redução de custos:
Elimina a necessidade de servidores dedicados para tarefas simples e periódicas, reduzindo significativamente os custos operacionais.

---

## Considerações Finais

A combinação desses serviços possibilita uma arquitetura moderna, escalável e financeiramente eficiente, adequada para pequenas e médias empresas do setor farmacêutico.
