# Ejercicio 7

def computegrade(grade):
    if (grade > 0.9 and grade < 1.0):
        grade = "A"
    elif (grade > 0.8 and grade < 0.9):
        grade = "B"
    elif (grade > 0.7 and grade < 0.8):
        grade = "C"
    elif (grade > 0.6 and grade < 0.7):
        grade = "D"
    elif (grade > 0 and grade < 0.6):
        grade = "F"
    else:
        grade = "Error, calificación no válida"
    return grade

try:
    score = float(input("Ingrese la calificación (0.1 - 1.00): "))
    grade = computegrade (score)
    print ("El gradondensu calificación es:", grade)
except:
    print ("Error, calificación no válida")
    