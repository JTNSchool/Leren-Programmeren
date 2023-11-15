from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
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
count = 9
for i in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for i in range(count):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(count):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    count -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()