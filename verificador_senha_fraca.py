# Verificador de senha fraca

##Regras da senha
##A senha será considerada aceitável se:

senha = input("Insira a senha: ")

##Contiver ao menos 1 caractere especial (!@#$%&*)
def tem_caractere_especial(texto):
    especial = "!@#$%&*"
    return any(c in especial for c in texto)

##Tiver pelo menos 8 caracteres
def pelo_menos8(texto):
    return len(texto) >= 8

##Contiver ao menos 1 número
def pelo_menos_um_numero(texto):
    return any(s.isdigit() for s in texto)

##Contiver ao menos 1 letra maiúscula
def pelo_menos_maiuscula(texto):
    return any(s.isupper() for s in texto)


oito_senha = pelo_menos8(senha)
numero_senha = pelo_menos_um_numero(senha)
maiuscula_senha = pelo_menos_maiuscula(senha)
caractere_especial_senha = tem_caractere_especial(senha)

if oito_senha and numero_senha and maiuscula_senha and caractere_especial_senha:
    print("Válido")
else:
    print("Inválido")
    
    