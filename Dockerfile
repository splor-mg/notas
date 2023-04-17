FROM rocker/r-ver:4.2.3

WORKDIR /project

RUN /rocker_scripts/install_python.sh
RUN /rocker_scripts/install_quarto.sh

COPY requirements.txt .
COPY DESCRIPTION .

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends libxt6
RUN python -m pip install -r requirements.txt
RUN Rscript -e "install.packages('renv')" && Rscript -e 'renv::install()'

ENTRYPOINT ["/bin/bash"]
