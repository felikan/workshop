import re
from collections import OrderedDict
from os import listdir, replace
from os.path import isfile, join
from pathlib import Path

exclude_html_tag = '(?:</[^>]*>(?:<[^>]*/>)?)|(?:<[^>]*>.*?</[^>]*>(?:<[^>]*/>)?)|'

regex = OrderedDict()
regex["comment"] = re.compile(exclude_html_tag+'(\/{2}.*$)')
regex["funct"] = re.compile(exclude_html_tag+'(\w+(?=\s*\())')
regex["number"] = re.compile(exclude_html_tag+'((?<!\w)[0-9]+)')
regex["punct"] = re.compile(exclude_html_tag+'([,;\(\)\{\}])')
regex["math"] = re.compile(exclude_html_tag+'([+-\/*])')
regex["logic"] = re.compile(exclude_html_tag+'(={3}|!=|<=|>=|<|>)')

path = Path(__file__).parent / '../resources/code_snippets'
code_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.txt')]
for file in code_files:
    file_path = path / file
    target_path = path / (file.removesuffix('.txt') + '.html')
    with file_path.open() as f, target_path.open('w+') as t:
        t.write("<code class='codeblock'>")
        for i, line in enumerate(f):
            # print('line {nr}: {line}'.format(nr=i, line=line))
            target_line = line
            for key, value in regex.items():
                matches = value.finditer(target_line)
                # print("{type}s: {m}".format(type=key, m=list(matches)))
                for i, m in enumerate(matches):
                    # print('match #{nr}: {match}'.format(nr=i, match=m))
                    match = list(value.finditer(target_line))[i]
                    if match.group(1):
                        html_tag = '<span class="{token_class}">{content}</span>'.format(token_class=key, content = match.group(1))
                        target_line = target_line[:match.start()]+html_tag+target_line[match.end():]
            if (target_line == "\n"):
                target_line = "</br>"
            t.write("<p>"+target_line+"</p>")
        t.write("</code>")