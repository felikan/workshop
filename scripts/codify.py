import re
from os import listdir
from os.path import isfile, join
from pathlib import Path

comment = re.compile('\/{2}.*$')
number = re.compile('(?<!\w)[0-9]+')
punct = re.compile('[,;\(\)\{\}]')
math = re.compile('[+-\/*]')
logic = re.compile('={3}|!=|<=|>=|<|>')
funct = re.compile('\w+(?=\s*\()\b')

path = Path(__file__).parent / '../resources/code_snippets'
code_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.txt')]
for file in code_files:
    file_path = path / file
    target_path = path / (file.removesuffix('.txt') + '.html')
    with file_path.open() as f, target_path.open('w+') as t:
        for line in f:
            # print(line)
            print(comment.search(line))

# with path.open() as f:
#     [print(line) for line in f]

#codeblocks = [open]