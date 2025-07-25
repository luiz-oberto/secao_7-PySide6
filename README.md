# secao_7-PySide6
Repositório para estudos de PySide6

## Aula 340 - Instalando o Pyside6 no seu ambiente virtual
-> [DOCUMENTAÇÃO PYSIDE6](https://doc.qt.io/qtforpython-6/gettingstarted.html)

- Criando ambiente virtual
```bash
python -m venv env
source env/bin/activate
```

- Instalando PySide6
```bash
pip install pyside6
```

- Testando instalação
```bash
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
```
