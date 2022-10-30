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

## Docker 

https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a

### Build or update the image

```
    docker build -t jupyterlab:latest
```

### Awake temporal container

```
    docker run --rm -it -p 8888:8888 jupyterlab:latest
```

### Awake services using docker compose 

```
    docker compose up
```

#### If you get an error starting your external volume

```
    docker volume create <volume-name>
```


