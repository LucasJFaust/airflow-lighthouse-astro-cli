# tests/dags/test_dag_example.py

# Importa o pytest para criar testes e o DagBag para carregar as DAGs do projeto
import pytest
from airflow.models import DagBag

# Instancia o DagBag, que é responsável por carregar todas as DAGs do diretório configurado
# Ele simula o comportamento do Airflow durante o parsing das DAGs
# Isso é útil para garantir que nenhuma DAG esteja com erro de sintaxe ou importação
dagbag = DagBag()

def get_dags():
    """
    Retorna uma lista de tuplas com:
    - dag_id: o identificador da DAG
    - objeto DAG carregado
    - localização do arquivo onde a DAG está definida

    Aqui restringimos apenas à DAG 'dag_pipeline_simples', que é a única neste projeto.
    """
    return [
        (dag.dag_id, dag, dag.fileloc)
        for dag in dagbag.dags.values()
        if dag.dag_id == "dag_pipeline_simples"
    ]

# Este decorador parametriza o teste para que ele rode para cada DAG retornada em get_dags()
# Usamos o caminho do arquivo como ID para facilitar identificação de onde veio o erro em caso de falha
@pytest.mark.parametrize(
    "dag_id,dag,fileloc", get_dags(), ids=[x[2] for x in get_dags()]
)
def test_dag_retries(dag_id, dag, fileloc):
    """
    Teste que verifica se a DAG possui pelo menos 2 tentativas de retry configuradas.
    Isso é uma boa prática para tornar pipelines mais resilientes a falhas temporárias.
    """
    retries = dag.default_args.get("retries")

    # Garante que o campo 'retries' foi definido nos argumentos padrão da DAG
    assert retries is not None, f"{dag_id} em {fileloc} não tem retries definidos."

    # Verifica se o número de retries é no mínimo 2
    assert retries >= 2, f"{dag_id} em {fileloc} deve ter retries >= 2."
