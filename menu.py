import os
import getpass
import pyfiglet
import socket
import subprocess as sp
os.system("clear")

# Contributors
os.system("tput setaf 3")
print("""
\n\tHacktober 2021 - Project Contributors
\t1. Yagyandatta Murmu (Author)
\t2. Deepak Patra
\t3. Laxman Naik
\t4. Sweta Sardar
""")
input("\nEnter To Continue...")
os.system("clear")

# Design
os.system("tput setaf 4")
title = pyfiglet.figlet_format("Hacktober", font = "epic" )
print(title)
os.system("tput setaf 2")
msg = pyfiglet.figlet_format("Welcome You", font = "digital" )
print(msg)



# Auth
passwd = getpass.getpass(" Enter Your Password : ")

if passwd != "hacktober":
	print("Your password is invalid. Please try again")
	exit()


where = input("Where you want to run this menu ? (local/remote) : ")
print(where)


def print_msg_box(msg, indent=1, width=None, title=None):
    os.system("tput setaf 2")
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

while True:
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\t Menu Bar")
	os.system("tput setaf 7")
	print("\t\t-----------------------")
	msg = "press 0 : Linux Command menu\n" \
	      "Press 1 : Hadoop menu\n" \
	      "Press 2 : Docker menu\n" \
	      "Press 3 : Web Server menu\n" \
	      "Press 4 : AWS menu\n" \
	      "Press 5 : Exit\n" 
	print_msg_box(msg=msg, indent=2, title='All Services') 

	if where == "local":
		os.system("tput setaf 1")
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check your IP \n" \
				     "Press 4 : Check RAM Status \n" \
				     "Press 5 : Check Storage details \n" \
				     "press 6 : To Clear Cache\n" \
			       	 "press 7 : To Transfer File to Other Linux System\n" \
				     "press 8 : Query any command details\n" \
				     "press 9 : Go to Last Menu\n" \
				     "press 10 : To Exit" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				os.system("tput setaf 3")
				print(ch)
				if int(ch) == 0:
					exit()
				elif int(ch) == 1:
					os.system("date")


				elif int(ch) == 2:
					os.system("cal")

				elif int(ch) == 3:
					os.system("ifconfig")

				elif int(ch) == 4:
					os.system("free -m")
				elif int(ch) == 5:
					os.system("df -h")
				elif int(ch) == 6:
					os.system("echo 3 > /proc/sys/vm/drop_caches")
				elif int(ch) == 7:
					ip = input("Enter IP of target system : ")
					user = input("Enter username : ")
					src = input("Enter your source file path : ")
					dest = input("Enter destination folder path where you want to copy : ")
					output = getpass.getstatusoutput("scp {} {}@{}:{}".format(src, user,ip,dest))
				elif int(ch) == 8:
					cmd_name = input("Enter Command Name: ")
					os.system(f"man {cmd_name}")
				elif int(ch) == 9:
					break
				elif int(ch) == 10:
					exit()

				else:
					print("Incorrect Input")
				input("\nEnter To Continue...")
