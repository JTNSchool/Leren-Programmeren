from RobotArm import RobotArm
robotArm = RobotArm('exercise 1')
robotArm.speed = 3
robotArm.reportFlaws = False
# Jouw python instructies zet je vanaf hier:
#RobotArm.moveRight()
#RobotArm.moveLeft()
#RobotArm.grab()
#RobotArm.drop()
#RobotArm.scan()
#RobotArm.wait()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()