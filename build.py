# -*- coding: utf-8 -*-
# 用 data.py 生成单文件 index.html（零外部依赖）
import html, urllib.parse, pathlib
from data import CITIES, SOURCES
E = html.escape

def maps(name, addr):
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(f"{name}, {addr}")

def badge(label, ok, note):
    cls = {True: "ok", False: "no", None: "mix"}[ok]
    mark = {True: "✓", False: "—", None: "有分歧"}[ok]
    return f'<span class="bd {cls}" title="{E(note)}"><b>{label}</b> {mark}</span>'

def pick(i, p):
    zh = f'<span class="pz">{E(p["zh"])}</span>' if p.get("zh") else ""
    why = "".join(f"<li>{E(w)}</li>" for w in p["why"])
    phone = f'<a class="btn ghost" href="tel:{E(p["phone"])}">打电话</a>' if p.get("phone") else ""
    tip = f'<p class="tip">{E(p["tip"])}</p>' if p.get("tip") else ""
    return f'''<article class="pick">
  <div class="ph"><span class="rk">{i}</span><div><h4>{E(p["name"])}</h4>{zh}</div><span class="area">{E(p["area"])}</span></div>
  <div class="bds">{badge("英文榜单", p["en_ok"], p["en_note"])}{badge("小红书", p["xhs_ok"], p["xhs_note"])}</div>
  <p class="bdn">英文侧：{E(p["en_note"])}；小红书：{E(p["xhs_note"])}</p>
  <ul class="why">{why}</ul>
  <dl><dt>点什么</dt><dd>{E(p["order"])}</dd><dt>时间</dt><dd>{E(p["hours"])}</dd><dt>地址</dt><dd>{E(p["addr"])}</dd></dl>
  {tip}
  <div class="acts"><a class="btn" href="{E(maps(p["name"], p["addr"]))}" target="_blank" rel="noopener">导航</a>{phone}</div>
</article>'''

def dish(d):
    warn = f'<p class="warn">{E(d["warn"])}</p>' if d.get("warn") else ""
    aside = f'<p class="aside">{E(d["aside"])}</p>' if d.get("aside") else ""
    avoid = f'<p class="avoid">{E(d["avoid"])}</p>' if d.get("avoid") else ""
    picks = "".join(pick(i + 1, p) for i, p in enumerate(d["picks"]))
    return f'''<section class="dish" id="{d["id"]}">
  <h3>{E(d["name"])} <small>{E(d["en"])}</small></h3>
  <p class="lead">{E(d["lead"])}</p>{warn}
  {picks}{aside}{avoid}
</section>'''

def city(c):
    out = []
    for g in c["groups"]:
        chips = "".join(f'<a href="#{d["id"]}">{E(d["name"])}</a>' for d in g["dishes"])
        dishes = "".join(dish(d) for d in g["dishes"])
        out.append(f'''<section class="grp" id="{g["id"]}">
  <h2>{E(g["name"])}</h2>
  <p class="gnote">{E(g["note"])}</p>
  <nav class="chips">{chips}</nav>
  {dishes}
</section>''')
    return f'''<section class="city" id="{c["id"]}">
  <h1>{E(c["name"])}</h1>
  <p class="intro">{E(c["intro"])}</p>
  <p class="checked">{E(c["checked"])}，营业时间以店家当天为准</p>
  {"".join(out)}
</section>'''

tabs = "".join(f'<a href="#{c["id"]}" class="on">{E(c["short"])}</a>' for c in CITIES) + '<span class="more">更多城市陆续添加</span>'
srcs = "".join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in SOURCES)

page = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="按城市整理的美食攻略，英文榜单和小红书两边核对。">
<title>吃什么 · 美食攻略</title>
<style>
:root{{--bg:#f7f3ea;--card:#fffdf8;--ink:#232019;--ink2:#6b6458;--line:#e6dfd1;--accent:#1f6f5c;--accent-ink:#fff;
  --ok:#1f7a4d;--ok-bg:#e5f3ea;--no:#7a7466;--no-bg:#efebe2;--mix:#9a5b00;--mix-bg:#fbefd9;--warn:#9a3412;--warn-bg:#fdeee6;--soft:#efe8da}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#14130f;--card:#1e1c17;--ink:#efe9dc;--ink2:#aaa292;--line:#35312a;--accent:#5cc3a3;--accent-ink:#0d1a15;
  --ok:#6fd49b;--ok-bg:#1c3328;--no:#a39d8f;--no-bg:#2a2721;--mix:#f0b25a;--mix-bg:#3a2c16;--warn:#ff9e7a;--warn-bg:#3a2119;--soft:#28251f}}}}
:root[data-theme="dark"]{{--bg:#14130f;--card:#1e1c17;--ink:#efe9dc;--ink2:#aaa292;--line:#35312a;--accent:#5cc3a3;--accent-ink:#0d1a15;
  --ok:#6fd49b;--ok-bg:#1c3328;--no:#a39d8f;--no-bg:#2a2721;--mix:#f0b25a;--mix-bg:#3a2c16;--warn:#ff9e7a;--warn-bg:#3a2119;--soft:#28251f}}
*{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0 auto;max-width:680px;background:var(--bg);color:var(--ink);padding:0 16px calc(40px + env(safe-area-inset-bottom));
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"PingFang SC","Helvetica Neue","Noto Sans SC","Microsoft YaHei",sans-serif}}
a{{color:var(--accent);text-decoration:none}}
header{{padding:22px 0 8px}}
.brand{{font-size:13px;letter-spacing:.24em;color:var(--ink2);margin:0}}
.tabs{{position:sticky;top:0;z-index:5;background:var(--bg);display:flex;gap:6px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line);overflow-x:auto}}
.tabs a{{padding:6px 14px;border-radius:999px;font-weight:600;font-size:15px;border:1.5px solid var(--line);color:var(--ink2);white-space:nowrap}}
.tabs a.on{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
.tabs .more{{font-size:12px;color:var(--ink2);white-space:nowrap;margin-left:4px}}
h1{{font-size:28px;margin:18px 0 6px}}
.intro{{color:var(--ink2);font-size:14px;margin:0 0 4px}}
.checked{{color:var(--ink2);font-size:12px;margin:0 0 6px}}
h2{{font-size:20px;margin:26px 0 6px;padding-top:8px;border-top:3px solid var(--ink)}}
.gnote{{font-size:14px;background:var(--soft);border-radius:12px;padding:10px 12px;margin:8px 0 10px}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 6px}}
.chips a{{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:14px;color:var(--ink)}}
.dish{{scroll-margin-top:64px}}
h3{{font-size:22px;margin:28px 0 4px}}
h3 small{{font-size:13px;color:var(--ink2);font-weight:400;letter-spacing:.04em;margin-left:6px}}
.lead{{margin:0 0 10px;font-size:15px}}
.warn,.avoid{{background:var(--warn-bg);border-left:3px solid var(--warn);border-radius:8px;padding:9px 12px;font-size:14px;margin:0 0 12px}}
.aside{{background:var(--soft);border-radius:10px;padding:10px 12px;font-size:14px;color:var(--ink);margin:4px 0 12px}}
.pick{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;margin:0 0 12px;box-shadow:0 1px 2px rgba(0,0,0,.04),0 6px 18px rgba(60,40,10,.05)}}
.ph{{display:flex;gap:10px;align-items:flex-start}}
.rk{{flex:0 0 28px;height:28px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;margin-top:2px}}
.ph h4{{margin:0;font-size:18px;line-height:1.3}}
.pz{{display:block;font-size:13px;color:var(--ink2)}}
.area{{margin-left:auto;font-size:12px;color:var(--ink2);border:1px solid var(--line);border-radius:999px;padding:2px 8px;white-space:nowrap}}
.bds{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 2px}}
.bd{{font-size:12px;padding:2px 9px;border-radius:999px}}
.bd b{{font-weight:600}}
.bd.ok{{background:var(--ok-bg);color:var(--ok)}}.bd.no{{background:var(--no-bg);color:var(--no)}}.bd.mix{{background:var(--mix-bg);color:var(--mix)}}
.bdn{{font-size:12px;color:var(--ink2);margin:2px 0 8px}}
.why{{margin:0 0 8px;padding-left:18px;font-size:15px}}.why li{{margin:3px 0}}
dl{{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;margin:0;font-size:14px}}
dt{{color:var(--ink2);white-space:nowrap}}dd{{margin:0}}
.tip{{font-size:13px;color:var(--ink2);margin:8px 0 0}}
.acts{{display:flex;gap:8px;margin-top:12px}}
.btn{{display:inline-flex;align-items:center;justify-content:center;min-height:40px;padding:0 16px;border-radius:10px;background:var(--accent);color:var(--accent-ink);font-weight:600;font-size:14px}}
.btn.ghost{{background:transparent;color:var(--accent);border:1.5px solid var(--accent)}}
footer{{margin-top:34px;border-top:1px solid var(--line);padding-top:14px;font-size:13px;color:var(--ink2)}}
footer ul{{padding-left:18px;margin:6px 0}}
</style>
</head>
<body>
<header><p class="brand">吃什么 · 美食攻略</p></header>
<nav class="tabs" id="tabs">{tabs}</nav>
{"".join(city(c) for c in CITIES)}
<footer>
  <p>英文侧资料来源：</p><ul>{srcs}</ul>
  <p>中文侧来自小红书公开探店笔记和评论区。只有一边有口碑的店会在卡片上标出来。</p>
</footer>
</body>
</html>
'''
pathlib.Path(__file__).with_name("index.html").write_text(page, encoding="utf-8")
print("built", len(page), "bytes")
