from sublime_plugin import TextCommand
from json_reindent import parse_input, format_output
import sublime
import logging

logger = logging.getLogger(__name__)

# Use settings only on ST3
SETTINGS_FILE = "JSONReindent.sublime-settings"
settings = {}


class SublimeJsonReindentCommand(TextCommand):

    def run(self, edit, syntax_sensitive=False):
        if self.region_set_empty(self.view.sel()):
            self.parse_region(edit, sublime.Region(0, self.view.size()))
        else:
            region_set = self.view.sel()
            for region in region_set:
                self.parse_region(edit, region)

    def region_set_empty(self, region_set):
        for region in region_set:
            if not region.empty():
                return False
        return True

    def parse_region(self, edit, region):
        content = self.view.substr(region)

        try:
            json_data = parse_input(content)
        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            output = format_output(
                json_data,
                indent=self.view.settings().get("tab_size", 2),
                separators=(",", ": "),
                sort_keys=settings.get("sort_keys") is True,
                ensure_ascii=False
            )
            self.view.replace(
                edit,
                region,
                output
            )


def plugin_loaded():
    global settings
    settings = sublime.load_settings(SETTINGS_FILE)
