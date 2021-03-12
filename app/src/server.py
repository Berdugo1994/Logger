import flask
from flask import request
import mysql.connector
from datetime import datetime


class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        """
        Manages the connection to MySql DB.

        Uses mysql_native_password plugin.

        Parameters
        -----------
        password_file: basestring
            Path to the password file.

        """
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user,
            password=pf.read(),
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def show_all(self):
        """
        Debugging function, see all the logs saved in the system.
        :return: list of all the actions at the system.
        """
        self.cursor.execute('SELECT * FROM log')
        rec = []
        for c in self.cursor:
            rec.append(c)
        return rec

    def write_to_db(self, ip, method, data, time):
        """

        :param ip: str
            ip of user reaching the app.
        :param method: str
            Rest method: {POST/GET/DELETE/PUT}
        :param data: str
            The content of the request
        :param time: str
            The time of reaching the app. GMT +00:00
        """
        query = "INSERT INTO log (ip, method, data, time) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(query, (ip, method, data, time))
        self.connection.commit()

    def clear_db(self):
        """
        Debugging function, clears all the data in the system.
        :return: list of all the actions at the system.
        """
        self.cursor.execute('DROP TABLE IF EXISTS log')
        self.cursor.execute('CREATE TABLE log (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), method VARCHAR(255),'
                            'data VARCHAR(255), time VARCHAR(255))')


server = flask.Flask(__name__)
conn = None


# Routes And Logics.


@server.route('/showall', methods=['GET', 'POST', 'DELETE', 'PUT'])
def show_all():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    rec = conn.show_all()
    result = []
    for c in rec:
        result.append(c)
    return flask.jsonify({"response": result})


@server.route('/cleardb', methods=['GET'])
def clear_db():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    conn.clear_db()
    return flask.jsonify({"result": "log table cleard."})


@server.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def insertion_db():
    now = datetime.now()
    ip = str(request.remote_addr)
    method = str(request.method)
    data = str(request.data.decode('UTF-8'))
    time = str(now.strftime("%H:%M:%S"))
    print('your log details recorded.')
    print('IP', ip, '\nMETHOD', method, '\nDATA', data, '\nTIME', time)
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    conn.write_to_db(ip, method, data, time)
    return flask.jsonify(ip=ip, method=method, data=data, time=time)


if __name__ == '__main__':
    """
    Runs the app on localhost , Port :5000.
    """
    server.run(debug=True, host='0.0.0.0', port=5000)
