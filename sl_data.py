import psycopg2
HOST = 'HOST'
USER = 'USER'
Database = 'DATABASE'
PASSWD = 'PASSWD'
#Connection variables

db = psycopg2.connect(host= HOST, database=Database, user = USER, password = PASSWD)

cursor = db.cursor()

#Creating table if not present when bot starts
def setup_db():
    cursor.execute('''
    create table if not exists main(
     channel_id varchar(30),
     author_id varchar(30),
     message varchar(30)
     )
    ''')

#Update user search history
def update_history(message,query):
    channel=str(message.channel)
    author=str(message.author)
    cursor.execute('''INSERT INTO main VALUES(%s,%s,%s)''',(channel,author,str(query)))
    db.commit()

#Fetch recent terms searched by user
def show_history(message,search_term):
    channel=str(message.channel)
    author=str(message.author)
    cursor.execute(''' Select message from main where channel_id = %s and author_id = %s and message like %s''',(channel,author,'%'+search_term+'%'))
    result= cursor.fetchall()
    return result
