def saludar(nombre: str) -> str:
    return f"¡Hola, {nombre}! Bienvenido al laboratorio."

def main():
    print("=== GESTIÓN DE PROYECTOS CON GIT Y GITHUB ===")
    usuario = input("Por favor, ingresa tu nombre: ").strip()
    if usuario:
        print(saludar(usuario))
    else:
        print("¡Hola, estudiante!")

if __name__ == "__main__":
    main()
