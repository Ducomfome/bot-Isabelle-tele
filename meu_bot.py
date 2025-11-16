import telebot
import time
import random
import os

# =========== ÁREA DE CONFIGURAÇÃO (FINAL E CORRETA) ===========
TOKEN = "8272120672:AAFPTNTVl7JveC-C-52BCbLK_-wF0iIdKKI" # Token do @Isabellegerentebot
CHAT_ID = "-1002765666559" # ID do grupo "Isabelle - prévias🫦"
INTERVALO_ENTRE_POSTS_EM_MINUTOS = 60 # RITMO NORMAL: 1 POST POR HORA

# =========== ARSENAL DE POSTS ATUALIZADO COM LEGENDAS EM INGLÊS ===========
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
    {"legenda": "This content is addictive...\nOnce you start, you can't stop 💫\nClick below 👇", "midia": "AgACAgEAAxkBAAEf_ClpGQAB9PaDpvvK9kbzzGm2127NtbAAAhALaxu1oMlE-IaeSE0qYRUBAAMCAAN4AAM2BA", "texto_botao_1": "🔥 VIP ACCESS 🔥", "link_botao_1": "https://t.me/ISABELLEVIPGRUPOBOT", "texto_botao_2": "📲 MY WHATSAPP 📲", "link_botao_2": "https://t.me/MeuWhastAppbot"},
    
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

# Daqui pra baixo, o motor da máquina.
# ---------------------------------------------------------------------
# Verifica se o token foi carregado do servidor (para deploy online)
if "BOT_TOKEN" in os.environ:
    TOKEN = os.environ["BOT_TOKEN"]

if TOKEN is None:
    print("ERRO CRÍTICO: Token não encontrado. Defina a variável TOKEN ou a variável de ambiente BOT_TOKEN.")
    exit()

bot = telebot.TeleBot(TOKEN)
print(">>> BOT COM FUNIL DUPLO INICIADO. Operação em máxima potência. <<<")

while True:
    try:
        post_aleatorio = random.choice(posts)
        markup = telebot.types.InlineKeyboardMarkup()

        # Criando os dois botões a partir das informações do post
        btn1 = telebot.types.InlineKeyboardButton(text=post_aleatorio["texto_botao_1"], url=post_aleatorio["link_botao_1"])
        btn2 = telebot.types.InlineKeyboardButton(text=post_aleatorio["texto_botao_2"], url=post_aleatorio["link_botao_2"])

        # Adicionando os dois botões na mesma linha, lado a lado
        markup.add(btn1, btn2)
        
        bot.send_photo(CHAT_ID, photo=post_aleatorio['midia'], caption=post_aleatorio['legenda'], reply_markup=markup)
        print(f"Post com botão duplo enviado: {post_aleatorio['legenda']}")
        
        print(f"Próximo post em {INTERVALO_ENTRE_POSTS_EM_MINUTOS} minutos...")
        time.sleep(INTERVALO_ENTRE_POSTS_EM_MINUTOS * 60)
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}. Verificando o file_id: {post_aleatorio.get('midia', 'N/A')}")
        time.sleep(30)