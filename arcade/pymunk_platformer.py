import arcade

SCREEN_TITLE = "PyMunk Platformer"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

# Size of screen to show, in pixels
SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player_sprite: arcade.Sprite | None = None

        # Sprite lists we need
        self.player_list: arcade.SpriteList | None = None
        self.wall_list: arcade.SpriteList | None = None
        self.bullet_list: arcade.SpriteList | None = None
        self.item_list: arcade.SpriteList | None = None

        # Track the current state of what key is pressed
        self.left_pressed: bool = False
        self.right_pressed: bool = False


    def setup(self):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        pass


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()