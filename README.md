# Onboarding & Compliance Tracker 🚚💼

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Excel-Openpyxl-217346?logo=microsoftexcel&logoColor=white" alt="Excel" />
  <img src="https://img.shields.io/badge/Domain-Logistics-F59E0B" alt="Logistics" />
  <img src="https://img.shields.io/badge/Status-MVP-blue" alt="Status" />
</p>

**Automatização de auditoria de documentos e controle de conformidade regulatória para terceiros e temporários em operações logísticas.**

---

## 📌 Sobre o Projeto

Em grandes operações logísticas e Centros de Distribuição (CDs), a gestão de terceiros, motoristas agregados e mão de obra temporária é um desafio crítico. A entrada de colaboradores sem treinamentos obrigatórios (como NR-11 e NR-35) ou com exames médicos vencidos (ASO) expõe a empresa a **riscos trabalhistas, multas pesadas e gargalos operacionais na portaria/doca**.

O **Onboarding & Compliance Tracker** é um MVP (Produto Mínimo Viável) desenvolvido em Python que automatiza a auditoria desses registros. O script transforma o processo manual de conferência de planilhas em um fluxo automatizado de segundos, calculando prazos de validade e gerando uma **Lista de Bloqueio** em tempo real para a operação.

### 🎯 Objetivos de Engenharia de Produção & Logística

* **Garantia de Compliance:** mitigação de riscos legais e trabalhistas na cadeia de suprimentos.
* **Redução de Lead Time:** agilização do onboarding e da liberação de acesso na portaria do CD.
* **Gestão Visual / KPIs:** geração automática de indicadores de conformidade para apoiar a tomada de decisão gerencial.

---

## ⚙️ Como Funciona (Fluxo do Processo)

1. **Input de dados:** o sistema lê uma base de dados (`.csv` ou `.xlsx`) com a lista de colaboradores e as datas de entrega/vencimento de seus documentos (CNH, ASO, EPI, treinamentos).
2. **Processamento (Python):** o script compara as datas com o dia atual e classifica o status de cada documento.
3. **Output de resultados:**
   * Geração de uma nova planilha formatada com os alertas (`Conforme`, `A Vencer`, `Irregular`).
   * Emissão de um relatório executivo com os KPIs de conformidade da operação.
   * Criação automática da **Lista de Bloqueio** (quem não está apto a operar).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**: linguagem base.
* **Pandas:** manipulação e higienização da base de dados.
* **Openpyxl:** leitura e escrita de arquivos Excel.
* **Datetime** (biblioteca padrão do Python): cálculos de prazos e vencimentos. Não precisa ser instalada.

---

## 📁 Estrutura do Repositório

```text
onboarding-checklist-automation/
│
├── data/
│   ├── sample_onboarding.csv          # Base de dados fictícia para teste do script
│   └── compliance_report.xlsx         # Relatório final (gerado pelo sistema)
│   └── compliance_report_example.csv  # Relatório de exemplo demonstrativo (visível no GitHub)
│
├── src/
│   └── checker.py                     # Código-fonte principal da automação
│
├── requirements.txt                   # Dependências do projeto (pandas, openpyxl)
├── README.md                          # Documentação do projeto
└── .gitignore                         # Arquivos ignorados pelo Git
```

> 💡 O arquivo `compliance_report.xlsx` é **gerado** a cada execução, então ele aparece na pasta `data/` somente depois que o script roda.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* [Python 3.11 ou superior](https://www.python.org/downloads/) instalado na sua máquina.
* [Git](https://git-scm.com/downloads) para clonar o repositório.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/hugoarcanjodev/onboarding-checklist-automation.git
   cd onboarding-checklist-automation
   ```

2. **(Opcional, recomendado) Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o script de auditoria:**
   ```bash
   python src/checker.py
   ```

5. **Verifique os resultados:**
   O terminal exibirá o resumo dos KPIs e o arquivo `data/compliance_report.xlsx` será gerado (ou atualizado).

---

## 📈 Indicadores Gerados (KPIs)

O MVP foi desenhado para reportar métricas essenciais para a liderança de logística:

* **Taxa de Conformidade Geral (%):** percentual da frota/equipe totalmente regularizada.
* **Índice de Risco:** quantidade de colaboradores com documentos vencidos.
* **Gargalo de Onboarding:** tempo médio para um novo parceiro atingir o status "Conforme".

---

## 🗺️ Próximos Passos (Backlog de Melhorias)

- [ ] Integração com o Streamlit para criar um dashboard interativo na web.
- [ ] Alertas automáticos via WhatsApp/e-mail para gestores de frota sobre documentos a vencer.
- [ ] Conexão com banco de dados SQL para armazenar o histórico de conformidade.

---

## 🧑‍💻 Autor

<p>
  <a href="https://www.linkedin.com/in/hugo-arcanjo/">
    <img src="https://img.shields.io/badge/LinkedIn-Hugo_Arcanjo-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/hugoarcanjodev/">
    <img src="https://img.shields.io/badge/GitHub-hugoarcanjodev-181717?logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

Desenvolvido por **Hugo Arcanjo**