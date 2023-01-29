import os
import arcade

script_dir = os.path.dirname(__file__)
rel_path = "../HUGame/Game_Images/"
abs_file_path = os.path.join(script_dir,rel_path)


SCREEN_WIDTH =1280
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Harvard_HomeWork"
SPRITE_SCALING = 0.1
MOVEMENT_SPEED = 4


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH -1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, SCREEN_TITLE):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.player_list = None
        self.player_sprite = None


        self.top_wall1 = None
        self.top_wall2 = None
        self.top_wall3 = None
        self.top_wall4 = None
        self.top_wall5 = None
        self.top_wall6 = None
        self.top_wall7 = None
        self.top_wall8 = None
        self.top_wall9 = None
        self.top_wall10 = None
        self.top_wall11 = None

        self.side_wall1 = None
        self.side_wall2 = None
        self.side_wall3 = None
        self.side_wall4 = None
        self.side_wall5 = None
        self.side_wall6 = None
        self.side_wall7 = None
        self.side_wall8 = None
        self.side_wall9 = None
        self.side_wall10 = None
        self.side_wall11 = None
        self.side_wall12 = None
        self.side_wall13 = None


        self.walls_list = None
        arcade.set_background_color(arcade.color.WHITE)

    def setup_01(self):
        self.player_list = arcade.SpriteList()
        self.walls_list = arcade.SpriteList(use_spatial_hash=True)


        self.player_sprite = Player(abs_file_path + str("h_logo.png"),SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 420
        self.player_list.append(self.player_sprite)

#===================================================================================================

        self.top_wall1 = Player(abs_file_path + str("top_wall01.png"),0.3)
        self.top_wall1.center_x = 135
        self.top_wall1.center_y = 450
        self.walls_list.append(self.top_wall1)

        self.top_wall2 = Player(abs_file_path + str("top_wall01.png"),0.3)
        self.top_wall2.center_x = 135
        self.top_wall2.center_y = 140
        self.walls_list.append(self.top_wall2)

        self.top_wall3 = Player(abs_file_path + str("top_wall01.png"),0.3)
        self.top_wall3.center_x = 250
        self.top_wall3.center_y = 140
        self.walls_list.append(self.top_wall3)

        self.top_wall4 = Player(abs_file_path + str("top_wall02.png"),0.15)
        self.top_wall4.center_x = 220
        self.top_wall4.center_y = 220
        self.walls_list.append(self.top_wall4)

        self.top_wall5 = Player(abs_file_path + str("top_wall02.png"),0.3)
        self.top_wall5.center_x = 375
        self.top_wall5.center_y = 200
        self.walls_list.append(self.top_wall5)

        self.top_wall6 = Player(abs_file_path+ str("top_wall03.png"),0.3)
        self.top_wall6.center_x = 450
        self.top_wall6.center_y = 450
        self.walls_list.append(self.top_wall6)

        self.top_wall7 = Player(abs_file_path+ str("top_wall03.png"),0.35)
        self.top_wall7.center_x = 790
        self.top_wall7.center_y = 448
        self.walls_list.append(self.top_wall7)

        self.top_wall8 = Player(abs_file_path+ str("top_wall03.png"),0.35)
        self.top_wall8.center_x = 670
        self.top_wall8.center_y = 183
        self.walls_list.append(self.top_wall8)

        self.top_wall9 = Player(abs_file_path + str("top_wall01.png"),0.13)
        self.top_wall9.center_x = 865
        self.top_wall9.center_y = 250
        self.walls_list.append(self.top_wall9)

        self.top_wall10 = Player(abs_file_path + str("top_wall02.png"),0.3)
        self.top_wall10.center_x = 950
        self.top_wall10.center_y = 199
        self.walls_list.append(self.top_wall10)

        self.top_wall11 = Player(abs_file_path + str("top_wall01.png"),0.13)
        self.top_wall11.center_x = 865
        self.top_wall11.center_y = 418
        self.walls_list.append(self.top_wall11)

#===============================================================================================

        self.side_wall1 = Player(abs_file_path + str("side_wall.png"),0.1)
        self.side_wall1.center_x = 75
        self.side_wall1.center_y = 395
        self.walls_list.append(self.side_wall1)

        self.side_wall2 = Player(abs_file_path + str("side_wall.png"),0.1)
        self.side_wall2.center_x = 190
        self.side_wall2.center_y = 395
        self.walls_list.append(self.side_wall2)

        self.side_wall3 = Player(abs_file_path + str("side_wall.png"),0.1)
        self.side_wall3.center_x = 75
        self.side_wall3.center_y = 280
        self.walls_list.append(self.side_wall3)

        self.side_wall4 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall4.center_x = 190
        self.side_wall4.center_y = 280
        self.walls_list.append(self.side_wall4)

        self.side_wall5 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall5.center_x = 75
        self.side_wall5.center_y = 200
        self.walls_list.append(self.side_wall5)

        self.side_wall6 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall6.center_x = 250
        self.side_wall6.center_y = 280
        self.walls_list.append(self.side_wall6)

        self.side_wall7 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall7.center_x = 250
        self.side_wall7.center_y = 400
        self.walls_list.append(self.side_wall7)

        self.side_wall8 = Player(abs_file_path + str("side_wall.png"), 0.05)
        self.side_wall8.center_x = 310
        self.side_wall8.center_y = 170
        self.walls_list.append(self.side_wall8)

        self.side_wall9 = Player(abs_file_path + str("side_wall.png"), 0.14)
        self.side_wall9.center_x = 840
        self.side_wall9.center_y = 335
        self.walls_list.append(self.side_wall9)

        self.side_wall10 = Player(abs_file_path + str("side_wall.png"), 0.14)
        self.side_wall10.center_x = 890
        self.side_wall10.center_y = 335
        self.walls_list.append(self.side_wall10)

        self.side_wall11 = Player(abs_file_path + str("side_wall.png"), 0.10)
        self.side_wall11.center_x = 1010
        self.side_wall11.center_y = 260
        self.walls_list.append(self.side_wall11)

        self.side_wall12 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall12.center_x = 1010
        self.side_wall12.center_y = 380
        self.walls_list.append(self.side_wall12)

        self.side_wall13 = Player(abs_file_path + str("side_wall.png"), 0.1)
        self.side_wall13.center_x = 1010
        self.side_wall13.center_y = 405
        self.walls_list.append(self.side_wall13)


    def on_draw(self):
        self.clear()
        self.player_list.draw()

#===================================================================

        self.top_wall1.draw()
        self.top_wall2.draw()
        self.top_wall3.draw()
        self.top_wall4.draw()
        self.top_wall5.draw()
        self.top_wall6.draw()
        self.top_wall7.draw()
        self.top_wall8.draw()
        self.top_wall9.draw()
        self.top_wall10.draw()
        self.top_wall11.draw()

#==================================================================

        self.side_wall1.draw()
        self.side_wall2.draw()
        self.side_wall3.draw()
        self.side_wall4.draw()
        self.side_wall5.draw()
        self.side_wall6.draw()
        self.side_wall7.draw()
        self.side_wall8.draw()
        self.side_wall9.draw()
        self.side_wall10.draw()
        self.side_wall11.draw()
        self.side_wall12.draw()
        self.side_wall13.draw()

    def on_update(self,delta_time):
        self.player_list.update()

#===================================================================

        colliding_TW1 = arcade.check_for_collision(self.player_sprite,self.top_wall1)
        if colliding_TW1:
            self.player_sprite.change_y = 0

        colliding_TW2 = arcade.check_for_collision(self.player_sprite,self.top_wall2)
        if colliding_TW2:
            self.player_sprite.change_y = 0

        colliding_TW3 = arcade.check_for_collision(self.player_sprite,self.top_wall3)
        if colliding_TW3:
            self.player_sprite.change_y = 0

        colliding_TW4 = arcade.check_for_collision(self.player_sprite,self.top_wall4)
        if colliding_TW4:
            self.player_sprite.change_y = 0

        colliding_TW5 = arcade.check_for_collision(self.player_sprite,self.top_wall5)
        if colliding_TW5:
            self.player_sprite.change_y = 0

        colliding_TW6 = arcade.check_for_collision(self.player_sprite,self.top_wall6)
        if colliding_TW6:
            self.player_sprite.change_y = 0

        colliding_TW7 = arcade.check_for_collision(self.player_sprite,self.top_wall7)
        if colliding_TW7:
            self.player_sprite.change_y = 0

        colliding_TW8 = arcade.check_for_collision(self.player_sprite,self.top_wall8)
        if colliding_TW8:
            self.player_sprite.change_y = 0

        colliding_TW9 = arcade.check_for_collision(self.player_sprite,self.top_wall9)
        if colliding_TW9:
            self.player_sprite.change_y = 0

        colliding_TW10 = arcade.check_for_collision(self.player_sprite,self.top_wall10)
        if colliding_TW10:
            self.player_sprite.change_y = 0

        colliding_TW11 = arcade.check_for_collision(self.player_sprite,self.top_wall11)
        if colliding_TW11:
            self.player_sprite.change_y = 0
#====================================================================

        colliding_SW1 = arcade.check_for_collision(self.player_sprite,self.side_wall1)
        if colliding_SW1:
            self.player_sprite.change_x = 0

        colliding_SW2 = arcade.check_for_collision(self.player_sprite,self.side_wall2)
        if colliding_SW2:
            self.player_sprite.change_x = 0

        colliding_SW3 = arcade.check_for_collision(self.player_sprite,self.side_wall3)
        if colliding_SW3:
            self.player_sprite.change_x = 0

        colliding_SW4 = arcade.check_for_collision(self.player_sprite,self.side_wall4)
        if colliding_SW4:
            self.player_sprite.change_x = 0

        colliding_SW5 = arcade.check_for_collision(self.player_sprite,self.side_wall5)
        if colliding_SW5:
            self.player_sprite.change_x = 0

        colliding_SW6 = arcade.check_for_collision(self.player_sprite,self.side_wall6)
        if colliding_SW6:
            self.player_sprite.change_x = 0


        colliding_SW7 = arcade.check_for_collision(self.player_sprite,self.side_wall7)
        if colliding_SW7:
            self.player_sprite.change_x = 0

        colliding_SW8 = arcade.check_for_collision(self.player_sprite,self.side_wall8)
        if colliding_SW8:
            self.player_sprite.change_x = 0

        colliding_SW9 = arcade.check_for_collision(self.player_sprite,self.side_wall9)
        if colliding_SW9:
            self.player_sprite.change_x = 0

        colliding_SW10 = arcade.check_for_collision(self.player_sprite,self.side_wall10)
        if colliding_SW10:
            self.player_sprite.change_x = 0

        colliding_SW11 = arcade.check_for_collision(self.player_sprite,self.side_wall11)
        if colliding_SW11:
            self.player_sprite.change_x = 0

        colliding_SW12 = arcade.check_for_collision(self.player_sprite,self.side_wall12)
        if colliding_SW12:
            self.player_sprite.change_x = 0

        colliding_SW13 = arcade.check_for_collision(self.player_sprite,self.side_wall13)
        if colliding_SW13:
            self.player_sprite.change_x = 0



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
    window.setup_01()
    arcade.run()

main()