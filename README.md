# web scraping para extraccion de infromacion de vehiculos a partir de sus placas

Obtener infromacion de la página publica de consultas vehiculares a través del número de placa los modelos de carros,
tipo de servicio que prestan, años de los vehículos, etc. Para realizar análisis de posibles provincias donde se podrían colocar ciertos tipos de vehículos,
podría ser de acuerdo a su zona geográfica,modelo más utilizado, verificar la vida útil, etc.

para ejecutar el script es necesario tener instalado las siguientes bibliotecas>

```
pip install requests
pip install beautifulsoup4
```

El script se debe ejecutar de la siguiente manera:

```
python consulta_placas.py
```

Actualmente se extrae los siguientes campos a partir de un numero de placa del vehiculo "NUMERO_PLACA"
- MARCA
- COLOR
- ANIO DE MATRICULA
- MODELO
- CLASE
- FECHA DE MATRICULA
- ANIO
- SERVICIO
- FECHA DE CADUCIDAD

Esto nos retorna un archivo .CSV con informacion de todas las placas ingresadas
