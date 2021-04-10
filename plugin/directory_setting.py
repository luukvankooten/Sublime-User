import sublime
import sublime_plugin

class DirectorySetting(sublime_plugin.EventListener):

	def on_activated(self, view):
		view.window().set_sidebar_visible(True)