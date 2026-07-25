s = "abcbef"
seen = ""
for ch in s:
    if ch in seen:
        print(ch)
        break
    seen += ch