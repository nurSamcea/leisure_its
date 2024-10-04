import os

def get_final_report():
    # List of Markdown files to include
    files_to_include = [os.path.join('docs', f) for f in os.listdir('docs') if f.endswith('.md')]

    # Main Markdown file
    main_file = 'final_report.md'

    with open(main_file, 'w', encoding='utf-8') as outfile:
        for fname in files_to_include:
            with open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')  # Add a newline between files

    print(f'Final report written to {main_file}')

if __name__ == '__main__':
    get_final_report()
