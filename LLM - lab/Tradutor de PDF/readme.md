# Local LLM PDF Translator (PT-BR)

Este é um tradutor de documentos PDF profissional de alta fidelidade que roda **100% localmente**. Ele utiliza IA de visão para entender o layout do PDF e modelos de linguagem de grande escala (LLMs) para uma tradução contextualizada.

---

## Funcionalidades
* **Extração Inteligente:** Usa `Docling` (IBM) para converter PDFs complexos em Markdown, preservando tabelas e títulos.
* **Tradução Contextual:** Tradução de Inglês para Português Brasileiro usando `Ollama` (Llama 3 / Phi-3).
* **Processamento em Blocos (Chunking):** Divide textos longos para evitar estouro de memória (VRAM/RAM).
* **Privacidade Total:** Nenhum dado sai da sua máquina.

---

## Pré-requisitos

1.  **Python 3.10+** instalado.
2.  **Ollama** instalado e rodando ([ollama.com](https://ollama.com)).
3.  **Modelo baixado:** No terminal, execute:
    ```bash
    ollama run llama3:8b
    ```

---

## Estrutura do Projeto

```text
LLM - lab/
└── Tradutor de PDF/
    ├── input/              # Coloque seus PDFs em inglês aqui
    ├── output/             # Onde os arquivos traduzidos serão salvos
    ├── core.py             # Lógica de extração e tradução
    ├── tradutor.py         # Script principal de execução
    ├── .env                # Configurações de modelo e chaves
    ├── requirements.txt    # Dependências do Python
    └── README.md           # Este manual