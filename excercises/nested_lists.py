'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    records = []
    min_score = float('inf')
    second_min_score = float('inf')
    
    for _ in range(int(input())):
        name = input().strip()
        score = float(input().strip())
        records.append([name, score])
        
        if score < min_score:
            second_min_score = min_score
            min_score = score
        elif min_score < score < second_min_score:
            second_min_score = score
    
    second_min_students = [name for name, score in records if score == second_min_score]
    second_min_students.sort()
    
    for student in second_min_students:
        print(student)
