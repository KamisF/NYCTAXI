import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def main():
    # Lista de pacotes para instalar
    packages = []
    with open('requirements.txt', 'r') as f:
        packages = f.read().splitlines()

    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Instalando {package}...")
            install(package)

    # Aqui você pode colocar seu código principal
    print("Todas as dependências estão instaladas!")

if __name__ == "__main__":
    main()