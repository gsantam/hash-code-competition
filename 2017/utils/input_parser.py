class InputParser():

	def __init__(self, path):
		self.path = path

	def parse(self):

		with open(self.path, 'r') as file:
			num_videos, num_endpoints, num_requests, num_caches, cache_sizes = file.readline().split(' ')
			print("Num Videos: {}".format(num_videos))
			print("Num Endpoints: {}".format(num_endpoints))
			print("Num Requests: {}".format(num_requests))
			print("Num Caches: {}".format(num_caches))
			print("Cache Sizes: {}".format(cache_sizes))

