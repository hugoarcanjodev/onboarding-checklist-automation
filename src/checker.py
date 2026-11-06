from datetime import datetime
import os
import pandas as pd


def carregar_dados(caminho_input):
    """Carrega a base de dados dos colaboradores."""
    if not os.path.exists(caminho_input):
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado em: {caminho_input}"
        )
    return pd.read_csv(caminho_input)


def avaliar_status_documento(data_vencimento, data_hoje):
    """Calcula o status do documento com base na regra de negócio logístico."""
    if pd.isna(data_vencimento):
        return "Pendente / Ausente"

    # Converte a string de data para objeto datetime
    dt_vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    dias_restantes = (dt_vencimento - data_hoje).days

    if dias_restantes < 0:
        return "Irregular"
    elif dias_restantes <= 30:
        return "A Vencer"
    else:
        return "Conforme"


def processar_compliance(df):
    """Processa a matriz de compliance e define o status geral de cada colaborador."""
    hoje = datetime.now().date()
    colunas_datas = [c for c in df.columns if c.startswith("vencimento_")]

    # Criar colunas de status individuais para cada documento
    for col in colunas_datas:
        nome_status_col = col.replace("vencimento_", "status_")
        df[nome_status_col] = df[col].apply(
            lambda x: avaliar_status_documento(x, hoje)
        )

    # Identificar o status geral do colaborador baseado na pior condição
    colunas_status = [c for c in df.columns if c.startswith("status_")]

    def definir_status_geral(linha):
        status_valores = linha[colunas_status].values
        if "Irregular" in status_valores or "Pendente / Ausente" in status_valores:
            return "Irregular"
        elif "A Vencer" in status_valores:
            return "A Vencer"
        return "Conforme"

    df["status_geral"] = df.apply(definir_status_geral, axis=1)
    return df


def gerar_relatorio_kpis(df):
    """Gera visibilidade gerencial (Gestão Visual) através do terminal."""
    total_colaboradores = len(df)
    conformes = len(df[df["status_geral"] == "Conforme"])
    a_vencer = len(df[df["status_geral"] == "A Vencer"])
    irregulares = len(df[df["status_geral"] == "Irregular"])

    taxa_conformidade = (conformes / total_colaboradores) * 100

    print("\n" + "=" * 50)
    print("📈 RELATÓRIO EXECUTIVO - ONBOARDING & COMPLIANCE")
    print("=" * 50)
    print(f"Total de Colaboradores Auditados: {total_colaboradores}")
    print(f"🟢 Status Conforme: {conformes}")
    print(f"🟡 Status A Vencer (Próximos 30 dias): {a_vencer}")
    print(f"🔴 Status Irregular / Vencido: {irregulares}")
    print("-" * 50)
    print(f"📊 TAXA DE CONFORMIDADE GERAL: {taxa_conformidade:.1f}%")
    print("=" * 50)

    if irregulares > 0:
        print("\n❌ LISTA DE BLOQUEIO OPERACIONAL (ACESSO NEGADO):")
        bloqueados = df[df["status_geral"] == "Irregular"]
        for idx, row in bloqueados.iterrows():
            print(f" - [ID {row['id']}] {row['nome']} ({row['tipo_vinculo']})")
        print("=" * 50 + "\n")


def main():
    # Definição dos caminhos de arquivos de forma segura
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_input = os.path.join(base_dir, "data", "sample_onboarding.csv")
    caminho_output = os.path.join(base_dir, "data", "compliance_report.xlsx")

    print("[INFO] Iniciando auditoria de documentos regulatórios...")

    # Fluxo principal do MVP
    df_raw = carregar_dados(caminho_input)
    df_processado = processar_compliance(df_raw)

    # Exibe KPIs de engenharia de produção no terminal
    gerar_relatorio_kpis(df_processado)

    # Exporta os resultados detalhados para visualização do time de Logística
    df_processado.to_excel(caminho_output, index=False)
    print(f"[SUCCESS] Relatório detalhado exportado para: {caminho_output}")


if __name__ == "__main__":
    main()
