"""
singleObj.py :=> singleton objects for clamav commands and services
"""

from ClamAVResources import ClamAVCommands, ClamdService

clamav_commands = ClamAVCommands.object()
clamav_service = ClamdService.object()

if __name__ == "__main__":
    # test any code here
    print(clamav_service.isOK())
    pass
