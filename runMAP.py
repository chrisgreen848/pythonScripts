import os 
import glob
#########Scan for all weights files and put in to list #########
holdDir = "D:/tekvids/imgs/weights/boattinythird/"
os.chdir(holdDir)
fileNo = 0
weightsList = []
for file in glob.glob("*.weights"):
    weightsList.append(file)

print(weightsList)


newHoldDir = "D:/yolov4/darknet/Release/"
os.chdir(newHoldDir)
weightLoc = "D:/tekvids/imgs/weights/boattinythird/"

###-----Running MAP YOLO on every set of weights in directory -----------##
for i in range(len(weightsList)):
    weights = weightLoc + weightsList[i]
    cfg = "D:/yolov4/darknet/cfg/boattiny.cfg"
    data =  "D:/yolov4/darknet/cfg/boat.data"
    prog = "darknet.exe detector map"
    command = prog + " " + data + " " + cfg +" " + weights
    cmd = "cmd /c"
    newCmd = cmd + ' "' + command + '"'
    print(newCmd)
    os.system(newCmd)
