from llama_cpp import Llama

# Caminho do modelo baixado no LM Studio
# modelo_path = '/home/marcelo/.lmstudio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf'

modelo_path = '/home/marcelo/.lmstudio/models/lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf'

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

profissão = 'mecânico'

text_to_analize = f"""
Com base **apenas** no texto abaixo, responda: Qual era a profissão de John Von Neumann?

Responda com uma frase curta e objetiva.

Texto:
===
Espaços de Hilbert foram criados por David Hilbert, que os estudou no contexto de equações integrais. 
O {profissão} John von Neumann criou a nomenclatura "der abstrakte Hilbertsche Raum" em seu famoso trabalho 
em operadores Hermitianos não limitados, publicado em 1929. 
Talvez, John Von Neumann seja o {profissão} que melhor reconheceu a importância desse trabalho original.

Os elementos de espaço de Hilbert abstratos são chamados vetores. Em aplicações, eles são tipicamente 
sequências de números complexos ou funções. Em Mecânica Quântica, por exemplo, um sistema físico é 
descrito por um espaço de Hilbert complexo que contém os vetores de estado, que contém todas as 
informações do sistema e complexidades multifocais.
===
"""

print(text_to_analize)

resposta = llm(text_to_analize, max_tokens=100)
print("\nResposta do modelo:")
print(resposta["choices"][0]["text"])