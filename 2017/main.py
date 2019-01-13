from utils.input_parser import InputParser
from utils.output_parser import OutputParser


input_parser = InputParser('inputs/example.in')
input_parser.parse()

output_parser = OutputParser(input_parser,'inputs/example.out')
output_parser.parse()