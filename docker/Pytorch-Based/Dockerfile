FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-devel


RUN apt-get -y update && apt-get -y install --no-install-recommends wget parallel
RUN pip install -U pip && pip install ipython jupyterlab

WORKDIR /workspace

ENV SHELL /bin/bash

COPY ./entrypoint.sh /
ENTRYPOINT sh /entrypoint.sh


RUN wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.1.tar.gz && \
    gunzip -c openmpi-4.1.1.tar.gz | tar xf - && cd openmpi-4.1.1 && \
	mkdir build && cd build/ && \
	../configure --prefix=/usr --with-cuda --enable-mpi-thread-multiple && \
	make -j $(nproc) all && \
	make install && \
	ldconfig
    
    
RUN apt install -y --no-install-recommends openssh-client openssh-server && \
		mkdir -p /var/run/sshd