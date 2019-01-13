import random

class Solver():

	def __init__(self, input_problem):
		self.input_problem = input_problem

	def random_solution():
		solution = {}
		for idx_cache in range(self.input_problem.num_caches):
			videos = []
			cache_size = 0
			videos_set = set(self.input_problem.videos.keys())
			while cache_size < self.input_problem.cache_capacity and len(videos_set) > 0:
				idx_video = random.sample(videos_set,1)[0]
				videos.append(idx_video)
				videos_set.remove(idx_video)

			solution[idx_cache] = videos
		return solution
