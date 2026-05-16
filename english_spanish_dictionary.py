import json
import os

DATA_FILE = "dictionary_data.json"


def load_dictionary():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "hello": "hola",
        "goodbye": "adiós",
        "please": "por favor",
        "thank you": "gracias",
        "yes": "sí",
        "no": "no",
        "water": "agua",
        "food": "comida",
        "friend": "amigo",
        "house": "casa",
    }


def save_dictionary(dictionary):
    with open(DATA_FILE, "w") as f:
        json.dump(dictionary, f, indent=2, ensure_ascii=False)


def add_word(dictionary):
    english = input("Enter English word: ").strip().lower()
    if not english:
        print("Word cannot be empty.")
        return

    if english in dictionary:
        print(f"'{english}' already exists with translation: {dictionary[english]}")
        overwrite = input("Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            return

    spanish = input("Enter Spanish translation: ").strip()
    if not spanish:
        print("Translation cannot be empty.")
        return

    dictionary[english] = spanish
    save_dictionary(dictionary)
    print(f"Added: {english} -> {spanish}")


def lookup_word(dictionary):
    english = input("Enter English word to look up: ").strip().lower()
    if english in dictionary:
        print(f"{english} -> {dictionary[english]}")
    else:
        print(f"'{english}' not found in dictionary.")


def list_all(dictionary):
    if not dictionary:
        print("Dictionary is empty.")
        return
    print(f"\n{'English':<20} {'Spanish'}")
    print("-" * 35)
    for english, spanish in sorted(dictionary.items()):
        print(f"{english:<20} {spanish}")
    print(f"\nTotal words: {len(dictionary)}")


def delete_word(dictionary):
    english = input("Enter English word to delete: ").strip().lower()
    if english in dictionary:
        confirm = input(f"Delete '{english}' ({dictionary[english]})? (y/n): ").strip().lower()
        if confirm == "y":
            del dictionary[english]
            save_dictionary(dictionary)
            print(f"Deleted '{english}'.")
    else:
        print(f"'{english}' not found.")


def main():
    dictionary = load_dictionary()
    print("English-Spanish Dictionary")

    while True:
        print("\n1. Add word\n2. Look up word\n3. List all words\n4. Delete word\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_word(dictionary)
        elif choice == "2":
            lookup_word(dictionary)
        elif choice == "3":
            list_all(dictionary)
        elif choice == "4":
            delete_word(dictionary)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
