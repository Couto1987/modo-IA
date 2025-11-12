import requests
import datetime
import locale

def consultar_cotacao_moeda():
    """
    Consulta a cotação de uma moeda em relação ao Real (BRL) usando a Awesome API.
    Exibe valor atual, máxima, mínima e data/hora da última atualização.
    Trata erros de conexão e moeda inexistente.
    """
    
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
        except locale.Error:
            print("Aviso: Falha ao configurar a exibição de moeda. O valor será exibido sem formatação BRL completa.")

    print("💵 Consultor de Cotação de Moedas em Tempo Real! ⏱️")
    print("---")
    
    # 1. Pede o código da moeda (ex: USD, EUR, BTC)
    moeda_base = input("Digite o código da moeda que deseja consultar (ex: USD para Dólar, EUR para Euro): ").upper().strip()
    
    # 2. Monta o par de moedas para a URL (ex: USDBRL, EURBRL)
    par_moeda = f"{moeda_base}BRL"
    
    # 3. Monta a URL da API
    url_api = f"https://economia.awesomeapi.com.br/json/last/{par_moeda}"
    
    print(f"\n🌍 Tentando buscar a cotação de {moeda_base} em relação ao BRL...")
    
    try:
        resposta = requests.get(url_api, timeout=10)
        
        dados = resposta.json()
        
        # 4. Trata o retorno da API
        if resposta.status_code == 200:
            
            if not dados:
                print(f"\n❌ Falha na Busca! O par de moedas {par_moeda} (cotação de {moeda_base} para Real) não foi encontrado.")
                print("Verifique se você digitou o código da moeda corretamente (ex: USD, EUR, JPY).")
                
            else:
                cotacao = dados[par_moeda]
                
                valor_atual = float(cotacao['bid'])
                valor_maximo = float(cotacao['high'])
                valor_minimo = float(cotacao['low'])
                timestamp_atualizacao = int(cotacao['timestamp'])
                
                data_hora_atualizacao = datetime.datetime.fromtimestamp(timestamp_atualizacao)
                
                # 5. Exibindo as informações
                print("\n✅ Sucesso! Dados da Cotação Encontrados:")
                print("---")
                print(f"💰 **Moeda Consultada:** {cotacao['name']}")
                print(f"➡️ **Valor Atual (Compra):** {locale.currency(valor_atual, grouping=True)}")
                print(f"🔼 **Máxima 24h:** {locale.currency(valor_maximo, grouping=True)}")
                print(f"🔽 **Mínima 24h:** {locale.currency(valor_minimo, grouping=True)}")
                print(f"📅 **Última Atualização:** {data_hora_atualizacao.strftime('%d/%m/%Y às %H:%M:%S')}")
                print("---")
                
        else:
            print(f"\n❌ Falha na comunicação com a API (HTTP {resposta.status_code}). Tente novamente mais tarde.")

    # 6. Tratando Erros de Conexão (Timeout, sem internet, etc.)
    except requests.exceptions.RequestException as e:
        print("\n🚨 **ERRO DE REQUISIÇÃO!**")
        print("Não foi possível acessar a API. Verifique sua conexão com a internet.")
        print(f"Detalhe do erro: {e}")
    except Exception as e:
        print("\n⚠️ **OCORREU UM ERRO INESPERADO.**")
        print("Pode ser um problema temporário no formato dos dados da API.")
        print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
consultar_cotacao_moeda()