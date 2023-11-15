from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
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
count = 1
while True:
    robotArm.grab()
    if robotArm.scan() == "":
        break
    for i in range(count):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(count):
        robotArm.moveLeft()
    count += 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()