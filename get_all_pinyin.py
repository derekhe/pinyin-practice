from pypinyin import pinyin, lazy_pinyin, Style

with open("./resource/words.txt", "rt", encoding="utf-8") as f:
    content = f.read()

all_py = {}
for w in content:
    py = pinyin(w, style=Style.TONE3, heteronym=True)[0][0]
    if py in all_py:
        continue
    all_py[py] = w

print(all_py)