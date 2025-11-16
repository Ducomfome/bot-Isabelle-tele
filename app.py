import telebot
import os
from flask import Flask, request
import logging
import json
import time
import random
import threading

# =========== CONFIGURAÇÃO ===========
TOKEN = os.getenv("BOT_TOKEN", "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI")
CHAT_ID = "-1002765666559"
INTERVALO_ENTRE_POSTS_EM_MINUTOS = 60

# =========== INICIALIZAÇÃO ===========
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# =========== DEBUG ===========
logging.basicConfig(level=logging.DEBUG)
print(">>> BOT ISABELLE - VERSÃO FINAL <<<")

# =========== ARSENAL DE POSTS ===========
posts = [
    {
        "legenda": "You can't see this on my Instagram...\nWant more? Click below 👇", 
        "midia": "AgACAgEAAxkBAAEf_BFpGQABUd0NjEhExUTVX0uJVrQ4udYAAgMLaxu1oMlEHmX9-lkG9foBAAMCAAN4AAM2BA", 
        "texto_botao_1": "🔥 VIP ACCESS 🔥", 
        "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", 
        "texto_botao_2": "📲 MY WHATSAPP 📲", 
        "link_botao_2": "https://t.me/MeuWhastAppbot"
    },
    {
        "legenda": "This is just a preview...\nThe full video is much hotter 🔥\nClick below 👇", 
        "midia": "AgACAgEAAxkBAAEf_BJpGQABUWBxcjEKAAHX7jSVG0fakTtFAAIEC2sbtaDJRPKEefnxzRLHAQADAgADeAADNgQ", 
        "texto_botao_1": "🔥 VIP ACCESS 🔥", 
        "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", 
        "texto_botao_2": "📲 MY WHATSAPP 📲", 
        "link_botao_2": "https://t.me/MeuWhastAppbot"
    }
]

# =========== FUNÇÃO PARA POST AUTOMÁTICO ===========
def enviar_post_automatico():
    try:
        post_aleatorio = random.choice(posts)
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text=post_aleatorio["texto_botao_1"], url=post_aleatorio["link_botao_1"])
        btn2 = telebot.types.InlineKeyboardButton(text=post_aleatorio["texto_botao_2"], url=post_aleatorio["link_botao_2"])
        markup.add(btn1, btn2)
        
        bot.send_photo(CHAT_ID, photo=post_aleatorio['midia'], caption=post_aleatorio['legenda'], reply_markup=markup)
        print(f"✅ POST AUTOMÁTICO ENVIADO: {post_aleatorio['legenda']}")
        return True
    except Exception as e:
        print(f"❌ ERRO AO ENVIAR POST: {e}")
        return False

# =========== THREAD PARA POSTS AUTOMÁTICOS ===========
def posts_automaticos():
    print("⏰ THREAD DE POSTS AUTOMÁTICOS INICIADA")
    while True:
        try:
            enviar_post_automatico()
            time.sleep(INTERVALO_ENTRE_POSTS_EM_MINUTOS * 60)
        except Exception as e:
            print(f"❌ Erro na thread: {e}")
            time.sleep(60)

# =========== PROCESSAMENTO DE COMANDOS ===========
def process_message(message):
    print(f"🔍 MENSAGEM: {message.text}")
    print(f"🔍 CHAT: {message.chat.id}")
    
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, "🤖 Olá! Eu sou a Isabelle Bot!\n\nEstou funcionando perfeitamente! 💫\n\nUse /post para enviar conteúdo.")
            print("✅ /start respondido!")
            
        elif message.text == '/post':
            if str(message.chat.id) == CHAT_ID:
                bot.send_message(message.chat.id, "🔄 Enviando post...")
                if enviar_post_automatico():
                    bot.send_message(message.chat.id, "✅ Post enviado com sucesso!")
                else:
                    bot.send_message(message.chat.id, "❌ Erro ao enviar post.")
            else:
                bot.send_message(message.chat.id, "❌ Este comando só funciona no grupo VIP.")
            print("✅ /post processado!")
            
        else:
            bot.send_message(message.chat.id, "🤖 Use /start ou /post")
            
    except Exception as e:
        print(f"❌ ERRO: {e}")

# =========== WEBHOOK ===========
@app.route('/')
def index():
    return "🤖 Bot Isabelle - VERSÃO FINAL!"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("🌐 Webhook chamado")
    try:
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            data = json.loads(json_string)
            
            # Processa manualmente a mensagem
            if 'message' in data:
                message = telebot.types.Message.de_json(data['message'])
                process_message(message)
            
            print("✅ Update processado!")
            return 'OK', 200
            
        return 'Bad Request', 400
    except Exception as e:
        print(f"❌ Erro webhook: {e}")
        return 'Error', 500

# =========== INICIALIZAÇÃO ===========
if __name__ == '__main__':
    print(">>> BOT ISABELLE INICIANDO <<<")
    
    # Inicia thread de posts automáticos
    thread_posts = threading.Thread(target=posts_automaticos, daemon=True)
    thread_posts.start()
    
    print(">>> BOT INICIADO COM SUCESSO! <<<")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
