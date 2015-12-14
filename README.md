➢	Higher level architecture:-

<img width="626" alt="screen shot 2015-12-06 at 11 17 11 am" src="https://cloud.githubusercontent.com/assets/13231166/11785035/9f495b8c-a2a5-11e5-9594-8356eeae57f9.png">


➢	 Components flow and integration

1.	Git:- User commit code on remote/local repo and that will be hook or schedule by Jenkins.
2.	Artifact Server:- Work as artifact storage which stores all deployment components and code based on specific build.
3.	Docker image Generator: -  Create individual docker image with specific build plan and number, bootstrap docker image with Chef for normalize configuration.
4.	Docker private Repo:- Get docker image from image generator and store locally as it is further use in deployment.
5.	Mesos cluster:- Push docker image into marathon than will generate container and leverage it into any of the slave. And finally it will produce deployment URL in which latest code reside.


➢	 prerequisite:-

1. SVN/git/Bitbucket repository
2. Jenkins Server :
      -> OS : CentOS 7
      -> Install package : OpenJDK 7 , jenkins, curl, Openssl-client
3. Artiface Server : 
      -> OS : CentOS 7
      -> Install package : curl, Openssl-client
4. Docker-Engine : 
      -> OS : Ubuntu 14.04 TLS
      -> Install package : curl, Docker, Openssl-client
5. Docker Private Repo :
      -> OS : Ubuntu 14.04 TLS
      -> Install package : curl, Docker, Openssl-client
6. Mesos Master : 
      -> OS : Ubuntu 14.04
      -> Install package : openJDK 8, mesos, zookeeper, marathon, curl
7. Mesos Slave :
      -> OS : Ubuntu 14.04 TLS
      -> Install package : openJDK 8, mesos, zookeeper

➢	 How to use :-
