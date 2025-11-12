import requests 
import json     

def buscar_usuario_aleatorio():
    """
    Acessa a Random User API, busca um usuário e exibe seus dados.
    Também trata erros de conexão.
    """
    
    url_api = "https://randomuser.me/api/"
    
    print("🌍 Tentando buscar um usuário fictício aleatório...")
    
    try:
        # 1. Fazendo a requisição
        resposta = requests.get(url_api, timeout=10)
        
        # 2. Verificando o status da resposta HTTP
        if resposta.status_code == 200:
            
            # 3. Pegando os dados JSON e extraindo as informações
            dados = resposta.json()
            
            
            usuario = dados['results'][0]
            
            
            nome_completo = (
                f"{usuario['name']['title']}. "
                f"{usuario['name']['first']} "
                f"{usuario['name']['last']}"
            )
            
            
            email = usuario['email']
            pais = usuario['location']['country']
            
            # 4. Exibindo as informações de forma didática
            print("\n✅ Conexão bem-sucedida! Usuário encontrado:")
            print("---")
            print(f"👤 **Nome Completo:** {nome_completo}")
            print(f"📧 **E-mail:** {email}")
            print(f"🌎 **País:** {pais}")
            print("---")
            
        else:
            print(f"\n❌ Falha na comunicação com a API (HTTP {resposta.status_code}).")
            print("Pode ser um erro temporário do servidor deles.")

    # 5. Tratando Erros de Conexão (o nosso "plano B"!)
    except requests.exceptions.RequestException as e:
        
        print("\n🚨 **ERRO NA CONEXÃO!**")
        print("Não foi possível acessar a internet ou a API.")
        print(f"Detalhe do erro: {e}")
        print("Verifique sua conexão e tente novamente.")

# --- Execução do Programa ---
buscar_usuario_aleatorio()