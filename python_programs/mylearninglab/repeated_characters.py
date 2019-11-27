string = "thequickbrownfoxjumpsoverthelazydog"
print("given string is", string)
count = {}
print(dir(count))
for x in string :
    if x in count.keys() :
        count[x] = count[x] + 1
    else :
        count[x] = 1
print(count)
for x in count.keys() :
    print(x, "occurs for", count[x], "times.")
        