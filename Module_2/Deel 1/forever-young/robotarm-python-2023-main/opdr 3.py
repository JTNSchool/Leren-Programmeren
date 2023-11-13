from RobotArm import RobotArm
robotArm = RobotArm('exercise 3')
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
for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()