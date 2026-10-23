"""List atomic source items (URLs, code spans, quoted strings, numbers with units) missing from a built skill.

usage: python3 -I -X utf8 coverage.py <src_root> <out_root> <skill> [kinds]
kinds: comma list of url,code,quote,num (default all)
"""
import os, re, sys

G = {
    'anti-ai-slop-escrita-ptbr': ['anti-ai-slop-writing', 'humanizar'],
    'anti-slop': ['anti-slop', 'slop-eval', 'ultimate-design-system-master', 'design-md-validator'],
    'web-discoverability': ['agent-ready-cloudflare', 'geo-optimization', 'substack-expert'],
    'revenue-centric-design': ['revenue-centric-design'],
    'motion-ad': ['motion-ad'],
    'human-browser': ['navegador-humano'],
    'skill-evaluation': ['skill-evaluation'],
}
SRC, OUT, SKILL = sys.argv[1:4]
KINDS = set((sys.argv[4] if len(sys.argv) > 4 else 'url,code,quote,num').split(','))
FENCE = re.compile(r'^(```|~~~)[^\n]*\n.*?^\1\s*$', re.M | re.S)
EXT = ('.md', '.json', '.py', '.cjs', '.html', '.txt')


def walk(root):
    for dp, _, fn in os.walk(root):
        for f in sorted(fn):
            if f.lower().endswith(EXT):
                yield os.path.join(dp, f)


def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()


blob = norm(' '.join(open(p, encoding='utf-8', errors='replace').read() for p in walk(os.path.join(OUT, SKILL))))
missing = {}
for s in G[SKILL]:
    for p in walk(os.path.join(SRC, s)):
        if not p.endswith('.md'):
            continue
        t = FENCE.sub('', open(p, encoding='utf-8', errors='replace').read())
        items = []
        if 'url' in KINDS:
            items += [('url', u.rstrip('.,;)')) for u in re.findall(r'https?://[^\s)>\]`"]+', t)]
        if 'code' in KINDS:
            items += [('code', c) for c in re.findall(r'`([^`\n]{3,80})`', t)]
        if 'quote' in KINDS:
            items += [('quote', q) for q in re.findall(r'["“]([^"”\n]{3,60})["”]', t)]
        if 'num' in KINDS:
            items += [('num', n) for n in re.findall(r'\b\d+(?:[.,]\d+)?\s?(?:%|px|ms|KB|MB|chars?|caracteres|palavras|words|linhas|lines|dias|days|x)\b', t)]
        for k, v in items:
            if norm(v) not in blob:
                missing.setdefault(os.path.relpath(p, SRC).replace(os.sep, '/'), set()).add((k, v))
n = 0
for f, its in sorted(missing.items()):
    print(f'## {f} ({len(its)})')
    for k, v in sorted(its):
        print(f'  [{k}] {v}')
        n += 1
print(f'TOTAL missing: {n}')
