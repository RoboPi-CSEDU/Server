from nanpy import (ArduinoApi, SerialManager)
from time import sleep

speed_left= 10 
speed_right= 11          
rot_left_1= 8  
rot_left_2= 9  
rot_right_1= 12  
rot_right_2= 13

try:
	connection = SerialManager()
	a= ArduinoApi(connection = connection)
except:
	print("Failed to connect")

  
a.pinMode(speed_left,a.OUTPUT)
a.pinMode(speed_right,a.OUTPUT)
    
a.pinMode(rot_left_1,a.OUTPUT)
a.pinMode(rot_left_2,a.OUTPUT)
    
a.pinMode(rot_right_1,a.OUTPUT)
a.pinMode(rot_right_2,a.OUTPUT)


def run(code):
    print("Running NanPy Code :")
    print(code)

    commands= code.split()
        
    for c in commands:
        if c == "mf":
            move_forward()
        elif c == "mb":
            move_back()
        elif c == "tl":
            turn_left()
        elif c == "tr":
            turn_right()
    stop_now()
                
	
def move_forward():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,255)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,255)
			
    sleep(3)



def move_back():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,255)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,255)
    a.analogWrite(rot_right_2,0)
			
    sleep(3)


def turn_right():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,255)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,255)
			
    sleep(0.5)

def turn_left():
    a.analogWrite(speed_left,255)
    a.analogWrite(speed_right,255)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,255)

    a.analogWrite(rot_right_1,255)
    a.analogWrite(rot_right_2,0)
			
    sleep(0.5)

def stop_now():
    a.analogWrite(speed_left,0)
    a.analogWrite(speed_right,0)
				
    a.analogWrite(rot_left_1,0)
    a.analogWrite(rot_left_2,0)

    a.analogWrite(rot_right_1,0)
    a.analogWrite(rot_right_2,0)
			
    sleep(1)
