# 💻️🔌️ BORN2BEROOT  
### por Pablo Marcos Sánchez 

## 📑 Índice
1. Descripción del proyecto  
2. Configuración máquina virtual  
3. Sudo 
4. Configuración SSH  
5. Configuración UFW  
6. Contraseñas y políticas de seguridad  
7. Script monitoring.sh
8. Crontab

---

## 📘 Descripción del proyecto

 Born2beroot es un proyecto de 42madrid en el que debemos configurar y hacer seguro un servidor Linux dentro de un máquina virtual. A lo largo del proyecto he aprendido:
 
 - Gestión de usuarios y grupos
 - Configuración de sudo
 - Protocolo de red SSH
 - Frewall UFW
 - LVM
 - Políticas de contraseñas
 - Creación de un script de monitorización automática con crontab
 
 Este proyecto nos sirve de ayuda para introducirnos en la administración de sistemas y endurecimiento de servidores de manera básica.
 
---
 
## 🎛️ Configuración de la máquina virtual
 
 La configuración lleva su tiempo y cada paso es importante, a continuación los muestro:
 
 1. Instalar la ISO de Debian. (La elegido frente a Rocky porque consume menos recursos y hay más documentación y tutoriales.)
 2. Tener instalado VirtualBox. Y crear una nueva máquina.
 3. Configurar el nombre y ubicación de la máquina.
 4. Asignar memoria RAM. En mi caso 1024MB.
 5. Crear el disco duro virtual en formato VDI y reservado dinámicamente.
 6. Establer 12GB de tamaño de disco.
 7. Entrar en la configuración, una vez creada, y adjuntamos la ISO previamente instalada.
 8. Iniciar la máquina.
 9. Ahora debes seleccionar el lenguaje, localización, y el tipo de teclado.
 10. Configurar la red, estableciendo un nombre de host y un dominio. (Esta última opción no es necesaria).
 11. Establecer una contraseña para el usuario 'root'. Y creamos nuestro usuario con su nombre y contraseña.
 12. Configurar zona horaria.
 13. Elegir el disco en el que queremos crear la partición.
 14. ELegir una contraseña para el cifrado LVM.
 15. Seleccionar la cantidad de grupo de volúmenes que se utilizará durante el particionado. En mi caso la memoria total.
 16. Configurar el gestor de paquetes.
 17. Por último, intalar el cargador de arranque GRUB. (que nos permite arrancar uno de los múltiples S.O).
 
 Con estos pasos completados la instalación ya estaría finalizada.
 
---
 
## 🦸️Sudo

 Este comando nos permite ejecutar comandos con privilegios de superusuario (root) de forma temporal.
 Para que nuestro usuario pueda utilizar esta maravillosa comando hay que hacer una pequeña instalación:
 
 1. Cambiar al usuario root mediante el comando 'su'.
 2. Introducir la contraseña correspondiente asignada durante la configuración de la máquina.
 3. Instalar el paquete sudo con el siguiente comando: 'apt install sudo'.
 4. Reiniciar el sistema: 'sudo reboot'.
 5. Comprobar si la instalación ha ido bien sudo -V.
 
 Y ya tendríamos instalado sudo y listo para utilizar.
 Lo único que faltaría es modificar el archivo sudoers para decidir que privilegios tendrá el superusuario. Así queda el mío:
 
- touch /etc/sudoers.d/sudo_config  --> Crea un archivo que almacenerá nuestra política de sudo.
- mkdir /var/log/sudo  --> Crea un directorio.
- nano /etc/sudoers.d/sudo_config  --> Editamos el archivo.
- Una vez que estemos editando el archivo debemos configurarlo con los siguientes comandos:

	passwd_tries=3 : Total de intentos para ingresar la contraseña de sudo.
	badpass_message="mensaje" : el mensaje que se mostrará cuando la contraseña falle.
	logfile="/var/log/sudo/sudo_config" : Ruta donde se almacenarán los registros de sudo.
	log_input, log_output : Qué se registrará.
	iolog_dir="/var/log/sudo" : Qué se registrará.
	requiretty : TTY se vuelve obligatorio
	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin" : Carpetas que se excluirán de sudo
 
---

## 📦️Instalación y configuración SSH

 SSH es un protocolo de red que permite conectarse de forma segura a una máquina remota desde otra, gestionándola a través de una terminal.
 Para instalarlo debemos seguir los siguientes pasos:
 
 1. Actualizar el sistema con el siguiente comando: 'sudo apt update'.
 2. Instalar el servidor OpenSSH -> 'sudo apt install openssh-server'.
 3. Verificar instalación mediante: 'sudo service ssh status'.
 
 Con esto ya estaría instalado el servicio, ahora debemos configurarlo:
 
 1. Para ello debemos entrar el archivo de configuraciones: 'su'  'nano /etc/ssh/sshd_config'
 2. Y modificar el archivo. Cambiar de 22 a 4242. y PermitRootLogin no.
 3. Y modificar el puerto a 4242 en el archivo /etc/ssh/ssh_config' también.
 4. Reiniciar el servicio SSH. 'sudo service ssh restart'.
 5. Comprobar el estado: 'sudo service ssh status'.

 Por último para realizar la conexión debemos hacer:
 
 1. Apagar la máquina y entrar en la configuración de esta.
 2. En el apartado de red clicar en reenvío de puertos.
 3. Agregar una nueva regla y en esta indicamos que los puertos invitado y anfitrión sean 4242.
 4. Para conectarnos vía SSH desde nuestra máquina física utilizamos el comando:  'ssh pmarcos-@localhost -p 4242'.

 Y ya tendríamos todo listo.
 
