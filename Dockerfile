#Base image had gpu configured, conda installed, git installed. you can install any other image
FROM usmanawais/pytorch-gpu-env:latest
RUN git clone https://github.com/vqdang/hover_net
RUN conda env create -f ./hover_net/environment.yml
RUN echo "source activate hovernet" > ~/.bashrc
ENV PATH /opt/conda/envs/hovernet/bin:$PATH
RUN pip install torch==1.6.0 torchvision==0.7.0 notebook --user
