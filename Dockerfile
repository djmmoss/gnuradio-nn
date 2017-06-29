FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python-pip gnuradio cmake
RUN pip install --upgrade pip && pip install numpy tqdm h5py tensorflow keras

WORKDIR /app
ADD . /app

# Setup GNURadio Neural Network
RUN mkdir build && \
	cd build && \
	cmake ../gr-neural_networks && \
	make && \
	make install && \
	ldconfig

CMD ["grcc", "-e", "nn_learn_example.grc"]