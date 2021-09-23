from ursina import *

#config
window.title = 'cad prototype idea "ursacad"'          # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen

x = 0
y = 0
z = 0 


app = Ursina()
print(app.get_size.__format__.__str__)
#bsc = (app.getSize / 0.8)     # mathematical cont that works out the perfect scale for the window of usinacad application aka BUTTON SIZE CONST





class cam:
 cam = Entity(model = "cube", color = color.white, position=(0,0,0), parent = scene)
 

class sketch:
  sketch =Button(scale =(0.21 ,0.2), text = "sketch" , position = (-4.9,3.1),color = color.red , parent = scene)
  def input(self,key):
   if self.hovered:
    if key == 'left mouse down':
     msgbox("scetch button clicked")

def update():
	global block_pick
	


# keys to move the camera from the blocky boi

	if held_keys['a']: camera.x-= 1 * time.dt
	if held_keys['w']: camera.y+=1 * time.dt
	if held_keys['s']: camera.y -=1 * time.dt
	if held_keys['d']: camera.x+=1 * time.dt
	if held_keys['e']: camera.z +=1 * time.dt
	if held_keys['q']: camera.z -=1 * time.dt

# run

try :
 app.run()
finally:
	print("ended")



























