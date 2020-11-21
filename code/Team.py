from config import *
from TeamMember import TeamMember

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
        while(True):
            x = random.randint(0,len(self.teamMembers)) -1
            if (not self.teamMembers[x].wasCaptain):
                self.teamMembers[x].isCurrentCaptain = True
                self.teamMembers[x].wasCaptain = True
                break
            else:
                continue
    
    def __GetTeamCaptain(self):
        for member in self.teamMembers:
            if (member.isCurrentCaptain):
                return member
    
    def GetCurrentTeamSize(self):
        return len(self.teamMembers)
   
    def TryToAddTeamMember(self, member):
        if (not member.chosen):
            if (member not in self.__GetTeamMembersHistory()):
                self.__ChooseTeamMember(member)

    def FinalizeTeam(self):
        self.__AddHistoryToTeamMembers()
        self.__ChooseCaptain()
    
    def TeamSummary(self):
        captain = self.__GetTeamCaptain()
        strTeamNumber = "Team Number: %s" %str(self.teamNumber)
        strTeam = "Team members: \n"
        for member in self.teamMembers:
            strTeam += member.Summary() + "\n"        
        return strTeamNumber + "\n" + strTeam + "\n"