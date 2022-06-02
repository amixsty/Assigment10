
import arcade
import random


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 16
        self.height = 16
        self.center_x = 250
        self.center_y = 250
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)


class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__("apple.png")
      #  self.color = arcade.color.RED
        self.center_x = random.randint(0,500)
        self.center_y = random.randint(0,400)
        self.width = 40;
        self.height = 40;



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=400,title="Amixsty Snake :)")
        self.background_color = arcade.color.SAFFRON
        self.food = Apple()
        self.player = Snake()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            print("up")
        elif symbol == arcade.key.S:
            print("down")    
        elif symbol == arcade.key.A:
            print("left")  
        elif symbol == arcade.key.D:
            print("right")              
    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.player.draw()



g = Game()

arcade.run()
