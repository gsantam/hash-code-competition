from utils.input_parser import InputParser
from utils.output_parser import OutputParser
from solver import Solver


input_parser = InputParser('inputs/example.in')
input_parser.parse()

output_parser = OutputParser(input_parser,'inputs/example.out')
output_parser.parse()

solver = Solver(input_parser)
solver.random_solution()
