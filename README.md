# Bendu
                                                   
[![linting: pylint](https://img.shields.io/badge/linting-pylint-green)](https://github.com/PyCQA/pylint)
[![Python 3.9.7](https://img.shields.io/badge/python-3.9.7-blue.svg)](https://www.python.org/downloads/release/python-397/)
![release passing](https://github.com/tmavroeid/bendu/actions/workflows/release.yml/badge.svg)
[![Github vulnerabilities](https://img.shields.io/github/license/tmavroeid/bendu)](https://img.shields.io/github/license/tmavroeid/bendu)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/tmavroeid/bendu)
[![Github vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/tmavroeid/bendu)](https://img.shields.io/snyk/vulnerabilities/github/tmavroeid/bendu)
[![Github release date](https://img.shields.io/github/release-date/tmavroeid/bendu)](https://img.shields.io/github/release-date/tmavroeid/bendu)
 ![visitors](https://visitor-badge.glitch.me/badge?page_id=tmavroeid.bendu)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/tmavroeid)

##### Table of Contents  
- [Introduction](#introduction)
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
- [Usage](#usage)
- [Testing](#testing)
- [Help](#help)
- [Technologies](#technologies)

## Introduction
This python tool automates operations with docker containers by utilizing the Docker Remote API. This python tool implements the following:

- Building a Docker Image from a given Dockerfile and an application (a ‘Hello world’ web application)
- Starting a few instances of the Docker Image in different containers
- Validating that the container instances are running
  - Validating the status of the service running inside the container (health check)
- Monitoring the resource usage of each container (CPU, I/O, etc)
- Consolidating the log output of all the container instances into one centralized log file.

## Getting Started

### Prerequisites

Please make sure you've already ***Python3***. The tool is utilizing the ***Docker Remote API*** , the ***Python SDK for Docker*** and the python package ***Click***. The ***Remote API*** is set up in tcp://0.0.0.0:2376. For the purpose of using the tool, you should set up the Remote API likewise. The following instructions apply to Ubuntu 16.04 and Debian 9.9 (stretch).

Install the Python SDK and Click:
```
apt-get install python3-pip
pip3 install docker
pip3 install click
```
Edit the file:
```
sudo nano /lib/systemd/system/docker.service
```
Update with:
```
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2376
```
Then, restart the docker service running below commands:
```
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl status docker
```

For older versions than Ubuntu 16.04 you can use the instructions in the following source,  [Enabling and accessing Docker Engine API on a remote docker host on Ubuntu](https://medium.com/@sudarakayasindu/enabling-and-accessing-docker-engine-api-on-a-remote-docker-host-on-ubuntu-16-04-2c15f55f5d39)

## Usage

The tool is equipped with five commands: *build*, *deploy*, *validate*, *stats* and *logging* as presented below:

```
python3 bendu.py [build, deploy, validate, stats, logging] --help
```


## Testing

To test the python tool follow the instructions below.
1. First install virtual environment:

```
apt-get install virtualenv
```

2. Then, in the same depth as the project make a folder named ***venv***:

```
mkdir venv
```

3. Execute the following command:

```
virtualenv -p python3 venv/
```
4. Get up and running a virtual environment by running executing:

```
. venv/bin/activate
pip3 install --editable .
```

5. Finally, execute the *build* command to build the image according the instructions that are defined in a Dockerfile:

```
bendu --help
bendu build -d ./data -t "alpine_hello_world:1"
```

6. Exit virtual environment by invoking:

```
deactivate
```


## Help

Each one of these commands has each one functionality which can be over-viewed by invoking each command followed by **--hep**.

## Technologies
* [Docker](https://www.docker.com/)
* [Click](https://click.palletsprojects.com/en/7.x/)
* [Python SDK for Docker](https://docker-py.readthedocs.io/en/stable/)
