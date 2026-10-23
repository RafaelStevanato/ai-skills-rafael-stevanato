"""Validate the consolidated skill pack.

usage: python3 -I validate.py <src_root> <out_root> [skill ...]
"""
import os, re, sys, json
import yaml

SRC, OUT = sys.argv[1], sys.argv[2]
ONLY = set(sys.argv[3:])

GROUPS = {
    'anti-ai-slop-escrita-ptbr': ['anti-ai-slop-writing', 'humanizar'],
    'anti-slop': ['anti-slop', 'slop-eval', 'ultimate-design-system-master', 'design-md-validator'],
    'web-discoverability': ['agent-ready-cloudflare', 'geo-optimization', 'substack-expert'],
    'revenue-centric-design': ['revenue-centric-design'],
    'motion-ad': ['motion-ad'],
    'human-browser': ['navegador-humano'],
    'skill-evaluation': ['skill-evaluation'],
}
OLD_NAMES = ['anti-ai-slop-writing', 'humanizar', 'human-ai', 'slop-eval', 'ultimate-design-system-master',
             'design-md-validator', 'agent-ready-cloudflare', 'geo-optimization', 'substack-expert', 'navegador-humano']
EN_DIRECTIVE = 'EXECUTION DIRECTIVE (INPUT vs. OUTPUT SEPARATION)'
PT_DIRECTIVE = 'DIRETRIZ DE EXECUÇÃO (SEPARAÇÃO INPUT vs. OUTPUT)'
ALLOWED_KEYS = {'name', 'description', 'license', 'metadata'}
FENCE = re.compile(r'^(```|~~~)[^\n]*\n(.*?)^\1\s*$', re.M | re.S)
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def read(p):
    return open(p, encoding='utf-8', errors='replace').read()


def text_files(root):
    for dp, _, fn in os.walk(root):
        for f in fn:
            if os.path.splitext(f)[1].lower() in ('.md', '.json', '.py', '.cjs', '.js', '.html', '.txt', ''):
                yield os.path.join(dp, f)


report = {}
for skill, sources in GROUPS.items():
    if ONLY and skill not in ONLY:
        continue
    root = os.path.join(OUT, skill)
    errs, warns = [], []
    report[skill] = {'errors': errs, 'warnings': warns}
    sk = os.path.join(root, 'SKILL.md')
    if not os.path.isfile(sk):
        errs.append('missing SKILL.md')
        continue
    body = read(sk)
    m = re.match(r'^---\n(.*?)\n---\n', body, re.S)
    if not m:
        errs.append('no frontmatter')
    else:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception as e:
            errs.append(f'frontmatter yaml error: {e}')
            fm = {}
        extra = set(fm) - ALLOWED_KEYS
        if extra:
            errs.append(f'unexpected frontmatter keys: {sorted(extra)}')
        name = fm.get('name', '')
        if name != skill:
            errs.append(f'name {name!r} != folder {skill!r}')
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', str(name)) or len(str(name)) > 64:
            errs.append(f'bad name format {name!r}')
        desc = str(fm.get('description', ''))
        if not desc:
            errs.append('empty description')
        if len(desc) > 1024:
            errs.append(f'description {len(desc)} chars > 1024')
        if '<' in desc or '>' in desc:
            errs.append('angle bracket in description')
        md = fm.get('metadata')
        if md is not None:
            if not isinstance(md, dict):
                errs.append('metadata not a map')
            else:
                bad = [k for k, v in md.items() if not isinstance(v, str)]
                if bad:
                    errs.append(f'metadata non-string values: {bad}')
        after = body[m.end():m.end() + 1200]
        want = PT_DIRECTIVE if skill == 'anti-ai-slop-escrita-ptbr' else EN_DIRECTIVE
        if want not in after:
            errs.append('execution directive missing at top of SKILL.md')
    lines = body.count('\n')
    if lines > 500:
        warns.append(f'SKILL.md has {lines} lines (> 500)')
    # nested SKILL.md
    for dp, _, fn in os.walk(root):
        if 'SKILL.md' in fn and dp != root:
            errs.append(f'nested SKILL.md in {os.path.relpath(dp, root)}')
    # links resolve
    for p in text_files(root):
        if not p.endswith('.md'):
            continue
        t = read(p)
        for href in LINK.findall(FENCE.sub('', t)):
            if re.match(r'^[a-z]+:', href) or href.startswith('mailto'):
                continue
            tgt = os.path.normpath(os.path.join(os.path.dirname(p), href))
            if not os.path.exists(tgt):
                errs.append(f'broken link in {os.path.relpath(p, root)}: {href}')
        for ref in set(re.findall(r'`((?:references|scripts|assets)/[A-Za-z0-9_./-]+)`', t)):
            if not os.path.exists(os.path.join(root, ref)) and '*' not in ref and '<' not in ref:
                warns.append(f'backtick path not found in {os.path.relpath(p, root)}: {ref}')
        prose = re.sub(r'\A---\n.*?\n---\n', '', t, count=1, flags=re.S)
        for old in OLD_NAMES:
            if re.search(r'(?<![\w-])' + re.escape(old) + r'(?![\w-])', prose):
                warns.append(f'old skill name {old!r} in {os.path.relpath(p, root)}')
    # code block preservation
    out_blob = norm('\n'.join(read(p) for p in text_files(root)))
    missing = []
    total = 0
    for s in sources:
        for p in text_files(os.path.join(SRC, s)):
            if not p.endswith('.md'):
                continue
            for _, code in FENCE.findall(read(p)):
                c = norm(code)
                if len(c) < 12:
                    continue
                total += 1
                if c not in out_blob:
                    missing.append(f'{os.path.relpath(p, SRC)}: {c[:90]}')
    report[skill]['code_blocks_total'] = total
    report[skill]['code_blocks_missing'] = missing

print(json.dumps(report, indent=1, ensure_ascii=False))
