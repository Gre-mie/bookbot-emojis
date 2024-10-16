import re

file_paths = {
            "boot.dev": ["messages/boot.dev/october.txt", "messages/boot.dev/september.txt"],
            "donthedeveloper": ["messages/donthedeveloper/october.txt", "messages/donthedeveloper/september.txt"]
            }

def open_file(file_path):
    try:
        with open(file_path) as text_string:
            return text_string.read()
    except FileNotFoundError:
        print(f"\n\033[38;5;{172}m{file_path} \033[31mFile Not Found\n\033[39m...")

# returns the number of times an emoji is used in all files
def total_emoji_num(file_paths):
    total = 0
    # iterates through all the files in file_paths
    for discord in file_paths:
        for path in file_paths[discord]:
            current_file = open_file(path)
            # uses a regex that checks for anything that isn't a letter, number and specified punctuation chars
            for char in current_file:
                if re.match(r'[^\w\s\',-./#—:\[\]"<!>?()=&@%]', char):
                    total += 1
    return total

def count_which_popular_emojis_I_use(file_paths):
    # List of top 10 emojis of 2023 from: https://www.meltwater.com/en/blog/top-emojis-2023
    top_ten_emojis = {'😊': 0, '✨': 0, '🥰': 0, '😍': 0, '🙏': 0, '🔥': 0, '❤️': 0, '🤣': 0, '😭': 0, '😂': 0}

    # iterates through all the files in file_paths
    for discord in file_paths:
        for path in file_paths[discord]:
            current_file = open_file(path)

            # increments an emoji counter in the top_ten_emojis, dict each time it finds a matching emoji in the files
            for char in current_file:
                if char in top_ten_emojis:
                    top_ten_emojis[char] += 1

    return top_ten_emojis

def count_my_popular_emojis(discord):
    count_emojis = {}

    for path in file_paths[discord]:
        current_file = open_file(path)
        for char in current_file:
            # uses a regex that checks for anything that isn't a letter, number and specified punctuation chars
            if re.match(r'[^\w\s\',-./#—:\[\]"<!>?()=&@%]', char):
                if char in count_emojis:
                    count_emojis[char] += 1
                else:
                    count_emojis[char] = 1

    return count_emojis

def combine_dicts(dict_1, dict_2):
    combined = dict_1
    # adds the two dict values together returning a new dict
    for key in dict_2:
        if key in combined:     
            combined[key] += dict_2[key]
        else:
            combined[key] = dict_2[key]

    return combined

# prints a dictinary formated as a horizontal bar chart
def print_table(dict, title_string):
    print(f"\n{title_string}\n")
    # some emojies need an extra space to get the pipes to line up
    need_space = ["\u2060", '❤️']
    row = []

    for item in dict:
        row.append(item)

        if item in need_space:
            row.append(' ')

        red = 200
        green = 75
        blue = 50
        row.append(f"\033[38;2;{red};{green};{blue}m |")
        # adds the number of hashes for the horizontal bar chart
        for i in range(dict[item]):
            bar_col = f"\033[38;2;{red};{green};{blue}m"

            red -= 20
            blue += 20
            # prevents colour values becomeing more than their max
            if red > 255:
                red = red % 255
            if blue > 255:
                blue = blue % 255
            row.append(bar_col)
            row.append('#')

        default_col = f"\033[39m"
        row.append(default_col)
        # prints the row
        print("".join(row))
        row = []


def main():

    print("\n---x---X---x--- Emoji Counter ---x---X---x---")

    total_emojis = total_emoji_num(file_paths)
    print(f"Total emojies in all messages: {total_emojis}")
    
    # dictinaries of counted emojies
    popular_emojis = count_which_popular_emojis_I_use(file_paths)
    boot_dev_emojis = count_my_popular_emojis("boot.dev")
    donthedeveloper_emojis = count_my_popular_emojis("donthedeveloper")
    my_emoji_count = combine_dicts(boot_dev_emojis, donthedeveloper_emojis)

    print_table(my_emoji_count, "---x--- Total emojis in all messages, September-October ---x---")
    print_table(boot_dev_emojis, "---x--- Boot.dev, general-lounge, September-October ---x---")
    print_table(donthedeveloper_emojis, "---x--- donthedeveloper, general channel, September-October ---x---")
    print_table(popular_emojis, "---x--- 10 most popular emojis 2023, September-October ---x---")
    

main()