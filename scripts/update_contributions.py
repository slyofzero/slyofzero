#!/usr/bin/env python3
"""
update_contributions.py
Fetches live contribution data for slyofzero from ghchart and transforms 
0-commit squares into the Dark Slate (#24292F / #2E343B) palette.
"""
import urllib.request
import os

USERNAME = "slyofzero"
ACCENT_HEX = "e07a5f"
URL = f"https://ghchart.rshah.org/{ACCENT_HEX}/{USERNAME}"

def update():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        svg = resp.read().decode("utf-8")

    # Replace #EEEEEE (white zero-commit squares) with dark slate/blackish #24292F and subtle #2E343B border
    svg = svg.replace("fill:#EEEEEE", "fill:#24292F;stroke:#2E343B;stroke-width:0.6")
    
    # Replace label colors with warm stone #9E998F
    svg = svg.replace("fill:#767676", "fill:#9E998F")
    svg = svg.replace('fill="#767676"', 'fill="#9E998F"')

    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "github-contributions.svg")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated {out_path} successfully.")

if __name__ == "__main__":
    update()
