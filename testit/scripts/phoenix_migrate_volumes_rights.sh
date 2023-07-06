#! /bin/bash
PROJECT_NAME=$1
testit_volumes=("license-volume" "verification-volume" "trusted-certificates-volume")
for volume in ${testit_volumes[@]}; do 
    volume=$(docker inspect "${PROJECT_NAME}_${volume}" --format '{{ .Mountpoint }}'); 
    chown -R 611:0 $volume && chmod -R g=u $volume;
done
ssl_volume=$(docker inspect "${PROJECT_NAME}_ssl-volume" --format '{{ .Mountpoint }}');
chown -R 101:0 $ssl_volume && chmod -R g=u $ssl_volume
