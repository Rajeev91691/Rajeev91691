#!/usr/bin/env python3
"""
Render data/contributions.json as a standalone, high-performance GitHub Streak Card SVG.
Guarantees 100% uptime and 0ms latency served directly from GitHub CDN.
"""
import json
import os

HERE = os.path.dirname(__file__)
IN_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "streak-card.svg")

def render_streak_svg(data):
    current_streak = data["current_streak"]["length"]
    longest_streak = data["longest_streak"]["length"]
    total_contributions = data["total_contributions"]
    
    start_date = data["current_streak"].get("start", "")
    end_date = data["current_streak"].get("end", "")
    longest_start = data["longest_streak"].get("start", "")
    longest_end = data["longest_streak"].get("end", "")
    
    range_start = data["range"]["start"]
    range_end = data["range"]["end"]

    width = 495
    height = 195
    bg_color = "#0a0e14"
    card_bg = "#0d1420"
    border_color = "#1f6feb"
    text_color = "#e6edf3"
    muted_color = "#7d8590"
    accent_color = "#22d3ee"
    fire_color = "#ff5f56"
    gold_color = "#f2cc60"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <style>
    .stat-title {{ font-size: 13px; fill: {muted_color}; font-weight: 500; }}
    .stat-value {{ font-size: 26px; fill: {accent_color}; font-weight: 700; }}
    .stat-sub {{ font-size: 11px; fill: {muted_color}; }}
    .fire {{ font-size: 22px; }}
  </style>
  <rect width="{width}" height="{height}" rx="12" fill="{card_bg}"/>
  <rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="12" fill="none" stroke="{border_color}" stroke-opacity="0.55"/>
  
  <!-- Total Contributions Column -->
  <g transform="translate(40, 45)">
    <text x="0" y="0" class="stat-title">Total Contributions</text>
    <text x="0" y="36" class="stat-value" fill="{text_color}">{total_contributions:,}</text>
    <text x="0" y="58" class="stat-sub">{range_start} - {range_end}</text>
  </g>
  
  <!-- Divider 1 -->
  <line x1="175" y1="35" x2="175" y2="155" stroke="{border_color}" stroke-opacity="0.3"/>
  
  <!-- Current Streak Column -->
  <g transform="translate(200, 45)">
    <text x="0" y="0" class="stat-title">Current Streak 🔥</text>
    <text x="0" y="36" class="stat-value" fill="{fire_color}">{current_streak} <tspan font-size="16" fill="{muted_color}">days</tspan></text>
    <text x="0" y="58" class="stat-sub">{start_date} - {end_date}</text>
  </g>
  
  <!-- Divider 2 -->
  <line x1="335" y1="35" x2="335" y2="155" stroke="{border_color}" stroke-opacity="0.3"/>
  
  <!-- Longest Streak Column -->
  <g transform="translate(355, 45)">
    <text x="0" y="0" class="stat-title">Longest Streak ⚡</text>
    <text x="0" y="36" class="stat-value" fill="{gold_color}">{longest_streak} <tspan font-size="16" fill="{muted_color}">days</tspan></text>
    <text x="0" y="58" class="stat-sub">{longest_start} - {longest_end}</text>
  </g>
</svg>'''
    return svg

if __name__ == "__main__":
    with open(IN_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    svg = render_streak_svg(data)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH} ({len(svg)} bytes)")
