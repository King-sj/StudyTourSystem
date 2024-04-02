#!/bin/bash

# Usage: warning "This is a warning message."

info() {
echo -e "\033[0;34m INFO: $1 \033[0m"
}

warning() {
echo -e "\033[0;33m WARNING: $1 \033[0m"
}

notice() {
echo -e "\033[0;32m NOTICE: $1 \033[0m"
}

error() {
echo -e "\033[0;31m ERROR: $1 \033[0m"
}

bug() {
echo -e "\033[0;31m BUG: $1 \033[0m"
}


# Assign the script's name with its path
SCRIPT="$0"

# Extract the directory from the script path
DIR=$(dirname "$SCRIPT")

# Print the directory
# echo "脚本所在目录是: ${DIR}"
