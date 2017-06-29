# gnuradio-nn

## Build the Docker Image
$ docker build -t gnuradio-nn .

## Run it to put it in the docker ps history
docker run -it \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
gnuradio-nn

## Extact out the id of the last run container
export containerId=$(docker ps -l -q)

## Allow the ID of the last run container to access the hosts X11 server
xhost +local:`docker inspect --format='{{ .Config.Hostname }}' $containerId`

## Restart the container and it should connect to the hosts X11 server
docker start $containerId