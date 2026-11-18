"""Gera a thumbnail de uma página para a vitrine.

Uso:  python make_thumb.py <nome> <url>
Ex.:  python make_thumb.py meu-app https://wallyboy22.github.io/meu-app/
Cria thumbs/<nome>.webp (640x400). Depois, adicione  thumb: "thumbs/<nome>.webp"  ao item no index.html.
"""
import os, subprocess, sys, tempfile
from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

name, url = sys.argv[1], sys.argv[2]
tmp = os.path.join(tempfile.gettempdir(), f"thumb_{name}.png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--window-size=1280,800", "--virtual-time-budget=15000",
                f"--screenshot={tmp}", url], capture_output=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thumbs", f"{name}.webp")
Image.open(tmp).convert("RGB").resize((640, 400), Image.LANCZOS).save(out, quality=80)
os.remove(tmp)
print("ok:", out)
