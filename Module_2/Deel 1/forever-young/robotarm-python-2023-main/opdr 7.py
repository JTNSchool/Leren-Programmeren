from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
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
for a in range(5):
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if a < 4:
        robotArm.moveRight()
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()