import requests

def consultar_cep():
    """
    Pede um CEP ao usuário, consulta a API ViaCEP e exibe as informações 
    de endereço (logradouro, bairro, cidade, estado).
    Trata erros de conexão e CEP inexistente.
    """
    
    print("🏠 Consultor de Endereço por CEP! 📪")
    print("---")
    
    # 1. Pede o CEP ao usuário
    cep = input("Digite o **CEP** que você quer consultar (apenas números, ex: 01001000): ")
    
    cep = cep.replace("-", "").replace(".", "").strip()
    
    # 2. Verifica se o CEP tem o tamanho correto (8 dígitos)
    if not cep.isdigit() or len(cep) != 8:
        print("\n❌ CEP inválido! Por favor, digite 8 dígitos numéricos.")
        return

    # 3. Monta a URL da API
    url_api = f"https://viacep.com.br/ws/{cep}/json/"
    
    print(f"\n🌍 Tentando buscar endereço para o CEP {cep}...")
    
    try:
        resposta = requests.get(url_api, timeout=10)
        
        dados = resposta.json()

        # 4. Trata o retorno da API
        if resposta.status_code == 200:
            if 'erro' in dados and dados['erro']:
                print(f"\n❌ Falha na Busca! O CEP **{cep}** não foi encontrado/é inexistente.")
                
            else:
                logradouro = dados.get('logradouro', 'Não informado') # .get() evita erro se o campo for vazio
                bairro = dados.get('bairro', 'Não informado')
                cidade = dados.get('localidade', 'Não informado')
                estado = dados.get('uf', 'Não informado')
                
                print("\n✅ Sucesso! Endereço Encontrado:")
                print("---")
                print(f"🛣️ **Logradouro:** {logradouro}")
                print(f"🏘️ **Bairro:** {bairro}")
                print(f"🏙️ **Cidade:** {cidade}")
                print(f"🗺️ **Estado (UF):** {estado}")
                print("---")
                
        else:
            
            print(f"\n❌ Falha na comunicação com a API (HTTP {resposta.status_code}). Tente novamente mais tarde.")

    # 5. Tratando Erros de Conexão (Timeout, sem internet, etc.)
    except requests.exceptions.RequestException as e:
        print("\n🚨 **ERRO DE CONEXÃO!**")
        print("Não foi possível acessar a API. Verifique sua conexão com a internet.")
        print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
consultar_cep()