from sublime_plugin import TextCommand
import sublime
import collections
import json
import logging

logger = logging.getLogger(__name__)

# Use settings only on ST3
SETTINGS_FILE = "JSONReindent.sublime-settings"
settings = {}


class JsonReindentCommand(TextCommand):

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

        # Use OrderedDict if exists
        params = {}
        if hasattr(collections, 'OrderedDict'):
            params['object_pairs_hook'] = collections.OrderedDict

        try:
            json_data = json.loads(
                content,
                strict=settings.get('strict') is True,
                **params)
        except Exception as e:
            logger.error(e, exc_info=True)
        else:
            self.view.replace(
                edit,
                region,
                json.dumps(
                    json_data,
                    indent=self.view.settings().get("tab_size", 2),
                    separators=(',', ': '),
                    sort_keys=settings.get('sort_keys') is True,
                    ensure_ascii=False
                )
            )


def plugin_loaded():
    global settings
    settings = sublime.load_settings(SETTINGS_FILE)
