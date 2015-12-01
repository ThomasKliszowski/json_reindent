# JSONReindent

[![Build Status](https://travis-ci.org/ThomasKliszowski/json_reindent.svg?branch=master)](https://travis-ci.org/ThomasKliszowski/json_reindent)
[![Coverage Status](https://coveralls.io/repos/ThomasKliszowski/json_reindent/badge.svg?branch=master&service=github)](https://coveralls.io/github/ThomasKliszowski/json_reindent?branch=master)

## Description

Sublime Text 2/3 Plugin - JSON Reindent: reindent file or selection


## Usage

Open your Sublime Text command palette (**Ctrl+Shift+P**) and type "**JSON Reindent**".

This will reindent your whole file, or your selection if exists.

The error output is in your Sublime Text Console.


## Logs

- **2.0.0**: Use PyYAML to parse user input because YAML is a superset of JSON. This way, the script is less restrictive than the use of the JSON parser, ie: the plugin is able to parse a JSON with trailing commas. In addition to that, you can parse a YAML file and format it to JSON by using this plugin.
- **1.1.1**: Fix non-ascii bug.
- **1.1.0**: Disable sorting by default, add a settings file to enable it (see Settings > JSON Reindent > Settings - Default) only on ST3.
- **1.0.1**: JSON Reindent now uses  users's tab_size instead of 2 spaces to indent json
- **1.0**: Enable user to reindent current file or selection (single or multiple), silent if it can't
