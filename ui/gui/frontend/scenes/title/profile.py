class CreateProfile:
    def __init__(self, root):
        self.root = root

    def set_frames(self):
        pass

    def set_widgets(self):
        pass

    def display_frames(self):
        pass

    def display_widgets(self):
        pass

    def remove_content(self):
        pass

    def exit_scene(self, success):
        if success:
            pass
        else:
            self.root.change_scene("title")

class SelectProfile:
    pass
