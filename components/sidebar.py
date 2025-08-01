from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerLabel,
    MDNavigationDrawerItem,
    MDNavigationDrawerDivider,
)
class Sidebar(MDNavigationDrawer):
    def __init__(self, screen_changer=None, **kwargs):
        super().__init__(**kwargs)

        self.screen_changer = screen_changer

        self.menu = MDNavigationDrawerMenu()
        self.label = MDNavigationDrawerLabel(text="Navigation")
        self.home_item = MDNavigationDrawerItem(text = "Hub",icon = "home", on_release=lambda x: self.screen_changer.switch_screen("Hub"))
        self.task_item = MDNavigationDrawerItem(text = "Tasks",icon = "note-plus-outline", on_release=lambda x: self.screen_changer.switch_screen("Tasks"))
        self.settings_item = MDNavigationDrawerItem(text = "Settings",icon = "cog", on_release=lambda x: self.screen_changer.switch_screen("Settings"))
        

        self.menu.add_widget(self.label)
        self.menu.add_widget(self.home_item)
        self.menu.add_widget(self.task_item)
        self.menu.add_widget(self.settings_item)
        self.add_widget(self.menu)

    def toggle_sidebar(self, *args):
        if self.state == "open":
            self.set_state("close")
        else:
            self.set_state("open")


        