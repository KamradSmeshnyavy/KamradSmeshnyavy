#!/usr/bin/env python3
"""Generates animated SVG assets for the Phrack-style profile README.

Usage: python3 scripts/gen-assets.py [out_dir]   (default: <repo>/assets)
"""
import random
import sys
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"
# Rosé Pine — https://rosepinetheme.com/palette
BG = "#191724"       # base
WIN = "#1f1d2e"      # surface
OVERLAY = "#26233a"  # overlay
MUTED = "#6e6a86"    # muted
TEXT = "#e0def4"     # text
LOVE = "#eb6f92"     # love
GOLD = "#f6c177"     # gold
ROSE = "#ebbcba"     # rose
PINE = "#31748f"     # pine
FOAM = "#9ccfd8"     # foam
IRIS = "#c4a7e7"     # iris

random.seed(0x1337)


def write(name, body):
    (OUT / name).write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", OUT / name)


def p(x):
    return f"{max(0.0, min(100.0, x)):.2f}%"


GLOW = """
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%">
  <feGaussianBlur stdDeviation="2.2" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>"""

SCAN = """
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
  <rect width="4" height="2" fill="#000" fill-opacity="0.35"/>
</pattern>"""


def spans(segs):
    """segs: list of (text, color[, extra attrs]) -> tspans"""
    out = []
    for s in segs:
        text, color = s[0], s[1]
        extra = s[2] if len(s) > 2 else ""
        out.append(f'<tspan fill="{color}" {extra}>{escape(text)}</tspan>')
    return "".join(out)


# --------------------------------------------------------------------------- #
# banner.svg
# --------------------------------------------------------------------------- #
LOGO = [
    "██╗  ██╗ █████╗ ███╗   ███╗██████╗  █████╗ ██████╗ ",
    "██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗",
    "█████╔╝ ███████║██╔████╔██║██████╔╝███████║██║  ██║",
    "██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║██║  ██║",
    "██║  ██╗██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝",
    "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ",
]


