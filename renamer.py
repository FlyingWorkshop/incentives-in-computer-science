from pathlib import Path
import re

def extract_number(s):
    match = re.search(r'lec(\d+)', s)
    return int(match.group(1)) if match else None

def generate_label(title):
    # Generate a label from the title by converting to lowercase and replacing spaces with hyphens
    return title.strip().lower().replace(' ', '-')

def to_title_case(title):
    # Convert the title to title case
    return title.title()

def get_label_from_user(block_type, block_content):
    blue_block_type = f"\033[94m{block_type}\033[0m"
    print(f"Unlabeled {blue_block_type} detected, would you like to provide a title and label?")
    print(block_content)
    title = input("Title: ").strip()
    if not title:
        return None, None
    title = to_title_case(title)
    label = generate_label(title)
    return title, label

def confirm_label(title, generated_label):
    print(f"Title detected: '{title}'")
    print(f"Automatically generated label: '{generated_label}'")
    confirm = input("Press Enter to confirm or provide a custom label: ").strip()
    if confirm == '':
        return generated_label
    else:
        return confirm

def process_markdown(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    prf_pattern = re.compile(r'```{prf:(\w+)}([^\n]*)(\n(?:\n|.)+?)```')
    matches = prf_pattern.finditer(content)

    red_file_name = f"\033[91m{input_file}\033[0m"
    modified_content = []
    last_end = 0

    for match in matches:
        block_type = match.group(1)
        title = match.group(2)
        block_content = match.group(3)
        
        if block_type in ('proof', 'remark', 'example', 'theorem', 'practice'):
            continue

        if ':label:' not in block_content:
            print(red_file_name)
            title = title.strip()
            if title:
                generated_label = generate_label(title)
                label = confirm_label(title, generated_label)
            else:
                title, label = get_label_from_user(block_type, block_content)
                if not label:
                    continue
            
            labeled_block = f'```{{prf:{block_type}}} {title.strip()}\n:label: {label}\n{block_content.strip()}\n```'
        
            modified_content.append(content[last_end:match.start()])
            modified_content.append(labeled_block)
            last_end = match.end()

    modified_content.append(content[last_end:])

    with open(output_file, 'w') as file:
        file.write(''.join(modified_content))

    green_output_file = f"\033[92m{output_file}\033[0m"
    print(f"Modified content written to {green_output_file}")

def main():
    notes_folder = Path("docs/notes")
    sorted_note_paths = sorted(notes_folder.iterdir(), key=lambda x: extract_number(str(x)))
    output_folder = Path("notes_output")
    output_folder.mkdir(exist_ok=True)

    for note_path in sorted_note_paths:
        process_markdown(note_path, output_folder / note_path.name)

if __name__ == "__main__":
    main()
