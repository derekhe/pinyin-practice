from pypinyin import pinyin, lazy_pinyin, Style

with open("./resource/words.txt","rt",encoding="utf-8") as f:
    content = f.read()

all_py = set()
for w in content:
    for py in pinyin(w, style=Style.TONE3, heteronym=True)[0]:
        all_py.add(py)

print(sorted(all_py))