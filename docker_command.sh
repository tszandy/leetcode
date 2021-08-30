docker build -f Dockerfile_cpp -t tszandy/ubuntu_cpp:0.01 . 

#windows
docker run --rm -v C:\Users\44498\Desktop\leetcode\cpp_program:/home/wei/cpp_program -it tszandy/ubuntu_cpp:0.01 /bin/bash

#ubuntu
docker run --rm -v /home/ice/leetcode/cpp_program:/home/wei/cpp_program -it tszandy/ubuntu_cpp:0.01 /bin/bash

#mac
docker run --rm -v /Users/weixie/leetcode/cpp_program:/home/wei/cpp_program -it tszandy/ubuntu_cpp:0.01 /bin/bash

#docker command 

#docker list all containers
docker ps -a

#docker list all running containers
docker ps

#docker list all images
docker images

#docker list ip address of running container ${container_name_or_id}
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${container_name_or_id}

#docker run base ubuntu in detach mode --rm remove container when unrunning -t -i stdin interacitive
docker run --rm -ti ubuntu:18.04

#docker run base ubuntu in detach mode --rm remove container when unrunning -d detach -t -i stdin interacitive
docker run --rm -dti ubuntu:18.04

#docker run nvidia ubuntu runtime --gpus attached gpu 
docker run --rm --gpus all -dti nvidia/cuda:11.4.1-runtime-ubuntu18.04 /bin/bash

#docker run nvidia ubuntu runtime --gpus attached gpu 
docker run --rm --gpus all -ti nvidia/cuda:11.4.1-runtime-ubuntu18.04 /bin/bash

#rm all unrunning docker containers
docker container prune
docker rm $(docker ps -aq)

#docker 
docker attach ${container_name_or_id} --detach-keys "ctrl-a"


