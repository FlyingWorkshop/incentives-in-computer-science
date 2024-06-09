from pathlib import Path
import re

def extract_number(s):
    match = re.search(r'lec(\d+)', s)
    return int(match.group(1)) if match else None

def add_index_block(content):
    prf_pattern = re.compile(r'```{prf:(\w+)}([^\n]*)(\n(?:\n|.)+?)```')
    matches = prf_pattern.finditer(content)

    modified_content = []
    last_end = 0

    for match in matches:
        block_type = match.group(1)
        title = match.group(2).strip()
        block_content = match.group(3).strip()

        if title and ':label:' in block_content:
            index_block = f'```{{index}} {title}\n```'

            modified_content.append(content[last_end:match.start()])
            modified_content.append(index_block + '\n')
            modified_content.append(match.group(0))
            last_end = match.end()
        else:
            modified_content.append(content[last_end:match.end()])
            last_end = match.end()

    modified_content.append(content[last_end:])
    return ''.join(modified_content)

def process_markdown(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    modified_content = add_index_block(content)

    with open(output_file, 'w') as file:
        file.write(modified_content)

    green_output_file = f"\033[92m{output_file}\033[0m"
    print(f"Modified content written to {green_output_file}")

def main():
    notes_folder = Path("docs/notes")
    sorted_note_paths = sorted(notes_folder.iterdir(), key=lambda x: extract_number(str(x)))
    output_folder = Path("notes_indexed")
    output_folder.mkdir(exist_ok=True)

    for note_path in sorted_note_paths:
        process_markdown(note_path, output_folder / note_path.name)

if __name__ == "__main__":
    main()
