# ufc

I'll try to predict winners next clash

## Develop

### Create local environment for dependencies

```
    python3 -m venv /path/to/new/virtual/environment
```

### Install dependencies using pip

```
    pip install -r /path/to/requirements.txt
```

### Run Jupyter in your machine

```
    jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
```

### Postgres container

```
    docker run -d \
        --name <name> \
        -p 5432:5432 \
        -e POSTGRES_PASSWORD=<password> \
        -v /postgres/data:/var/lib/postgresql/data \
        postgres:latest
```

You can import csv using dbeaver but for export a hole database you need to use `pg_dump`

```
    pg_dump -U <user> -W -h localhost ufc > ufc.sql
```

### Mongo container
```
    docker run -d \ 
            -p 27017:27017  \
            --name <name> \
            -e MONGO_INITDB_ROOT_USERNAME=mongo \
            -e MONGO_INITDB_ROOT_PASSWORD=mongo \
            mongo:latest
```

## Deliver

https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a

### Build the project

sudo sh Make.sh

### Build or update the jupyterlab image

```
    cd wkdir/ \
    docker build -t jupyterlab:latest
```

### Build or update the postgres image

```
    cd postgres/ \
    docker build -t postgreslab:latest
```

### Awake temporal container

```
    docker run --rm -it -p 8888:8888 jupyterlab:latest
```

### Awake services using docker compose 

```
    docker compose up
```

#### If you get an error starting because of the external volume (see docker-compose.yaml)

```
docker volume create <volume-name>
```


