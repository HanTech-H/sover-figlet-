#!bin/usr/evn python3
import subprocess as sp 
os =  input("Hi what is your os linux or android >>>")
if (os == "Linux" or os == "linux"):
	text = input("write you text >>>")
	sp.run(" sudo apt install figlet -y", shell=True)
	sp.run("figlet " + text, shell=True)
if (os == "Android" or os == "android"):
	text = input("write you text >>>")
	sp.run("pkg install figlet -y", shell=True)
	sp.run("clear", shell=True)
	sp.run("figlet " + text, shell=True)