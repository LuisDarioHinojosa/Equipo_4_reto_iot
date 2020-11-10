import mysql.connector


def createConnection(user, password, database):
    try:
        cnx = mysql.connector.connect(
            user=user, password=password, host="127.0.0.1", database=database)
        cursor = cnx.cursor()
        return cursor, cnx
    except mysql.connector.Error as err:

        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        # Si la base de datos no existe
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def stopConnection(cursor, cnx):
    if f'{cnx}' in locals() or f'{cnx}' in globals():
        cursor.close()


def createPerson(name, birthDay, complexion, userP,  user, password):
    cursor, cnx = createConnection(user, password, "iot_reto")
    query = (
        f"INSERT INTO persons (name, birth_date,complexion, password) values(\"{name}\",\"{birthDay}\",{complexion},\"{userP}\");")
    cursor.execute(query)
    cnx.commit()
    stopConnection(cursor, cnx)


def createHeartbeatRegister(heartBeat, date, hour, status, idPerson, user, password):
    cursor, cnx = createConnection(user, password, "iot_reto")
    query = (
        f"INSERT INTO heart_meditions (heartbeat_rate, rate_date,hour, status,id_person) values({heartBeat},\"{date}\",\"{hour}\",\"{status}\",{idPerson});")
    cursor.execute(query)
    cnx.commit()
    stopConnection(cursor, cnx)


def createOxygenRegister(oxygen, date, hour, status, idPerson, user, password):
    cursor, cnx = createConnection(user, password, "iot_reto")
    query = (
        f"INSERT into oxygen_meditions (oxygen_blood,rate_date,hour,id_person,status) values ({oxygen},\"{date}\",\"{hour}\",{idPerson},\"{status}\");")
    cursor.execute(query)
    cnx.commit()
    stopConnection(cursor, cnx)


# createHeartbeatRegister(150.0, "20-10-15", "08:00:00","ya colgo los tenis", 1, "root", "(phoskyGUP28)")

# createPerson("emilia", "2020-10-15", 1, "antunez", "root", "(phoskyGUP28)")
#createOxygenRegister(12, "20-10-15", "12:01:12","anemia", 1, "root", "(phoskyGUP28)")

"""
createPerson("luis", "2020-10-15", 1, "1111", "root", "(phoskyGUP28)")
createPerson("edgar", "2020-10-15", 1, "1111", "root", "(phoskyGUP28)")
createPerson("emilio", "2020-10-15", 1, "1111", "root", "(phoskyGUP28)")
createPerson("octavio", "2020-10-15", 1, "1111", "root", "(phoskyGUP28)")
createPerson("hoalberto", "2020-10-15", 1, "1111", "root", "(phoskyGUP28)")
"""

cursor, cnx = createConnection("root", "(phoskyGUP28)", "iot_reto")
query = (f"SELECT * FROM heart_meditions")
cursor.execute(query)
for result in cursor:
    print(result)
cnx.commit()


stopConnection(cursor, cnx)
