# Pedindo para o usuário inserir um nome
name = input("Digite seu nome: ")

# Verifica se é string e se tem mais de 2 caracteres
def validate_name(name):
    if not type(name) == str:
        print (False)
    elif len(name) <= 2:
        print(False)
    else:
        print(True)
validate_name(name)

top_level_domains = []

# Verificando se o email é válido
with open("dominios_validos.txt", "r") as f:
    conteudo = f.read().strip()
    # Remove aspas e divide pelos pontos e vírgulas
    top_level_domains = [dominio.strip().replace('"', '') for dominio in conteudo.split(";") if dominio.strip()]

email = input("Digite seu email: ")

def validate_email(email):
    # Verificando se tem o @ no email inserido pelo usuário 
    if "@" not in email: 
        return False

    # Percorrendo os domínios válidos
    for domains in top_level_domains:
        if domains in email: # Verifica se o domínio aparece na string do email
            return True
    return False # Caso não tenha encontrado nenhum domínio

print(validate_email(email))