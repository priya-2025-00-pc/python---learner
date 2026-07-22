s = input("Enter a string: ")

visited = ""

for ch in s:
    if s.count(ch) > 1 and ch not in visited:
        print(ch)
        visited += ch
