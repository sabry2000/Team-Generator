class TeamMember:
    def __init__(self, memberID, name):
        self.memberID = memberID
        self.name = name
        self.history = []
        self.chosen = False
        self.wasCaptain = False
        self.isCurrentCaptain = False
    
    def __GetNameAndIDString(self):
        return "Name: %s(#%s)\n" %(self.name, str(self.memberID))

    def Summary(self):
        strNameAndID = self.__GetNameAndIDString()
        strIsCurrentCaptain = "%s" %("(Current Captain)\n" if self.isCurrentCaptain else "\n")
        return strNameAndID + strIsCurrentCaptain + "\n"

    def ToString(self):
        strID = "ID: %s\n" %str(self.memberID)
        strName = "Name: %s\n" %self.name
        strWasCaptain = "Was Captain: %s\n" %("Yes" if self.wasCaptain else "No")
        strIsCurrentCaptain = "Is Current Captain: %s\n" %("Yes" if self.isCurrentCaptain else "No")
        
        strHistory = "Team Member History: \n"
        for previousTeammate in self.history:
            strPreviousTeammateInfo = ("%s" %(previousTeammate.__GetNameAndIDString()))
            strHistory += strPreviousTeammateInfo

        return strID + strName + strWasCaptain + strIsCurrentCaptain +  strHistory + "\n"