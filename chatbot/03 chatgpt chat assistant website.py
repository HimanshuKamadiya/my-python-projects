import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a helping hand for the user"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "chatbot")

demo.launch(share=True)