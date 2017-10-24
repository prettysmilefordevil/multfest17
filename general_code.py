import c_utils as ut
import psycopg2

class ConnectionExits:
	def __new__(cls, database_url):
		try:
			credentials = ut.database_url_parse(database_url)
			connection = psycopg2.connect(database=credentials['database'], user=credentials['user'],
										  password=credentials['password'], host=credentials['host'],
										  port=credentials['post'])
			connection.cursor()
			return connection, connection.cursor()
		except psycopg2.OperationalError:
			return False


class Timetable:
	def __new__(cls, database_url):
		connection_exists = ConnectionExits(database_url)
		if connection_exists:
			return super(Timetable, cls).__new__(cls)
		else:
			return False

	def __init__(self, database_url):
		connection_exists = ConnectionExits(database_url)
		self.connection, self.cursor = connection_exists