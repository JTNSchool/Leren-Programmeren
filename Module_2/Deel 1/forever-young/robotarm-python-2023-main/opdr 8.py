from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 5
robotArm.reportFlaws = False
# Jouw python instructies zet je vanaf hier:
#RobotArm
#moveRight()
#moveLeft()
#grab()
#drop()
#scan()
#wait()
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()