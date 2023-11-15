from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
robotArm.reportFlaws = False
# Jouw python instructies zet je vanaf hier:
#RobotArm
#moveRight()
#moveLeft()
#grab()
#drop()
#scan()
#wait()
for i in range(8):
    robotArm.moveRight()

for i in range(8):
    robotArm.grab()
    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()