import hashlib
import csv
lines = csv.reader(open('./words.txt'))
for line in lines:

    result = hashlib.md5()
    result.update(f'valentine:{line[0]}'.encode('utf-8'))
    if result.hexdigest() == '485367564cf25ea630623dc403d97ced':
        print(line)
