FROM postgres:11-alpine

COPY data/most_recent_event.sql /docker-entrypoint-initdb.d/
COPY data/task_dummy.sql /docker-entrypoint-initdb.d/
COPY data/ufc_master.sql /docker-entrypoint-initdb.d/
COPY data/upcoming_event.sql /docker-entrypoint-initdb.d/

