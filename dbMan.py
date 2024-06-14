import sqlite3
from rich.prompt import Prompt
from rich import print

def createMessage():
    db = sqlite3.connect('msgs.db')
    msg = ""
    while(not(msg.__len__() > 2 and msg.__len__() <= 280)):
        msg = input("Digite uma mensagem contendo entre 3 e 280 caracteres\n$ ")
    db.execute("INSERT INTO tweet (msg) VALUES(?)", [msg])
    db.commit()
    db.close()
    print("[green][bold]Mensagem registrada![/bold] Agora espere o bot enviar a mensagem.[/green]")


while (True):
    todo = Prompt.ask("""
                O que desejas fazer?
                      [magenta]1.[/magenta] [bold]Novo Tweet[/bold]
                      [magenta]2.[/magenta] [bold]Listar Tweets[/bold]
                      [magenta]3.[/magenta] [bold]Atualizar Tweet[/bold]
                      [magenta]4.[/magenta] [bold]Apagar Tweet[/bold]
                      [red]0. Sair[/red]
                      """, 
                      choices=["1", "2", "3", "4", "0"], show_choices=False)

    match todo:
        case "0":
            exit()
        case "1":
            createMessage()