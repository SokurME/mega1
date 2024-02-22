import csv
def hash(s):
    p = 67
    m = 10 ** 9 + 9
    alph = ''.join([chr(i) for i in range(ord('А'), ord('я') + 1)])
    alph += ' '
    hash_ = 0
    k = 0
    for i in s:
        hash_ += s.index(i) + 1 * p ** k % m
        k += 1
    return hash_


students_with_hash = []
with open('students.csv', encoding="utf8") as f:
    reader = list(csv.DictReader(f, delimiter=','))
for row in reader:
    row['id'] = hash(row['Name'])
    print(row)
    students_with_hash.append(row)
with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writeheader()
    w.writerows(students_with_hash)
