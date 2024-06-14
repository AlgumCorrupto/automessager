from rich import print
from rich.prompt import Prompt
import os

print("""
    ███████     ███ 
  ███░░░░░███  ░░░  
 ███     ░░███ ████ 
░███      ░███░░███ 
░███      ░███ ░███ 
░░███     ███  ░███ 
 ░░░███████░   █████
   ░░░░░░░    ░░░░░ 

 """)
print('    Desenvolvido por Paulo Artur (https://github.com/AlgumCorrupto).\n')
print("Você pode configurar a database digitando [yellow bold]0[/yellow bold]")
print("Você pode rodar a aplicação digitando [yellow bold]1[/yellow bold]\n\n")

while True:
    val = Prompt.ask(prompt="Qual programa quer rodar?", choices=["0", "1"])
    if val == '0':
        os.system('python3 dbMan.py')
    else:
        os.system('python3 sender.py')
