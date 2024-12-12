import copy

# Example list
words = ["apple", "banana", "cherry"]

# 1. Copying the list by assignment (both lists will share the same reference)
words_copy_same_ref = words

# 2. Copying the list using the copy() method (this creates a new reference)
words_copy_diff_ref = words.copy()

# 3. Copying the list using deepcopy() (to ensure even nested lists would have a new reference)
words_copy_deep_diff_ref = copy.deepcopy(words)

# Print the ID of each list
print(f"ID of 'words': {id(words)}")
print(f"ID of 'words_copy_same_ref': {id(words_copy_same_ref)}")
print(f"ID of 'words_copy_diff_ref': {id(words_copy_diff_ref)}")
print(f"ID of 'words_copy_deep_diff_ref': {id(words_copy_deep_diff_ref)}")

# Checking if both lists are the same or different
if id(words) == id(words_copy_same_ref):
    print("The lists 'words' and 'words_copy_same_ref' are the same (same reference).")
else:
    print("The lists 'words' and 'words_copy_same_ref' are different (different reference).")

if id(words) == id(words_copy_diff_ref):
    print("The lists 'words' and 'words_copy_diff_ref' are the same (same reference).")
else:
    print("The lists 'words' and 'words_copy_diff_ref' are different (different reference).")

if id(words) == id(words_copy_deep_diff_ref):
    print("The lists 'words' and 'words_copy_deep_diff_ref' are the same (same reference).")
else:
    print("The lists 'words' and 'words_copy_deep_diff_ref' are different (different reference).")
