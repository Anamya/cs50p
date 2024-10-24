import emoji


emj = input("Input: ")

emojized = emoji.emojize(emj, language='alias')

print(f"Output: {emojized}")
