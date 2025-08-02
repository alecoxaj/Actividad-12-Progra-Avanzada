print("Bienvenido al programa de cálculo de promedios")

try:
    estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
except:
    print("ERROR, Ingresa un número válido.")
else:
    i = 1
    while i <= estudiantes:
        print(f"\nEstudiante {i}: ")

        nombre = ""
        while True:
            nombre = input("Ingresa el nombre del estudiante: ")
            if nombre == "":
                print("ERROR, El nombre no puede estar vacío")
            else:
                try:
                    float(nombre)
                    print("ERROR, el nombre no puede ser un número.")
                except:
                    break
        notas_valida = False
        while True:
            try:
                notas = int(input(f"¿Cuántas notas tiene {nombre}?: "))
                notas_valida = True
            except ValueError:
                print("ERROR, Ingresa un número válido")
            except Exception as e:
                print("Se produjo un error inesperado.", e)
            if notas_valida:
                break

        try:
            total = 0
            if notas != 0:
                j = 1
                while j <= notas:
                    nota = float(input(f"Ingresa la nota {j}: "))
                    total += nota
                    j += 1

                promedio = total / notas
                print(f"El promedio de {nombre}: es {promedio}")
            else:
                print("No se puede calcular promedio con 0 notas.")

        except ValueError:
            print("ERROR, debes ingresar números válidos")
        except TypeError:
            print("ERROR, no puedes combinar diferentes tipos de texto.")
        except ZeroDivisionError:
            print("ERROR, no puedes dividir por cero.")
        except Exception as e:
            print("Se produjo un error inesperado.", e)
        else:
            print("Estudiante procesado correctamente.")
        finally:
            print("Programa finalizado.")
            i += 1

