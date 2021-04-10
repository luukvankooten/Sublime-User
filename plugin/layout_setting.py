import sublime
import sublime_plugin

class LayoutSetting(sublime_plugin.EventListener):

	def on_activated(self, view):
		view.window().set_sidebar_visible(True)