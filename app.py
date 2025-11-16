import telebot
import os
from flask import Flask, request
import logging

# =========== CONFIGURAÇÃO ===========
TOKEN = os.getenv("BOT_TOKEN", "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI")
CHAT_ID = "-1002765666559"

# =========== INICIALIZAÇÃO ===========
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# =========== DEBUG ===========
logging.basicConfig(level=logging.DEBUG)
print(">>> BOT INICIANDO - DEBUG ATIVADO <<<")

# =========== ARSENAL DE POSTS SIMPLIFICADO ===========
posts = [
    {
        "legenda": "You can't see this on my Instagram...\nWant more? Click below 👇", 
        "midia": "AgACAgEAAxkBAAEf_BFpGQABUd0NjEhExUTVX0uJVrQ4udYAAgMLaxu1oMlEHmX9-lkG9foBAAMCAAN4AAM2BA", 
        "texto_botao_1": "🔥 VIP ACCESS 🔥", 
        "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", 
        "texto_botao_2": "📲 MY WHATSAPP 📲", 
        "link_botao_2": "https://t.me/MeuWhastAppbot"
    }
]

# =========== FUNÇÃO PARA POST ===========
def enviar_post():
    try:
        post = posts[0]
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text=post["texto_botao_1"], url=post["link_botao_1"])
        btn2 = telebot.types.InlineKeyboardButton(text=post["texto_botao_2"], url=post["link_botao_2"])
        markup.add(btn1, btn2)
        
        bot.send_photo(CHAT_ID, photo=post['midia'], caption=post['legenda'], reply_markup=markup)
        print("✅ POST ENVIADO COM SUCESSO!")
        return True
    except Exception as e:
        print(f"❌ ERRO AO ENVIAR POST: {e}")
        return False

# =========== DEBUG - CAPTURA TODAS AS MENSAGENS ===========
@bot.message_handler(func=lambda message: True)
def debug_all_messages(message):
    print(f"🔍 DEBUG - MENSAGEM RECEBIDA:")
    print(f"   Chat ID: {message.chat.id}")
    print(f"   Texto: {message.text}")
    print(f"   From: {message.from_user.first_name}")
    print(f"   Chat type: {message.chat.type}")
    print(f"   Comando: {message.text if message.text else 'None'}")
    
    # Responde a TODAS as mensagens para debug
    try:
        if message.text and message.text.startswith('/'):
            bot.reply_to(message, f"🔍 DEBUG: Comando recebido - {message.text}")
        else:
            bot.reply_to(message, f"🔍 DEBUG: Mensagem recebida - {message.text}")
        print("✅ Resposta de debug enviada!")
    except Exception as e:
        print(f"❌ Erro ao enviar resposta debug: {e}")

# =========== COMANDOS DO BOT ===========
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(f"🎯 Comando /start detectado!")
    try:
        bot.reply_to(message, "Olá! Eu sou a Isabelle Bot 🤖\n\nEstou funcionando perfeitamente! 💫\n\nUse /post para enviar um conteúdo.")
        print("✅ Resposta /start enviada!")
    except Exception as e:
        print(f"❌ Erro ao responder /start: {e}")

@bot.message_handler(commands=['post'])
def send_post(message):
    print(f"🎯 Comando /post detectado!")
    try:
        bot.reply_to(message, "🔄 Enviando post...")
        if enviar_post():
            bot.reply_to(message, "✅ Post enviado com sucesso!")
        else:
            bot.reply_to(message, "❌ Erro ao enviar post.")
        print("✅ Comando /post processado!")
    except Exception as e:
        print(f"❌ Erro ao processar /post: {e}")

# =========== WEBHOOK CONFIGURATION ===========
@app.route('/')
def index():
    return "🤖 Bot Isabelle está funcionando perfeitamente! 🚀"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("🌐 Webhook chamado pelo Telegram")
    try:
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            
            # Debug do update
            if update.message:
                print(f"📨 Update contém mensagem: {update.message.text}")
            else:
                print("📨 Update sem mensagem")
                
            bot.process_new_updates([update])
            print("✅ Update processado com sucesso!")
            return 'OK', 200
        else:
            print("❌ Content-type inválido")
            return 'Bad Request', 400
    except Exception as e:
        print(f"❌ Erro no webhook: {e}")
        return 'Error', 500

# =========== INICIALIZAÇÃO DO WEBHOOK ===========
def set_webhook():
    webhook_url = "https://bot-isabelle-tele.onrender.com/webhook"
    try:
        bot.remove_webhook()
        bot.set_webhook(url=webhook_url)
        print(f"✅ Webhook configurado: {webhook_url}")
    except Exception as e:
        print(f"❌ Erro ao configurar webhook: {e}")

# =========== INICIALIZAÇÃO ===========
if __name__ == '__main__':
    print(">>> BOT ISABELLE INICIANDO <<<")
    
    # Configura webhook
    set_webhook()
    
    print(">>> BOT INICIADO COM SUCESSO! <<<")
    print(">>> AGUARDANDO MENSAGENS... <<<")
    
    # Inicia servidor Flask
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
