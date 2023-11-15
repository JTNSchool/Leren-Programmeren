from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
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
move = 10
for i in range(5):
    move -= 1
    robotArm.grab()
    for i in range(move):
        robotArm.moveRight()
    robotArm.drop()
    move -= 1
    for i in range(move):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()