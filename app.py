import telebot
import os
from flask import Flask, request
import logging

# =========== CONFIGURAÇÃO ===========
TOKEN = os.getenv("BOT_TOKEN", "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI")

# =========== INICIALIZAÇÃO ===========
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# =========== DEBUG ===========
logging.basicConfig(level=logging.DEBUG)
print(">>> BOT INICIANDO - VERSÃO SIMPLES <<<")

# =========== HANDLER ÚNICO E SIMPLES ===========
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    print(f"🔍 MENSAGEM RECEBIDA: {message.text}")
    print(f"🔍 CHAT ID: {message.chat.id}")
    print(f"🔍 FROM: {message.from_user.first_name}")
    
    try:
        if message.text == '/start':
            bot.reply_to(message, "🎉 FUNCIONANDO! Bot simples está respondendo!")
            print("✅ /start respondido!")
            
        elif message.text == '/post':
            bot.reply_to(message, "📸 Post seria enviado aqui!")
            print("✅ /post respondido!")
            
        else:
            bot.reply_to(message, f"🤖 Recebido: {message.text}")
            print("✅ Mensagem genérica respondida!")
            
    except Exception as e:
        print(f"❌ ERRO: {e}")

# =========== WEBHOOK ===========
@app.route('/')
def index():
    return "🤖 Bot SIMPLES funcionando!"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("🌐 Webhook chamado")
    try:
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            print("✅ Update processado!")
            return 'OK', 200
        return 'Bad Request', 400
    except Exception as e:
        print(f"❌ Erro webhook: {e}")
        return 'Error', 500

# =========== INICIALIZAÇÃO ===========
if __name__ == '__main__':
    print(">>> BOT INICIADO! <<<")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
