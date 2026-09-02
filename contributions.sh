#!/usr/bin/env bash
set -e

# Fetch latest contributions from GitHub and re-render SVG artifacts
echo "Fetching GitHub contributions for Rajeev91691..."
python3 scripts/fetch_contributions.py 2>/dev/null || python scripts/fetch_contributions.py

echo "Rendering contribution heatmap SVG..."
python3 scripts/render_heatmap_svg.py 2>/dev/null || python scripts/render_heatmap_svg.py

echo "Rendering streak card SVG..."
python3 scripts/render_streak_svg.py 2>/dev/null || python scripts/render_streak_svg.py

echo "Done! Heatmap and streak card updated."
