from RobotArm import RobotArm
robotArm = RobotArm('exercise 6')
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
robotArm.moveRight()
for i in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()