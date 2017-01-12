import pyodbc, getpass, argparse

def getParameters():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--driver', dest='driver')
    parser.add_argument('-s', '--server', dest='server')
    parser.add_argument('-p', '--port', dest='port')
    parser.add_argument('-b', '--database', dest='database')
    parser.add_argument('-u', '--user', dest='user')

    args = vars(parser.parse_args())

    argsList = ['driver', 'server', 'port', 'database', 'user']

    n=0

    print('Enter missing connection data:')
    for x in argsList:
        if args[x]:
            continue
        else:
            args[x] = raw_input(x + ':\t')
            n=n+1

    if (n == 0):
        print('All connection data entered.')

    print('Review connection data:')
    for y in argsList:
        print('\t{0}:\t{1}'.format(y, args[y]))

    return args


def connect(dic):
    cnxnStr = "DRIVER=" + dic['driver'] + ";SERVER=" + dic['server'] + ";PORT=" + dic['port'] + ";DATABASE=" + dic['database'] + ";UID=" + dic['user'] + ";PWD=" + getpass.getpass()
    cnxn = pyodbc.connect(cnxnStr)
    cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    cnxn.setencoding(str, encoding='utf-8')
    cnxn.setencoding(unicode, encoding='utf-8', ctype=pyodbc.SQL_CHAR)
    return cnxn

def linecount(cnxn):
    dic = {}
    cursor = cnxn.cursor()
    cursor.tables()
    rows = cursor.fetchall()
    for r in rows:
        #TODO Currently hardcoded for MS SQL
        if (r[1] != u'dbo'):
            continue
        cursor.execute("SELECT count(*) FROM {0}.{1}.{2}".format(r[0], r[1], r[2]))
        x = cursor.fetchone()
        print(r[0] + "," + r[1] + "," + r[2] + "," + str(x[0]))

def promptForParameter(prompt):
    return raw_input(prompt)
