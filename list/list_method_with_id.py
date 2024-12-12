def play_game():
    words = []  # Initialize an empty list to store words

    while True:
        print("\nMenu:")
        print("1. Add a word to the list")
        print("2. Remove a word from the list")
        print("3. Delete a word by position")
        print("4. View the list")
        print("5. Create a copy with same ID")
        print("6. Create a copy with different ID")
        print("7. Exit")
        print("8. Extend the list with another list")
        print("9. Insert a word at a specific position")
        print("10. Sort the list")
        print("11. Reverse the list")
        print("12. Clear the entire list")
        print("13. Count occurrences of a word")

        choice = input("Choose an option (1-13): ").strip()

        if choice == "1":
            # Append a word to the list
            word = input("Enter a word to add: ").strip()
            words.append(word)
            print(f"'{word}' has been added to the list.")

        elif choice == "2":
            # Remove a word by value
            word = input("Enter the word to remove: ").strip()
            if word in words:
                words.remove(word)
                print(f"'{word}' has been removed from the list.")
            else:
                print(f"'{word}' is not in the list.")

        elif choice == "3":
            # Delete a word by its position
            if not words:
                print("The list is empty!")
            else:
                print("\nCurrent list:")
                for i, word in enumerate(words, start=1):
                    print(f"{i}: {word}")

                try:
                    position = int(input("Enter the position of the word to delete: ").strip())
                    if 1 <= position <= len(words):
                        del words[position - 1]
                        print("The word has been deleted.")
                    else:
                        print("Invalid position!")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            # View the list
            if words:
                print("\nCurrent list:")
                for i, word in enumerate(words, start=1):
                    print(f"{i}: {word}")
            else:
                print("The list is empty!")

        elif choice == "5":
            # Create a copy with the same reference (ID)
            words_copy_same_ref = words
            print(f"ID of 'words': {id(words)}")
            print(f"ID of 'words_copy_same_ref': {id(words_copy_same_ref)}")
            if id(words) == id(words_copy_same_ref):
                print("The lists 'words' and 'words_copy_same_ref' are the same (same reference).")
            else:
                print("The lists 'words' and 'words_copy_same_ref' are different (different reference).")

        elif choice == "6":
            # Create a copy with a different reference (ID)
            words_copy_diff_ref = words.copy()
            print(f"ID of 'words': {id(words)}")
            print(f"ID of 'words_copy_diff_ref': {id(words_copy_diff_ref)}")
            if id(words) == id(words_copy_diff_ref):
                print("The lists 'words' and 'words_copy_diff_ref' are the same (same reference).")
            else:
                print("The lists 'words' and 'words_copy_diff_ref' are different (different reference).")

        elif choice == "7":
            # Exit the game
            print("Goodbye!")
            break

        elif choice == "8":
            # Extend the list with another list
            new_words = input("Enter a list of words separated by space to extend the current list: ").strip().split()
            words.extend(new_words)
            print(f"The list has been extended with: {new_words}")

        elif choice == "9":
            # Insert a word at a specific position
            word = input("Enter a word to insert: ").strip()
            try:
                position = int(input("Enter the position to insert the word: ").strip())
                if 1 <= position <= len(words) + 1:  # Allow inserting at the end too
                    words.insert(position - 1, word)
                    print(f"'{word}' has been inserted at position {position}.")
                else:
                    print("Invalid position!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "10":
            # Sort the list
            if words:
                words.sort()
                print("The list has been sorted alphabetically.")
            else:
                print("The list is empty!")

        elif choice == "11":
            # Reverse the list
            if words:
                words.reverse()
                print("The list has been reversed.")
            else:
                print("The list is empty!")

        elif choice == "12":
            # Clear the entire list
            words.clear()
            print("The list has been cleared.")

        elif choice == "13":
            # Count occurrences of a word
            word = input("Enter a word to count its occurrences: ").strip()
            count = words.count(word)
            print(f"The word '{word}' appears {count} times in the list.")

        else:
            print("Invalid choice! Please choose a valid option.")

print("Welcome to the Word Editor Game!")
play_game()
