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

nano /etc/profile.d/java.sh
  #/bin/bash
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
  
reboot

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

After confirming that the nifi instance is functional download and extract the zip file for this repository into the Apache Nifi installation folder. 

Open the directory in a terminal and set the upstream branch

git push --set-upstream <host> <branch>


download the latest mariadb java connector and place into nifi lib folder