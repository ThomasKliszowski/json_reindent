from sublime_plugin import TextCommand
from sublime import Region
import json

# -----------------------------------------------------------------------------

class JsonReindentCommand(TextCommand):
    def run(self, edit, syntax_sensitive=False):
        print self.region_set_empty(self.view.sel())
        if self.region_set_empty(self.view.sel()):
            self.parse_region(edit, Region(0, self.view.size()))
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
            json_data = json.loads(content)
        except Exception:
            pass
        else:
            self.view.replace(edit, region, json.dumps(json_data, indent=2, sort_keys=True, separators=(',', ': ')))
        
