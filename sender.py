import datetime
import tweepy
import sqlite3
import rich
import time
import os

def sendMsg():
    db = sqlite3.connect('msgs.db')
    res = db.execute("SELECT msg FROM tweet")
    msgs = res.fetchone()
    r = open('isSend', 'r')
    content = r.read()
    r.close()
    if(content == '1'):
        print("Mensagem já enviada hoje!")
        return
    
    try:
        msg = msgs[0]
        w = open('isSend', 'w')
        w.flush()
        w.write('1')
        w.close()
    except:
        print("Mensagens Vazias, FEED ME MORE!!!!")
        return  
    
    try: 
        client.create_tweet(text=msg)
        rich.print("[cyan]Tweet enviado:[/cyan] " + msg)
    except:
        rich.print("[red]Tweet não enviado, provavelmente houve uma mensagem duplicada![/red]")
    db.close()
    print(msgs[0])
    return msg

rich.print("Você pode sair à qualquer momento pressionando [yellow bold]Ctrl + C[/yellow bold]")
try:   
    COOMER_KEY      = os.environ["COOMER_KEY"]
    COOMER_SECRET   = os.environ["COOMER_SECRET"]
    BEARER_TOKEN    = os.environ["BEARER_TOKEN"] 
    ACCESS_KEY      = os.environ["ACCESS_KEY"]
    ACCESS_SECRET   = os.environ["ACCESS_SECRET"]

    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=COOMER_KEY,
        consumer_secret=COOMER_SECRET,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET
    )

    already = False
    while(True):
        now = datetime.datetime.now().weekday()
        if now == 2:
            if not already:
                msg = sendMsg()
                db = sqlite3.connect('msgs.db')
                db.execute('DELETE FROM tweet WHERE msg = ?;', [msg])
                db.commit()
                db.close()
            already = True
        # Se hoje for qualquer outro dia
        else:
            try:
                w = open('isSend', 'w')
                w.flush()
                w.write('0')
                w.close()
            except:
                print("Houve uma tentativa falha de escrever no cache!")
            already = False
        #dormir por uma hora
        time.sleep(1200)
except KeyboardInterrupt:
    os.system('python3 hello.py')