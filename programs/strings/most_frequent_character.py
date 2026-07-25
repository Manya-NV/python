s="programming"
max_ch=""
max_count=0
for ch in s:
    count=s.count(ch)
    if count>max_count:
        max_count=count
        max_ch=ch
    print(max_ch,max_count)