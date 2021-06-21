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

MYSQL_CONFIGURATION = {
	"host" : "localhost",
	"user" : "admin",
	"password" : "keredsnevets13579",
	"database" : "jaya_abadi"
}

class MysqlController():

	sql = None
	conn = None

	def __init__(self, load_data=False):
		self.conn = pymysql.connect(host=MYSQL_CONFIGURATION["host"],
									user=MYSQL_CONFIGURATION["user"],
									password=MYSQL_CONFIGURATION["password"],
									database=MYSQL_CONFIGURATION["database"],
									autocommit=True,
									cursorclass=pymysql.cursors.DictCursor)

	def connection(self):
		return self.conn

	def set_sql(self, sql):
		self.sql = sql
		return self

	def execute(self):
		
		conn = self.conn

		"""Execute SQL Command"""
		with conn.cursor() as cursor:
			try :
				cursor.execute(self.sql)
				conn.commit()
				print("Success")
				return cursor.fetchall()
			except Exception as e:
				print(e)