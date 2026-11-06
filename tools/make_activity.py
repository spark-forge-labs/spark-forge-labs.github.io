#!/usr/bin/env python3
"""Regenerate activity.json from a local clone: python3 tools/make_activity.py /path/to/epicenter [ref]"""
import json,subprocess,sys,collections,datetime
repo=sys.argv[1]; ref=sys.argv[2] if len(sys.argv)>2 else 'origin/main'
out=subprocess.check_output(['git','-C',repo,'log',ref,'--format=%ad','--date=short'],text=True).split()
days=collections.Counter(out)
json.dump({"repo":"spark-forge-labs/epicenter","generated":datetime.date.today().isoformat(),"total":len(out),"days":dict(sorted(days.items()))},open('activity.json','w'),separators=(',',':'))
print(len(out),'commits over',len(days),'days')
