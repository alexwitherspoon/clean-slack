# clean-slack
python script/docker to clean Slack Files

* Github repo: [alexwitherspoon/clean-slack](https://github.com/alexwitherspoon/clean-slack)
* Dockerhub repo: [alexwitherspoon/clean-slack](https://hub.docker.com/r/alexwitherspoon/clean-slack/)

## What it does!
Runs a python scrypt to clean slack files after N days (30 by default)

### Run via Cron
Install to /opt
```shell
cd /opt
git clone https://github.com/alexwitherspoon/clean-slack.git
```

Install via crontab -e
```shell
*/15 * * * * cd /opt/clean-slack && git stash && git pull && chmod +x /opt/clean-slack/clean-slack.py && python /opt/clean-slack/clean-slack.py
```

# OR Run via Docker

## How to use this image

### Bundled Apps
* Debian Stable
* curl
* python

## Use for your own Dockerfile in your own project.

Include the following at the top of your project.

    FROM alexwitherspoon:clean-slack
    
## Configure it!

Follow these instructions here: https://github.com/alexwitherspoon/clean-slack/blob/master/clean-slack.conf.example

The file inside the container to edit is at:

    /opt/clean-slack/clean-slack.conf

## Run this image on a docker host

Modify "/<local>/clean-slack.conf" to point to your config file on the docker host. An example config is found here: https://github.com/alexwitherspoon/clean-slack/blob/master/clean-slack.conf.example

    docker pull alexwitherspoon/clean-slack
    docker run --name clean-slack -d --restart=always -v /<local>/clean-slack.conf:/opt/clean-slack/clean-slack.conf alexwitherspoon/clean-slack

## How to Connect to it!
Docker exec.

    docker exec -i -t clean-slack env TERM=xterm bash -l


## Things got out of hand, how do I kill it?

Show all running docker instances

    docker ps -a

When you've found the bear's container id, run this:

    docker kill <container-id>
    docker rm <container-id>
    docker rmi <container-id>
