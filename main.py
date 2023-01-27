import arcade

SCREEN_WIDTH =900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Harvard HomeWork"
SPRITE_SCALING = 0.1
MOVEMENT_SPEED = 4



class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__()
        self.player_list = None
        self.player_sprite = None
        self.walls = None
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player("D:/Python/HUGame/Game_Images/h_logo.png",SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 420
        self.player_list.append(self.player_sprite)



    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        arcade.draw_line(50, 450, 50, 200, arcade.color.BLACK, 4)  # first room left wall
        arcade.draw_line(50, 450, 170, 450, arcade.color.BLACK, 4)  # first room top wall
        arcade.draw_line(170, 450, 170, 250, arcade.color.BLACK, 4)  # first room right wall
        arcade.draw_line(170, 250, 220, 250, arcade.color.BLACK, 4)  # first small wall
        arcade.draw_line(50, 200, 270, 200, arcade.color.BLACK, 4)  # first room floor
        arcade.draw_line(220, 250, 220, 420, arcade.color.BLACK, 4)  # above first room small wall
        arcade.draw_line(270, 200, 270, 260, arcade.color.BLACK, 4)  # small wall right tunnel wall
    def on_update(self,delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()

main()