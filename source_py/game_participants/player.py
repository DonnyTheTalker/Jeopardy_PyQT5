from source_py.game_participants.game_member import GameMember


# Игрок, управляемый человеком

class Player(GameMember):
    def __init__(self, name, image, background_color):
        GameMember.__init__(self, name)
        self.image = image
        self.background_color = background_color
