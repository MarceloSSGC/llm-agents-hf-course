from llama_cpp import Llama

# Caminho do modelo baixado no LM Studio
modelo_path = '/home/marcelo/.lmstudio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf'

# modelo_path = '/home/marcelo/.lmstudio/models/lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf'

try:
    print("Carregando o modelo...")
    llm = Llama(model_path=modelo_path)  # Ajuste o caminho se necessário
    print("Modelo carregado com sucesso!")

    # Teste com uma pergunta
    pergunta = "Qual é a capital da China? (responda em português)"
    resposta = llm(pergunta, max_tokens=100)

    print("\nResposta do modelo:")
    print(resposta["choices"][0]["text"])

except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")


#==========================================================================================