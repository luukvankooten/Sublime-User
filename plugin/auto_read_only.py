from fnmatch import fnmatch
import sublime_plugin
import sublime

class AutoReadOnly(sublime_plugin.EventListener):

    PATTERNS = [
        "/Applications/Sublime Text.app/Contents/MacOS/*.py",
        "**/Python.framework/*/lib/*.py",
        "**/.rustup/**.rs",
        "**/.cargo/**.rs",
        "**/node_modules/**.js"
    ]

    def on_load(self, view):
        # window = view.window()
        view_path = view.file_name()

        if self.does_match(view_path):
            view.set_read_only(True)
            view.set_status(str(self), "read-only")

    def does_match(self, path):
        for pattern in self.PATTERNS:
            if fnmatch(path, pattern):
                return True
                break

        return False
