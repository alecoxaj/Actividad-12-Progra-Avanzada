print("Bienvenido al programa de cálculo de promedios")

try:
    estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
    for i in range(estudiantes):
        print(f"Estudiante {i+1}")
        input(f"Ingresa el nombre del estudiante: ")
        nota = int(input("Ingresa la cantidad de notas: "))
        for j in range(nota):
           nota = input(f"Ingresa la nota {i+1}")
        try:
            promedio = nota/estudiantes
        except ValueError:
            print("ERROR, debes ingresar números válidos")
        except TypeError:
            print("ERROR, no puedes combinar diferentes tipos de texto.")
        except ZeroDivisionError:
            print("ERROR, no puedes dividir por zero.")
        except Exception as e:
            print("Se produjo un error inesperado.", e)
        else:
            print("")
