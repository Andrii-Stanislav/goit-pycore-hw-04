import pathlib
import os

def total_salary(absolute_path):
    if not os.path.exists(absolute_path):
        return 'File does not exist'
    
    total_sum = 0
    total_employees = 0
    with open(pathlib.Path(absolute_path)) as file:
        for line in file:
            name, salary = line.strip().split(',')
            total_sum += int(salary.strip())
            total_employees += 1
    
    average_salary = total_sum / total_employees

    return f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average_salary}"
