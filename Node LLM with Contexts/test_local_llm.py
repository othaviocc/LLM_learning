#!/usr/bin/env python3
# coding: utf-8

import os
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

class QuizBrain:
    def __init__(self, context_folder_path: str):
        print("Inicializa Perguntas")
        
        self.context1 = ""
        self.context2 = ""
        try:
            with open(os.path.join(context_folder_path, 'context1.txt'), 'r', encoding='utf-8') as f:
                self.context1 = f.read()
            with open(os.path.join(context_folder_path, 'context2.txt'), 'r', encoding='utf-8') as f:
                self.context2 = f.read()
            print("Contextos carregados")
        except Exception as e:
            print(f"Falha: {e}")
            
        self.template = f"""
Use the following context to answer the question. The information in the context has top priority.
Your answer must be a complete sentence that shows you understood the question.
For example, if the question is 'What is the capital of Germany?', answer 'The capital of Germany is Berlin'.

--- CONTEXT 1 ---
{self.context1}
-------------------

--- CONTEXT 2 ---
{self.context2}
-------------------

Now, answer the following question in English: '{{question}}'
"""
        
        try:
            model_name = "gemma:2b"
            ollama_base_url = "http://localhost:11434"
            
            print(f"Configurando LangChain com o modelo: {model_name}")
            self.llm = Ollama(base_url=ollama_base_url, model=model_name, temperature=0.0)
            self.prompt = PromptTemplate.from_template(self.template)
            self.chain = self.prompt | self.llm
            print("LLM e LangChain Chain configurados com sucesso!")
        except Exception as e:
            print(f"Falha ao configurar o LangChain/Ollama: {e}")
            self.chain = None

    def ask(self, question: str) -> str:
        if not self.chain:
            return "Erro: A chain do LangChain não foi inicializada corretamente."

        print("\nInvocando a chain do LangChain com o prompt")
        try:
            answer = self.chain.invoke({"question": question})
            return answer.strip()
        except Exception as e:
            return f"Erro ao invocar a chain do LangChain: {e}"

if __name__ == '__main__':
    context_folder = os.path.join(os.path.dirname(__file__), 'contexts')

    quiz_brain = QuizBrain(context_folder)
    #pergunte aqui
    pergunta_de_teste = "What is the main goal of the RoboCup@Home league?"
    
    import time
    start_time = time.time()
    resposta = quiz_brain.ask(pergunta_de_teste)
    end_time = time.time()
    
    print("\n Teste feito")
    print(f"Pergunta: {pergunta_de_teste}")
    print(f"Resposta: {resposta}")
    print(f"(Tempo de resposta: {end_time - start_time:.2f} segundos)")