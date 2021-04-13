import sublime
import sublime_plugin

class LayoutSetting(sublime_plugin.EventListener):

	def __init__(self):
		self.user_toggled_side_bar = False

	def on_activated(self, view):
		window = view.window()

		if "folder" in view.window().extract_variables() and window.active_panel() is None:
			window.run_command("toggle_terminus_panel")

		if self.user_toggled_side_bar:
			window.set_sidebar_visible(True)

		window.set_minimap_visible(False)

	def on_window_command(self, window, command_name, args):
		if command_name == "toggle_side_bar":
			self.user_toggled_side_bar = True

		return None