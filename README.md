# 🔒 DIO-CyberSec-Final-Project

### Autor: Diegodevcyber

---

### 📜🛑 **COPYRIGHT E TERMOS DE USO  (DISCLAIMER)** 🛑

**© 2025 Diegodevcyber.** Todo o material contido neste repositório é fornecido exclusivamente para **fins educacionais e de pesquisa em Cibersegurança**.

> **⚠️ Atenção:** A execução destes códigos deve ser feita **somente** em ambientes **isolados e controlados** (Máquinas Virtuais ou Sandboxes). O autor não se responsabiliza por qualquer dano ou uso indevido que viole a lei.

---

---

### 🎯🛑 **VISÃO GERAL E OBJETIVOS DO PROJETO** 🛑

Este projeto demonstra o funcionamento técnico do **Ransomware** e **Keylogger** em um ambiente seguro, focando na **Reflexão sobre Defesa**.

### Objetivos de Aprendizagem

* Compreender o ciclo de ataque: exploração da criptografia ($Fernet$) e da captura de *input* ($pynput$).
* Identificar vulnerabilidades de sistemas e a importância do fator humano na segurança.
* Documentar estratégias de **mitigação** e **prevenção** contra ameaças digitais.

---

### 🔑🛑 **ANÁLISE DETALHADA DE ATAQUE** 🛑

### 3.1. Ransomware Simulado: Sequestro de Dados

Este módulo demonstra como a criptografia simétrica é usada para sequestrar dados e simular o pedido de resgate. 

| Arquivo | Função | Módulos Chave | Análise do Mecanismo |
| :--- | :--- | :--- | :--- |
| **`ransomware_ataque.py`** | **Ataque (Criptografia):** Gera a chave e criptografa arquivos no diretório `arquivos_teste/`, renomeando-os para `.locked`. | `cryptography.fernet` | A chave é a **única forma** de reversão. É gerada uma nota de resgate (`LEIA ISSO.txt`) no diretório alvo. |
| **`ransomware_recuperacao.py`** | **Defesa (Simulada):** Simula a ação de recuperação, utilizando a chave secreta para descriptografar os arquivos e restaurar o acesso. | `cryptography.fernet` | Reverte o dano, demonstrando que a segurança do dado depende da chave. |

### 3.2. Keylogger Simulado: Captura e Exfiltração de Teclas

Este módulo foca na captura de eventos do teclado e na exfiltração furtiva dos dados coletados. 

| Arquivo | Função | Módulos Chave | Análise da Furtividade e Exfiltração |
| :--- | :--- | :--- | :--- |
| **`keylogger_local.py`** | **Captura Local:** Usa $pynput$ para registrar todas as teclas digitadas em um arquivo de log (`log.txt`). | `pynput` | Demonstra a intercepção de *input* em tempo real. |
| **`keylogger_remoto_email.py`** | **Exfiltração Remota:** Utiliza $threading.Timer$ para agendar o envio periódico do `log.txt` via **SMTP** ($smtplib$) para um e-mail remoto. | `pynput`, `smtplib`, `threading` | O uso de agendamento e a necessidade de configurar credenciais de **App Password** simulam técnicas reais de exfiltração em intervalos. |

---

### 🛡️🛑 **REFLEXÃO E ESTRATÉGIAS DE DEFESA (MITIGAÇÃO)** 🛑

O principal valor deste projeto é a capacidade de aplicar o conhecimento na **defesa**.

| Estratégia de Defesa | Princípio de Ação | Como Mitiga o Ransomware/Keylogger |
| :--- | :--- | :--- |
| **Backup 3-2-1** | Manter 3 cópias de dados em 2 tipos de mídia, com 1 cópia *offline* (fora do local). | **Neutralização do Resgate:** Permite a restauração completa dos dados, tornando o ataque de Ransomware ineficaz. |
| **Firewall de Aplicação** | Monitoramento e bloqueio de tráfego de saída incomum na rede. | **Bloqueio da Exfiltração:** Impede que o Keylogger abra a conexão SMTP para enviar o `log.txt` para o atacante. |
| **Sandboxing & Virtualização** | Executar programas suspeitos em ambientes isolados. | **Contenção:** Restringe os efeitos do Ransomware e do Keylogger apenas ao ambiente de teste. |
| **EDR (Endpoint Detection and Response)** | Detecta padrões de comportamento suspeito e anômalo. | **Detecção Comportamental:** Identifica o acesso não autorizado e maciço a arquivos (Ransomware) ou o *hooking* do teclado (Keylogger). |
| **Conscientização do Usuário** | Treinamento constante sobre *phishing* e engenharia social. | **Prevenção na Fonte:** Impede que o usuário execute o *malware* inicial, quebrando a cadeia de ataque no primeiro elo. |

---

### ⚙️🛑 **SETUP DO AMBIENTE DE TESTE (GUIA DE INSTALAÇÃO)** 🛑

Siga este guia para configurar seu ambiente de testes de forma segura.

### A. Pré-Requisitos

1.  **Python 3:** Instalado e configurado no seu sistema.
2.  **Git:** Para clonar o repositório.

### B. Instalação das Dependências

Instale todas as bibliotecas necessárias usando o arquivo `requirements.txt`.

#### Passo 1: Clonagem e Navegação
```bash
git clone [https://github.com/Diegodevcyber/Malware-Simulado-Python-Educacional.git](https://github.com/Diegodevcyber/Malware-Simulado-Python-Educacional.git)
cd Malware-Simulado-Python-Educacional
```
#### Passo 2: Criação e Ativação do Ambiente Virtual (Recomendado)
Use um ambiente virtual (venv) para isolar as dependências do projeto.

