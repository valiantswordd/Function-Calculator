import math

def calcular_afim():
    print("\n--- Função Afim: f(x) = ax + b ---")
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        
        if a == 0:
            print("Isso é uma função constante. Não possui raiz a menos que b também seja 0.")
        else:
            raiz = -b / a
            print(f"Raiz da função afim: x = {raiz}")
    except ValueError:
        print("Erro: Digite apenas números.")

def calcular_quadratica():
    print("\n--- Função Quadrática: f(x) = ax² + bx + c ---")
    try:
        a = float(input("Digite o valor de a: "))
        if a == 0:
            print("Se 'a' é 0, a função não é quadrática! Calculando como afim...")
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            # No caso de ax² + bx + c com a=0, vira bx + c
            if b != 0: print(f"Raiz: x = {-c/b}")
            return

        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        delta = (b**2) - (4 * a * c)
        print(f"\nDelta (Δ) = {delta}")

        if delta < 0:
            print("A função não possui raízes reais (Δ < 0).")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"A função possui uma raiz real: x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"A função possui duas raízes reais:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            
    except ValueError:
        print("Erro: Digite apenas números válidos.")

def menu():
    while True:
        print("\n" + "="*30)
        print("   SUPER CALCULADORA DE RAÍZES")
        print("="*30)
        print("1. Função Afim (1º grau)")
        print("2. Função Quadrática (2º grau)")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            calcular_afim()
        elif opcao == '2':
            calcular_quadratica()
        elif opcao == '3':
            print("Saindo... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
