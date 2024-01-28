with open('article.txt', 'r') as file:
    text = file.read()

replacements = {'.': '', ',': '', '\n': ' ', "'s": '', '-': ' ', '"': '', '(': '', ')': ''}
new_text = text.replace('\n', ' ')

for old, new in replacements.items():
    new_text = new_text.replace(old, new)

split_filtered_words = [word.lower() for word in new_text.split(' ') if not word.isdigit()]

word_counts = {}
for word in split_filtered_words:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_items = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

second_highest_tuple = None

for tuple_ in sorted_items:
    if tuple_[1] != sorted_items[0][1]:
        second_highest_tuple = tuple_
        break

if second_highest_tuple is not None:
    print(f"The second-highest word in the text is: '{second_highest_tuple[0]}' and it repeats {second_highest_tuple[1]} times.")
else:
    print("No second-highest word found. ")



