class OutputParser():

	def __init__(self, parsed_input,path_output):
		self.path_output = path_output
		self.parsed_input = parsed_input
		print(self.parsed_input)
		self.score = 0
		self.denominator = 0

	def parse(self):
		with open(self.path_output, 'r') as file:
			cache_servers_of_videos = dict()
			for i,line in enumerate(file.readlines()):
				if i==0:
					described_cache_servers = int(line)
				else:
					splitted_line = line.split(" ")
					cache_server_id = int(splitted_line[0])

					video_ids = set()
					total_video_size = 0

					for video_id in splitted_line[1:]:
						video_id = int(video_id)
						video_ids.add(video_id)
						assert video_id in list(self.parsed_input.videos.keys())
						total_video_size+=self.parsed_input.videos[video_id]
						if video_id not in cache_servers_of_videos:
							cache_servers_of_videos[video_id] = set()
						cache_servers_of_videos[video_id].add(cache_server_id)
					assert total_video_size <= self.parsed_input.cache_capacity

			for request in self.parsed_input.requests:
				idx_video  = request["idx_video"]
				idx_endpoint = request["idx_endpoint"]
				size = request["size"]
				sorted_caches = sorted(self.parsed_input.endpoints[idx_endpoint]["caches"].items(), key=lambda kv: kv[1])
				if idx_video in cache_servers_of_videos:
					cache_servers_of_video = cache_servers_of_videos[idx_video]
					for cache in sorted_caches:
						if cache[0] in cache_servers_of_video:
							self.score+= size*(self.parsed_input.endpoints[idx_endpoint]["datacenter_latency"] - cache[1])
							break

				self.denominator+=size
			import math
			print(math.floor(self.score*1000/self.denominator))







