#!/bin/bash

PROJECT_NAME=$1

# Move migration volumes to original volumes and cleanup

migration_volumes=("new-minio-data-volume" "new-avatars-minio-data-volume")
for volume in ${migration_volumes[@]}; do
    volume_original="$(sed s/new-//g <<<$volume)";
    rm -rf $(docker inspect "${PROJECT_NAME}_${volume_original}" --format '{{ .Mountpoint }}')
    mv $(docker inspect "${PROJECT_NAME}_${volume}" --format '{{ .Mountpoint }}') $(docker inspect "${PROJECT_NAME}_${volume_original}" --format '{{ .Mountpoint }}' | sed s/_data//g);
    docker volume rm "${PROJECT_NAME}_${volume}";
done
