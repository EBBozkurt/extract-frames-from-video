from enum import Enum

class EnumContentRowStates(Enum):
    WaitingForAnalysis = 10
    Splitting = 8
    Splitted = 7
    Analyzing = 6
    WaitingForApproval = 4
    Approved = 0
    Deleted = 1
