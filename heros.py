import csv

class Heros:
	英雄列表 = {}
	def __init__(self):
		with open('heros.csv', newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:
				self.英雄列表[row[0]] = list(filter(None, row[1:]))

	def is射手(self, hero):
		return (hero in self.英雄列表["射手"])

	def is法师(self, hero):
		return (hero in self.英雄列表["法师"])

	def is战士(self, hero):
		return (hero in self.英雄列表["战士"])

	def is坦克(self, hero):
		return (hero in self.英雄列表["坦克"])

	def is刺客(self, hero):
		return (hero in self.英雄列表["刺客"])

	def is辅助(self, hero):
		return (hero in self.英雄列表["辅助"])
