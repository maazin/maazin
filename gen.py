# Generates theme-aware SVG assets for the GitHub profile README.
# Re-run after editing any copy below.

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"

THEMES = {
    "dark":  dict(bg="#0D1117", fg="#F0F6FC", muted="#8B949E", faint="#6E7681",
                  line="#21262D", chip="#161B22", chipline="#30363D", accent="#58A6FF"),
    "light": dict(bg="#FFFFFF", fg="#1F2328", muted="#59636E", faint="#818B98",
                  line="#D1D9E0", chip="#F6F8FA", chipline="#D1D9E0", accent="#0969DA"),
}

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------------------------------------------------------- hero
STATS = [("12%", "app CTR lift", "Publix, 500K+ txns"),
         ("800+", "students served", "RAG assistant"),
         ("45%", "faster solver", "18.3ms to 10.0ms")]

def hero(t):
    c = THEMES[t]
    W, H = 1280, 400
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-label="Maazin Shaikh, Software Engineer and AI/ML Engineer">']
    o.append(f'''<defs>
  <radialGradient id="glow" cx="50%" cy="0%" r="72%">
    <stop offset="0%" stop-color="{c["accent"]}" stop-opacity="{0.13 if t=="dark" else 0.09}"/>
    <stop offset="100%" stop-color="{c["accent"]}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{c["line"]}" stop-opacity="0"/>
    <stop offset="50%" stop-color="{c["accent"]}" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="{c["line"]}" stop-opacity="0"/>
  </linearGradient>
</defs>''')
    o.append(f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')

    cx = W / 2
    o.append(f'<text x="{cx}" y="128" text-anchor="middle" font-family="{MONO}" font-size="13" '
             f'letter-spacing="4.5" fill="{c["accent"]}" fill-opacity="0.9">SOFTWARE · AI/ML · DATA</text>')
    o.append(f'<text x="{cx}" y="205" text-anchor="middle" font-family="{FONT}" font-size="68" '
             f'font-weight="600" letter-spacing="-1.8" fill="{c["fg"]}">Maazin Shaikh</text>')
    o.append(f'<text x="{cx}" y="243" text-anchor="middle" font-family="{FONT}" font-size="19" '
             f'fill="{c["muted"]}">I build ML and LLM systems that reach real users.</text>')
    o.append(f'<rect x="{cx-230}" y="278" width="460" height="1" fill="url(#rule)"/>')

    span = 372
    for i, (big, lab, sub) in enumerate(STATS):
        x = cx + (i - 1) * span
        o.append(f'<text x="{x}" y="333" text-anchor="middle" font-family="{FONT}" font-size="34" '
                 f'font-weight="600" letter-spacing="-0.8" fill="{c["fg"]}">{esc(big)}</text>')
        o.append(f'<text x="{x}" y="356" text-anchor="middle" font-family="{FONT}" font-size="14" '
                 f'fill="{c["muted"]}">{esc(lab)}</text>')
        o.append(f'<text x="{x}" y="375" text-anchor="middle" font-family="{MONO}" font-size="11.5" '
                 f'fill="{c["faint"]}">{esc(sub)}</text>')
        if i < len(STATS) - 1:
            o.append(f'<rect x="{x + span/2}" y="316" width="1" height="52" fill="{c["line"]}"/>')
    o.append('</svg>')
    return "\n".join(o)

# --------------------------------------------------------------- stack
GROUPS = [
  ("Languages",      ["Python","Go","TypeScript","SQL","Java","C++","C#","R","Bash"]),
  ("AI & ML",        ["LangGraph","LangChain","RAG","MCP","PyTorch","Hugging Face","scikit-learn","PySpark","Databricks"]),
  ("Backend",        ["FastAPI","Flask","Node.js","PostgreSQL","pgvector","Redis","MongoDB","REST","SSE"]),
  ("Frontend",       ["React","Next.js","SvelteKit","Tailwind","Vite"]),
  ("Infrastructure", ["Docker","GitHub Actions","AWS","Azure","GCP","Fly.io","Vercel"]),
]

def stack(t):
    c = THEMES[t]
    W = 1280
    PAD, LABW, ROWH, CH, GAP = 44, 168, 52, 30, 9
    H = PAD * 2 + ROWH * len(GROUPS) - (ROWH - CH) + 8
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-label="Technology stack">']
    o.append(f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>')
    y = PAD
    for gi, (label, items) in enumerate(GROUPS):
        o.append(f'<text x="{PAD}" y="{y + CH/2 + 4.5}" font-family="{MONO}" font-size="12" '
                 f'letter-spacing="1.6" fill="{c["faint"]}">{esc(label.upper())}</text>')
        x = PAD + LABW
        for it in items:
            w = len(it) * 7.35 + 26
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{CH}" rx="{CH/2}" '
                     f'fill="{c["chip"]}" stroke="{c["chipline"]}" stroke-width="1"/>')
            o.append(f'<text x="{x + w/2:.1f}" y="{y + CH/2 + 4.5}" text-anchor="middle" '
                     f'font-family="{FONT}" font-size="13.5" fill="{c["fg"]}">{esc(it)}</text>')
            x += w + GAP
        if gi < len(GROUPS) - 1:
            o.append(f'<rect x="{PAD}" y="{y + CH + (ROWH-CH)/2 - 0.5}" width="{W-2*PAD}" height="1" '
                     f'fill="{c["line"]}" fill-opacity="0.7"/>')
        y += ROWH
    o.append('</svg>')
    return "\n".join(o)

for t in THEMES:
    open(f"hero-{t}.svg", "w").write(hero(t))
    open(f"stack-{t}.svg", "w").write(stack(t))
print("generated")
