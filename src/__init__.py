from sys import argv
from src.models.instance import Instance


def main():
    if len(argv) >= 2:
        instance_name: str = argv[1]
        instance: Instance = Instance(instance_name)
        instance.execute()
    else:
        print("Veuillez renseigner un nom d'instance en argument.")


if __name__ == '__main__':
    main()
