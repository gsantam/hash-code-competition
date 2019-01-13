class InputParser():

	def __init__(self, path):
		self.path = path

	def parse(self):
		with open(self.path, 'r') as file:
			num_videos, num_endpoints, num_requests, self.num_caches, self.cache_capacity = [int(x) for x in file.readline().split(' ')]
			
			self.videos = { idx_video : int(video_size.replace('\n','')) for idx_video, video_size in enumerate(file.readline().split(' ')) }

			self.endpoints = {}
			for idx_endpoint in range(num_endpoints):
				datacenter_latency, num_caches = [int(x) for x in file.readline().split(' ')]
				cache_dict = {}
				for j in range(num_caches):
					idx_cache, cache_latency = [int(x) for x in file.readline().split(' ')]
					cache_dict[idx_cache] = cache_latency
				self.endpoints[idx_endpoint] = {
					'datacenter_latency' : datacenter_latency,
					'caches' : cache_dict
				}

			self.requests = []
			for idx_request in range(num_requests):
				idx_video, idx_endpoint, request_size = [int(x) for x in file.readline().split(' ')]
				self.requests.append({
					'idx_video' : idx_video,
					'idx_endpoint': idx_endpoint,
					'size' : request_size
				})

