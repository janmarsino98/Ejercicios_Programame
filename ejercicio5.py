

def get_classified(entry):
    n_classified = int(entry.split("\n")[0].split(" ")[1])
    classification = {}
    for line in entry.split("\n")[1:]:
        team1, team2, goals1, goals2 = line.split(" ")
        if goals1 == goals2:
            winner = "draw"
            
        elif goals1 > goals2:
            winner = team1
        else:
            winner = team2
            
        try:
            classification[team1]["dif"] += int(goals1) - int(goals2)
        except KeyError:
            classification[team1] = {"dif": int(goals1) - int(goals2), "points": 0}
            
        try:
            classification[team2]["dif"] += int(goals2) - int(goals1)
        except KeyError:
             classification[team2] = {"dif": int(goals2) - int(goals1), "points": 0}
            
        if winner != "draw":
            classification[winner]["points"] += 3
            
        else:
            try:
                classification[team1]["points"] += 1
            except KeyError:
                classification[team1]["points"] = 1
            try:
                classification[team2]["points"] += 1    
            except KeyError:
                classification[team2]["points"] += 1 
                
        sorted_classification = sorted(classification.items(), key=lambda x: [x[1]["points"], x[1]["dif"]], reverse=True)
        top_2_teams = sorted_classification[:n_classified]
    for team in top_2_teams:
        print(team[0])
        
            
        
            
sample_entry = """3 1
1 2 3 0
1 3 3 0
2 3 0 0"""

get_classified(sample_entry)