from sys import argv
from src.models.instance import Instance


def main():
    if len(argv) >= 2:
        instance_name: str = argv[1]
        try:
            instance: Instance = Instance(instance_name)
            instance.execute()
        except Exception:
            print("L'instance \"" + instance_name + "\" est introuvable ou n'a pas pu être exécutée.")
    else:
        print("Veuillez renseigner un nom d'instance en argument.")


if __name__ == '__main__':
    main()
