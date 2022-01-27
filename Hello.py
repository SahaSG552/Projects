text = """London is the capital of Great Britain.
        More than six million people live in London.
        London lies on both banks of the river Thames.
        It is the largest city in Europe and one of the largest cities in the world. 
        London is not only the capital of the country, it is also a very big port, 
        one of the greatest commercial centres in the world, a university city, 
        and the seat of the government of Great Britain!""".lower().split()
text = [t.strip(',.!?:;') for t in text]

# result = dict.fromkeys(text,0)
# for word in text:
#     if word in result:
#         result[word] += 1

result = {}
for word in text:
    result[word] = result.get(word, 0) + 1

print(sorted([i for i in result.keys() if result[i] == min(result.values())])[0])