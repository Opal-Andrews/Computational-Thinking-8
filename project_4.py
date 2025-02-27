# Section 1 - Setup
import codesters, random 
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("cherry twist")
cherry_twist_points = 0
time = 10
stage.set_background("warehouse")
object_speed = 5
object_speed += 3.
cherry_twist_points = 0
cherry_twist_points += 1
player.goto (-199,-199)
# Section 2 - Objects
def falling_object():
    global object_speed, cherry_twist_points, time
    if time > 0 and cherry_twist_points < 15:
        x = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("lime", x, y)
        time -= 1
        # object.set_size(10)
        object.set_y_speed(-object_speed)
stage.event_interval(falling_object, 10)

# section 3 - collision
def collision(player, object):
    global cherry_twist_points, time


    if object.get_image_name() == "lime":
        stage.remove_sprite(object)
        cherry_twist_points +=1
        if time <= 0:
            player.say("You lose!",7)
        if cherry_twist_points == 15:
            player.say ("You win!",7)

player.event_collision(collision)

#section 4 - controls

def move_left (cherry_twist):
    cherry_twist.move_left (5)

def move_right (cherry_twist):
    cherry_twist.move_right (5)
player.event_key("right", move_right)
player.event_key("left", move_left)


