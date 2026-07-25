s="abcd"
for i in range(len(s)):
    rotation=s[i:]+s[:i]
print(rotation)