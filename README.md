# ufc

I'll try to predict winners next clash

## Develop

### Postgres container

```
    cd postgres/ \
    docker build -t postgresdev:latest .
```

```
    docker run -d \
        --name posgresdev \
        -p 5432:5432 \
        -e POSTGRES_PASSWORD=postgres \
        postgresdev:latest
```

You can create a dump with all postgres schema using `pg_dump`

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

### DNS resolution

As I don't want to change dns name before run docker compose what I do is

add dns resolution inside '/etc/hosts' file. [source](https://stackoverflow.com/questions/19652555/add-static-dns-entry)

### Run Jupyter in your machine

#### Create local environment for dependencies

```
    python3 -m venv /path/to/new/virtual/env
```

#### Install dependencies using pip

```
    pip install -r /path/to/requirements.txt
```

Not you can run jupyter for work

```
    jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
```

## Deliver

https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a

### Build the project

```
    sudo sh Make.sh
```

### Awake services using docker compose 

```
    docker compose up
```

### Turn off services using docker compose 

```
    docker compose up
```

