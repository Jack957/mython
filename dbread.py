import MySQLdb

db= MySQLdb.connect(host="localhost", user="root", passwd="banana",db="wordpress")

cursor = db.cursor()
stmt = "SELECT * from wp_options"
cursor.execute(stmt)

rows = cursor.fetchall ()
for row in rows:
    print "Row: "
    for col in row :
        print "Column: %s" % (col)
    print "End of Row"
print "Number of rows returned: %d" % cursor.rowcount

cursor.close()

db.close()

