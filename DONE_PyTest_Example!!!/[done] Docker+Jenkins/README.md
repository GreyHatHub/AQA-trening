На основе: https://progler.ru/blog/kak-nastroit-jenkins-v-konteynere-docker


sudo apt-get install docker.io
docker pull jenkins/jenkins
docker run -d --name jenkins -p 8080:8080 -v $PWD/jenkins/ jenkins/jenkins
http://127.0.0.1:8080
docker logs jenkins
