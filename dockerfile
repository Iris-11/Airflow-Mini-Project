FROM apache/airflow:3.0.0

USER root

# Install dependencies for Oracle Instant Client
RUN apt-get update && apt-get install -y libaio1 wget unzip && rm -rf /var/lib/apt/lists/*

# Download and unzip Oracle Instant Client 21.9 (change version if needed)
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basic-linux.x64-21.9.0.0.0.zip && \
    wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-sdk-linux.x64-21.9.0.0.0.zip && \
    unzip instantclient-basic-linux.x64-21.9.0.0.0.zip -d /opt/oracle/ && \
    unzip instantclient-sdk-linux.x64-21.9.0.0.0.zip -d /opt/oracle/ && \
    rm instantclient-basic-linux.x64-21.9.0.0.0.zip instantclient-sdk-linux.x64-21.9.0.0.0.zip

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_9:$LD_LIBRARY_PATH
ENV ORACLE_HOME=/opt/oracle/instantclient_21_9

# Install cx_Oracle Python package
RUN pip install cx_Oracle

USER airflow
