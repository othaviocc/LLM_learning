import requests
import base64
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

class SDImageEngine:
    def __init__(self):
        self.url = os.getenv("SD_URL", "http://127.0.0.1:7860")
        self.output_dir = os.getenv("OUTPUT_DIR", "outputs")
        os.makedirs(self.output_dir, exist_ok=True)

    def gerar_imagem(self, prompt, neg_prompt="", steps=25, width=512, height=512):
        print(f"Enviando prompt para o Stable Diffusion...")
        
        payload = {
            "prompt": prompt,
            "negative_prompt": neg_prompt,
            "steps": steps,
            "width": width,
            "height": height,
            "sampler_name": "DPM++ 2M Karras",
            "cfg_scale": 7
        }

        try:
            response = requests.post(url=f'{self.url}/sdapi/v1/txt2img', json=payload)
            response.raise_for_status()
            r = response.json()

            # Decodificar a imagem base64
            for i in r['images']:
                image = Image.open(BytesIO(base64.b64decode(i.split(",",1)[0])))
                
                # Gerar nome único baseado no prompt (simplificado)
                filename = f"gen_{len(os.listdir(self.output_dir)) + 1}.png"
                save_path = os.path.join(self.output_dir, filename)
                
                image.save(save_path)
                return save_path

        except Exception as e:
            return f"Erro na conexão: {e}. Verifique se a flag --api está ativa no SD."