def banner():
    W, H = 1000, 320
    hexchars = "0123456789abcdef"
    rain = []
    for i in range(45):
        x = 14 + i * 22
        n = 22
        chars = "".join(random.choice(hexchars) for _ in range(n))
        ts = "".join(
            f'<tspan x="{x}" dy="16" fill-opacity="{0.12 + 0.88 * k / n:.2f}">{c}</tspan>'
            for k, c in enumerate(chars)
        )
        dur = random.uniform(7, 16)
        begin = -random.uniform(0, dur)
        op = random.uniform(0.10, 0.30)
        rain.append(
            f'<text y="0" opacity="{op:.2f}">{ts}'
            f'<animateTransform attributeName="transform" type="translate" '
            f'from="0 -380" to="0 {H}" dur="{dur:.2f}s" begin="{begin:.2f}s" '
            f'repeatCount="indefinite"/></text>'
        )

    logo = "".join(
        f'<text x="500" y="{106 + i * 22}" text-anchor="middle" textLength="640" '
        f'lengthAdjust="spacingAndGlyphs">{escape(l)}</text>'
        for i, l in enumerate(LOGO)
    )

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="KAMRAD — Phrack-style banner">
<defs>
  {GLOW}
  {SCAN}
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  <radialGradient id="vig" cx="50%" cy="50%" r="65%">
    <stop offset="0" stop-color="{BG}" stop-opacity="0.92"/>
    <stop offset="0.55" stop-color="{BG}" stop-opacity="0.55"/>
    <stop offset="1" stop-color="{BG}" stop-opacity="0.15"/>
  </radialGradient>
  <linearGradient id="logoG" gradientUnits="userSpaceOnUse" x1="180" y1="0" x2="820" y2="0">
    <stop offset="0" stop-color="{LOVE}"/>
    <stop offset="0.5" stop-color="{IRIS}"/>
    <stop offset="1" stop-color="{FOAM}"/>
  </linearGradient>
  <linearGradient id="band" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{IRIS}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{IRIS}" stop-opacity="0.07"/>
    <stop offset="1" stop-color="{IRIS}" stop-opacity="0"/>
  </linearGradient>
  <g id="logo">{logo}</g>
  <clipPath id="slice">
    <rect x="0" y="0" width="{W}" height="9">
      <animate attributeName="y" dur="5s" repeatCount="indefinite" calcMode="discrete"
        values="120;120;150;112;176;133;195;120" keyTimes="0;0.88;0.9;0.915;0.93;0.945;0.96;1"/>
      <animate attributeName="height" dur="5s" repeatCount="indefinite" calcMode="discrete"
        values="9;9;14;6;10;18;7;9" keyTimes="0;0.88;0.9;0.915;0.93;0.945;0.96;1"/>
    </rect>
  </clipPath>
  <style>
    text {{ font-family: {FONT}; white-space: pre; font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; }}
    .crt {{ animation: flick 7s infinite; }}
    @keyframes flick {{ 0%,100% {{opacity:1}} 41% {{opacity:1}} 42% {{opacity:.86}} 43% {{opacity:1}} 77% {{opacity:.93}} 78% {{opacity:1}} }}
    .gr {{ animation: gr 5s infinite steps(1); mix-blend-mode: screen; }}
    .gc {{ animation: gc 5s infinite steps(1); mix-blend-mode: screen; }}
    .gs {{ animation: gs 5s infinite steps(1); }}
    @keyframes gr {{ 0%,88%,97%,100% {{transform:translate(0,0);opacity:0}} 89% {{transform:translate(-6px,1px);opacity:.85}} 91% {{transform:translate(4px,-2px);opacity:.7}} 93% {{transform:translate(-3px,0);opacity:.85}} 95% {{transform:translate(2px,1px);opacity:.5}} }}
    @keyframes gc {{ 0%,88%,97%,100% {{transform:translate(0,0);opacity:0}} 89% {{transform:translate(6px,-1px);opacity:.85}} 91% {{transform:translate(-4px,2px);opacity:.7}} 93% {{transform:translate(3px,0);opacity:.85}} 95% {{transform:translate(-2px,-1px);opacity:.5}} }}
    @keyframes gs {{ 0%,88%,97%,100% {{opacity:0}} 89%,96% {{opacity:1}} }}
    .cur {{ animation: blink 1s infinite steps(1); }}
    @keyframes blink {{ 0%,100% {{opacity:1}} 50% {{opacity:0}} }}
    .band {{ animation: band 6s linear infinite; }}
    @keyframes band {{ from {{transform:translateY(-120px)}} to {{transform:translateY({H}px)}} }}
  </style>
</defs>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g font-size="13" fill="{IRIS}">{"".join(rain)}</g>
  <rect width="{W}" height="{H}" fill="url(#vig)"/>
  <g class="crt">
    <text x="500" y="40" text-anchor="middle" font-size="15" fill="{TEXT}" letter-spacing="1">==Phrack Inc.==</text>
    <text x="500" y="63" text-anchor="middle" font-size="12.5" fill="{GOLD}" fill-opacity="0.9">Volume 0x45, Issue 0x01, Phile #0x01 of 0x07</text>

    <g font-size="22" font-weight="700">
      <use href="#logo" class="gr" fill="{LOVE}"/>
      <use href="#logo" class="gc" fill="{FOAM}"/>
      <use href="#logo" fill="url(#logoG)" filter="url(#glow)"/>
      <g clip-path="url(#slice)" class="gs"><use href="#logo" fill="{TEXT}" transform="translate(14 0)"/></g>
    </g>

    <text x="500" y="256" text-anchor="middle" font-size="15" fill="{TEXT}" letter-spacing="1.5">malware research <tspan fill="{IRIS}">·</tspan> reverse engineering <tspan fill="{IRIS}">·</tspan> low-level dev<tspan class="cur" fill="{IRIS}"> █</tspan></text>

    <text x="28" y="300" font-size="12" fill="{FOAM}">[+] uid=1337(kamrad) gid=0x41(reversers)</text>
    <text x="972" y="300" text-anchor="end" font-size="12" fill="{MUTED}">ELF 64-bit LSB · x86-64 · not stripped</text>
  </g>
  <rect class="band" width="{W}" height="120" fill="url(#band)"/>
  <rect width="{W}" height="{H}" fill="url(#scan)" opacity="0.5"/>
