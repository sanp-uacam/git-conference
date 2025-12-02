"""
Funciones auxiliares para la interfaz de consola
"""

import os
import platform

def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo"""
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("MENÚ PRINCIPAL")
    print("-" * 40)
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Salir")
    print("-" * 40)

def obtener_numero(mensaje: str = "Ingrese un número: ") -> float:
    """
    Solicita un número al usuario con validación
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        float: Número ingresado por el usuario
        
    Raises:
        ValueError: Si el usuario ingresa algo no numérico
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            
            # Permitir salir con 'q' o 'quit'
            if entrada.lower() in ['q', 'quit', 'exit', 'salir']:
                raise KeyboardInterrupt("Usuario canceló la operación")
            
            # Convertir a float
            numero = float(entrada)
            return numero
            
        except ValueError:
            print(" Error: Debe ingresar un número válido.")
            print("   Ejemplos: 5, 3.14, -2.5")
            print("   O escriba 'q' para cancelar")

def mostrar_resultado(operacion: str, a: float, b: float, resultado: float):
    """
    Muestra el resultado de una operación formateado
    
    Args:
        operacion (str): Nombre de la operación
        a (float): Primer número
        b (float): Segundo número
        resultado (float): Resultado de la operación
    """
    print("\n" + "═" * 50)
    print(f"  OPERACIÓN: {operacion.upper()}")
    print("═" * 50)
    print(f"  Números: {a} y {b}")
    print(f"  Resultado: {resultado}")
    print("═" * 50)

if __name__ == "__main__":
    # Pruebas del módulo de helpers
    print("Módulo de helpers - Pruebas:")
    print(f"Número ingresado: {obtener_numero('Ingrese un número de prueba: ')}")