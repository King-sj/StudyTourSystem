#!/bin/bash
. ./script/utils/index.sh

# 主动导入脚本
script_path="./script/src"
for file in "$script_path"/*.sh; do
  # echo $file
  . "$file"
done
