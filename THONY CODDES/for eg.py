import language_tool_python

def identify_grammatical_mistakes(text):
    # Initialize the language tool
    tool = language_tool_python.LanguageTool('en-US')
    
    # Check the text for mistakes
    matches = tool.check(text)
    
    # Print out the mistakes
    if matches:
        print("\nGrammatical mistakes found:")
        for match in matches:
            print(f"Error: {match.message}")
            print(f"Suggestion: {', '.join(match.replacements)}")
            print(f"Context: '{text[match.offset:match.offset + match.errorLength]}'")
            print("-" * 40)
    else:
        print("No grammatical mistakes found.")

if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Please enter a sentence or paragraph to check for grammatical mistakes:\n")
    
    # Identify mistakes in the user input
    identify_grammatical_mistakes(user_input)