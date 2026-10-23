"""Print the blueprint entry for one target file, plus the skill-wide dedup_map, conflicts and path_rewrites.

usage: python3 -I -X utf8 bp.py <skill> [target-path]
Without a target path, list the target files.
"""
import json, sys

skill = sys.argv[1]
b = json.load(open(f'_handoff/blueprints/{skill}.json', encoding='utf-8'))
if len(sys.argv) < 3:
    for t in b['target_files']:
        print(t['path'], '|', t.get('action'), '|', t.get('est_words_after'))
    sys.exit()
want = sys.argv[2]
for t in b['target_files']:
    if t['path'] == want:
        print(json.dumps(t, indent=1, ensure_ascii=False))
for k in ('dedup_map', 'conflicts', 'path_rewrites', 'critical_assets', 'drop_list', 'notes'):
    print(f'\n## {k}')
    print(json.dumps(b.get(k), indent=1, ensure_ascii=False))
