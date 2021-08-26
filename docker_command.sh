docker build -f Dockerfile_cpp -t tszandy/ubuntu_cpp:0.01 . 

docker run -v /Users/weixie/leetcode/cpp_program:/home/wei/cpp_program -it tszandy:ubuntu_cpp /bin/bash
