import json


class Utils:

	@staticmethod
	def json_file_to_dict(json_file):
		with open(json_file) as f:
			return (json.load(f))