FROM astrocrpublic.azurecr.io/runtime:3.0-2

# Instala bibliotecas adicionais necessárias para as DAGs
RUN pip install --no-cache-dir requests