import json, os, sys, re
S = sys.argv[1]; target = sys.argv[2]
b = json.load(open(f'{S}/bp/{target}.json'))
od = f'{S}/bp/slices/{target}'; os.makedirs(od, exist_ok=True)
allfiles = [{'path': f['path'], 'action': f['action'], 'purpose': f['purpose']} for f in b['target_files']]
out = []
for f in b['target_files']:
    p = f['path']; base = os.path.basename(p)
    def hit(s): return p in s or (base in s and base != 'SKILL.md') or (p == 'SKILL.md' and 'SKILL.md' in s)
    sl = {
        'target': target, 'file': f, 'all_target_files': allfiles,
        'critical_assets': [a for a in b.get('critical_assets', []) if a.get('target_file', '') in (p, base) or p in a.get('target_file', '')],
        'dedup_map': [d for d in b.get('dedup_map', []) if hit(d.get('kept_in', '')) or any(hit(x) for x in d.get('found_in', []))],
        'conflicts': b.get('conflicts', []), 'path_rewrites': b.get('path_rewrites', []),
        'drop_list': b.get('drop_list', []), 'broken_refs': b.get('broken_refs', []), 'notes': b.get('notes', ''),
    }
    if p == 'SKILL.md':
        sl['frontmatter_description_draft'] = b['frontmatter_description_draft']
        sl['skill_md_outline'] = b['skill_md_outline']
    name = re.sub(r'[^A-Za-z0-9._-]', '_', p)
    json.dump(sl, open(f'{od}/{name}.json', 'w'), ensure_ascii=False, indent=1)
    out.append({'path': p, 'action': f['action'], 'slice': f'{od}/{name}.json', 'est': f.get('est_words_after', 0)})
print(json.dumps(out, ensure_ascii=False))
