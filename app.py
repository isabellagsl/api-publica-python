import requests
import json

def main():
    try:
        url = "https://jsonplaceholder.typicode.com/users/1"
        response = requests.get(url)  # Faz requisição GET para a API
        
        if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
            data = response.json()  # Converte resposta para JSON
            
            print("\n=== INFORMAÇÕES DO USUÁRIO ===")
            print(f"Nome: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Telefone: {data['phone']}")
            print(f"Website: {data['website']}")
            
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)  # Salva dados em arquivo JSON
            
            print("\nDados salvos em data.json!")
            
        else:
            print(f"Erro na requisição: Codigo {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Erro de conexao: Verifique sua internet")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()