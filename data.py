import csv

def LoadData():
	data = []
	with open('data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			match = {}
			match["time"] = row[0]
			match["result"] = row[1]
			match["players"] = []
			match["oponents"] = []
			for i in range(5):
				player = {}
				player["charactor"] = row[i*2+2]
				player["player"] = row[i*2+3]
				match["players"].append(player)
				match["oponents"].append(row[i+12])
			data.append(match)
	return data

def total_win_rate(data):
	win_match = 0
	total_match = 0
	for match in data:
		if match["result"] == "1":
			win_match += 1
		total_match += 1
	print ("胜利场次：" + str(win_match))
	print ("总共场次：" + str(total_match))
	print ("胜率：" + str(float(win_match)/float(total_match)))
	return float(win_match)/float(total_match)

def player_win_rate(data, player, bias = 3):
	win_rate_by_charactor = {}
	for match in data:
		for p in match["players"]:
			if p["player"] == player:
				if p["charactor"] not in win_rate_by_charactor:
					win_rate_by_charactor[p["charactor"]] = {"win_match":int(match["result"]), "total_match":1}
				else:
					win_rate_by_charactor[p["charactor"]]["total_match"] += 1
					win_rate_by_charactor[p["charactor"]]["win_match"] += int(match["result"])

	print('-'*10 + player + '-'*10)
	for name in win_rate_by_charactor.keys():
		if int(win_rate_by_charactor[name]["total_match"]) < bias:
			continue
		win_rate = float(win_rate_by_charactor[name]["win_match"]) / float(win_rate_by_charactor[name]["total_match"])
		print (name + f': {win_rate:.2f}')
	return win_rate_by_charactor

def oponent_analysis(data, bias = 3,ranking = 5):
	win_rate_by_charactor = {}
	for match in data:
		for o in match["oponents"]:
			if o not in win_rate_by_charactor:
				win_rate_by_charactor[o] = {"win_match":int(match["result"]), "total_match":1}
			else:
				win_rate_by_charactor[o]["total_match"] += 1
				win_rate_by_charactor[o]["win_match"] += int(match["result"])

	for oponent in list(win_rate_by_charactor.keys()):
		if win_rate_by_charactor[oponent]["total_match"] < bias:
			del win_rate_by_charactor[oponent]
			continue
		win_rate_by_charactor[oponent]["win_rate"] = float(win_rate_by_charactor[oponent]["win_match"])/float(win_rate_by_charactor[oponent]["total_match"])
	sorted_win_rate = [(k, v["win_rate"]) for k, v in sorted(win_rate_by_charactor.items(), key=lambda item: item[1]["win_rate"])]
	
	print ('-'*10+"对阵英雄胜率(最低)："+'-'*10)
	for i in range(ranking):
		print (sorted_win_rate[i])
	print ('-'*10+"对阵英雄胜率(最高)："+'-'*10)
	for i in range(ranking):
		print (sorted_win_rate[-1-i])
	return win_rate_by_charactor

data = LoadData()
print(data[0])
total_win_rate(data)
player_win_rate(data,"彼地此时JQ")
player_win_rate(data,"星河涛涛")
player_win_rate(data,"知乎乎锤锤锤")
player_win_rate(data,"小俞总")
player_win_rate(data,"此时彼地HJ")
print(oponent_analysis(data, bias=1, ranking = 10))
