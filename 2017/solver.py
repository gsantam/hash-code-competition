import random
import math

class Solver():

	def __init__(self, input_problem):
		self.input_problem = input_problem

	def _cost(self, solution):
		score = denominator = 0
		cache_servers_of_videos = dict()
		for cache_server_id, videos in solution.items():

			video_ids = set()
			total_video_size = 0

			for video_id in videos:
				video_id = int(video_id)
				video_ids.add(video_id)
				assert video_id in list(self.input_problem.videos.keys())
				total_video_size+=self.input_problem.videos[video_id]
				if video_id not in cache_servers_of_videos:
					cache_servers_of_videos[video_id] = set()
				cache_servers_of_videos[video_id].add(cache_server_id)
			print("{} <= {}".format(total_video_size, self.input_problem.cache_capacity))
			assert total_video_size <= self.input_problem.cache_capacity

		for request in self.input_problem.requests:
			idx_video  = request["idx_video"]
			idx_endpoint = request["idx_endpoint"]
			size = request["size"]
			sorted_caches = sorted(self.input_problem.endpoints[idx_endpoint]["caches"].items(), key=lambda kv: kv[1])
			if idx_video in cache_servers_of_videos:
				cache_servers_of_video = cache_servers_of_videos[idx_video]
				for cache in sorted_caches:
					if cache[0] in cache_servers_of_video:
						score += size*(self.input_problem.endpoints[idx_endpoint]["datacenter_latency"] - cache[1])
						break

			denominator+=size
		
		return math.floor(score*1000/denominator)

	def random_solution(self):
		solution = {}
		for idx_cache in range(self.input_problem.num_caches):
			videos = []
			cache_size = 0
			videos_set = set(self.input_problem.videos.keys())
			while cache_size < self.input_problem.cache_capacity and len(videos_set) > 0:
				idx_video = random.sample(videos_set,1)[0]
				if (self.input_problem.videos[idx_video] + cache_size) > self.input_problem.cache_capacity:
					break
				else:
					videos.append(idx_video)
					videos_set.remove(idx_video)
					cache_size += self.input_problem.videos[idx_video]
					solution[idx_cache] = videos
		return solution