# Hadoop...

		elif int(ch) == 1:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg ="Press 1 : Install Jdk and Hadoop\n" \
				     "Press 2 : Configure  NameNode\n" \
				     "Press 3 : Start NameNode Service\n" \
				     "Press 4 : Configure  DataNode\n" \
				     "Press 5 : Start DataNode Service\n" \
				     "Press 6 : Configure Client\n" \
				     "Press 7 : Cluster Report\n" \
				     "press 8 : Check SafeMode(nameNode)\n" \
				     "press 9 : Disable Safemode in Namenode \n" \
				     "press 10 : Upload a File into Cluster\n" \
				     "press 11 : Go Back\n" \
				     "press 0 : Exit.."
				print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
	#Hadoop-installation


				if int(ch) == 1:
					os.system("rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")


	#namenode

				elif int(ch) == 2:
					os.system("rm -rf /nn")
					os.system("mkdir /nn")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
					
					<!-- Put site-specific property overrides in this file. -->
						
					<configuration>
					<property>
					<name>dfs.name.dir</name>
					<value>/nn</value>
					</property>
					</configuration>""")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://0.0.0.0:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system('hadoop namenode -format ')
				elif int(ch) == 3:
					os.system('hadoop-daemon.sh start namenode')

	#dataNode

				elif int(ch) == 4:
					os.system("rm -rf /dn")
					os.system("mkdir /dn")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>dfs.data.dir</name>
					<value>/dn</value>
					</property>
					</configuration>""")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://192.168.43.102:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
				elif int(ch) == 5:
					os.system("hadoop-daemon.sh start datanode")


	#clint

				elif int(ch) == 6:
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://192.168.43.102:9001</value>
					</property>
					</configuration> """)
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close

	#other basic commands

				elif int(ch) == 7:
					os.system("hadoop dfsadmin -report | less")

				elif int(ch) == 8:
					os.system("hadoop dfsadmin -safemode get")
				elif int(ch) == 9:
					os.system("hadoop dfsadmin -safemode leave")
				elif int(ch) == 10:
					name = input('Enter File Name :')
					os.system(f"hadoop fs -put {name}/")
				elif int(ch) == 11:
					break
				elif int(ch) == 0:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")

#docker

		elif int(ch) == 2:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Verify Docker is Installed or Not\n" \
				      "Press 1 : Install Docker\n" \
				      "Press 2 : Start Docker\n" \
				      "Press 3 : List All Docker Images\n" \
				      "Press 4 : Pull Docker Image\n" \
				      "Press 5 : Launch a Container with Name\n" \
				      "Press 6 : List Running Docker Containers\n" \
				      "press 7 : Start a Container\n" \
				      "press 8 : Get Terminal of runing container\n" \
				      "press 9 : Stop a Container \n" \
				      "Press 10 : Delete a Container\n" \
				      "Press 11: Delete an Image\n" \
				      "Press 12: Delete all Container\n" \
				      "Press 13: Go Back\n" \
				      "Press 14: Exit.." 
				print_msg_box(msg=msg, indent=2, title='Docker Command:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)

				if int(ch) == 0:
					os.system("rpm -q docker-ce")

	#docker installation

				elif int(ch) == 1:
					os.system('yum install docker-ce')
				elif int(ch) == 2:
					os.system('systemctl start docker')
				elif int(ch) == 3:
					os.system('docker images -a')
				elif int(ch) == 4:
					OS = input("Enter docker image name :")
					os.system(f'docker pull -i {OS}')
				elif int(ch) == 5:  
					NAME = input("Enter imagename and version (OSname:00.00):")
					myName = input("Give a new OS name :")
					os.system(f'docker run -it --name {myName} {NAME}')
				elif int(ch) == 6:
					os.system('docker ps')
				elif int(ch) == 7:
					NAME = input("Enter The OS name :")
					os.system(f'docker start {NAME}')
				elif int(ch) == 8:
					NAME = input("Enter The OS name :")
					os.system(f'docker attach {NAME}')
				elif int(ch) == 9:
					NAME = input("Enter The OS name :")
					os.system(f'docker stop {NAME}')
				elif int(ch) == 10:
					NAME = input("Enter The OS name :")
					os.system('docker rm -f {NAME}')
				elif int(ch) == 11:
					NAME = input("Enter The image name :")
					os.system('docker rmi -f {NAME}')
				elif int(ch) == 12:
					os.system('docker rm `docker ps -a -q` ')
				elif int(ch) == 13:
					break
				elif int(ch) == 14:
					exit()

				else:
					print("Incorrect Number")
				input("\nEnter To Continue...")

# webserver

		elif int(ch) == 3:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check Apache Web Server is Installed or Not\n" \
				      "Press 1 : Start Httpd Service\n" \
				      "Press 2 : Disable Firewall and Set Enforcing\n" \
				      "Press 3 : Restart Httpd Service\n" \
				      "Press 4 : Configure Total Webserver\n" \
				      "Press 5 : Go Back\n" \
				      "press 6 : Exit.. "
				print_msg_box(msg=msg, indent=2, title='webserver Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q httpd")

				elif int(ch) == 1:
					os.system('yum install httpd;systemctl start httpd')
				elif int(ch) == 2:
					os.system('systemctl stop firewalld;setenforce 0')
				elif int(ch) == 3:
					os.system('systemctl restart httpd')
				elif int(ch) == 4:
					Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
					IP=Soc.getsockname()[0]
					T=input("\tEnter your message to preview on web :")
					
					os.system('yum install httpd')
					os.system('cd /var/www/html/')
					os.system('touch web.html')
					os.system(f'echo "{T}" > /var/www/html/web.html')
					os.system('systemctl start httpd')
					os.system('systemctl stop firewalld')
					os.system('setenforce 0')
					os.system(f'firefox http://"{IP}"/web.html')
				elif int(ch) == 5:
					break
				elif int(ch) == 6:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")

# AWS

		elif int(ch) == 4:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check if AWS-Cli is Installed or Not\n" \
				      "Press 1 : Create your Security Group \n" \
				      "Press 2 : Create your Key-Pair \n" \
				      "Press 3 : Launch an Instance \n" \
				      "Press 4 : Describe your Instance \n" \
				      "Press 5 : Start your Instance \n" \
				      "Press 6 : Stop your Instance \n" \
				      "Press 7 : Terminate your Instance \n" \
				      "Press 8 : Create an EBS Storage \n" \
				      "Press 9 : Attach EBS with ec2 Instance \n" \
				      "Press 10 : Create a S3 Bucket \n" \
				      "Press 11 : Create CloudFront \n" \
				      "Press 12 : Go Back\n" \
				      "press 13 : Exit.. \n"
				print_msg_box(msg=msg, indent=2, title='AWS Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q aws")
				elif int(ch) == 1:
					name = input("Enter Group Name : ")
					des  = input("Enter description : ")
					os.system(f"aws ec2 create-security-group --group-name {name} --description '{des}' ")
				elif int(ch) == 2:
					name = input("Enter Key Name : ")
					os.system(f'aws ec2 create-key-pair --key-name {name} --query KeyMaterial > awskey.pem --output text > {name}.pem')
				elif int(ch) == 3:
					while True:
						os.system("clear")
						os.system("tput setaf 2")
						msg ="Press 0 : Want to write your  own \n" \
						     "Press 1 : Amazon Linux 2 AMI (HVM), SSD Volume Type \n" \
						     "Press 2 : Red Hat Enterprise Linux 8 (HVM), SSD Volume Type \n" \
						     "Press 3 : SUSE Linux Enterprise Server 15 SP2 (HVM), SSD Volume Type \n" \
						     "Press 4 : Ubuntu Server 20.04 LTS (HVM), SSD Volume Type \n" \
						     "Press 5 : Microsoft Windows Server 2019 Base \n" \
						     "press 6 : Microsoft Windows Server 2019 Base with Containers \n" 
						     
						print_msg_box(msg=msg, indent=2, title='Choose Your AMI:') 
						os.system("tput setaf 4")
						ch=input("choose your option : ")
						os.system("tput setaf 4")
						print(ch)
						if int(ch) == 0:
							ami = input("Enter your AMI : ")
						elif int(ch) == 1:
							ami = "ami-0e306788ff2473ccb"
						elif int(ch) == 2:
							ami = "ami-0a9d27a9f4f5c0efc"
						elif int(ch) == 3:
							ami = "ami-0d0522ed4db1debd6"
						elif int(ch) == 4:
							ami = "ami-0a4a70bd98c6d6441"
						elif int(ch) == 5:
							ami = "ami-0994975f92b8520bc"
						elif int(ch) == 6:
							ami = "ami-0cc51168ed03dd131"
						else:
							print("Invalid choice")
						

						os.system("clear")
						os.system("tput setaf 2")
						msg ="Press 0 : Write your own \n" \
						     "Press 1 : ap-south-1a \n" \
						     "Press 2 : ap-south-1b \n" \
						     "Press 3 : ap-south-1c \n" 
						     
						print_msg_box(msg=msg, indent=2, title='Choose Your zone:') 
						os.system("tput setaf 4")
						ch=input("Choose your Option : ")
						os.system("tput setaf 4")
						print(ch)
						if int(ch) == 0:
							subnet = input("Enter your zone : ")
						elif int(ch) == 1:
							subnet = "subnet-b86168d0"
						elif int(ch) == 2:
							subnet = "subnet-63e39c2f"
						elif int(ch) == 3:
							subnet = "subnet-9458d9ef"
						else:
							print("Invalid choice")
						break

					sg = input("Enter Your security group id : ")
					key = input("Enter Your key-name : ")



					#print(f"entered ami- {ami} and zone - {subnet} and {sg} and {key}")

					

					os.system(f"aws ec2 run-instances --image-id  {ami} --instance-type t2.micro --count 1 --subnet-id {subnet} --security-group-ids {sg} --key-name {key}")


				elif int(ch) == 4:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 describe-instances --instance-ids {id}")
				elif int(ch) == 5:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 start-instances --instance-ids {id}")
				elif int(ch) == 6:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 stop-instances --instance-ids {id}")
				elif int(ch) == 7:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 terminate-instances --instance-ids {id}")
				elif int(ch) == 8:
					size = input("Enter your Volume Size (in GB): ")
					os.system(f"aws ec2 create-volume --availability-zone ap-south-1a --size {size}")
				elif int(ch) == 9:
					id = input("Enter your Volume Id : ")
					ids = input("Enter your instance id : ")
					os.system(f"aws ec2 attach-volume  --volume-id {id} --instance-id {ids}  --device /dev/sdf")
				elif int(ch) == 10:
					name = input("Enter the Bucket Name: ")
					os.system(f"aws s3api create-bucket --bucket  {name} --create-bucket-configuration LocationConstraint=ap-south-1")
				elif int(ch) == 11:
					name = input("Enter the Domain Name: ")
					name = input("Enter the file name with extension (unknown.jpg): ")
					os.system(f"aws cloudfront create-distribution --origin-domain-name {name}.s3.amazonaws.com --default-root-object {fname}")

				elif int(ch) == 12:
					break
				elif int(ch) == 13:
					exit()

				else:
					print("Incorrect Number")
					input("\n Enter To Continue...")

		elif int(ch) == 5:
			exit()



	elif where == "remote":
		ip = input("Enter remote IP: ")
		print(ip)
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check IP\n" \
				     "Press 4 : Check Httpd Status\n" \
				     "Press 5 : Start Httpd \n" \
				     "press 6 : To Clear Cache\n" \
			       	 "press 7 : To Change any Command Name\n" \
				     "press 8 : Go Back \n" \
				     "press 9 : To Exit\n" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 1:
					os.system("ssh {} date".format(ip))
				elif int(ch) == 2:
					os.system("ssh {} cal".format(ip))
				elif int(ch) == 3:
					os.system("ssh {} ifconfig".format(ip))
				elif int(ch) == 4:
					os.system("ssh {} systemctl status httpd".format(ip))
				elif int(ch) == 5:
					os.system("ssh {} systemctl start httpd".format(ip))
				elif int(ch) == 6:
					os.system("ssh {} echo 3 > /proc/sys/vm/drop_caches".format(ip))
				elif int(ch) == 7:
					print("change name")
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()
				else:
					print("Incorrect Number")
				input("\nEnter To Continue...")

						#hadoop

		elif int(ch) == 1:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg="press 0 : To Exit\n"\
					"Press 1 : Install Jdk and Hadoop\n"\
				    "Press 2 : Configure  DataNode\n" \
				    "Press 3 : Configure  NameNode\n" \
				    "Press 4 : Configure Client\n" \
				    "Press 5 : Check the Connected Datanodes\n" \
				    "press 6 : Check SafeMode in NameNode\n" \
				    "press 7 : Disable Safemode in Namenode\n " \
				    "press 8 : Go Back..\n" \
				    "press 9 : Exit \n"
				print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
						#Hadoop-installation


				if int(ch) == 1:
					os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
					os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip))

						#namenode

				elif int(ch) == 2:
					os.system("ssh {} rm -rf /nn".format(ip))
					os.system("ssh {} mkdir /nn".format(ip))
					os.system("ssh {} ".format(ip))
					f=open("/etc/hadoop/hdfs-site.xml","w")
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
					
					<!-- Put site-specific property overrides in this file. -->
						
					<configuration>
					<property>
					<name>dfs.name.dir</name>
					<value>/nn</value>
					</property>
					</configuration>""")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://0.0.0.0:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system("ssh {} hadoop namenode -format".format(ip))
					os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))

						#dataNode

				elif int(ch) == 3:
					os.system("ssh {} rm -rf /nn".format(ip))
					os.system("ssh {} mkdir /nn".format(ip))
					os.system("ssh {} ".format(ip))
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>dfs.data.dir</name>
					<value>/dn</value>
					</property>
					</configuration>""")
					f=open("/etc/hadoop/hdfs-site.xml","w")
					f.write(x)
					f.close
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://192.168.43.102:9001</value>
					</property>
					</configuration> 
					""")
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close
					os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))


						#clint

				elif int(ch) == 4:
					os.system("ssh {} ".format(ip))
					x=("""<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
					<!-- Put site-specific property overrides in this file. -->
				
					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://192.168.43.102:9001</value>
					</property>
					</configuration> """)
					f=open("/etc/hadoop/core-site.xml","w")
					f.write(x)
					f.close

						#other basic commands

				elif int(ch) == 5:
					os.system("ssh {} hadoop dfsadmin -report | less".format(ip))
				elif int(ch) == 6:
					os.system("ssh {} hadoop dfsadmin -safemode get".format(ip))
				elif int(ch) == 7:
					os.system("ssh {} hadoop dfsadmin -safemode leave".format(ip))
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()
				else:
					print("Incorrect Number")
				input("\ncontinue...")

						#docker


		elif int(ch) == 2:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg = "press 0 : To Verify Docker is Installed or Not\n" \
				      "Press 1 : Install Docker-ce and Start the Service\n" \
				      "Press 2 : Check All Docker Images\n" \
				      "Press 3 : Pull a Docker Image and Run\n" \
				      "Press 4 : Check Running Docker Containers\n" \
				      "Press 5 : Check the Connected Datanodes\n" \
				      "press 6 : check safeMode in nameNode\n" \
				      "press 7 : disable safemode in namenode\n" \
				      "press 8 : Go back \n" \
				      "press 9 : exit..." 
				print_msg_box(msg=msg, indent=2, title='Docker Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
						#Docker-installation


				if int(ch) == 0:
					os.system("ssh {} rpm -q docker-ce".format(ip))

				#docker installation

				elif int(ch) == 1:
					os.system("ssh {} yum install docker-ce".format(ip))
					os.system("ssh {} systemctl start docker".format(ip))
				elif int(ch) == 2:
					os.system("ssh {} docker images -a".format(ip))
				elif int(ch) == 3:
					os.system("ssh {} docker ps -a".format(ip))
				elif int(ch) == 4:
					os.system("ssh {} ".format(ip))
					OS = input("Enter docker image name :")
					os.system(f'docker load -i {OS}'.format(ip))
					NAME = input("Enter imagename and version :")
					os.system(f'docker run -it {NAME}'.format(ip))
				elif int(ch) == 5:
					os.system("ssh {} docker ps".format(ip))

				else:
					os.system("tput setaf 1")
					print("Incorrect Number")
				input("\ncontinue...")
		elif int(ch) == 3:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check Apache Web Server is Installed or Not\n" \
				      "Press 1 : Start Httpd Service\n" \
				      "Press 2 : Disable Firewall and Set Enforcing\n" \
				      "Press 3 : Restart Httpd Service\n" \
				      "Press 4 : Configure Total Webserver\n" \
				      "Press 5 : Go Back\n" \
				      "press 6 : Exit.. "
				print_msg_box(msg=msg, indent=2, title='AWS Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q httpd")

				elif int(ch) == 1:
					os.system('yum install httpd;systemctl start httpd'.format(ip))
				elif int(ch) == 2:
					os.system('systemctl stop firewalld;setenforce 0'.format(ip))
				elif int(ch) == 3:
					os.system('systemctl restart httpd'.format(ip))
				elif int(ch) == 4:
					Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
					IP=Soc.getsockname()[0]
					T=input("\tEnter your message to preview on web :")
					
					os.system('yum install httpd'.format(ip))
					os.system('cd /var/www/html/'.format(ip))
					os.system('touch web.html'.format(ip))
					os.system(f'echo "{T}" > /var/www/html/web.html'.format(ip))
					os.system('systemctl start httpd'.format(ip))
					os.system('systemctl stop firewalld'.format(ip))
					os.system('setenforce 0'.format(ip))
					os.system(f'firefox http://"{IP}"/web.html'.format(ip))
				elif int(ch) == 5:
					break
				elif int(ch) == 6:
					exit()

				else:
					print("Incorrect Number")
				input("\ncontinue...")

		elif int(ch) == 4:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg = "press 0 : Check if AWS-Cli is Installed or Not\n" \
				      "Press 1 : Create your Security Group \n" \
				      "Press 2 : Create your Key-Pair \n" \
				      "Press 3 : Launch an Instance \n" \
				      "Press 4 : Describe your Instance \n" \
				      "Press 5 : Start your Instance \n" \
				      "Press 6 : Stop your Instance \n" \
				      "Press 7 : Terminate your Instance \n" \
				      "Press 8 : Create an EBS Storage \n" \
				      "Press 9 : Attach EBS with ec2 Instance \n" \
				      "Press 10 : Create a S3 Bucket \n" \
				      "Press 11 : Create CloudFront \n" \
				      "Press 12 : Go Back\n" \
				      "press 13 : Exit.. \n"
				print_msg_box(msg=msg, indent=2, title='AWS Commands:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 0:
					os.system("rpm -q aws".format(ip))
				elif int(ch) == 1:
					name = input("Enter Group Name : ")
					des  = input("Enter description : ")
					os.system(f"aws ec2 create-security-group --group-name {name} --description '{des}' ".format(ip))
				elif int(ch) == 2:
					name = input("Enter Key Name : ")
					os.system(f'aws ec2 create-key-pair --key-name {name} --query KeyMaterial > awskey.pem --output text > {name}.pem'.format(ip))
				elif int(ch) == 3:
					while True:
						os.system("clear")
						os.system("tput setaf 2")
						msg ="Press 0 : Want to write your  own \n" \
						     "Press 1 : Amazon Linux 2 AMI (HVM), SSD Volume Type \n" \
						     "Press 2 : Red Hat Enterprise Linux 8 (HVM), SSD Volume Type \n" \
						     "Press 3 : SUSE Linux Enterprise Server 15 SP2 (HVM), SSD Volume Type \n" \
						     "Press 4 : Ubuntu Server 20.04 LTS (HVM), SSD Volume Type \n" \
						     "Press 5 : Microsoft Windows Server 2019 Base \n" \
						     "press 6 : Microsoft Windows Server 2019 Base with Containers \n" 
						     
						print_msg_box(msg=msg, indent=2, title='Choose Your AMI:') 
						os.system("tput setaf 4")
						ch=input("choose your option : ")
						os.system("tput setaf 4")
						print(ch)
						if int(ch) == 0:
							ami = input("Enter your AMI : ")
						elif int(ch) == 1:
							ami = "ami-0e306788ff2473ccb"
						elif int(ch) == 2:
							ami = "ami-0a9d27a9f4f5c0efc"
						elif int(ch) == 3:
							ami = "ami-0d0522ed4db1debd6"
						elif int(ch) == 4:
							ami = "ami-0a4a70bd98c6d6441"
						elif int(ch) == 5:
							ami = "ami-0994975f92b8520bc"
						elif int(ch) == 6:
							ami = "ami-0cc51168ed03dd131"
						else:
							print("Invalid choice")
						

						os.system("clear")
						os.system("tput setaf 2")
						msg ="Press 0 : Write your own \n" \
						     "Press 1 : ap-south-1a \n" \
						     "Press 2 : ap-south-1b \n" \
						     "Press 3 : ap-south-1c \n" 
						     
						print_msg_box(msg=msg, indent=2, title='Choose Your zone:') 
						os.system("tput setaf 4")
						ch=input("Choose your Option : ")
						os.system("tput setaf 4")
						print(ch)
						if int(ch) == 0:
							subnet = input("Enter your zone : ")
						elif int(ch) == 1:
							subnet = "subnet-b86168d0"
						elif int(ch) == 2:
							subnet = "subnet-63e39c2f"
						elif int(ch) == 3:
							subnet = "subnet-9458d9ef"
						else:
							print("Invalid choice")
						break

					sg = input("Enter Your security group id : ")
					key = input("Enter Your key-name : ")



					#print(f"entered ami- {ami} and zone - {subnet} and {sg} and {key}")

					

					os.system(f"aws ec2 run-instances --image-id  {ami} --instance-type t2.micro --count 1 --subnet-id {subnet} --security-group-ids {sg} --key-name {key}")


				elif int(ch) == 4:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 describe-instances --instance-ids {id}".format(ip))
				elif int(ch) == 5:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 start-instances --instance-ids {id}".format(ip))
				elif int(ch) == 6:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 stop-instances --instance-ids {id}".format(ip))
				elif int(ch) == 7:
					id = input("Enter your Instance Id : ")
					os.system(f"aws ec2 terminate-instances --instance-ids {id}".format(ip))
				elif int(ch) == 8:
					size = input("Enter your Volume Size (in GB): ")
					os.system(f"aws ec2 create-volume --availability-zone ap-south-1a --size {size}".format(ip))
				elif int(ch) == 9:
					id = input("Enter your Volume Id : ")
					ids = input("Enter your instance id : ")
					os.system(f"aws ec2 attach-volume  --volume-id {id} --instance-id {ids}  --device /dev/sdf".format(ip))
				elif int(ch) == 10:
					name = input("Enter the Bucket Name: ")
					os.system(f"aws s3api create-bucket --bucket  {name} --create-bucket-configuration LocationConstraint=ap-south-1".format(ip))
				elif int(ch) == 11:
					name = input("Enter the Domain Name: ")
					name = input("Enter the file name with extension (unknown.jpg): ")
					os.system(f"aws cloudfront create-distribution --origin-domain-name {name}.s3.amazonaws.com --default-root-object {fname}".format(ip))

				elif int(ch) == 12:
					break
				elif int(ch) == 13:
					exit()

				else:
					print("Incorrect Number")
					input("\n Enter To Continue...")

		elif int(ch) == 5:
			exit()



	else:
		os.system("tput setaf 1")
		print("Login is not supported....")
		exit()

	input("\nPlease Enter to Continue....")





















