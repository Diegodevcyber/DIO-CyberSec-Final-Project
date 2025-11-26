from cryptography.fernet import Fernet
import os
import pathlib

# =======================================================================
# CONFIGURAÇÕES DE RECUPERAÇÃO
# =======================================================================
DIRETORIO_ALVO = "ransomware_simulado/arquivos_teste"
EXTENSAO_CRIPTOGRAFADA = ".locked"
KEY_FILE = "ransomware_simulado/chave.key"

def carregar_chave(key_path=KEY_FILE):
    """Carrega a chave Fernet a partir do arquivo."""
    return open(key_path, "rb").read()

def descriptografar_arquivo(caminho_arquivo, chave):
    """Descriptografa o arquivo .locked e o salva com seu nome original."""
    f = Fernet(chave)
    try:
        with open(caminho_arquivo, "rb") as file:
            dados_encriptados = file.read()
        
        dados_descriptografados = f.decrypt(dados_encriptados) 
        
        # Remove a extensão .locked para obter o nome original
        caminho_original = str(caminho_arquivo).removesuffix(EXTENSAO_CRIPTOGRAFADA)
        
        with open(caminho_original, "wb") as file:
            file.write(dados_descriptografados) 
            
        os.remove(caminho_arquivo)
        
    except Exception as e:
        print(f"Erro ao descriptografar {caminho_arquivo}. Verifique se a chave está correta: {e}")

def encontrar_arquivos_locked(diretorio):
    """Percorre o diretório e retorna uma lista de caminhos de arquivos com a extensão .locked."""
    lista = []
    for caminho in pathlib.Path(diretorio).rglob('*'):
        if caminho.is_file() and str(caminho).endswith(EXTENSAO_CRIPTOGRAFADA):
            lista.append(caminho)
    return lista

def main():
    try:
        chave = carregar_chave()
    except FileNotFoundError:
        print(f"Erro: Chave de descriptografia '{KEY_FILE}' não encontrada.")
        return

    arquivos = encontrar_arquivos_locked(DIRETORIO_ALVO)
    
    if not arquivos:
         print("Nenhum arquivo criptografado (.locked) encontrado para descriptografar.")
         return
         
    print(f"Iniciando descriptografia de {len(arquivos)} arquivos...")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        
    print("Arquivos restaurados com sucesso!")

if __name__ == "__main__":
    main()