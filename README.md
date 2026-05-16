# data-quality-etl-pipeline
# Pipeline Corporativa de ETL e Data Quality com Python &amp; Pandas 
# Pipeline Corporativa de ETL e Data Quality com Python & Pandas

Este projeto simula uma pipeline real de engenharia e análise de dados focada em **Quality Assurance (Garantia de Qualidade)** e **Higienização de Dados (Data Cleaning)** para cenários de Operações Logísticas e Recursos Humanos.

O script utiliza estruturas avançadas de repetição em Python para gerar uma base de dados sintética em larga escala (acima de 1.200 registros) contendo anomalias estruturais propositais, simulando falhas comuns de integração de sistemas ou input humano.

### 📊 Funcionalidades do Projeto:
1. **Módulo de Auditoria Automatizada:** Varre a base bruta em busca de inconformidades, emitindo notificações estruturadas em linguagem corporativa caso sejam detectados logs contaminados.
2. **Data Cleaning & Higienização:** * Identificação e eliminação de registros duplicados (`drop_duplicates`).
   * Tratamento de integridade nula para campos ausentes (`fillna`).
   * Padronização de strings e remoção de espaçamentos inválidos (`strip` / `title`).
   * Correção e normalização de outliers críticos de performance.
3. **Módulo de Data Delivery:** Entrega um relatório consolidado com o volume líquido processado, taxa de integridade restabelecida e amostragem dos dados limpos prontos para consumo por ferramentas de BI (Power BI/Tableau) ou armazenamento em bancos de dados (SQL Server).

### 🛠️ Tecnologias Utilizadas:
* Python 3.x
* Pandas (Manipulação e Análise de Dados)
* Math & Datetime (Regras de negócio e temporalidade)
