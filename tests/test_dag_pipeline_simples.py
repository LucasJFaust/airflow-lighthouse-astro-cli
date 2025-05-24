# tests/test_dag_pipeline_simples.py

# Importa a função para carregar DAGs do Airflow
from airflow.models import DagBag

def test_dag_loaded_successfully():
    """
    Testa se a DAG 'dag_pipeline_simples' foi carregada corretamente
    sem erros de importação ou parsing.
    """
    dagbag = DagBag()  # Carrega todas as DAGs disponíveis no projeto
    dag = dagbag.get_dag("dag_pipeline_simples")

    # Verifica se a DAG foi realmente encontrada
    assert dag is not None, "DAG 'dag_pipeline_simples' não foi carregada."

    # Verifica se não há erros de importação
    assert len(dagbag.import_errors) == 0, f"Erros de importação encontrados: {dagbag.import_errors}"

def test_dag_has_expected_tasks():
    """
    Verifica se as tasks principais da DAG estão presentes.
    """
    dag = DagBag().get_dag("dag_pipeline_simples")

    # Lista esperada de task_ids da DAG
    expected_tasks = {
        "extrair_dados",
        "transformar_dados",
        "salvar_dados"
    }

    # Obtém os task_ids definidos na DAG
    dag_tasks = set(dag.task_ids)

    # Verifica se todas as tasks esperadas estão presentes
    for task in expected_tasks:
        assert task in dag_tasks, f"Task '{task}' não encontrada na DAG."
