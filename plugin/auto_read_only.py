from fnmatch import fnmatch
import sublime_plugin

class AutoReadOnly(sublime_plugin.EventListener):

    PATTERNS = [
        "/Applications/Sublime Text.app/Contents/MacOS/*.py",
        "*/Python.framework/*/lib/*.py",
        "*/.cargo/**.rs"
    ]

    def on_load_async(self, view):
        window = view.window();
        view_path = view.file_name()
        for pattern in self.PATTERNS:
            if fnmatch(view_path, pattern):
                view.set_read_only(True)
                view.set_status(str(self), "read-only")
                print(
                    "[{0}] {1!r} matched pattern {2!r}".format(
                        self.__class__.__name__, view_path, pattern
                    )
                )
                break