# Airflow-Mini-Project
Learning the fundamentals of Apache Airflow through a hands-on mini-project. This demo project uses open APIs to collect data and applies a basic ETL (Extract, Transform, Load) pipeline using Airflow. 

## Details
Create a DAG to 
1. load ISS(International Space Station) location
2. Use OpenStreetMaps API to reverese geocode the address of the location

Sample output of Airflow UI- 
![alt text](image.png)

![alt text](image-1.png)

sample output:


Log message source details: sources=["/opt/airflow/logs/dag_id=iss_dag/run_id=manual__2025-06-01T11:02:47.640122+00:00/task_id=reverse_geocode/attempt=1.log"]
[2025-06-01, 16:32:52] INFO - DAG bundles loaded: dags-folder, example_dags: source="airflow.dag_processing.bundles.manager.DagBundlesManager"
[2025-06-01, 16:32:52] INFO - Filling up the DagBag from /opt/airflow/dags/iss_location.py: source="airflow.models.dagbag.DagBag"
[2025-06-01, 16:32:52] INFO - Task instance is in running state: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO -  Previous state of the Task instance: queued: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Current task name:reverse_geocode: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Dag name:iss_dag: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - The ISS currently is above: Municipio de Cañada de Gómez, Departamento Iriondo, 2505, Argentina.: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Done. Returned value was: Municipio de Cañada de Gómez, Departamento Iriondo, 2505, Argentina: source="airflow.task.operators.airflow.providers.standard.decorators.python._PythonDecoratedOperator"
[2025-06-01, 16:32:52] INFO -  latitude:-32.7150: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Pushing xcom: ti="RuntimeTaskInstance(id=UUID('01972b28-8e6d-7cf7-9e7a-b8096cc64955'), task_id='reverse_geocode', dag_id='iss_dag', run_id='manual__2025-06-01T11:02:47.640122+00:00', try_number=1, map_index=-1, hostname='02497a58636d', context_carrier={}, task=<Task(_PythonDecoratedOperator): reverse_geocode>, bundle_instance=LocalDagBundle(name=dags-folder), max_tries=2, start_date=datetime.datetime(2025, 6, 1, 11, 2, 51, 568020, tzinfo=TzInfo(UTC)), end_date=None, is_mapped=False)": source="task"
[2025-06-01, 16:32:52] INFO - longitude:-61.4837: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO -  :): chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Task instance in success state: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO -  Previous state of the Task instance: running: chan="stdout": source="task"
[2025-06-01, 16:32:52] INFO - Task operator:<Task(_PythonDecoratedOperator): reverse_geocode>: chan="stdout": source="task"