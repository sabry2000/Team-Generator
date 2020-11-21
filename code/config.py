import random
import pickle
import json
import os

__allPlayersTextFileName = "AllPlayers.txt"
__allTeamsTextFileName = "AllTeams.txt"
__allTeamsObjectFileName = "TeamsObject"
__allNamesFileName = "names.json"

__currentDirectory = os.path.dirname(__file__)
__resultsFolder = os.path.join(__currentDirectory, '..\\', 'results\\')

STR_AllPlayersInformationDirectory = os.path.join(__resultsFolder, __allPlayersTextFileName)
STR_AllTeamsInformationDirectory = os.path.join(__resultsFolder, __allTeamsTextFileName)
STR_AllTeamsObjectDirectory = os.path.join(__currentDirectory, __allTeamsObjectFileName)
STR_AllNamesJSONDirectory = os.path.join(__currentDirectory,'..\\', __allNamesFileName)