---

## 🔥️ Instalación y configuración UFW 

 UFW es una interfaz simplificada para el cortafuegos iptables de Linux, diseñada para que sea fácil de usar y configurar.
 A continuación enseño los pasos para instalarlo y configurarlo:
 
 1. Instalar el paquete UFW: 'sudo apt install ufw'.
 2. Habilitar el firewall: 'sudo ufw enable'.
 3. Permitir que nuestro firewall acepte las conexiones que se realizarán en el puerto 4242: 'sudo ufw allow 4242'.
 4. Comprobar que todo ha salido bien: 'sudo ufw status'.

 Y con estas cuatro cositas tendríamos todo listo.
 
---

## 🔑️ Políticas de contraseñas

 Este punto consiste en modificar el archivo 'login.defs' para endurecer las contraseñas de los usuarios y hacerlas más seguras.
 Así ha quedado mi archivo:
- nano /etc/login.defs  --> Editarlas definiciones de inicio de sesión.
- Modificar parámetros de contraseña: Localice y cambie los siguientes parámetros:
	Cambiar: PASS_MAX_DAYS 99999→PASS_MAX_DAYS 30
	Cambiar: PASS_MIN_DAYS 0→PASS_MIN_DAYS 2
- sudo apt install libpam-pwquality  -->  Instala la biblioteca de calidad de contraseñas.
- nano /etc/pam.d/common-password  --> Edita la configuración de PAM.
- Debajo de retry=3 debemos agregar los siguientes comandos.

	minlen=10 ➤ El mínimo de caracteres que debe contener una contraseña.
	ucredit=-1 ➤ La contraseña debe contener al menos una letra mayúscula. Debemos escribirla con un signo -, ya que así se sabe que se refiere al mínimo de 				caracteres; si se añade un signo +, se referirá al máximo de caracteres.
	dcredit=-1 ➤ La contraseña debe contener al menos un dígito.
	lcredit=-1 ➤ La contraseña debe contener al menos una letra minúscula.
	maxrepeat=3 ➤ La contraseña no puede tener el mismo carácter repetido tres veces consecutivas.
	reject_username ➤ La contraseña no puede contener el nombre de usuario dentro de sí misma.
	difok=7 ➤ La contraseña debe contener al menos siete caracteres diferentes de la última contraseña utilizada.
	enforce_for_root ➤ Implementaremos esta política de contraseña para root.

---

## 📜️ Script monitoring.sh

 Un script es una secuencia de comandos almacenados en un archivo que, al ejecutarse, realizará la función de cada comando.
 Y este en concreto al ejecutarse nos mostrará por pantalla las especificaciones de la máquina y si todo está en orden.
 Ha sido me ha quedado:
 
	#!/bin/bash

	# ARCH
	arch=$(uname -a)

	# CPU PHYSICAL
	cpuf=$(grep "physical id" /proc/cpuinfo | wc -l)

	# CPU VIRTUAL
	cpuv=$(grep "processor" /proc/cpuinfo | wc -l)

	# RAM
	ram_total=$(free --mega | awk '$1 == "Mem:" {print $2}')
	ram_use=$(free --mega | awk '$1 == "Mem:" {print $3}')
	ram_percent=$(free --mega | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')

	# DISK
	disk_total=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_t += $2} END {printf ("%.1fGb\n"), disk_t/1024}')
	disk_use=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} END {print disk_u}')
	disk_percent=$(df -m | grep "/dev/" | grep -v "/boot" | awk '{disk_u += $3} {disk_t+= $2} END {printf("%d"), disk_u/disk_t*100}')

	# CPU LOAD
	cpul=$(vmstat 1 2 | tail -1 | awk '{printf $15}')
	cpu_op=$(expr 100 - $cpul)
	cpu_fin=$(printf "%.1f" $cpu_op)

	# LAST BOOT
	lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')

	# LVM USE
	lvmu=$(if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi)

	# TCP CONNEXIONS
	tcpc=$(ss -ta | grep ESTAB | wc -l)

	# USER LOG
	ulog=$(users | wc -w)

	# NETWORK
	ip=$(hostname -I)
	mac=$(ip link | grep "link/ether" | awk '{print $2}')

	# SUDO
	cmnd=$(journalctl _COMM=sudo | grep COMMAND | wc -l)

	wall  << EOF	
		Architecture: $arch
		CPU physical: $cpuf
		vCPU: $cpuv
		Memory Usage: $ram_use/${ram_total}MB ($ram_percent%)
		Disk Usage: $disk_use/${disk_total} ($disk_percent%)
		CPU load: $cpu_fin%
		Last boot: $lb
		LVM use: $lvmu
		Connections TCP: $tcpc ESTABLISHED
		User log: $ulog
		Network: IP $ip ($mac)
		Sudo: $cmnd cmd"
		EOF

---

## ⏰️ Crontab
 
 Crontab es un gestor de procesos en segundo plano. Los procesos especificados se ejecutarán a la hora que especifique en el archivo crontab.
 
 1. Para configurar correctamente crontab, debemos editar el archivo crontab con el siguiente comando: 'sudo crontab -u root -e'.
 2. Y al final del archivo añadiremos: '*/10 * * * * sh /path_to_file.sh'.
 
 Este cambio nos va a permitir que el archivo se muestre de manera automatizada cada 10 minutos.

---
