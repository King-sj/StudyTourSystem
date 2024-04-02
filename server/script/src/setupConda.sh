#!/bin/sh
# Variables
PYTHON_VERSION=3.12.1
VIRTUAL_ENV_NAME=StuySystem

# Define Miniconda installer script names and installation path
MINICONDA_INSTALLER_SCRIPT="Miniconda3-latest-Linux-x86_64.sh"
MINICONDA_INSTALLER_SCRIPT_WIN="Miniconda3-latest-Windows-x86_64.exe"
MINICONDA_PREFIX="$HOME/miniconda3" # Change this to your preferred installation directory

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    error "curl is not installed. Please install curl and try again."
    exit 1
fi

# Check if Conda is installed
CONDA_PATH=$(which conda)

if [ -z "$CONDA_PATH" ]; then
    info "Conda is not installed. Beginning Miniconda installation."

    # Determine OS and download appropriate Miniconda installer
    case "$(uname)" in
    "Darwin"|"Linux")
        # macOS or Linux
        if [ "$DEBUG" != "true" ]; then
            curl -L "https://repo.anaconda.com/miniconda/$MINICONDA_INSTALLER_SCRIPT" -o $MINICONDA_INSTALLER_SCRIPT
        fi
        chmod +x $MINICONDA_INSTALLER_SCRIPT
        ./$MINICONDA_INSTALLER_SCRIPT -b -f -p $MINICONDA_PREFIX
        info "Miniconda installed."
        rm $MINICONDA_INSTALLER_SCRIPT
        # Add Miniconda to PATH for current session and future sessions
        export PATH="$MINICONDA_PREFIX/bin:$PATH"
        sudo echo "export PATH=\"$MINICONDA_PREFIX/bin:$PATH\"" >> /etc/profile
        source /etc/profile
        info "add conda and more($PATH) to env path done."
        ;;
    "MINGW32_NT"|"MINGW64_NT")
        # Windows (assuming Git Bash or similar is being used)
        if [ "$DEBUG" != "true" ]; then
            curl -L "https://repo.anaconda.com/miniconda/$MINICONDA_INSTALLER_SCRIPT_WIN" -o $MINICONDA_INSTALLER_SCRIPT_WIN
        fi
        start /wait "" $MINICONDA_INSTALLER_SCRIPT_WIN /InstallationType=JustMe /RegisterPython=0 /S /D="%UserProfile%\Miniconda"
        info "Miniconda installed."
        rm $MINICONDA_INSTALLER_SCRIPT_WIN
        ;;
    *)
        warning "Unsupported OS."
        exit 1
        ;;
    esac
else
    notice "Conda is already installed at $CONDA_PATH"
    MINICONDA_PREFIX=$(conda info --base)
fi

# begin install python
echo "Installing Python=$PYTHON_VERSION virtual enviroment by conda..."

# 检查是否有激活的环境
active_env=$(conda env list | grep '\*' | awk '{print $1}')

notice "check active env: $active_env"
if [ -n "$active_env" ]; then
    info "Deactivating the current conda environment($active_env)..."
    source deactivate || conda deactivate
fi

# 检查虚拟环境是否已存在
if conda info --envs | grep -q "^$VIRTUAL_ENV_NAME\s"; then
    notice "Virtual environment $VIRTUAL_ENV_NAME already exists."
else
    # create env and install python
    echo "Creating virtual environment $VIRTUAL_ENV_NAME with Python $PYTHON_VERSION..."
    conda create -n "$VIRTUAL_ENV_NAME" python="$PYTHON_VERSION" -y
fi

# 激活虚拟环境
echo "Activating virtual environment $VIRTUAL_ENV_NAME..."
source activate "$VIRTUAL_ENV_NAME" || conda activate "$VIRTUAL_ENV_NAME"

# 更新conda
echo "Updating conda..."
conda update --name base conda

active_env=$(conda env list | grep '\*' | awk '{print $1}')
notice "Setup $active_env complete."


# Check Python version
echo "Testing Python version..."
# 根据操作系统设置 Python 命令
py="python"
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
  # Linux 或 macOS
  py="python3"
  echo "Running on Linux compatibility layer"
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  # Windows 或 Windows 下的兼容层
  echo "Running on Windows or Windows compatibility layer"
  # Windows 默认使用 python 命令
else
  notice "Unknown platform"
fi


python_version=$($py --version) # 使用之前设置的 $py 变量
echo "Current Python version: $python_version"
if [[ $python_version != "Python $PYTHON_VERSION"* ]]; then
    bug "Python was not installed correctly"
    exit 1
fi
# Check and install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Checking dependencies..."
    # 尝试安装依赖，并将输出重定向到一个临时文件
    #pip_install_output=$(mktemp)
    pip install -r requirements.txt #>"$pip_install_output" 2>&1
    # @note: 这里的输出会被重定向到临时文件中，所以这里的输出会被忽略掉, 实际使用体验不佳，故删除

    # 检查输出中是否有"Successfully installed"字样
    # if grep -q "Successfully installed" "$pip_install_output"; then
    #     echo "New dependencies installed."
    #     # 打印pip命令的输出内容
    #     cat "$pip_install_output"
    # else
    #     echo "All dependencies are already installed."
    # fi
    # # 删除临时文件
    # rm "$pip_install_output"
else
    error "requirements.txt not found."
fi

notice "Miniconda and Python$PYTHON_VERSION installation in environment $VIRTUAL_ENV_NAME completed successfully"