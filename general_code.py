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

	def get_cartoons(self, cartoon_date):
		self.cursor.execute("SELECT * FROM schedule WHERE c_date=%s",
							[cartoon_date])

		cartoon, cartoons = {}, {}

		for column in self.cursor:
			cartoon['c_id'] = column[0]
			cartoon['c_time'] = column[2]
			cartoon['c_name'] = column[3]
			cartoon['c_age'] = column[4]
			cartoon['c_place'] = column[5]
			cartoon['c_url'] = column[6]

			cartoons[cartoon['c_id']] = cartoon
			cartoon = {}
		print (cartoons)
		return cartoons