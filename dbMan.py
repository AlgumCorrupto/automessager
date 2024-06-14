import sqlite3
import io
from rich.prompt import Prompt
from rich import print
from rich.table import Table
from rich.console import Console

def createMessage():
    db = sqlite3.connect('msgs.db')
    msg = ""
    while(not(msg.__len__() > 2 and msg.__len__() <= 280)):
        msg = input("Digite uma mensagem contendo entre 3 e 280 caracteres\n$ ")
    db.execute("INSERT INTO tweet (msg) VALUES(?)", [msg])
    db.commit()
    db.close()
    print("[green][bold]Mensagem registrada![/bold] Agora espere o bot enviar a mensagem.[/green]")

def listMessage():
    db = sqlite3.connect('msgs.db')
    res = db.execute("SELECT * FROM tweet")
    table = Table(title="Tweets", leading=1)
    table.add_column("Id", justify="right", no_wrap=True)
    table.add_column("Mensagem", justify="left")
    for val in res.fetchall():
        msg = ""
        i = 0
        for char in val[1]:
            if(i == 50):
                msg+= '\n'
                i = 0
            msg += char
            i+=1
        #msg += '\n'

        table.add_row(str(val[0]), msg)
    db.close()
    console = Console()
    console.print(table)

def deleteMessage():
    val = input("Escolha uma das mensagens para ser apagada, pelo seu ID (o id das mensagens em 'Listar Tweets')")
    certain = Prompt.ask("Você tem certeza?", choices=['s', 'n'])
    if certain == 'n':
        return
    try: 
        db = sqlite3.connect('msgs.db')
        res = db.execute('DELETE FROM tweet where id = ?', [int(val)])
        db.commit()
        db.close()
        print('[green]Tweet apagado![/green]')
    except:
        print('[red]Não foi possível apagar o Tweet, tente novamente![/red]')

def updateMessage():
    val = input("Escolha uma das mensagens para ser atualizada! Pelo seu ID (o id das mensagens em 'Listar Tweets')\n$ ")
    certain = Prompt.ask("Você tem certeza?", choices=['s', 'n'])
    if certain == 'n':
        return
    db = sqlite3.connect("msgs.db")
    res = db.execute('SELECT msg FROM tweet WHERE id = ?', [int(val)])
    msg = ''
    try:
        msg = res.fetchone()
    except:
        print('[red]esse tweet não existe no banco de dados![/red]')
        return
    console = Console()
    #  stream=io.StringIO(msg[0]
    newMsg = Prompt.get_input(console=console, prompt="Edite a mensagem (copie a mensagem antiga se puder, para usar ela como base)\n$ ", password=False)
    res = db.execute('UPDATE tweet SET msg = ? WHERE id = ?', [newMsg, int(val)])
    db.commit()
    db.close()

while (True):
    todo = Prompt.ask("""
                O que deseja fazer?
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
        case "2":
            listMessage()
        case "3":
            updateMessage()
        case "4":
            deleteMessage()