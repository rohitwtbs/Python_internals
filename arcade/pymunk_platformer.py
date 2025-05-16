import arcade

screen_title = "Pymunk Platformer"
screen_width = 800
screen_height = 600

class GameWindow(arcade.Window):

    def __init__(self):
        pass

    def setup(self):
        pass

    def on_key_press(self):
        pass

    def on_key_release(self):
        pass

    def on_update(self):
        pass

    def on_draw(self):
        pass


def main():
    window = GameWindow(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()