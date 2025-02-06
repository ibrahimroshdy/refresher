#!/bin/bash

# branch image to pull
branch=develop
# Remove spaces around = in variable assignments
user=
token=

# ghcr.io login with token
docker login ghcr.io -u "$user" -p "$token"

# pull, tag and rmi
docker pull "ghcr.io/$user/refresher:$branch"
docker tag "ghcr.io/$user/refresher:$branch" refresherbackend
docker rmi "ghcr.io/$user/refresher:$branch"

# remove old images (with error handling)
docker images -f "dangling=true" -q | xargs -r docker rmi