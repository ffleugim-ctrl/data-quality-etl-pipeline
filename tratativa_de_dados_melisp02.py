import datetime
import random
import time
import pandas as pd


def gerar_dados_sujos_corporativos(linhas=1200):
    """Gera uma base de dados em larga escala com anomalias estruturais."""
    print("[INFO] Iniciando geração da base de dados bruta via Range...")

    # Listas de apoio para simular dados do ecossistema corporativo
    nomes_validos = [
        "Miguel Dantas",
        "Valquiria Silva",
        "Thales Souza",
        "Camila Ribeiro",
        "Heitor Almeida",
    ]
    setores = ["Retornos (DV)", "Resíduos", "Inventário", "Logística Inbound"]
    status_lote = ["Pronto", "Em Processo", "Bloqueado"]

    dados = []

    # Usando o range para criar a grande extensão que você pediu (>1000 linhas)
    for i in range(1, linhas + 1):
        # 1. Gerando ID do Colaborador (com alguns duplicados propositais)
        if i % 150 == 0:
            colaborador_id = f"REp-{1000 + (i - 1)}"  # ID repetido para gerar duplicata
        else:
            colaborador_id = f"REP-{1000 + i}"

        # 2. Gerando Nomes (com sujeiras de digitação espalhadas)
        nome = random.choice(nomes_validos)
        if i % 80 == 0:
            nome = f"  {nome.upper()}   "  # Espaços em branco e caixa alta total
        elif i % 120 == 0:
            nome = None  # Dado ausente/nulo

        # 3. Gerando Métricas Financeiras/Performance (com anomalias)
        score_performance = round(random.uniform(50.0, 100.0), 2)
        if i % 90 == 0:
            score_performance = (
                -99.0
            )  # Outlier/Valor impossível para performance

        # 4. Gerando Informações de Lotes Operacionais
        lote_id = f"LOT-{random.randint(5000, 9999)}"
        setor = random.choice(setores)
        status = random.choice(status_lote)

        # Montando a linha do DataFrame
        dados.append(
            {
                "ID_Colaborador": colaborador_id,
                "Nome": nome,
                "Setor": setor,
                "Score_Performance": score_performance,
                "Lote_Operacional": lote_id,
                "Status_Lote": status,
                "Data_Registro": datetime.date(2026, 5, 1)
                + datetime.timedelta(days=random.randint(0, 14)),
            }
        )

    # Transformando em DataFrame do Pandas
    df_bruto = pd.DataFrame(dados)

    # Injetando algumas linhas 100% duplicadas para o tratamento pegar
    df_bruto = pd.concat(
        [df_bruto, df_bruto.iloc[10:30]], ignore_index=True
    ).sample(frac=1)

    return df_bruto


def executar_pipeline_etl():
    # 1. Extração dos dados gerados via Range
    df_operacao = gerar_dados_sujos_corporativos(1250)
    total_inicial = len(df_operacao)

    print("-" * 70)
    print(f"[STATUS] Dataframe carregado com sucesso. Total de linhas: {total_inicial}")
    print("-" * 70)
    time.sleep(1)

    # 2. SISTEMA DE AUDITORIA E NOTIFICAÇÃO (O Alerta Corporativo que você queria)
    print("\n" + "=" * 70)
    print("🚨 [SISTEMA DE ALERTA DE QUALIDADE DE DADOS - LOGÍSTICA & HR] 🚨")
    print("=" * 70)

    # Analisando inconformidades
    duplicadas = df_operacao.duplicated(subset=["ID_Colaborador"]).sum()
    nulos_nome = df_operacao["Nome"].isnull().sum()
    outliers_score = (df_operacao["Score_Performance"] < 0).sum()

    # Disparando as notificações estruturadas
    if duplicadas > 0 or nulos_nome > 0 or outliers_score > 0:
        print(f"⚠️  [NOTIFICAÇÃO]: DETECTADO LOG DE DADOS INCONSISTENTES / CONTAMINADOS")
        print(
            f"   • Registro(s) Duplicado(s) detectado(s): {duplicadas} linha(s)."
        )
        print(
            f"   • Registro(s) de Integridade Nula (Campos Vazios): {nulos_nome} ocorrência(s)."
        )
        print(
            f"   • Outlier(s) Crítico(s) de Performance (Valores Negativos): {outliers_score} detectado(s)."
        )
        print(
            "\n[AÇÃO REQUERIDA]: Iniciando módulo de higienização automatizada..."
        )
    else:
        print("✅ [NOTIFICAÇÃO]: Base de dados em conformidade com as regras de negócio.")
    print("=" * 70 + "\n")

    time.sleep(2)

    # 3. MÓDULO DE TRATAMENTO E HIGIENIZAÇÃO (Data Cleaning)
    print("[MÓDULO DE TRATAMENTO]: Executando regras de higienização corporativa...")

    # Regra 1: Remover linhas com IDs duplicados (mantém o primeiro registro válido)
    df_limpo = df_operacao.drop_duplicates(
        subset=["ID_Colaborador"], keep="first"
    ).copy()

    # Regra 2: Tratar valores nulos no Nome preenchendo com padrão corporativo
    df_limpo["Nome"] = df_limpo["Nome"].fillna("NÃO IDENTIFICADO (AUDITORIA)")

    # Regra 3: Remover espaços em branco invisíveis nas pontas e padronizar para Capitalize (Iniciais Maiúsculas)
    df_limpo["Nome"] = df_limpo["Nome"].str.strip().str.title()

    # Regra 4: Corrigir outliers e valores negativos na Performance (substituir por zero ou pela média)
    # Aqui vamos usar uma máscara para zerar scores impossíveis (< 0)
    df_limpo.loc[df_limpo["Score_Performance"] < 0, "Score_Performance"] = 0.0

    print("✔️  [MÓDULO DE TRATAMENTO]: Processo concluído com sucesso.")
    time.sleep(1)

    # 4. CARGA / CONCLUSÃO DO PROCESSO
    total_final = len(df_limpo)
    linhas_removidas = total_inicial - total_final

    print("\n" + "=" * 70)
    print("📊 [RELATÓRIO DE HIGIENIZAÇÃO FINAL]")
    print("=" * 70)
    print(f"• Volume Bruto Inicial: {total_inicial} linhas.")
    print(f"• Volume Líquido Processado: {total_final} linhas.")
    print(f"• Linhas Corrompidas Descartadas: {linhas_removidas}")
    print(f"• Taxa de Integridade Restabelecida: {round((total_final / total_inicial) * 100, 2)}%")
    print("=" * 70)

    # Mostrando uma prévia dos dados limpos no terminal
    print("\n📌 [PREVIA DOS DADOS PROCESSADOS (TOP 5)]:")
    print(df_limpo.head())


# Executa o projeto de engenharia de dados
if __name__ == "__main__":
    executar_pipeline_etl()
