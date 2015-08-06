def main():
    teams = getTeamNames()

""" Get the team names and store then in a list """
def getTeamNames():
    numTeams = int(input("Please enter the number of teams you wish to add to the tournament: "))
    teamList = []
    count = 1
    while count <= numTeams:
        teamName = input("Please enter the name of team number %d " % count)
        teamList.append(teamName)
        count += 1
    return teamList

main()
