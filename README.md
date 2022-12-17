## Entorno Virtual

# Creación

```python
// interprete -m modulo nombre_carpeta
python -m venv venv
```

# Activar el entorno

```python
# Windows (PowerShell)
cd venv
cd Scripts
activate.bat | Activate.ps1
cd ..
cd ..

# Windows (GitBash)
source venv/Scripts/activate

# Linux | MacOS
source venv/bin/activate
```

# Desactivar el entorno

```python
# Windows (PowerShell)
cd venv
cd Scripts
deactivate.bat
cd ..
cd ..

# Windows (GitBash) | Linux | MacOS
deactivate
```

## PIP

# Listar las librerias instaladas

```python
pip list
```

# Instalar librerias

```python
pip install nombre_libreria
```

# Desinstalar librerias

```python
pip uninstall nombre_libreria
```

# Crear archivo de instalación de paquetes (requirements.txt)

```python
pip freeze > requirements.txt
```

# Instalar librerias desde requirements.txt

```python
pip install -r requirements.txt
```
