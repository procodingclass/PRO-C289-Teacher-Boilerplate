# keycodes : 
# 314 : left arrow 
# 315 : up arrow
# 316 : right arrow
# 317 : down arrow
# 87 : w
# 65 : a
# 83 : s
# 68 : d
# 49 : 1
# 50 : 2
# 51 : 3
# 52 : 4

from controller import Robot, Keyboard

bot = Robot()
keyboard = Keyboard()

timestep = 64

# Arm joints
shoulder_lift = bot.getDevice('shoulder_lift_joint')
shoulder_pan = bot.getDevice('shoulder_pan_joint')
elbow = bot.getDevice('elbow_joint')
wrist_1 = bot.getDevice('wrist_1_joint')
wrist_2 = bot.getDevice('wrist_2_joint')
wrist_3 = bot.getDevice('wrist_3_joint')

# enabling keyboard
keyboard.enable(timestep)

# method to move the arm
def move_bot(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, ):
    
    # arm joints
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist_1.setPosition(d)
    wrist_2.setPosition(e)
    wrist_3.setPosition(f)

# moving bot at initial positions
move_bot()

# variables to track joint positions
shoulder_lift_pos = 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist_1_pos = 0
wrist_2_pos = 0
wrist_3_pos = 0


while bot.step(timestep)  !=  -1:
    
    keypressed = keyboard.getKey()
           
    if keypressed  ==  317:                # down key is pressed
        shoulder_lift_pos += 0.01
    elif keypressed  ==  315:              # up key is pressed
        shoulder_lift_pos -= 0.01
    elif keypressed  ==  314:              # left key is pressed
        shoulder_pan_pos += 0.01
    elif keypressed  ==  316:              # right key is pressed
        shoulder_pan_pos -= 0.01
    elif keypressed  ==  87:               # w key is pressed
        elbow_pos -= 0.01
    elif keypressed  ==  83:               # s key is pressed
        elbow_pos += 0.01
    elif keypressed  ==  65:               # a key is pressed
        wrist_1_pos += 0.01
    elif keypressed  ==  68:               # d key is pressed
        wrist_1_pos -= 0.01
    elif keypressed  ==  49:               # 1 key is pressed
        wrist_2_pos += 0.01
    elif keypressed  ==  50:               # 2 key is pressed
        wrist_2_pos -= 0.01
    elif keypressed  ==  51:               # 3 key is pressed
        wrist_3_pos += 0.01
    elif keypressed  ==  52:               # 4 key is pressed
        wrist_3_pos -= 0.01
        
    
    move_bot(shoulder_lift_pos, shoulder_pan_pos, elbow_pos, 
             wrist_1_pos, wrist_2_pos, wrist_3_pos)