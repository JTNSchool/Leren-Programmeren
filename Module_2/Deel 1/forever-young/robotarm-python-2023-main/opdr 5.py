from RobotArm import RobotArm
robotArm = RobotArm('exercise 5')
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
for i in range(7):
    robotArm.moveRight()

for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if i < 7:
        robotArm.moveLeft()
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()