from utils.input_parser import InputParser
from utils.output_exporter import OutputExporter
from solver import Solver


input_parser = InputParser('inputs/example.in')
input_parser.parse()

solver = Solver(input_parser)
solution = solver.random_solution()

output_exporter = OutputExporter(solution,'inputs/our_example.out')
output_exporter.export()
