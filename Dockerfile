FROM mysql

ENV MYSQL_DATABASE=mysqlsampledatabase \
    MYSQL_ROOT_PASSWORD=root_password

ADD init.sql /docker-entrypoint-initdb.d

EXPOSE 3306
