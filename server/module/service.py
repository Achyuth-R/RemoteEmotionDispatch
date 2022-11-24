from server import LightRecordFile

def getLightRecord():
    LightRecordFileData = LightRecordFile.read()
    ParsedLightRecordFileData = int(LightRecordFile)
    return LightRecordFileData

def updateLightRecord(LightRecordData):
    if(LightRecordData == 1 or LightRecordData == 0):
        LightRecordFile.write(str(LightRecordData))
        return 0
    else:
        return 99