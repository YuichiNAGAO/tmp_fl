FROM nvidia/cuda:10.2-devel-ubuntu18.04



RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    pkg-config \
    software-properties-common
RUN apt-get install -y \
    inkscape \
    jed \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    libcurl3-dev \
    libfreetype6-dev \
    libzmq3-dev \
    libcupti-dev \
    pkg-config \
    libav-tools \
    libjpeg-dev \
    libpng-dev \
    zlib1g-dev \
    locales
RUN apt-get install -y \
    sudo \
    rsync \
    cmake \
    g++ \
    swig \
    vim \
    git \
    curl \
    wget \
    unzip \
    zsh \
    git \
    screen \
    tmux \
    openssh-server
RUN apt-get update && \
    apt-get install -y pciutils net-tools iputils-ping && \
    apt-get install -y htop
RUN add-apt-repository ppa:openjdk-r/ppa \
    && apt-get update \
    && apt-get install -y \
    openjdk-7-jdk \
    openjdk-7-jre-headless
    

ENV HOME /workspace
WORKDIR $HOME


RUN wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.1.tar.gz && \
    gunzip -c openmpi-4.0.1.tar.gz | tar xf - && cd openmpi-4.0.1 && \
	mkdir build && cd build/ && \
	../configure --prefix=/usr --with-cuda --enable-mpi-thread-multiple && \
	make -j $(nproc) all && \
	make install && \
	ldconfig


ENV PYTHON_VERSION=3.8
RUN curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    sh ~/miniconda.sh -b -p $HOME/conda && \
    rm ~/miniconda.sh
RUN $HOME/conda/bin/conda update -n base conda
RUN $HOME/conda/bin/conda create -y --name pytorch-py$PYTHON_VERSION python=$PYTHON_VERSION numpy pyyaml scipy ipython mkl mkl-include
RUN $HOME/conda/bin/conda install --name pytorch-py$PYTHON_VERSION -c soumith magma-cuda100
RUN $HOME/conda/bin/conda install --name pytorch-py$PYTHON_VERSION scikit-learn
RUN $HOME/conda/envs/pytorch-py$PYTHON_VERSION/bin/pip install pytelegraf pymongo influxdb kubernetes jinja2
ENV PATH $HOME/conda/envs/pytorch-py$PYTHON_VERSION/bin:$PATH



