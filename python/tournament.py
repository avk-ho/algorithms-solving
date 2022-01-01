# https://www.algoexpert.io/questions/Tournament%20Winner

# competitions is a list of pairs of "teams" [homeTeam, awayTeam]
# results is a list of either 0 or 1, 0 means awayTeam won, 1 means homeTeam won
# +3 points for a win, 0 for a loss

# First version
def tournamentWinner(competitions, results):

	score_tally = {}
	
	for i in range(0, len(competitions)):

		if results[i] == 0:
			results[i] = 1
		else:
			results[i] = 0

		winner = competitions[i][results[i]]
		#print(winner)
		if winner in score_tally:
			score_tally[winner] += 3
		else:
			score_tally[winner] = 3

	t_winner = ""
	max_score = 0

	for team in score_tally:
		if score_tally[team] > max_score:
			t_winner = team
			max_score = score_tally[team]

	#print(t_winner)
	return t_winner

competitions = [
    ["team1", "team2"],
    ["team2", "team3"],
    ["team3", "team1"]
]
results = [0, 0, 1]
tournamentWinner(competitions, results)

# Possibility to improve the O() T if we could check for an early tournament winner

# Version 2, include an early_win condition, ending the function earlier if a clear winner
# becomes evident 
# Improves the best case scenario (sorted competitions list, with the winner first), 
# but doesn't worsen impact in poor case scenario

def tournamentWinner(competitions, results):
	import math

	score_tally = {}
	t_winner = ""
	nb_matches = len(competitions)
	early_win = math.ceil(nb_matches / 2) * 3

	for i in range(0, nb_matches):

		if results[i] == 0:
			results[i] = 1
		else:
			results[i] = 0

		winner = competitions[i][results[i]]
		#print(winner)
		if winner in score_tally:
			score_tally[winner] += 3
		else:
			score_tally[winner] = 3

		if score_tally[winner] == early_win:
			t_winner = winner
			break

	if t_winner == "":
		max_score = 0

		for team in score_tally:
			if score_tally[team] > max_score:
				t_winner = team
				max_score = score_tally[team]

	#print(t_winner)
	return t_winner
