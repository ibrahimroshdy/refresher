#!/bin/bash

#/home/speedtest
              #├── deployment.sh
              #├── docker
              #│   ├── docker-compose.staging.yml
              #│   ├── grafana
              #│   │   └── provisioning
              #│   │       ├── dashboards
              #│   │       │   ├── dashboard.yml
              #│   │       │   ├── data
              #│   │       │   │   └── data-dashboard.json
              #│   │       │   └── prometheus
              #│   │       │       ├── docker_containers.json
              #│   │       │       ├── docker_host.json
              #│   │       │       ├── monitor_services.json
              #│   │       │       └── nginx_container.json
              #│   │       └── datasources
              #│   │           └── datasources.yml
              #│   └── prometheus
              #│       └── prometheus.yml
              #├── nginx
              #│   └── site-confs
              #│       ├── default
              #│       ├── flower
              #│       ├── grafana
              #│       └── speedtester
              #└── scripts
              #    └── cr_pull.sh


# run cr_pull.sh
figlet PACKAGES DOWNLOAD
./scripts/cr_pull.sh


# run swag container and shut it down
figlet HTTP/HTTPS
docker-compose -f docker/docker-compose.staging.yml up -d swag
docker-compose -f docker/docker-compose.staging.yml down

# copy nginx files
figlet nginx
cp -Rf ./nginx/  /home/withnoedge/swag/

# docker compose up
figlet SERVER READY
docker-compose -f docker/docker-compose.staging.yml up -d
