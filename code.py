
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_small_wall():
     turn_left()
     move()
     turn_right()
     move()
     turn_right()
     move()
     turn_left()
    
   
while(not at_goal()):
    if (wall_in_front()):
        if (right_is_clear()):
            turn_right()
  
        else:
            turn_left()
            
    elif (front_is_clear and left_is_clear()):
        turn_left()
    elif (front_is_clear and right_is_clear()):
        turn_right()
    if (front_is_clear()):
        move()
     
 
 
