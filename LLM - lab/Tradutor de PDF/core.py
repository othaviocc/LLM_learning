import ollama
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fpdf import FPDF

class EngineTradutor:
    def __init__(self, model_name="llama3"):
        self.model = model_name
        self.converter = DocumentConverter()
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)

    def extrair(self, path):
        return self.converter.convert(path).document.export_to_markdown()

    def traduzir_bloco(self, texto):
        prompt = f"Traduza do Inglês para Português Brasileiro. Mantenha a estrutura Markdown:\n\n{texto}"
        return ollama.generate(model=self.model, prompt=prompt)['response']

    def salvar_como_pdf(self, texto_markdown, caminho_saida):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        pdf.set_font("Helvetica", size=12)
        
        texto_limpo = texto_markdown.encode('latin-1', 'ignore').decode('latin-1')
        
        pdf.multi_cell(0, 10, txt=texto_limpo)
        pdf.output(caminho_saida)