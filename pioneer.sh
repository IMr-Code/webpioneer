#!/usr/bin/bash

#Tool: Webpioneer
#versao: 1.0

function website_osint(){

	banner
	echo -e "\e[32m -----> WEBSITE OSINT\e[0m\n"
	echo -e "O site usa protocolo http ou https??\n"
	echo "[1]- HTTP"
	echo "[2]- HTTPS"
	echo -e "\n"
	read -p ">>>>> " protocol

	if [ "$protocol" = "1" ]; then
		protocol="http"

		#Area de inicio do webosint

		clear

		banner
		echo -e "\e[32m----> WEBSITE OSIN\e[0m\n"

		echo "Exemplos: google.com, facebook.com, governo.gov.ao"
		echo ""

		read -p "Digite o dominio do alvo: " domain

		if (( ${#domain} > 4 )); then

			echo "Alvo valido, iniciando o ataque!"

			nmap -sV "$domain" -o nmap-scan.txt


		else
			echo -e "\e[31m[+] Alvo invalido, recomece [+]\e[0m"

		fi

	elif [ "$protocol" = "2" ]; then
		protocol="https"

	else
		echo -e "\e[31m[+] Escolha invalida! recomece...\e[0m"

	fi

}

function banner(){
	clear

	echo "Webpioneer" | figlet
	echo "====================="
}

function main(){

	banner
 
	echo "[1]- Website osint"
	echo "[2]- Whois Infomation"
	echo "[3]- Descoberta de directorios"
	echo "[4]- Scanner de Portas"
	echo "[5]- Ataques de Engenharia social"
	echo "[6]- Sair"
	echo -e "\n"
	read -p ">>> " option

	if [ "$option" = 1 ]; then

		website_osint

	else
		echo "[+] Escolha invalida [+]"

	fi

}

whiptail --title "WEBPIONEER" --msgbox "Bem vindo ao Webpioneer! uma ferramenta de hacking" 10 28

main
