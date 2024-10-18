@echo off

REM Activar el entorno virtual
call .venv\Scripts\activate

REM Actualizar pip
pip install --upgrade pip

REM Instalar dependencias
pip install -r requirements.txt

REM Eliminar la carpeta "public"
rmdir /s /q public

REM Inicializar Reflex
reflex init

REM Exportar solo el frontend
reflex export --frontend-only

REM Descomprimir frontend.zip en la carpeta "public"
powershell -Command "Expand-Archive -Force frontend.zip -DestinationPath public"

REM Eliminar el archivo frontend.zip
del frontend.zip

REM Desactivar el entorno virtual
deactivate