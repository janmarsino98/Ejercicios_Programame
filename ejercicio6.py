entry = """16
Switzerland Spain Netherlands SouthAfrica Japan Norway Sweden UnitedStates
Australia Denmark France Morocco England Nigeria Colombia Jamaica
1 5 2 0 3 1 5 4 2 0 4 0 4 2 1 0 2 1 1 2 7 6 2 1 2 1 1 3 1 0
0"""

def get_winner(entry):
    number_of_teams = int(entry.split("\n")[0])
    data = " ".join(entry.split("\n")[1:-1])
    teams = data.split(" ")[:number_of_teams]
    results = data.split(" ")[number_of_teams:]
    while len(teams) != 1:
        new_teams = []
        for i in range(len(teams)):
            if i % 2 == 0:
                team1 = teams[i]
                
            else:
                team2 = teams[i]
                
                if results[i] > results[i -1]:
                    new_teams.append(team2)
                    
                else:
                    new_teams.append(team1)
        
        results = results[len(new_teams)*2:]            
        teams = new_teams
        
    print(teams[0])
    
    
get_winner(entry)