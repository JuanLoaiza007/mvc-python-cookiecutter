#!/usr/bin/env python
import argparse
import subprocess
import sys


def print_debug(message):
    print(f"[manage.py]: {message}")


def main():
    parser = argparse.ArgumentParser(
        description="Administración de la aplicación"
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("configure", help="Prepara la aplicación")
    subparsers.add_parser("main", help="Ejecuta la función principal")
    subparsers.add_parser("run", help="Ejecuta la aplicación")
    subparsers.add_parser("other_command", help="Ejecuta otro comando")

    args = parser.parse_args()

    if args.command == "main":
        from src.main import main as main_command

        main_command()
    elif args.command == "configure":
        try:
            subprocess.run("git init .", shell=True)
            subprocess.run(
                "git config --global --add safe.directory .",
                shell=True,
            )
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    "requirements.txt",
                ]
            )
            subprocess.run("pre-commit install", shell=True)
            subprocess.run("pre-commit autoupdate", shell=True)
        except subprocess.CalledProcessError as e:
            print_debug(f"Error al instalar dependencias: {e}")
            sys.exit(1)

    elif args.command == "run":
        # from src.main import run

        # run()
        raise Exception("Not implemented yet")
    elif args.command == "other_command":
        # from src.main import other_command

        # other_command()
        raise Exception("Not implemented yet")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