### 1. Cria o ambiente virtual
```
python3 -m venv venv 
```

### 2. Ativa o ambiente virtual (Linux/macOS)
```
source venv/bin/activate 
```
### OU Ativa o ambiente virtual (Windows PowerShell)
```
.\venv\Scripts\Activate
```
#### Passo 3: Instalação dos Módulos

```
pip install -r requirements.txt
```

### ⚙️🛑 **EXECUÇÃO DOS SCRIPTS (COMANDOS DE TESTE)** 🛑

Para executar os módulos, navegue para o diretório principal do projeto no seu terminal e use os comandos abaixo. **Certifique-se de que o ambiente virtual está ativo.**

---

### 🔑🛑 **RANSOMWARE SIMULADO** 🛑

#### 1. Ataque (Criptografia)

* **Objetivo:** Simula a criptografia dos arquivos de teste.
* **Comando:**
    ```bash
    python ransomware_simulado/ransomware_ataque.py
    ```
* **Resultado:** Arquivos são criptografados com a extensão `.locked` e uma nota de resgate (`LEIA ISSO.txt`) é criada em `/ransomware_simulado/arquivos_teste`.

#### 2. Recuperação (Descriptografia)

* **Objetivo:** Simula a recuperação de dados, revertendo o processo de criptografia.
* **Comando:**
    ```bash
    python ransomware_simulado/ransomware_recuperacao.py
    ```
* **Resultado:** Arquivos são descriptografados e restaurados ao seu formato original (usa o arquivo `chave.key`).

---

### 📧🛑 **KEYLOGGER SIMULADO** 🛑

#### 1. Captura Local

* **Objetivo:** Inicia a captura de teclas, registrando-as em um arquivo local.
* **Comando:**
    ```bash
    python keylogger_simulado/keylogger_local.py
    ```
* **Log:** As teclas digitadas são salvas em `/keylogger_simulado/log.txt`.

#### 2. Captura e Envio Remoto (Exfiltração)

* **Objetivo:** Inicia a captura e o agendamento de envio do log por e-mail, simulando a exfiltração.
* **Comando:**
    ```bash
    python keylogger_simulado/keylogger_remoto_email.py
    ```
* **Atenção:** **Edite o script** para configurar as credenciais de e-mail antes de executar. Este script usa *threading.Timer* para o envio periódico.

## 🎉 Encerramento e Próximos Passos

Este projeto demonstra, de forma prática e ética, o poder e os riscos das ferramentas de ataque cibernético. Ao compreender a mecânica por trás de ameaças como Ransomware e Keylogger, reforçamos nosso compromisso com a defesa digital.

---

### 👉 Próximos Desafios (Ideias de Melhoria)

Para evoluir este projeto no seu portfólio, considere as seguintes extensões:

* **Ofuscação de Código:** Implementar técnicas simples de ofuscação (ex: `base64`, XOR) nos scripts para dificultar a análise estática.
* **Comunicação C2 (Command and Control):** Substituir o envio de e-mail por comunicação via requisição HTTP ($requests$) para um servidor simples, simulando um C2.
* **Detecção de Sandbox:** Adicionar verificações nos scripts para detectar se estão rodando em um ambiente virtual, abortando a execução para simular *malware* mais avançado.

### 🛑 **FLUXO DE ENVIO PARA O GITHUB** 🛑

Este guia detalha os comandos necessários para enviar (fazer o *push*) seu projeto finalizado do seu ambiente local para o seu repositório remoto no GitHub.

---

### 1. Inicialização e Preparação Local

Estes passos garantem que o seu diretório seja um repositório Git rastreável.

* **Inicializar o repositório Git** (Se esta for a primeira vez que você está usando o Git nesta pasta):
    ```bash
    git init
    ```

* **Adicionar todos os arquivos ao *staging area*** (Preparar para o *commit*):
    ```bash
    git add .
    ```

---

### 2. Confirmação (Commit) da Entrega Final

O *commit* salva a versão atual do seu projeto com uma mensagem descritiva.

* **Realizar o *commit* com a mensagem final:**
    ```bash
    git commit -m "Projeto Final: Implementacao completa e documentada de Ransomware e Keylogger para fins educacionais."
    ```

---

### 3. Conexão e Envio Remoto (Push)

Este é o passo que conecta seu projeto local ao GitHub e envia os arquivos.

#### **A. Conectar ao Repositório Remoto**

* **Comando:** Adiciona o link do seu repositório GitHub como destino (`origin`). **Substitua o *placeholder* pelo seu link real.**
    ```bash
    git remote add origin [SEU_LINK_DO_REPOSITORIO]
    ```

#### **B. Enviar para a Branch Principal**

* **Comando:** Envia todos os seus arquivos (branch `main`) para o GitHub.
    ```bash
    git push -u origin main
    ```

> **🔑 Dica:** Se o `git push` falhar, você pode precisar configurar um **Personal Access Token (PAT)** nas suas configurações do GitHub.
>
> ---

### 🔗🛑 **CONECTE-SE COM O AUTHOR** 🛑

Obrigado por revisar este projeto de aprendizado em cibersegurança. Mantenha-se atualizado e vamos nos conectar!

| Plataforma | Perfil |
| :--- | :--- |
| **GitHub** | [@Diegodevcyber](https://github.com/Diegodevcyber) |
| **LinkedIn** | *https://www.linkedin.com/in/diegodevcyber/* |

Bons estudos e mantenha-se seguro! 🔒

---

