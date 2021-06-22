#while(1) is a way of saying loop forever
while (1):
    #Move the Servo connected to S1 to 0 degrees
    motor.servo(motor.Servos.S1, 0)
    #We need to give the servo time to get to position
    basic.pause(1000)
    #Move the Servo connected to S1 to 90 degrees
    motor.servo(motor.Servos.S1, 90)
    basic.pause(1000)
