## Entorno Virtual

# Creación

```python
               //Nombre del entorno
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
