#!/bin/bash
# Shortcut — runs the pottery update script from the pottery/ folder
exec "$(dirname "$0")/pottery/update-pottery.sh" "$@"
