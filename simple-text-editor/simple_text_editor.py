def request_filename():
    while True:
        filename = input("Enter the filename to open or create: ").strip()

        if filename:
            return filename


def print_file_content(filename):
    try:
        with open(f'./simple-text-editor/{filename}', 'r', encoding='UTF-8') as file:
            content = file.read()
            print(content)

            return content
    except FileNotFoundError:
        print(f'{filename} not found. Creating a new file...')


def get_selected_option():
    print("Select one of the options for modifying the file:\n1. Overwrite\n2. Append new text to the end\n3. Replace text with new content")

    while True:
        selected_option = input("Choice: ").strip()

        if selected_option in ['1', '2', '3']:
            return selected_option


def request_new_content():
    print("\nEnter your text (type SAVE on a new line to save and exit): ")

    new_content = ''

    while True:
        line = input().lower()

        if line == 'save':
            return new_content

        new_content += line + '\n'


def write_content(filename: str, new_content: str, option: str):
    try:
        with open(f'./simple-text-editor/{filename}', 'a' if option == '2' else 'w', encoding='UTF-8') as file:
            file.write(new_content)
    except OSError:
        print(f'File {filename} could not be saved.')


def replace_text(filename: str, existing_content: str):
    text_to_replace = input("Enter a phrase or a word to replace: ").strip()
    new_text = input("Enter a content to replace the phrase with: ").strip()
    modified_content = existing_content.replace(text_to_replace, new_text)

    if len(modified_content) == len(existing_content):
        print(f'Did not find any occurrences of "{text_to_replace}"')

    with open(f'./simple-text-editor/{filename}', 'w', encoding='UTF-8') as file:
        file.write(modified_content)


def main():
    filename = request_filename()
    content = print_file_content(filename)
    selected_option = '1'

    if content:
        selected_option = get_selected_option()

    if selected_option != '3':
        new_content = request_new_content()
        write_content(filename, new_content, selected_option)
    else:
        replace_text(filename, content)

    print(f'File {filename} saved.')


if __name__ == '__main__':
    main()
