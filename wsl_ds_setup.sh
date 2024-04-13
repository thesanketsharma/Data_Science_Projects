# Install Anaconda (Miniconda) on WSL
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> $HOME/.bashrc
source $HOME/.bashrc
conda init
#restart terminal

#installing rapids
conda create --solver=libmamba -n rapids-24.04 -c rapidsai -c conda-forge -c nvidia  \
    rapids=24.04 python=3.11 cuda-version=12.0 \
    dask-sql jupyterlab dash graphistry tensorflow xarray-spatial pytorch







