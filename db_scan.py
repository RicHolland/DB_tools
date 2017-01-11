import pyodbc, getpass

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
        if (r[1] != u'dbo'):
            continue
        cursor.execute("SELECT count(*) FROM {0}.{1}.{2}".format(r[0], r[1], r[2]))
        x = cursor.fetchone()
        #print(type(x))
        #print(type(x[0]))
        #print(type(r))
        #print(type(r[0]))
        print(r[0] + "," + r[1] + "," + r[2] + "," + str(x[0]))
        #break

def promptForParameter(prompt):
    return raw_input(prompt)

#c = connect("FreeTDS", "haldexcommerce.cloudapp.net", "57500", "HaldexCommerce", "gabor")
#linecount(c)
