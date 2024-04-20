import re

def convert_markdown(input_file, output_file):
    print(f"Reading {input_file}")
    with open(input_file, 'r') as f:
        markdown_text = f.read()

    print("Converting...")
    
    pattern = r':::\s*(\w+)\n(.*?)\n:::'
    replacement = r'```{prf:\1}\n\2\n```'
    converted_text = re.sub(pattern, replacement, markdown_text, flags=re.DOTALL)

    converted_text = re.sub("\*Proof\.\*", "", converted_text)
    converted_text = re.sub("◻", "", converted_text)
    # TODO: change this to some custom CSS that changes "axiom" to something else
    converted_text = re.sub(r"{prf:mech}", r"{prf:axiom}", converted_text)


    print(f"Writing {output_file}")
    with open(output_file, 'w') as f:
        f.write(converted_text)

if __name__ == "__main__":
    input_file = "input.md"
    output_file = "output.md"
    convert_markdown(input_file, output_file)
