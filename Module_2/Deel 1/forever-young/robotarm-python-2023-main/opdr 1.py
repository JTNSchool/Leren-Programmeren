from RobotArm import RobotArm
robotArm = RobotArm('exercise 1')
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
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()