from Teams import Teams

if __name__ == "__main__":    
    scratch = input("New teams from scratch?(y/n): ")
    teams = Teams()

    if (scratch == "y"):
        numberOfTeams = int(input("How many teams?: "))
        teamSize = int(input("How many players per team?: "))
        teams.CreateNewTeamsFromScratch(numberOfTeams, teamSize)
    else:
        teams.CreateNewTeamsUsingExistingTeams()