</g>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{IRIS}" stroke-opacity="0.35" stroke-width="1.5"/>
</svg>
"""


# --------------------------------------------------------------------------- #
# Section headers:  |=----=[ 0x01 :: Title ]=----=|
# --------------------------------------------------------------------------- #
SECTIONS = [
    ("0x01", "Introduction"),
    ("0x02", "Arsenal"),
    ("0x03", "Recon"),
    ("0x04", "Disassembly of self"),
    ("0x05", "Telemetry"),
    ("0x06", "Greetz"),
]


def section(num, title):
    W, H = 1000, 56
    total = 96
    inner = len(f"[ {num} :: {title} ]")
    side = (total - 4 - inner)
    left, right = side // 2, side - side // 2
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{num} {escape(title)}">
<defs>
  {GLOW}
  <linearGradient id="sweep" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="0" y2="0">
    <stop offset="0" stop-color="{MUTED}"/>
    <stop offset="0.5" stop-color="{IRIS}"/>
    <stop offset="1" stop-color="{MUTED}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{W + 260} 0" dur="4.5s" repeatCount="indefinite"/>
  </linearGradient>
  <style>
    text {{ font-family: {FONT}; white-space: pre; font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; }}
    .cur {{ animation: blink 1.1s infinite steps(1); }}
    @keyframes blink {{ 0%,100% {{opacity:1}} 50% {{opacity:0}} }}
  </style>
</defs>
<rect width="{W}" height="{H}" rx="10" fill="{BG}"/>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="10" fill="none" stroke="{IRIS}" stroke-opacity="0.18"/>
<text x="500" y="33" text-anchor="middle" font-size="14">{spans([
        ("|=" + "-" * left + "=", "url(#sweep)"),
        ("[ ", IRIS),
        (num, GOLD, 'font-weight="700"'),
        (" :: ", FOAM),
        (title, IRIS, 'font-weight="700"'),
        (" ]", IRIS),
        ("=" + "-" * right + "=|", "url(#sweep)"),
    ])}</text>
</svg>
"""


# --------------------------------------------------------------------------- #
# Sequenced terminal-like window helpers
# --------------------------------------------------------------------------- #
def window(W, H, title, body, css, extra_defs=""):
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
<defs>
  {GLOW}
  {SCAN}
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="12"/></clipPath>
  {extra_defs}
  <style>
    text {{ font-family: {FONT}; white-space: pre; font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; }}
    .cur {{ animation: blink 1s infinite steps(1); }}
    @keyframes blink {{ 0%,100% {{opacity:1}} 50% {{opacity:0}} }}
    {css}
  </style>
</defs>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="{WIN}"/>
  <rect width="{W}" height="36" fill="{OVERLAY}"/>
  <rect y="36" width="{W}" height="1" fill="{IRIS}" fill-opacity="0.18"/>
  <circle cx="22" cy="18" r="6" fill="{LOVE}"/>
  <circle cx="42" cy="18" r="6" fill="{GOLD}"/>
  <circle cx="62" cy="18" r="6" fill="{FOAM}"/>
  <text x="{W / 2}" y="23" text-anchor="middle" font-size="12.5" fill="{MUTED}">{escape(title)}</text>
  {body}
  <rect width="{W}" height="{H}" fill="url(#scan)" opacity="0.35"/>
