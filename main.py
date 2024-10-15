import re

# List of top 10 emojis of 2023 from: https://www.meltwater.com/en/blog/top-emojis-2023
top_ten_emojis = ['😊', '✨', '🥰', '😍', '🙏', '🔥', '❤️', '🤣', '😭', '😂']

def open_file(file_path):
    try:
        with open(file_path) as text_string:
            return text_string.read()
    except FileNotFoundError:
        print(f"\n\033[38;5;{172}m{file_path} \033[31mFile Not Found\n\033[39m...")
    




def main():
    file_paths = {
            "boot.dev": ["messages/boot.dev/october.txt", "messages/boot.dev/september.txt"],
            "donthedeveloper": ["messages/donthedeveloper/october.txt", "messages/donthedeveloper/september.txt"]
            }

    for discord in file_paths:
        for path in file_paths[discord]:
            current_file = open_file(path)
            #print(current_file)
        

        
        





main()