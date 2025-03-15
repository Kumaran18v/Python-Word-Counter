def count_words(text):
    """returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """returns the number of characters excluding spaces."""
    return len(text.replace(" ", ""))

def main():
    """handles user input and displays word and character count."""
    text = input("enter a sentence or paragraph: ").strip()
    
    if not text:
        print("error: input cannot be empty.")
        return
    
    print(f"word count: {count_words(text)}")
    print(f"character count (excluding spaces): {count_characters(text)}")

if __name__ == "__main__":
    main()
