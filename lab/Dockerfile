FROM continuumio/miniconda3:4.10.3p1

WORKDIR /project

COPY ./README.md /project
COPY ./data /project/data
COPY ./notebooks /project/notebooks
COPY ./requirements.txt requirements.txt

RUN conda install --file requirements.txt

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]

