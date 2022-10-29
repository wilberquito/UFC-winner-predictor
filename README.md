# ufc

I'll try to predict winners next clash

## Enviroment instruccions

https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a

## Build or update the image

```
    docker build -t jupyterlab:latest
```

## Awake temporal container

```
    docker run --rm -it -p 8888:8888 jupyterlab:latest
```

## Awake services using docker compose 

```
    docker compose up
```

### If you get an error starting your external volume

```
    docker volume create <volume-name>
```


