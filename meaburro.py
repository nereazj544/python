def cal():

  print("Calculadora simple")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")

  # Obtener la opción del usuario
    opcion = input("Seleccione una operación (1-4): ")
    
    # Obtener los números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Realizar la operación seleccionada
    if opcion == "1":
        resultado = num1 + num2
        operacion = "suma"
    elif opcion == "2":
        resultado = num1 - num2
        operacion = "resta"
    elif opcion == "3":
        resultado = num1 * num2
        operacion = "multiplicación"
    elif opcion == "4":
        if num2 != 0:  # Evitar división por cero
            resultado = num1 / num2
            operacion = "división"
        else:
            return "Error: División por cero"
    else:
        return "Opción no válida"
    
    return f"El resultado de la {operacion} es: {resultado}"

# Ejecutar la calculadora
print(calculadora())
