grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
spisok=list(students)
spisok.sort()
a=0
jurnal = {}
for i in spisok:
    jurnal.update({spisok[a]: (sum(grades[a]) / len(grades[a]))})
    a=a+1
else: print(jurnal)

