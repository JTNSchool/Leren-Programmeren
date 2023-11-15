from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
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

block = 1

for i in range(4):
    for i in range(block):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    block += 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()