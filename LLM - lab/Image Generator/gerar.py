from image_engine import SDImageEngine

def main():
    engine = SDImageEngine()

    meu_prompt = (
        "A hyper-realistic portrait of a cyberpunk cat wearing neon glasses, "
        "highly detailed, 8k, cinematic lighting, purple and blue tones"
    )
    
    meu_prompt_negativo = "blurry, low quality, deformed, text, watermark, bad anatomy"

    # Executa a geração
    caminho = engine.gerar_imagem(
        prompt=meu_prompt,
        neg_prompt=meu_prompt_negativo,
        width=768, 
        height=768
    )

    print(f"Imagem gerada com sucesso em: {caminho}")

if __name__ == "__main__":
    main()