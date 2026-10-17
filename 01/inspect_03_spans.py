import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("01/3/3.html", "r", encoding="utf-8") as f:
    c = f.read()

spans = re.findall(r'<span class="math"[^>]*>(.*?)</span>', c)
print(f"Total spans in 01/3: {len(spans)}")
for s in spans[:25]:
    print(" ", s)
