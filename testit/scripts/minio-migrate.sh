#!/bin/bash
#
# Minio migration script
# Documentation: https://min.io/docs/minio/container/operations/install-deploy-manage/migrate-fs-gateway.html

sleep 10

prepareMigration() {
  mc admin config export SOURCE > config.txt
  mc admin config import TARGET < config.txt
  mc admin service restart TARGET
  mc admin cluster bucket export SOURCE
  mc admin cluster bucket import TARGET cluster-metadata.zip
  mc admin cluster iam export SOURCE
  mc admin cluster iam import TARGET SOURCE-iam-info.zip
}

mirrorBucketsList() {
  mc ls SOURCE | awk '{print $5}' | while read bucket
  do
    echo "Migration is in process, please wait..."
    mc mirror --preserve SOURCE/$bucket TARGET/$bucket >> /dev/null
    SOURCE_FILES_COUNT=$(mc ls --recursive SOURCE/$bucket | wc -l)
    TARGET_FILES_COUNT=$(mc ls --recursive TARGET/$bucket | wc -l)
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    NC='\033[0m'
    if [ "$SOURCE_FILES_COUNT" == "$TARGET_FILES_COUNT" ]; then
      printf "$bucket bucket migrated ${GREEN}sucessfully${NC}! \nSource files count: $SOURCE_FILES_COUNT\nTransferred files count: $TARGET_FILES_COUNT\n";
    else
      printf "$bucket bucket migration ${RED}failed${NC}! \nSource files: $SOURCE_FILES_COUNT\nFiles transferred: $TARGET_FILES_COUNT\n";
      exit 1;
    fi
  done
}

mc alias set SOURCE http://minio:9000 ${AWS_ACCESS_KEY} ${AWS_SECRET_KEY}
mc alias set TARGET http://new-minio:9000 ${AWS_ACCESS_KEY} ${AWS_SECRET_KEY}
prepareMigration
mirrorBucketsList

mc alias set SOURCE http://avatars-minio:9000 ${AVATARS_AWS_ACCESS_KEY} ${AVATARS_AWS_SECRET_KEY}
mc alias set TARGET http://new-avatars-minio:9000 ${AVATARS_AWS_ACCESS_KEY} ${AVATARS_AWS_SECRET_KEY}
prepareMigration
mirrorBucketsList

echo Done!

exec "$@"
