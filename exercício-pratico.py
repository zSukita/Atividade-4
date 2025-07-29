import re
from datetime import datetime

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e diferenças de maiúscula/minúscula.
    
    Parâmetros:
    texto (str): A palavra ou frase a ser verificada
    
    Retorna:
    str: "Sim" se for palíndromo, "Não" se não for
    """
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    
    # Verifica se é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias baseada no ano de nascimento.
    
    Parâmetros:
    ano_nascimento (int): O ano de nascimento da pessoa
    
    Retorna:
    int: A idade em dias
    """
    # Data atual
    data_atual = datetime.now()
    
    # Data de nascimento (assumindo 1º de janeiro do ano)
    data_nascimento = datetime(ano_nascimento, 1, 1)
    
    # Calcula a diferença em dias
    diferenca = data_atual - data_nascimento
    
    return diferenca.days

# Exemplos de uso:
if __name__ == "__main__":
    # Teste da função de gorjeta
    print("=== Teste Gorjeta ===")
    conta = 100.0
    porcentagem = 15
    gorjeta = calcular_gorjeta(conta, porcentagem)
    print(f"Conta: R$ {conta}")
    print(f"Gorjeta ({porcentagem}%): R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {conta + gorjeta:.2f}")
    
    print("\n=== Teste Palíndromo ===")
    # Exemplos de palíndromos
    exemplos = ["arara", "A base do teto desaba", "Socorram me subi no onibus em Marrocos", "python"]
    for exemplo in exemplos:
        resultado = verificar_palindromo(exemplo)
        print(f"'{exemplo}' é palíndromo? {resultado}")
    
    print("\n=== Teste Idade em Dias ===")
    # Exemplo de cálculo de idade
    ano = 1990
    dias = calcular_idade_em_dias(ano)
    print(f"Pessoa nascida em {ano} tem aproximadamente {dias} dias de vida")
    print(f"Isso equivale a aproximadamente {dias // 365} anos")