import random

def main():
    numTeams = int(input("Please enter the number of teams you wish to add to the tournament: "))
    numGroups = int(input("Please enter the number of groups you wish to make with the teams: "))
    teams = getTeamNames(numTeams)
    randomTeams = random.sample(teams, numTeams)
    toTextFile(randomTeams)

""" Get the team names and store then in a list """
def getTeamNames(numTeams):
    teamList = []
    count = 1
    while count <= numTeams:
        teamName = raw_input("Please enter the name of team number %d: " % count)
        teamList.append(teamName)
        count += 1
    return teamList

""" Randomly place teams into a text file """
def toTextFile(randomTeams):
    myFile = open("teams.txt", "w")
    for team in randomTeams:
        myFile.write(team + "\n")
    myFile.close()

main()
