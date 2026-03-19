#Configuração de ambiente

sudo apt-get update
sudo apt-get install -y ffmpeg

# Verifica se a pasta já existe antes de criar
if [ ! -d "gemma_env" ]; then
    python3 -m venv gemma_env
    echo "Ambiente 'gemma_env' criado."
else
    echo "Ambiente 'gemma_env' já existe."
fi

source gemma_env/bin/activate
pip install -r requirements.txt
deactivate

if ! command -v ollama &> /dev/null
then
    echo "Ollama não encontrado, instalando..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Ollama já está instalado."
fi

