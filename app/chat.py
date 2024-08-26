# chat.py
from .db import vectorstore
from transformers import GPT2Tokenizer
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def create_chat_prompt(context, history, question):
    
    messages = [
        {"role": "system", "content": "Você é um assistente que responde dúvidas e suas respostas devem estar relacionadas ao contexto. Quando não tiver certeza da resposta, pode fazer outra pergunta ao usuário. Caso não tenha resposta para a pergunta, você pode sugerir que o usuário entre em contato"},
        {"role": "system", "content": f"Atenção: Nunca saia do contexto, Leve em consideração esse contexto:. {context}"},
    ]
    messages.extend(history)
    messages.append({"role": "user", "content": question})


    return messages

def get_ai_response(prompt, context, history):
    chat_prompt = create_chat_prompt(context, history, prompt)
    print(chat_prompt)
    completion = ChatOpenAI(
        model="gpt-4-turbo", 
        temperature=0.2,
        max_tokens=4096,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    ai_msg = completion.invoke(chat_prompt)

    print(ai_msg)
    
    return ai_msg.content
