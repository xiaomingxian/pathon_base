import shutil

# shutil.move('/path/to/file.new', '/path/to/file')

if __name__ == '__main__':
    a = 0
    with open('aioa_demo.sql', 'r') as f:
        with open('oa_demo_source.sql', 'w') as g:
            for line in f.readlines():
                if 'INSERT '  not in line:
                    g.write(line)
