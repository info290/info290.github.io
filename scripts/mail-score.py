import csv
import webbrowser


entries = []

with open('class-review.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    rows = [*reader]
    headers = rows[0]
    rows = rows[1:]
    for i, row in enumerate(rows):
        entries.append({'id': i + 1, **{
            h: r
            for h, r in zip(headers, row)
        }})

title = '[INFO 290T] Class Reviews Progress'
class_size = 17
exclude = set([14])

for e in entries:
    eid = e['id']
    if eid > class_size or eid in exclude:
        continue
    name = e['Name']
    fname, lname = reversed(name.split(', '))
    email = e['Email Address']
    score = e['Final']

    s = 'mailto:'
    s += email
    s += '?cc=adityagp@berkeley.edu'
    s += f'&subject={title}'
    s += f'&body=Hello {fname},%0D%0A%0D%0A'
    s += f'Your class reviews score is {score}/10.%0D%0A%0D%0A'
    s += 'Please let me know if you have any questions.%0D%0A%0D%0A'
    s += 'Best,%0D%0AMick'
    s = s.replace(' ', '%20')
    print(s)
    webbrowser.open(s)


