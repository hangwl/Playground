import gradio as gr
import openai

openai.api_key = open("c:/Users/HangWei/Desktop/chatgptapi/key.txt","r").read().strip('\n')

message_history = [{"role": "user", "content": f"You are a sentiment analysis bot. I will provide you with user comments and feedback, and you will respond with a rating score from 1 to 5, with 1 reflecting the lowest possible score and 5 reflecting the highest possible score. Reply only with values from 1 to 5 for further input. Flag the input if it is inappropriate, sarcastic, or irrelevant. If you understand, say OK."}, 
                    {"role": "assistant", "content": f"OK"}]

def predict(input):
    global message_history
    message_history.append({"role": "user", "content": input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return response

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message here").style(container=False)
        txt.submit(predict, txt, chatbot)
        #txt.submit(lambda: "", None, txt)
        txt.submit(None, None, txt, _js="() => {''}")

demo.launch()