</g>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="12" fill="none" stroke="{IRIS}" stroke-opacity="0.3" stroke-width="1.5"/>
</svg>
"""


def sequence(lines, T, x0, y0, lh, fs, cw, bg):
    """lines: list of dict(segs, at, typed(bool), prefix_len).
    Every line fades in at `at` seconds; typed lines additionally reveal
    characters after the prompt one by one. Everything resets at end of T."""
    css, body = [], []
    for i, ln in enumerate(lines):
        y = y0 + i * lh
        at = ln["at"]
        start = at / T * 100
        css.append(
            f".l{i}{{animation:l{i} {T}s linear infinite}}"
            f"@keyframes l{i}{{0%,{p(start)}{{opacity:0}}{p(start + 0.05)},95%{{opacity:1}}98%,100%{{opacity:0}}}}"
        )
        body.append(f'<text class="l{i}" x="{x0}" y="{y}" font-size="{fs}">{spans(ln["segs"])}</text>')
        if ln.get("typed"):
            pre = ln.get("prefix_len", 0)
            n = sum(len(s[0]) for s in ln["segs"]) - pre
            dur = n * 0.055
            end = (at + dur) / T * 100
            cx = x0 + pre * cw
            width = n * cw + 14
            css.append(
                f".c{i}{{animation:c{i} {T}s linear infinite}}"
                f"@keyframes c{i}{{0%,{p(start)}{{transform:translateX(0);animation-timing-function:steps({n},end)}}"
                f"{p(end)}{{transform:translateX({width - 14:.1f}px);opacity:1}}"
                f"{p(end + 0.6 / T * 100)},100%{{transform:translateX({width - 14:.1f}px);opacity:0}}}}"
            )
            body.append(
                f'<g class="c{i}"><rect x="{cx}" y="{y - fs}" width="{width + 4:.1f}" height="{lh}" fill="{bg}"/>'
                f'<rect x="{cx}" y="{y - fs + 3}" width="{cw:.1f}" height="{fs + 1}" fill="{IRIS}" opacity="0.85"/></g>'
            )
    return "\n  ".join(body), "\n    ".join(css)


# --------------------------------------------------------------------------- #
# recon.svg — static analysis of ./kamrad + neofetch-style card
# --------------------------------------------------------------------------- #
def recon():
    W, H = 900, 480
    T = 16.0
    prompt = [("kamrad", IRIS, 'font-weight="700"'), ("@", MUTED), ("lab", FOAM), (" ~ ", TEXT), ("$ ", IRIS)]
    plen = sum(len(s[0]) for s in prompt)

    def cmd(text, at):
        return {"segs": prompt + [(text, TEXT)], "at": at, "typed": True, "prefix_len": plen}

    def out(segs, at):
        return {"segs": segs, "at": at}

    def kv(k, v, at, vc=TEXT):
        return out([("  ", TEXT), (f"{k:<9}", GOLD), (v, vc)], at)

    t = 0.4
    lines = [cmd("file ./kamrad", t)]
    t += 1.2
    lines.append(out([("./kamrad: ", TEXT), ("ELF 64-bit LSB pie executable", IRIS), (", x86-64, dynamically linked, not stripped", TEXT)], t))
    t += 0.6
    lines.append(cmd("checksec --file=./kamrad", t))
    t += 1.7
    lines.append(out([("  RELRO ", MUTED), ("Full", IRIS), ("   Canary ", MUTED), ("found", IRIS),
                      ("   NX ", MUTED), ("enabled", IRIS), ("   PIE ", MUTED), ("enabled", IRIS),
                      ("   Symbols ", MUTED), ("yes", GOLD)], t))
    t += 0.6
    lines.append(cmd("./kamrad --info", t))
    t += 1.3
    info = [
        ("user", "kamrad smeshnyavy", TEXT),
        ("role", "malware researcher · reverse engineer · low-level dev", IRIS),
        ("os", "GNU/Linux — Arch · Debian · NixOS", TEXT),
        ("shell", "nushell", TEXT),
        ("editor", "neovim", TEXT),
        ("langs", "C · C++ · Rust · Python · x86-64 · ARM64 · AVR asm", TEXT),
        ("tools", "IDA · Ghidra · radare2 · gdb · x64dbg · Wireshark", TEXT),
        ("focus", "unpacking · anti-debug · YARA · linux internals", TEXT),
    ]
    lines.append(out([("  " + "─" * 66, MUTED)], t))
    for k, v, c in info:
        t += 0.18
        lines.append(kv(k, v, t, c))
    t += 0.18
    lines.append(out([("  " + "─" * 66, MUTED)], t))
    t += 0.18
    lines.append(out([("  ", TEXT), ("███", LOVE), ("███", GOLD), ("███", ROSE), ("███", PINE),
                      ("███", FOAM), ("███", IRIS), ("███", TEXT)], t))
    t += 0.5
    lines.append({"segs": prompt + [("█", IRIS, 'class="cur"')], "at": t})

    body, css = sequence(lines, T, 24, 66, 22.5, 14, 8.43, WIN)
    return window(W, H, "kamrad@lab: ~ — nu", body, css)


# --------------------------------------------------------------------------- #
# disasm.svg — radare2-style listing with a stepping debugger cursor
# --------------------------------------------------------------------------- #
def disasm():
    W, H = 900, 520
    fs, lh, x0, y0 = 13, 22, 22, 70

    def ins(addr, byts, mn, ops, cmt="", arrow="           ", mc=TEXT):
        segs = [("│", MUTED), (arrow, GOLD), (f"0x{addr:08x}", FOAM), ("  ", TEXT),
                (f"{byts:<15}", MUTED), (f"{mn:<6}", mc, 'font-weight="700"'), (f"{ops:<26}", TEXT)]
        if cmt:
            segs.append(("; " + cmt, GOLD if cmt.startswith('"') else MUTED))
        return segs

    rows = [
        [("[0x00401136]> ", IRIS), ("pdf @ sym.main", TEXT)],
        [("┌ ", MUTED), ("148: ", MUTED), ("int ", FOAM), ("main", IRIS, 'font-weight="700"'), (" (int argc, char **argv);", TEXT)],
        [("│          ", MUTED), ("; var int64_t curiosity @ rbp-0x8", MUTED)],
        ins(0x401136, "55", "push", "rbp", mc=LOVE),
        ins(0x401137, "4889e5", "mov", "rbp, rsp"),
        ins(0x40113A, "488d3dc30e00.", "lea", "rdi, str.langs", '"C · C++ · Rust · Python"'),
        ins(0x401141, "e8eafeffff", "call", "sym.learn", mc=IRIS),
        ins(0x401146, "488d3dd20e00.", "lea", "rdi, str.asm", '"x86-64 · ARM64 · AVR"'),
        ins(0x40114D, "e8defeffff", "call", "sym.learn", mc=IRIS),
        ins(0x401152, "488d3de50e00.", "lea", "rdi, str.re", '"IDA · Ghidra · radare2"'),
        ins(0x401159, "e8b2feffff", "call", "sym.reverse", mc=IRIS),
        ins(0x40115E, "488d3df80e00.", "lea", "rdi, str.mal", '"unpack · YARA · IOCs"'),
        ins(0x401165, "e8a6feffff", "call", "sym.analyze", mc=IRIS),
        ins(0x40116A, "e8c1feffff", "call", "sym.read_phrack", arrow="      ┌──> ", mc=IRIS),
        ins(0x40116F, "85c0", "test", "eax, eax", arrow="      ╎    "),
        ins(0x401171, "75f7", "jne", "0x40116a", "never stop learning", arrow="      └──< ", mc=GOLD),
        ins(0x401173, "31c0", "xor", "eax, eax"),
        ins(0x401175, "c9", "leave", "", mc=LOVE),
        [("└", MUTED)] + ins(0x401176, "c3", "ret", "", mc=LOVE)[1:],
    ]

    # appear quickly, then a debugger "current instruction" bar steps through
    T = 15.0
    lines = [{"segs": r, "at": 0.25 + i * 0.09} for i, r in enumerate(rows)]
    lines[0]["typed"] = True
    lines[0]["prefix_len"] = 14
    body, css = sequence(lines, T, x0, y0, lh, fs, 7.83, WIN)

    first = 3  # row index of first instruction
    path = list(range(3, 16)) + [13, 14, 15] * 2 + [16, 17, 18]
    step = 0.42
    start = 2.6
    kf = [f"0%,{p(start / T * 100)}{{transform:translateY(0);opacity:0}}"]
    for k, r in enumerate(path):
        tt = (start + k * step) / T * 100
        kf.append(f"{p(tt + 0.01)}{{transform:translateY({(r - first) * lh}px);opacity:1}}")
    end = (start + len(path) * step) / T * 100
    kf.append(f"{p(end)},100%{{transform:translateY({(path[-1] - first) * lh}px);opacity:0}}")
    css += f"\n    .pc{{animation:pc {T}s infinite step-end}}@keyframes pc{{{''.join(kf)}}}"
    bar_y = y0 + first * lh - fs - 3
    bar = (
        f'<g class="pc"><rect x="10" y="{bar_y}" width="{W - 20}" height="{lh - 1}" rx="3" fill="{IRIS}" fill-opacity="0.12"/>'
        f'<rect x="10" y="{bar_y}" width="3" height="{lh - 1}" fill="{IRIS}"/>'
        f'<text x="{W - 26}" y="{bar_y + fs + 2}" text-anchor="end" font-size="11" fill="{IRIS}">◀ rip</text></g>'
    )

    # status line under the listing
    status_y = y0 + len(rows) * lh + 14
    status = (
        f'<text x="{x0}" y="{status_y}" font-size="12" fill="{MUTED}">'
        f'<tspan fill="{IRIS}">[0x00401136]</tspan> 19 instructions · 0 bugs found · ∞ iterations</text>'
    )
    return window(W, H, "r2 -A ./kamrad", bar + "\n  " + body + "\n  " + status, css)


# --------------------------------------------------------------------------- #
# footer.svg
# --------------------------------------------------------------------------- #
def footer():
    W, H = 1000, 170
    bar = "|=" + "-" * 41 + "=[ EOF ]=" + "-" * 42 + "=|"
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="EOF">
<defs>
  {GLOW}
  <linearGradient id="sweep" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
    <stop offset="0" stop-color="{MUTED}"/>
    <stop offset="0.5" stop-color="{IRIS}"/>
    <stop offset="1" stop-color="{MUTED}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{W + 300} 0" dur="5s" repeatCount="indefinite"/>
  </linearGradient>
  <style>
    text {{ font-family: {FONT}; white-space: pre; font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; }}
    .cur {{ animation: blink 1s infinite steps(1); }}
    @keyframes blink {{ 0%,100% {{opacity:1}} 50% {{opacity:0}} }}
    .breathe {{ animation: br 4s ease-in-out infinite; }}
    @keyframes br {{ 0%,100% {{opacity:.55}} 50% {{opacity:1}} }}
  </style>
</defs>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{IRIS}" stroke-opacity="0.3" stroke-width="1.5"/>
<text x="500" y="40" text-anchor="middle" font-size="14" fill="url(#sweep)">{escape(bar)}</text>
<text x="500" y="82" text-anchor="middle" font-size="13" fill="{FOAM}"><tspan fill="{GOLD}">--[ greetz</tspan>  phrack staff · the mentor · aleph one · liveoverflow · pwn.college · ctftime</text>
<text x="500" y="112" text-anchor="middle" font-size="13" fill="{MUTED}" class="breathe">"This is our world now... the world of the electron and the switch."</text>
<text x="500" y="146" text-anchor="middle" font-size="13" fill="{TEXT}"><tspan fill="{IRIS}">kamrad@lab ~ $</tspan> exit<tspan class="cur" fill="{IRIS}"> █</tspan></text>
</svg>
"""


write("banner.svg", banner())
for n, t in SECTIONS:
    write(f"section-{n}.svg", section(n, t))
write("recon.svg", recon())
write("disasm.svg", disasm())
write("footer.svg", footer())
