import db_scan, argparse

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



c = db_scan.connect(args)
db_scan.linecount(c)
