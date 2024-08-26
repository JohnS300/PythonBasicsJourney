'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    records= []
    min_record = float('inf')
    min_second_record = float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
        if min_record > score:
            min_second_record = min_record
            min_record = score
        elif (min_record < score) and (min_second_record > score):
            min_second_record = record
            
    second_to_last_records = [name for name,score in records if score==min_second_record]
    
    second_to_last_records.sort()
    
    for record in second_to_last_records:
        print(record)
