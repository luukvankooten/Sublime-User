import sublime
import sublime_plugin

class LayoutSetting(sublime_plugin.EventListener):
	def on_new_window_async(self, window):
		settings = window.settings()

		if "folder" in view.window().extract_variables() and window.active_panel() is None and settings.get("user_toggled_panel", False) is False:
			window.run_command("toggle_terminus_panel")

		if settings.get("user_toggled_side_bar", False) is False:
			window.set_sidebar_visible(True)

		window.set_minimap_visible(False)

	def on_window_command(self, window, command_name, args):
		settings = window.settings()
		
		if command_name == "hide_panel":
			settings.set("user_toggled_panel", True)

		if command_name == "toggle_side_bar":
			settings.set("user_toggled_side_bar", True)

		return None