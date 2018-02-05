import os

num_checked = 0
num_changed = 0
files_ignored = []

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') and file != 'delete_answers.py':
            num_checked += 1
            with open(os.path.join(subdir, file), 'r', encoding='utf8') as f:
                document = f.readlines()
                question = None
                for i, line in enumerate(document):
                    if not line.startswith('#') and not line.startswith('\n'):
                        question = document[:i]
                        break

            if question:
                num_changed += 1
                with open(os.path.join(subdir, file), 'w', encoding='utf8') as f:
                    f.writelines(question)
            else:
                files_ignored.append(os.path.join(subdir, file))


print('Removed answers from {} of {} files'.format(num_changed, num_checked))
if files_ignored:
    print('Files not modified:')
    for file in files_ignored:
        print(file)
