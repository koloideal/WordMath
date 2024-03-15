import sqlite3
import socket


def change_lang() -> None:

    pc_name = socket.gethostname().strip().replace(' ', '_')

    connection = sqlite3.connect('lang.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT now_lang FROM lang WHERE pc_names = "%s"''' % pc_name)
    language = cursor.fetchone()

    if language[0] == 'en':

        cursor.execute('''UPDATE lang SET now_lang = "ru" WHERE pc_names = "%s"''' % pc_name)
        connection.commit()

        cursor.close()
        connection.close()

    elif language[0] == 'ru':

        cursor.execute('''UPDATE lang SET now_lang = "en" WHERE pc_names = "%s"''' % pc_name)
        connection.commit()

        cursor.close()
        connection.close()

    else:

        return
