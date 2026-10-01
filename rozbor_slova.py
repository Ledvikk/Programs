try: 
    word = input("Zadejte slovo: ")
    if not word.isalpha():
        raise ValueError("Zadaný vstup není platné slovo.")
except ValueError as e:
    print(f"Chyba: {e}")

length = len(word)
first_char = word[0]
last_char = word[-1]
backward_word = word[::-1]
if backward_word == word:
    palindrome = "True"
else:
    palindrome = "False"

print(f"""
      Slovo: {word}
      Délka slova: {length}
      První znak: {first_char}
      Poslední znak: {last_char}
      Velkými písmeny: {word.capitalize()}
      Pozpátku: {backward_word}
      Palindrom: {palindrome}
""")