import datetime
import tweepy
import sqlite3
import rich
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
# como o bot funciona: a cada vez que o bot detectar que é dia de mandar mensagem, ele manda uma das mensagens que está na database
# e depois deleta ela!

    try: 
        client.create_tweet(text=msg)
        rich.print("[cyan]Tweet enviado:[/cyan] " + msg)
    except:
        rich.print("[red]Tweet não enviado, provavelmente houve uma mensagem duplicada![/red]")
    db.close()
    print(msgs[0])
    return msg

COOMER_KEY      = "seu consumer key"
COOMER_SECRET   = "seu consumer secret"
BEARER_TOKEN    =  "seu bearer token"
ACCESS_KEY      = "seu access key"
ACCESS_SECRET   = "seu access secret"

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
    # é essa a parte que verifica, basicamente um loop infinito q verifica se hoje é o dia
    # ele é um pouco burro, pois se ele for restartado no dia que é para ele mandar a mensagem, ele vai mandar ela, sem levar em consideração
    # se ele já havia mandado uma mensagem nesse dia.
    # isso é bem trivial, só fazer o caching se ele enviou ou não.
    # agora vou mostrar ele em ação, tem 2 mensagens dentro da databse.
    # Se hoje for quarta
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


