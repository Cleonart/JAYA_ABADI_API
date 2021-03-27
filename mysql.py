import pymysql.cursors
		
def conn():
	"""Make connection to mysql"""
	conn = pymysql.connect(host='localhost',
                    user='admin',
                    password='keredsnevets13579',
                    database='jaya_abadi',
                    autocommit=True,
                    cursorclass=pymysql.cursors.DictCursor)
	return conn

def connExecute(sql):
	"""Execute SQL Command"""
	with conn().cursor() as cursor:
		try :
			cursor.execute(sql)
			conn().commit()
			print("Success")
			return cursor.fetchall()
		except Exception as e:
			print(e)