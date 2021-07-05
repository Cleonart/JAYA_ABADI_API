import pymysql.cursors
import json

#MYSQL_CONFIGURATION = {
#	"host" : "localhost",
#	"user" : "admin",
#	"password" : "keredsnevets13579",
#	"database" : "jaya_abadi"
#}

MYSQL_CONFIGURATION = {
	"host" : "localhost",
	"user" : "sammy",
	"password" : "password",
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
				return cursor.fetchall()
			except Exception as e:
				return {"code" : "DATABASE_ERROR", "msg" : str(e.args)}

class SQLBuilder(MysqlController):
		"""
			When set, id must be at the
		"""

		key = None
		sql = ""

		def __init__(self):
			super().__init__()
			self.sql = ""

		def reset(self):
			self.key = None
			self.sql = ""
			return self

		def insert(self, table_name):
			self.sql = f"INSERT INTO `{table_name}` "
			return self	

		def delete(self, table_name):
			self.sql = f"DELETE FROM `{table_name}`"
			return self

		def select(self, _field, _from):
			if isinstance(_field, list):
				_field = ",".join(_field)
			self.sql = f"SELECT {_field} FROM `{_from}` "
			return self

		def inner_join(self, table):
			self.sql += f"INNER JOIN `{table}` "
			return self

		def where(self, condition):
			self.sql += "WHERE {} ".format(condition)
			return self

		def alias(self, alias_value):
			self.sql += f"AS `{alias_value}` "
			return self 

		def on(self, condition):
			self.sql += f"ON {condition} "
			return self

		def set(self, field):
			self.sql += "SET "
			fields = []
			for key in list(field.keys()):
				fields.append(f"`{key}` = '{field[key]}'")
			self.sql += ",".join(fields) + " "
			return self

		def on_duplicate_key(self, key):
			self.sql += "ON DUPLICATE KEY "
			self.key = key
			return self

		def update(self, field=None, table=False):
			self.sql += "UPDATE "
			if table:
				self.sql += "`{}`".format(table)
				return self
			
			fields = []
			if self.key != None:
				for key in list(field.keys()):
					if key != self.key:
						fields.append(f"`{key}` = '{field[key]}'")
				self.sql += ",".join(fields)
			return self

		def build(self):
			app = self
			super().set_sql(app.sql)
			return self.sql

		def execute(self):
			app = self
			super().set_sql(app.sql)
			return super().execute()
