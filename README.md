### Rastreamento Automático de Preços

Este projeto consiste em um script Python que rastreia o preço de um produto específico em um site e envia uma notificação por e-mail quando o preço cai abaixo de um determinado valor.

#### Funcionalidades

- **Rastreamento de Preço**: O script acessa uma página da web usando o módulo `requests` e analisa o HTML da página usando `BeautifulSoup` para extrair informações sobre o produto, como título e preço atual.

- **Notificação por E-mail**: Quando o preço do produto cai abaixo de um valor específico (definido pelo usuário), o script envia automaticamente uma notificação por e-mail usando o módulo `smtplib`. Isso permite que os usuários recebam alertas imediatos quando o preço desejado é alcançado.

#### Uso

Siga estas etapas para configurar e utilizar o rastreador de preços:

1. **Instalação de Dependências**

   Antes de executar o script, certifique-se de ter instalado todas as dependências listadas no arquivo `requirements.txt`. Você pode instalar as dependências utilizando o `pip` da seguinte forma:

   ```bash
   pip install -r requirements.txt
   ```

   Isso garantirá que todas as bibliotecas necessárias, como `requests` e `BeautifulSoup`, estejam disponíveis no seu ambiente Python.

2. **Configuração do Script**

   - **URL do Produto**: Defina a URL do produto que você deseja rastrear no script Python.
   
   - **Limite de Preço**: Especifique o valor limite abaixo do qual deseja receber notificações por e-mail quando o preço do produto cair.

   - **Configuração do E-mail**: No arquivo `emailtool.py`, atualize os detalhes do servidor SMTP, remetente, destinatário e credenciais de e-mail de acordo com sua configuração.

3. **Execução Automatizada (Opcional)**

   Para automatizar o rastreamento de preços e receber notificações em intervalos regulares, você pode configurar uma tarefa cron no Linux para executar o script em horários pré-definidos.

   - **Acessar o Crontab:** Abra um terminal e digite:
     ```bash
     crontab -e
     ```
     
   - **Agendar o Script:** Adicione a seguinte linha ao arquivo crontab para agendar o script para ser executado a cada hora (1 minuto após a hora):
     ```bash
     1 * * * * [caminho_para_main]/main.py
     ```
   - Substitua `[caminho_para_main]` pelo caminho do diretório onde está localizado `main.py`.

   Por exemplo:
   ```bash
   1 * * * * /usr/bin/python3/home/user/scripts/main.py
   ```


#### Observações

- Certifique-se de ter as permissões necessárias para executar o script e acessar a página da web do produto.
  
- Mantenha suas credenciais de e-mail e outras informações sensíveis em um local seguro e não compartilhe publicamente.

- O script pode ser personalizado para rastrear diferentes produtos ou incluir funcionalidades adicionais, como registrar histórico de preços.

Com essas instruções, você poderá configurar e utilizar o rastreador de preços para monitorar automaticamente o preço de um produto desejado e receber notificações oportunas por e-mail quando o preço atingir o valor desejado.
