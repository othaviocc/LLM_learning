import os
from pathlib import Path
from dotenv import load_dotenv
from core import EngineTradutor
from tqdm import tqdm

load_dotenv()

def executar_fluxo_completo():
    input_dir, output_dir = Path("input"), Path("output")
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    arquivo_nome = "documento.pdf" # nome arquivo
    input_path = input_dir / arquivo_nome
    output_pdf = output_dir / f"TRADUZIDO_{arquivo_nome}"
    
    if not input_path.exists():
        print(f"Erro: Coloque o arquivo '{arquivo_nome}' na pasta input.")
        return

    modelo = os.getenv("OLLAMA_MODEL", "llama3")
    engine = EngineTradutor(model_name=modelo)

    print(f"Extraindo texto do PDF original...")
    texto_en = engine.extrair(str(input_path))
    
    print(f"Traduzindo via {modelo} (Local)...")
    blocos = engine.splitter.split_text(texto_en)
    resultado_traduzido = []
    
    for bloco in tqdm(blocos, desc="Processando blocos"):
        res = engine.traduzir_bloco(bloco)
        resultado_traduzido.append(res)

    texto_final = "\n\n".join(resultado_traduzido)
    engine.salvar_como_pdf(texto_final, str(output_pdf))
    print(f"O seu novo PDF está em: {output_pdf}")

if __name__ == "__main__":
    executar_fluxo_completo()