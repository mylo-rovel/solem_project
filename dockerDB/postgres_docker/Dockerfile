FROM postgres:14.0

ADD /queries/ /docker-entrypoint-initdb.d/queries/
ADD deploy_schemas.sql /docker-entrypoint-initdb.d/
