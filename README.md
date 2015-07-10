JSONReindent
============

Sublime Text 2/3 Plugin - JSON Reindent: reindent file or selection


Usage
-----

Open your Sublime Text command palette (**Ctrl+Shift+P**) and type "**JSON Reindent**".

This will reindent your whole file, or your selection if exists.

The error output is in your Sublime Text Console.


Logs
----

- 1.1.1: Fix non-ascii bug.
- 1.1.0: Disable sorting by default, add a settings file to enable it (see Settings > JSON Reindent > Settings - Default) only on ST3.
- 1.0.1: JSON Reindent now uses  users's tab_size instead of 2 spaces to indent json
- 1.0: Enable user to reindent current file or selection (single or multiple), silent if it can't
