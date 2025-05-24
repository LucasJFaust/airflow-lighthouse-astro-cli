# Usa uma versão moderna do Astronomer Runtime (recomendado pela Astronomer)
FROM quay.io/astronomer/astro-runtime:8.2.0

# Instala bibliotecas adicionais necessárias
RUN pip install --no-cache-dir requests
