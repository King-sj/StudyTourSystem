#!/bin/bash
if [ -n "$DIR" ]; then
  echo DIR is $DIR
else
  warning "path does not exist"
fi

# 检查是否以 root 权限运行
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
if [ "$(id -u)" != "0" ]; then
  warning "This script must be run as root" 1>&2
  # 使用 sudo 重新执行当前脚本
  sudo bash "$0" "$@"
  exit $?
fi
fi

source /etc/profile