#!/usr/bin/env python3
"""
CALCULADORA MODULAR - Taller de Git
Interfaz por consola con funciones separadas en módulos
"""

#HOLA MUNDO

import os
from operations.suma import sumar
from operations.resta import restar
from utils.helpers import limpiar_pantalla, mostrar_menu, obtener_numero

def main():
    """Función principal de la calculadora"""
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("       CALCULADORA MODULAR")
        print("=" * 40)
        print()
        
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                realizar_suma()
            elif opcion == "2":
                realizar_resta()
            elif opcion == "3":
                print("\n¡Gracias por usar la calculadora!")
                break
            else:
                print("\n Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                
        except ValueError as e:
            print(f"\n Error: {e}")
            input("Presione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario.")
            break

def realizar_suma():
    """Maneja la operación de suma"""
    print("\n" + "=" * 40)
    print("           SUMA")
    print("=" * 40)
    
    a = obtener_numero("Ingrese el primer número: ")
    b = obtener_numero("Ingrese el segundo número: ")
    
    resultado = sumar(a, b)
    
    print(f"\nResultado: {a} + {b} = {resultado}")
    input("\nPresione Enter para continuar...")

def realizar_resta():
    """Maneja la operación de resta"""
    print("\n" + "=" * 40)
    print("           RESTA")
    print("=" * 40)
    
    a = obtener_numero("Ingrese el minuendo: ")
    b = obtener_numero("Ingrese el sustraendo: ")
    
    resultado = restar(a, b)
    
    print(f"\n Resultado: {a} - {b} = {resultado}")
    input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()