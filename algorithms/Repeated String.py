s = input().strip()
n = int(input().strip())
ains = s.count("a")
occurences = ains*(n//len(s))
print(occurences)
i = n - (n//len(s))*len(s)
occurences += s[:i].count("a")
print(occurences)
