import gradio as gr
import base64
import time
import random
import asyncio

class ChatModel:
    def __init__(self):
        self.history = [{"role": "system", "content": "Sen Türkçe konuşan genel amaçlı bir asistansın. Her zaman kullanıcının verdiği talimatları doğru, kısa ve güzel bir gramer ile yerine getir."}]

    async def generate_response(self, user_input):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch

        device = "cuda"
        model_id = "Karayel-DDI/KARAYEL-LLM-q4"

        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
        )

        self.history.append({"role": "user", "content": user_input})

        #inputs = tokenizer.apply_chat_template(
        #    self.history,
        #    add_generation_prompt=True,
        #    return_tensors="pt"
        #).to(model.device)
        
        
        
        input_ids = tokenizer.apply_chat_template(
            self.history,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(model.device)
        
        terminators = [
            tokenizer.eos_token_id,
            tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]
        
        outputs = model.generate(
            input_ids,
            #max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )

        #outputs = model.generate(
        #    **inputs,
        #    use_cache=True,
        #    do_sample=True,
        #    top_k=50,
        #    top_p=0.60,
        #    temperature=0.3,
        #    repetition_penalty=1.1
        #)

        out_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        out_text = out_text.split('assistant\n\n')[-1]
        self.history.append({"role": "assistant", "content": out_text})

        return out_text

    def clear_history(self):
        self.history = [{"role": "system", "content": "Sen Türkçe konuşan genel amaçlı bir asistansın. Her zaman kullanıcının verdiği talimatları doğru, kısa ve güzel bir gramer ile yerine getir."}]

chat_model = ChatModel()

with open("logo.jpeg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

css = """
<style>
    .logo-container {
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 100;
    }
    .logo {
        max-width: 100px;
        max-height: 80px;
    }
    .gradio-container {
        padding-top: 60px;
    }
    .thinking {
        font-style: italic;
        color: gray;
    }
</style>
"""

thinking_messages = [
    "🧠 Düşünüyorum...",
    "💡 Fikir üretiyorum...",
    "🔍 Araştırıyorum...",
    "📚 Bilgilerimi gözden geçiriyorum...",
    "⚙️ İşleniyor...",
    "🤔 Hımm, bir düşüneyim...",
    "🌟 İlham peşindeyim...",
    "🧩 Parçaları birleştiriyorum...",
    "🔮 Geleceği okuyorum...",
    "🎭 Cevabı formüle ediyorum..."
]

with gr.Blocks(css=css) as demo:
    gr.HTML(f'''
    <div class="logo-container">
        <img src="data:image/png;base64,{encoded_string}" alt="Logo" class="logo">
    </div>
    ''')
    
    gr.Markdown("# Karayel Rehberlik Uygulaması")
    
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Mesajınızı yazın")
    clear = gr.Button("Temizle", elem_classes=["primary-btn"])

    async def user(user_message, history):
        history = history + [[user_message, None]]
        return "", history

    async def bot(history):
        user_message = history[-1][0]
        thinking_message = random.choice(thinking_messages)
        
        # Düşünme mesajını göster
        history[-1][1] = f"<span class='thinking'>{thinking_message}</span>"
        yield history
        
        # Model cevabını bekle
        bot_message = await chat_model.generate_response(user_message)
        
        # Cevabı karakter karakter göster
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history

    def clear_history():
        chat_model.clear_history()
        return None

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(clear_history, None, chatbot, queue=False)

demo.launch()