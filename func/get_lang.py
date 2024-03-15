import sqlite3
import socket


def get_lang():

    pc_name = socket.gethostname().strip().replace(' ', '_')

    connection = sqlite3.connect('lang.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS lang 
                  (pc_names varchar(50) PRIMARY KEY, now_lang varchar(50) DEFAULT 'en')''')
    connection.commit()

    cursor.execute('''SELECT pc_names FROM lang''')
    names = cursor.fetchall()

    if (pc_name,) not in names:

        cursor.execute('''INSERT INTO lang (pc_names) VALUES ("%s")''' % pc_name)
        connection.commit()

        cursor.close()
        connection.close()

        return 'en'

    else:

        cursor.execute('''SELECT now_lang FROM lang WHERE pc_names="%s"''' % pc_name)

        lang = cursor.fetchone()

        cursor.close()
        connection.close()

        return lang[0]
