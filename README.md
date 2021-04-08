# nifi_flow

## Project Installation
Download Apache nifi Version 1.13.1 and appropriate nifi toolkit from

https://nifi.apache.org/download.html

    nifi-1.13.1-bin.tar.gz ( asc, sha256, sha512 )
    nifi-toolkit-1.13.1-bin.tar.gz ( asc, sha256, sha512 )

Or access these files from your local server.

Open a terminal console and run the following to install  a java JDK

    sudo apt-get update
    sudo apt-get install openjdk-8.jdk

Get the java installation directory

    update-alternatives --config java

Create a configuration file for the java environment config and reboot

Create a nifi instance configuration file - 
    
    <nifi installation location>/instance_props/instance_props.conf
  
Include the following values
    
    python_venv=<some_location>
    mariadb_dev_host=<somehost>
    mariadb_dev_port=<someport>
    mariadb_dev_username=<blah>
    nifi_installation_location=<dir>
    

Run the follwing
    
    nano /etc/profile.d/java.sh/bin/bash
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
  
reboot the system

Extract the nifi package and move to a suitable install location.

    tar -zxvf nifi01.13.1-bin.tar.gz
    mv nifi-1.13.1 <destination>

CD to <destination>
  
Install Nifi

    sudo bin/nifi.sh install

Start the service

    /etc/init.d/nifi start

Open a browser and navigate to localhost:8080/nifi
You may need to refresh after a few seconds.

# Running Multiple Instances (Dev, Test, etc)
Create a copy of the nifi folder and rename it appropriately

Update instance_props/instance_props.conf with unique setting for any target database/server/python venvs unique to the instance. ie A development database.

Update /conf/nifi.properties
    
    nifi.web.port=<new port number ie; 8081>
    
Remove nifi.properties from the git workflow as to not commit the port change value

    git update-index --skip-workflow conf/nifi.properties

Update /bin/nifi.sh

    SVC_Name=<new service name ie; nifi_dev>
    
Navigate to the new instance folder and open a terminal window. Execute

    sudo ./bin/nifi.sh install
    ./bin/nifi.sh start
    
Confirm instance status
    
    ./bin/nifi.sh status
    
Navigate to localhost:<port number>

*Note: Loading the second instance can sometimes take a little longer than one would expect.*
