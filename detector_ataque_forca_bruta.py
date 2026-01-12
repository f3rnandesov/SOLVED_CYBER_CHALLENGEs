

# Logs de entrada
# Lista de Tentativas de Log
logs = [
    "192.168.0.10,admin,FAIL",
    "192.168.0.10,admin,FAIL",
    "192.168.0.10,admin,FAIL",
    "192.168.0.10,admin,FAIL",
    "192.168.0.10,admin,FAIL",
    "192.168.0.20,user,SUCCESS",
    "10.0.0.5,root,FAIL",
    "10.0.0.5,root,FAIL",
    "10.0.0.5,root,FAIL",
]
# Dicionário Vazio
falhas_por_ip = {}


# Ler cada linha do log
for linha in logs:
    # Desempacotar cada log
    ip, usuario, status = linha.split(",")
    
    # Verificar tentativa falha
    if status == "FAIL":
        # Se o ip estiver no dicionario de falhas adicione mais UM
        if ip in falhas_por_ip:
            falhas_por_ip[ip] += 1
        # Se não, adicione UM
        else:
            falhas_por_ip[ip] = 1
            

#Se o total de tentativas de um determinado IP for maiorIgual a 5, imprima SUSPEITO de brute force
for ip, total in falhas_por_ip.items():
    if total >= 5:
        print(f"IP SUSPEITO: {ip} ({total} falhas)")

