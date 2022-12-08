import constants as preset
from ui.gui.frontend.scenes.title.title import *
from ui.gui.frontend.scenes.home.home import *
from ui.gui.frontend.scenes.security.security import *
from ui.gui.frontend.scenes.settings.settings import *


class SceneManager:
    def __init__(self, root):
        self.root = root
        self.configure_root()
        self.scenes = {
            "title": TitleScreen(self),
            "home": Home(self),
            "security": Security(self),
            "settings": Settings(self)
        }
        self.scene = None
        self.current_scene("title")

    def current_scene(self, scene_name):
        self.scene = self.scenes[scene_name]
        self.scene.display_content()

    def change_scene(self, new_scene):
        self.scene.remove_content()
        self.current_scene(new_scene)

    def configure_root(self):
        self.root.geometry(preset.default_geometry)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
