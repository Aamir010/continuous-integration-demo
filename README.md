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

Note : You need to put Jenkins, Artifact, and Docker-engine  public key to all servers for password less access.

1. Jenkins Server :-
      -> List of Jenkins plugins :- GIT plugin, Shared Objects Plugin, SSH Agent Plugin, Subversion Plug-in, Environment File Plugin, Docker plugin
      -> Unzip Jenkins demo job and placed into local /var/lib/jenkins/jobs/ directory.
      -> Configure build job from jenkins URL and twink necessary parameters.
2. Artifact Server :-
      -> Create 3 directories like Artifacts, cookbooks, and scripts into /home/ dir.
      -> And placed associated git contains into /home/scripts and /home/cookbooks/ accordingly.
      -> you need to download chef 12.5 debian package and put into /home directory for docker bootstraping process. URL : curl -L https://www.opscode.com/chef/install.sh | bash

3. Docker Private Repo :-
      -> Run Docker private repository in containter, forward port on localhost and mount volume to store an image.


➢	Details on working prototype :- 
      
      • We are adopting PHP to create working prototype, but it can leverage all other programing languages as well.
        -> As we know it is hard to manage dependency in PHP projects, so I have created dependency.json file and this file should reside in each project and customize accordingly.
        <img width="233" alt="screen shot 2015-12-15 at 11 17 56 am" src="https://cloud.githubusercontent.com/assets/13231166/11803118/a4f543a2-a31d-11e5-89e4-73de9ef8ccd9.png">
      • You can trigger build from Jenkins with hook or schedule.  So when build was trigger than it will downloaded your source code from Git and dump that code in Artifact server with specific build name and build number so you can easily get what code running or you can also rollback your application from previous build.
      • After pulling code, Dependency. json file decoded and their values are injecting into Jenkins environment variables.
         -> Note:- Dependency. json is loosely coupled so there is no need to tightly follow or hardcoded json it is just need valid json format.
      • Automation scripts are copy to Jenkins, which handle automation of application deployment.
      • Jenkins build point into task executor which generate dockerfile and this file is also pushed to Artifact server. Based on docker file , Docker engine is generates a docker image.
         -> This docker image is bootstrap with Chef recipe, which install and customize webserver.
      • Generated docker image is pushed into private docker registry.
      • Now deployment task has been triggers which call marathon API and generate individual environment for a specific build. And resources are allocated based on dependency. json file, if there is no resource available in mesos cluster than application is on puts itself on waiting stage and deploys when resources are available on cluster.
      • Developers/QA/PM/Ops have access on Marathon UI on that they can lookup their build plan stage and having one unique URL by accessing that they have their working code.
      
      
➢	Best use cases :-
      • Create build plan that will triggers daily at 9 AM, so your QA will have latest code to test which developer coded yesterday and if environment breaks than developer is also easily rollback or found the bug.
      • You can also make build plan for release branch which will tasted as well after kickoff or from develop branch. And how you can easily maintain version of your application and you have clear picture about your project pipeline.
      • You can also try variation on resources section on dependency. json file  with you can have accurate information on what specific resources how your application performs.


      
