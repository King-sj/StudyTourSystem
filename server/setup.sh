#!/bin/bash
# ------------------------------------
# 服务端启动脚本
# @athor SongJian(2175616761@qq.com)
# @date 2024-02-08
#------------------------------------
# some config
DEBUG=false
user=$(whoami)
. script/index.sh

info "User is $user"

if [ "$DEBUG" = true ]; then
  info "python's name is " "$py"
fi

nohup $py -u ./run.py >> ./daily.log 2>&1 &

if [ "$DEBUG" == true ]; then
  notice "Debug mode enabled."
else
  notice "Release mode enabled."
fi

printf "\n\n"
info "Server started. You could check all outputs in ./daily.log"
notice "if you wanna use conda,please input 'sudo bash','conda [[command]]'"
printf "\n"

