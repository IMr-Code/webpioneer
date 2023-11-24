#!/usr/bin/env python3

import os
import socket
import subprocess
import requests  # Adicionando a importação que estava ausente

os.system("rm ip_addresses.txt")

def banner():
    os.system('clear')
    os.system("echo 'WEBPIONNER 1.0' | figlet")
    print("================================")

def osint_tool():
    banner()
    print("\x1b[32m -----> OSINT TOOL\x1b[0m\n")

    domain = input("Digite o domínio do alvo: ")

    banner()
    print("\x1b[32m----> OSINT TOOL\x1b[0m\n")

    if len(domain) > 3:
        print("Alvo válido, iniciando a coleta de informações!\n")

        # Informações WHOIS
        print("\x1b[32m----> INFORMAÇÕES WHOIS\x1b[0m\n")
        whois_info = subprocess.check_output(["whois", domain], text=True)
        print(whois_info)

        # Scanner de Portas usando nmap
        print("\x1b[32m----> SCANNER DE PORTAS\x1b[0m\n")
        scan_ports_nmap(domain)
    else:
        print("\x1b[31m[+] Alvo inválido, recomece [+]\x1b[0m")

def scan_ports_nmap(domain):
    try:
        result = subprocess.check_output(["nmap", "-Pn", "-p", "1-1000", domain], text=True)
        result = result.replace("Nmap", "Webpioneer")
        result = result.replace("nmap.org", "webpioneer.org")
        print(result)

        # Armazenar IP em um arquivo
        with open("ip_addresses.txt", "a") as file:
            file.write(f"{domain}: {get_ip_address(domain)}\n")
    except subprocess.CalledProcessError:
        print("\x1b[31m[+] Erro ao executar o scanner de portas [+]\x1b[0m")

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Não foi possível obter o endereço IP"

def bruteforce_directories():
    base_url = input('Digite a URL: ')
    wordlist = "wordlist.txt"
    print("[+]========> ESSE PROCESSO PODE DEMORAR <========[+]")
    with open(wordlist, 'r') as file:
        directories = file.read().splitlines()

    for directory in directories:
        url = f"{base_url}/{directory}"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Directorio encontrado: {url}")
	else:
	    print("[+]- EXECUTANDO ATAQUE -[+]")
def main():
    banner()

    print("[1]- OSINT Tool")
    print("[2]- Bruteforce de Directorios")
    print("[3]- Hack camera")
    print("[4]- Sair")
    print("\n")
    option = input(">>> ")

    if option == "1":
        osint_tool()
    elif option == "2":
        bruteforce_directories()
    else:
        print("[+] Escolha inválida [+]")

if __name__ == "__main__":
    print("Bem-vindo ao SimplePioneer! Uma ferramenta simples de hacking")
    main()

