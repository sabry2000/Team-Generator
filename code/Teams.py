from config import *
from TeamMember import TeamMember
from Team import Team

class Teams:
    def __init__(self):
        self.teams = []
        self.allTeamMembersList = []
    
    def __WriteTeamsToTextFile(self):
        with open(STR_AllTeamsInformationDirectory,"w+") as fileWriter:
            fileWriter.write("Current Teams: ")
            for team in self.teams:
                fileWriter.write("\n*************************************")
                fileWriter.write("\n%s" %(team.TeamSummary()))

    def __WriteAllMembersInformationToTextFile(self):
        with open(STR_AllPlayersInformationDirectory,"w+") as fileWriter:
            fileWriter.write("All Players Information: ")
            for teamMember in self.allTeamMembersList:
                fileWriter.write("\n*************************************")
                fileWriter.write(teamMember.ToString())

    def __SaveTeams(self):
        with open(STR_AllTeamsObjectDirectory, 'wb') as f:
            pickle.dump(self.teams,f)
            print("Teams saved!")

    def __LoadTeams(self):
        with open(STR_AllTeamsObjectDirectory, 'rb') as f:
            self.teams = pickle.load(f)
            print("Teams loaded!")


    def __RandomizeTeams(self, numberOfTeams, teamSize):
        self.teams = []
        for teamNumber in range(numberOfTeams):
            team = Team(teamNumber + 1)
            while (team.GetCurrentTeamSize() != teamSize):
                x = random.randint(1,numberOfTeams * teamSize) - 1
                team.TryToAddTeamMember(self.allTeamMembersList[x])
            team.FinalizeTeam()
            self.teams.append(team)

    def __GenerateNewTeamMembersList(self, numberOfTeams, teamSize):
        with open(STR_AllNamesJSONDirectory) as namesFile:
            names = json.load(namesFile)
            namesDictionary = names['names']
            for i in range(numberOfTeams * teamSize):
                try:
                    member = TeamMember(i + 1, namesDictionary[i])
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