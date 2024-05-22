# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

{% if cookiecutter.language == "english" %}

## Topics

- [Setup](#setup)
  - [Requirements](#requirementss)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running application](#running-application)
- [License](#license)

## Setup

### Requirements

The following are required for the application to function properly:

- Python `{{cookiecutter.python_version}}+`.

### Installation

To run the project, follow these steps:

1. Clone the repository:

```
git clone repository_url
```

2. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the main.py from the root folder:

### Running application

#### on Windows

```
python main.py
```

#### on Linux/MacOS

```
python3 main.py
```

## License

{% if cookiecutter.license == "MIT" %}
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
{% elif cookiecutter.license == "Unlicense" %}
This project is not licensed following the [Unlicensed template](https://unlicense.org/).
{% endif %}

{% elif cookiecutter.language == "español" %}

## Temas

- [Setup](#setup)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
- [Uso](#uso)
  - [Ejecución de la aplicación](#ejecución-de-la-aplicación)
- [Licencia](#licencia)

## Setup

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio:

```
git clone url_del_repositorio
```

2. Instala las dependencias:

```
pip install -r requirements.txt
```

## Uso

Ejecute el main.py desde el directorio raíz:

### Ejecución de la aplicación

#### en Windows

```
python main.py
```

#### en Linux/MacOS

```
python3 main.py
```

## Licencia

{% if cookiecutter.license == "MIT" %}
Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).
{% elif cookiecutter.license == "Unlicense" %}
Este proyecto no está licenciado siguiendo la [Plantilla de Unlicense](https://unlicense.org/).
{% endif %}

{% endif %}
