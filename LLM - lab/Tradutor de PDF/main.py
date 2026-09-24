import os
import ollama
from dotenv import load_dotenv
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tqdm import tqdm

load_dotenv()

class LocalPDFTranslator:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL", "llama3")
        self.converter = DocumentConverter()
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=int(os.getenv("CHUNK_SIZE", 3000)),
            chunk_overlap=int(os.getenv("CHUNK_OVERLAP", 200))
        )

    def extract_text(self, pdf_path):
        print(f"Analisando PDF com Docling")
        result = self.converter.convert(pdf_path)
        return result.document.export_to_markdown()

    def translate_chunk(self, text_chunk, context_summary=""):
        prompt = (
            f"Você é um tradutor expert. Traduza o texto do INGLÊS para PORTUGUÊS BRASILEIRO.\n"
            f"Contexto anterior: {context_summary}\n\n"
            f"Regras:\n- Mantenha o formato Markdown\n- Seja fiel ao tom técnico\n"
            f"Texto para traduzir:\n{text_chunk}"
        )
        
        response = ollama.generate(model=self.model, prompt=prompt)
        return response['response']

    def run(self, input_file, output_file):
        # Extração
        raw_markdown = self.extract_text(input_file)
        
        # Divisão em pedaços
        chunks = self.splitter.split_text(raw_markdown)
        print(f"PDF dividido em {len(chunks)} partes para processamento.")

        translated_parts = []
        
        for i, chunk in enumerate(tqdm(chunks, desc="Traduzindo")):
            translation = self.translate_chunk(chunk)
            translated_parts.append(translation)

        final_text = "\n\n".join(translated_parts)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_text)
        
        print(f"Tradução concluída com sucesso! Salvo em: {output_file}")

if __name__ == "__main__":
    translator = LocalPDFTranslator()
    
    arquivo_entrada = "input/documento.pdf"
    arquivo_saida = "output/traduzido_final.md"
    
    if os.path.exists(arquivo_entrada):
        translator.run(arquivo_entrada, arquivo_saida)
    else:
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")