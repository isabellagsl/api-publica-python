# Consumo de API Pública com Python

## Pesquisa da API

1. Nome da API: JSONPlaceholder
2. Documentação: https://jsonplaceholder.typicode.com
3. O que oferece: Dados fictícios de usuários para testes
4. Autenticação: Não
5. Requisitos:Python 3.x, Biblioteca requests: pip install requests
6. Endpoint escolhido: /users/1
7. URL completa: https://jsonplaceholder.typicode.com/users/1
8. Código de status de sucesso: 200
9. Campos retornados:
   - name: Nome do usuário
   - email: Email do usuário
   - phone: Telefone
   - website: Site pessoal

## Exemplo de resposta JSON:
```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "Sincere@april.biz",
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org"
}

