#!/user/bin/python
import time

class clocking(object):
	"""It's for counting the period of time."""
	def __init__(self, arg):
		super(clocking, self).__init__()
		self.arg = arg

	def print_clock(self):
		print time.clock()