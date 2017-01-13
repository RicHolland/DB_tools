import db_scan

c = db_scan.connect(db_scan.getParameters())
db_scan.linecount(c)
