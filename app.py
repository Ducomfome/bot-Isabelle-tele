import telebot
import os
from flask import Flask, request
import logging
import json

# =========== CONFIGURAÇÃO ===========
TOKEN = os.getenv("BOT_TOKEN", "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI")
CHAT_ID = "-1002765666559"

# =========== INICIALIZAÇÃO ===========
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# =========== DEBUG ===========
logging.basicConfig(level=logging.DEBUG)
print(">>> BOT INICIANDO - PROCESSAMENTO MANUAL <<<")

# =========== FUNÇÃO PARA PROCESSAR MENSAGENS MANUALMENTE ===========
def process_message(message):
    print(f"🔍 PROCESSANDO MENSAGEM: {message.text}")
    print(f"🔍 CHAT ID: {message.chat.id}")
    print(f"🔍 FROM: {message.from_user.first_name}")
    
    try:
        if message.text == '/start':
            bot.send_message(message.chat.id, "🎉 FUNCIONOU! Processamento MANUAL!")
            print("✅ /start respondido!")
            
        elif message.text == '/post':
            # Post simples para teste
            bot.send_message(CHAT_ID, "📸 POST DE TESTE - Funcionando!")
            bot.send_message(message.chat.id, "✅ Post enviado no grupo!")
            print("✅ /post processado!")
            
        else:
            bot.send_message(message.chat.id, f"🤖 Recebido: {message.text}")
            print("✅ Mensagem genérica respondida!")
            
    except Exception as e:
        print(f"❌ ERRO ao processar: {e}")

# =========== WEBHOOK ===========
@app.route('/')
def index():
    return "🤖 Bot com processamento MANUAL!"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("🌐 Webhook chamado")
    try:
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            data = json.loads(json_string)
            
            print(f"📨 Dados recebidos: {json.dumps(data, indent=2)}")
            
            # Processa manualmente a mensagem
            if 'message' in data:
                message = telebot.types.Message.de_json(data['message'])
                process_message(message)
            
            print("✅ Update processado MANUALMENTE!")
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
