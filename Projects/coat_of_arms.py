###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("castle")


q1=codesters.Square(100,100,200,'blue')
q2=codesters.Square(-100,100,200,'purple')
q3=codesters.Square(-100,-100,200,'red')
q4=codesters.Square(100,-100,200, 'Navy')


s1=codesters.Sprite("waterbottle",100,100)
s2=codesters.Sprite("wienerdog", -100,-100)
s2.set_size (0.5)
s3=codesters.Sprite("milkjug", 100,-100)
s3.set_size (0.5)
s4=codesters.Sprite("fish",-100,100)
s4.set_size (0.6)

message1=codesters.Text("My name is Opal",0,220,"red")
message2=codesters.Text("I am very cool",0,-220,"black")