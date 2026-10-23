import os, sys, json
root = sys.argv[1]
TEXT_EXT = {'.md','.json','.py','.cjs','.js','.html','.txt','.yaml','.yml','.css','.sh','.ts',''}
tot_b=tot_w=txt_b=bin_b=0; files=0; per={}
for dp,dn,fn in os.walk(root):
    for f in fn:
        p=os.path.join(dp,f); rel=os.path.relpath(p,root); skill=rel.split(os.sep)[0]
        b=os.path.getsize(p); files+=1; tot_b+=b
        ext=os.path.splitext(f)[1].lower()
        d=per.setdefault(skill,{'bytes':0,'words':0,'text_bytes':0,'files':0})
        d['bytes']+=b; d['files']+=1
        if ext in TEXT_EXT or f in ('LICENSE','UPSTREAM_COMMIT','.gitignore'):
            w=len(open(p,encoding='utf-8',errors='replace').read().split())
            tot_w+=w; txt_b+=b; d['words']+=w; d['text_bytes']+=b
        else: bin_b+=b
print(json.dumps({'skills':len(per),'files':files,'total_kb':round(tot_b/1024,1),'text_kb':round(txt_b/1024,1),'binary_kb':round(bin_b/1024,1),'words_text':tot_w,'per':per},indent=1))
