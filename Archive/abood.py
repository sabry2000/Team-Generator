import random
import pickle

AllPlayersTextFileName = "AllPlayers.txt"
AllTeamsTextFileName = "AllTeams.txt"
AllTeamsObjectFileName = "TeamsObject"

names = ["Ahmed", "Abdullah", "ghj"]                     #<--Manually add people names to this list (make sure it is 100 people)

class TeamMember:
    def __init__(self, memberID, name):
        self.memberID = memberID
        self.name = name
        self.history = []
        self.chosen = False
        self.wasCaptain = False
        self.isCurrentCaptain = False
    
    def Summary(self):
        strName = "Name: %s\n" %self.name
        strIsCurrentCaptain = "%s" %("Current Captain\n" if self.isCurrentCaptain else "\n")
        return strName + strIsCurrentCaptain + "\n"

    def ToString(self):
        strID = "ID: %s\n" %str(self.memberID)
        strName = "Name: %s\n" %self.name
        strWasCaptain = "Was Captain: %s\n" %("Yes" if self.wasCaptain else "No")
        strIsCurrentCaptain = "Is Current Captain: %s\n" %("Yes" if self.isCurrentCaptain else "No")
        
        strHistory = "Team Member History: \n"
        for previousTeammate in self.history:
            strPreviousTeammateName = ("%s \t" %(previousTeammate.name))
            strHistory += strPreviousTeammateName

        return strID + strName + strWasCaptain + strIsCurrentCaptain +  strHistory + "\n"


class Team:
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.teamMembers = []

    def __GetTeamMembersHistory(self):
        teamHistory = []
        for teamMember in self.teamMembers:
            teamHistory.append(previousTeammate for previousTeammate in teamMember.history)
        return teamHistory

    def __ChooseTeamMember(self, member):
        member.chosen = True
        member.isCurrentCaptain = False
        self.teamMembers.append(member)
    
    def __AddHistoryToTeamMembers(self):
        for member in self.teamMembers:
            for otherMember in self.teamMembers:
                if (member != otherMember):
                    member.history.append(otherMember)
    
    def __ChooseCaptain(self):
        while(bool(1)):
            x = random.randint(0,len(self.teamMembers)) -1
            if (~self.teamMembers[x].wasCaptain):
                self.teamMembers[x].currentCaptain = True
                self.teamMembers[x].wasCaptain = True
                break
            else:
                continue
   
    def TryToAddTeamMember(self, member):
        if (~member.chosen):
            if (member not in self.__GetTeamMembersHistory()):
                self.__ChooseTeamMember(member)

    def FinalizeTeam(self):
        self.__AddHistoryToTeamMembers()
    
    def TeamSummary(self):
        strTeamNumber = "Team Number: %s" %str(self.teamNumber)
        strTeam = "Team members: \n"
        for member in self.teamMembers:
            strTeam += member.Summary() + "\n"
        
        return strTeamNumber + "\n" + strTeam + "\n"

class Teams:
    def __init__(self):
        self.teams = []
        self.allTeamMembersList = []
    
    def __WriteTeamsToTextFile(self):
        f = open(AllTeamsTextFileName,"w+")
        f.write("Current Teams: ")
        for team in self.teams:
            f.write("\n*************************************")
            f.write("\nTeam #" + str(team.teamNumber))
            f.write("\nTeam Members: \n")
            f.write("\n%s" %(team.TeamSummary()))
        f.close()

    def __WriteAllMembersInformationToTextFile(self):
        f = open(AllPlayersTextFileName,"w+")
        f.write("All Players Information: ")
        for teamMember in self.allTeamMembersList:
            f.write("\n*************************************")
            f.write(teamMember.ToString())
        f.close()

    def __SaveTeams(self):
        with open(AllTeamsObjectFileName, 'wb') as f:
            pickle.dump(self.teams,f)
            print("Teams saved!")

    def __LoadTeams(self):
        with open(AllTeamsObjectFileName, 'rb') as f:
            self.teams = pickle.load(f)
            print("Teams loaded!")


    def __RandomizeTeams(self, numberOfTeams, teamSize):
        self.teams = []
        for teamNumber in range(numberOfTeams):
            team = Team(teamNumber + 1)
            for _ in range(teamSize):
                while (True):
                    x = random.randint(1,numberOfTeams * teamSize) - 1
                    team.TryToAddTeamMember(self.allTeamMembersList[x])                       
                    break
                else:
                    continue
            team.FinalizeTeam()
            self.teams.append(team)

    def __GenerateNewTeamMembersList(self, numberOfTeams, teamSize):
        for i in range(numberOfTeams * teamSize):
            try:
                member = TeamMember(i + 1, names[i])
            except:
                member = TeamMember(i + 1,'')
            finally:
                self.allTeamMembersList.append(member)

    def __ConfigureTeamMembersList(self):
        for team in self.teams:
            for member in team.teamMembers:
                member.chosen = False
                self.allTeamMembersList.append(member)
        self.allTeamMembersList.sort(key=lambda member: member.memberID)        

    def CreateNewTeamsFromScratch(self, numberOfTeams, teamSize):        
        self.__GenerateNewTeamMembersList(numberOfTeams, teamSize)
        self.__RandomizeTeams(numberOfTeams, teamSize)
        self.__SaveTeams()
        self.__WriteAllMembersInformationToTextFile()
        self.__WriteTeamsToTextFile()

    def CreateNewTeamsUsingExistingTeams(self):
        self.__LoadTeams()
        self.__ConfigureTeamMembersList()
        numberOfTeams = len(self.teams)
        teamSize = int(len(self.allTeamMembersList) / numberOfTeams)
        self.__RandomizeTeams(numberOfTeams, teamSize)
        self.__SaveTeams()
        self.__WriteAllMembersInformationToTextFile()
        self.__WriteTeamsToTextFile()

if __name__ == "__main__":
    scratch = input("New teams from scratch?(y/n): ")
    teams = Teams()

    if (scratch == "y"):
        numberOfTeams = int(input("How many teams?: "))
        teamSize = int(input("How many players per team?: "))
        teams.CreateNewTeamsFromScratch(numberOfTeams, teamSize)
    else:
        teams.CreateNewTeamsUsingExistingTeams()
