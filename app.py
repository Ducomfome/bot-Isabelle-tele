import telebot
import os
from flask import Flask, request
import logging
import json
import time
import random
import threading
import requests

# =========== CONFIGURAÇÃO ===========
TOKEN = os.getenv("BOT_TOKEN", "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI")
CHAT_ID = "-1002765666559"
INTERVALO_ENTRE_POSTS_EM_MINUTOS = 60

# =========== INICIALIZAÇÃO ===========
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# =========== DEBUG ===========
logging.basicConfig(level=logging.DEBUG)
print(">>> BOT ISABELLE - ANTI-SONO ATIVADO <<<")

# =========== SISTEMA ANTI-SONO ===========
def keep_alive():
    """Faz requisições periódicas para manter o serviço acordado"""
    print("🔔 SISTEMA ANTI-SONO INICIADO")
    while True:
        try:
            response = requests.get("https://bot-isabelle-tele.onrender.com", timeout=10)
            print(f"🔔 Keep-alive: Serviço acordado (Status: {response.status_code})")
            time.sleep(300)  # 5 minutos entre chamadas
        except Exception as e:
            print(f"🔔 Keep-alive erro: {e}")
            time.sleep(60)  # Espera 1 minuto se der erro

# =========== ARSENAL COMPLETO - 24 POSTS ===========
posts = [
    # Post 1
    {"legenda": "You can't see this on my Instagram...\nWant more? Click below 👇", "midia": "AgACAgEAAxkBAAEf_BFpGQABUd0NjEhExUTVX0uJVrQ4udYAAgMLaxu1oMlEHmX9-lkG9foBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 2
    {"legenda": "This is just a preview...\nThe full video is much hotter 🔥\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_BJpGQABUWBxcjEKAAHX7jSVG0fakTtFAAIEC2sbtaDJRPKEefnxzRLHAQADAgADeAADNgQ", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 3
    {"legenda": "Imagine what happens next...\nI show everything in my VIP 😈\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_BZpGQABUf-17Oc8D_01tdkfhS2N7DMAAgcLaxu1oMlE0tm2yxOdecIBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 4
    {"legenda": "My best content is not free...\nBut it's worth every penny 💋\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_BRpGQABUdQ5_9r07JdpEJ0k_qSW5jsAAgYLaxu1oMlE7Z8alTRfGIwBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 5
    {"legenda": "This photo has a story...\nI tell it in my VIP 💬\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_BNpGQABUY_kGFCzLhRYxx9RJvJyDfAAgULaxu1oMlEU7OAYa2PZNQBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 6
    {"legenda": "Free preview is nice...\nBut VIP is better 💎\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_BxpGQABnSX0RL18B8zI2oYpCwW7ydsAAggLaxu1oMlEr1Q0TBRt8lUBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 7
    {"legenda": "What you see here is just 10%...\nMy VIP has the other 90% 🚀\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_B5pGQABneEYVD7WV6enls6lsLKU3_kAAgoLaxu1oMlEU8le9bJHWEIBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 8
    {"legenda": "I save my best moments for VIP members...\nWant to be one? 😏\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_B1pGQABnQO6RGCx04Ir_sYkF9-NjMwAAgkLaxu1oMlEDeYj-XxsBOcBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 9
    {"legenda": "This was too hot for Instagram...\nMy VIP has no limits 🔥\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_B9pGQABnbAtmRkEm5QO6KPBIrIKJvYAAgsLaxu1oMlE-kHKCLt56EUBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 10
    {"legenda": "If you like this...\nYou'll love my VIP content 🌟\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_CBpGQABnWB-vgSl_aBi7lo5c5hrbagAAgwLaxu1oMlEBL2KqtHynSgBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 11
    {"legenda": "Teasing is fun...\nBut showing everything is better 😈\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_CZpGQAB9Jhz5bUHsTiNMknNQu8-EbcAAg4Laxu1oMlErquPNUOy90MBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 12
    {"legenda": "Public content vs VIP content...\nYou already know which is better 💋\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_CdpGQAB9KfKqeUlUaoYZfddzP_B5joAAg0Laxu1oMlEkuys3U1KfRUBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 13
    {"legenda": "Just a little taste...\nThe full meal is in my VIP 🍑\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_ChpGQAB9JVCKAeOq5ROwsbBTOyh6ScAAg8Laxu1oMlEfJ0zstDPHOkBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 14
    {"legenda": "This content is addictive...\nOnce you start, you can't stop 💫\nClick below �👇", "midia": "AgACAgEAAxkBAAEf_ClpGQAB9PaDpvvK9kbzzGm2127NtbAAAhALaxu1oMlE-IaeSE0qYRUBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 15
    {"legenda": "The difference between preview and VIP...\nIs like night and day 🌙\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_C1pGQAB9Kppt66CCk84MIKS2FlRo6EAAhMLaxu1oMlECUR5UmEja9UBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 16
    {"legenda": "I sent this to the wrong person...\nNow I'm sending it to the right one - YOU 👀\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_CppGQAB9OnF1eYyNRUoLpOXZwg55oYAAhELaxu1oMlEPnrfm9NnqzwBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 17
    {"legenda": "Definition of 'adults only'...\nIf you're over 18, click below 🔞\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_CtpGQAB9B9jQP0ahitsRuSqoLr0PIgAAhILaxu1oMlEnBrRpxbtnPkBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 18
    {"legenda": "Some things I only do for paying members...\nThis is one of them 💰\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DVpGQFjf5PdCxnxWDhneLifhUTXYQACFQtrG7WgyURYpK_EbhpjJgEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 19
    {"legenda": "A secret between me, you...\nAnd whoever dares to click 🤫\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DRpGQFj2Sv2Gk3GZQyVFimjasH5awACFAtrG7WgyUQ7TfYQF_YPQQEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 20
    {"legenda": "Think of your dirtiest desire...\nIt's probably in my VIP video 😈\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DZpGQFjlEu8VzIrleHP-EQ6_w1ZCwACFgtrG7WgyURJ70Ao58sabQEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 21
    {"legenda": "I could describe what happens...\nBut it's better to see with your own eyes 👀\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DdpGQFjv4qyh3JOUo5fp3v5Szb-zwACFwtrG7WgyUSplvKNuT_bcAEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 22
    {"legenda": "This is not a test...\nIt's a trap of moans 💣\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DlpGQFjYeTHVUVrNSMOAoDXK2xFtQACGQtrG7WgyURlyVatJ941egEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 23
    {"legenda": "The uncensored version...\nNo platform would allow this online 🚫\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DhpGQFjaRSC8pPbKr3Wi7gmf4gkYAACGAtrG7WgyURi1nbpiNa6RwEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    # Post 24
    {"legenda": "If you think you've seen it all...\nClick below and think again 🤯\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_DtpGQFjQwsy7SrxG8rcSouGsHdpOAACGgtrG7WgyUTD-NSOQX5fqwEAAwIAA3gAAzYE", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"}
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
    print("⏰ THREAD DE POSTS AUTOMÁTICOS INICIADA - 24 POSTS DISPONÍVEIS")
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
            # MENSAGEM DE VENDAS DIRETA PRO VIP
            markup = telebot.types.InlineKeyboardMarkup()
            btn_vip = telebot.types.InlineKeyboardButton(text="🔥 COMPRAR VIP 🔥", url="https://t.me/ISABELLEVIPGRUPOBOT")
            btn_wpp = telebot.types.InlineKeyboardButton(text="📲 MEU WHATSAPP 📲", url="https://t.me/MeuWhastAppbot")
            markup.add(btn_vip, btn_wpp)
            
            resposta = """😈 **QUER VER MAIS DE MIM?** 😈

Essas prévias são só um gostinho do que você encontra no meu VIP!

💎 **MEU VIP INCLUI:**
✅ Conteúdo +18 exclusivo
✅ Fotos e vídeos sensuais
✅ Atenção personalizada
✅ Conteúdo que não posto em nenhum outro lugar

🔥 **PREÇOS IMBATÍVEIS:**
• 1 MÊS: R$19,90
• 3 MESES: R$49,90  
• VITALÍCIO: R$99,90

⚡ **GARANTA SEU ACESSO AGORA!**"""
            
            bot.send_message(message.chat.id, resposta, reply_markup=markup, parse_mode='Markdown')
            print("✅ /start - Direcionado para compra do VIP!")
            
        elif message.text == '/post':
            if str(message.chat.id) == CHAT_ID:
                # ENVIA DIRETO SEM MENSAGENS EXTRAS
                if enviar_post_automatico():
                    print("✅ /post executado silenciosamente!")
                else:
                    bot.send_message(message.chat.id, "❌ Erro ao enviar post.")  # Só erro aparece
            else:
                bot.send_message(message.chat.id, "❌ Este comando só funciona no grupo VIP.")
            print("✅ /post processado!")
            
        else:
            # Se mandar qualquer outra coisa, direciona pro VIP também
            markup = telebot.types.InlineKeyboardMarkup()
            btn_vip = telebot.types.InlineKeyboardButton(text="🔥 VER VIP 🔥", url="https://t.me/ISABELLEVIPGRUPOBOT")
            markup.add(btn_vip)
            
            bot.send_message(message.chat.id, "🤖 Quer ver conteúdo exclusivo? Clique abaixo! 👇", reply_markup=markup)
            
    except Exception as e:
        print(f"❌ ERRO: {e}")

# =========== WEBHOOK ===========
@app.route('/')
def index():
    return "🤖 Bot Isabelle - ANTI-SONO ATIVADO! 24/7!"

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
    print(f">>> ARSENAL: {len(posts)} POSTS CARREGADOS <<<")
    
    # Inicia thread de posts automáticos
    thread_posts = threading.Thread(target=posts_automaticos, daemon=True)
    thread_posts.start()
    
    # Inicia sistema anti-sono
    keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
    keep_alive_thread.start()
    
    print(">>> BOT INICIADO COM SUCESSO! <<<")
    print(">>> ANTI-SONO ATIVADO - SERVIRÁ 24/7! <<<")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
