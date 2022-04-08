FROM nvidia/cuda:10.2-devel-ubuntu18.04

RUN apt-get update && apt-get install -y curl
ENV PATH=/opt/conda/bin:$PATH
RUN curl -L -v -o ~/miniconda.sh -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && chmod +x ~/miniconda.sh && ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh && /opt/conda/bin/conda install -y python=$PYTHON_VERSION conda-build pyyaml numpy ipython&& /opt/conda/bin/conda clean -ya # buildkit 


RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN git clone https://github.com/vqdang/hover_net
RUN conda env create -f ./hover_net/environment.yml

ENV PATH /opt/conda/envs/hovernet/bin:$PATH #add to path to make conda accessible

RUN echo "source activate hovernet" > ~/.bashrc \
	&& pip install torch==1.6.0 torchvision==0.7.0 notebook --user    

#need for notebook to be accessible
ENV PATH=~/.local/bin:$PATH 
ENV PATH=/opt/conda/bin:$PATH

RUN echo "source activate hovernet" > ~/.bashrc \
	&& apt-get update && apt install -y git
    
RUN echo "source activate hovernet" > ~/.bashrc# #activate hovernet env
