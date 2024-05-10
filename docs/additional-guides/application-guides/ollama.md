
`ollama.def`:

```console
Bootstrap: docker
From: ollama/ollama:latest
# ollama containers https://github.com/iportilla/ollama-lab

%post
    # install miniconda
    apt-get -y update && apt-get install -y wget bzip2
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    export PATH="/opt/conda/bin:$PATH"
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate" >> ~/.bashrc

    # install pip
    apt-get install -y python3-pip

    # configure conda
    conda config --add channels conda-forge

    # install ollama
    pip3 install ollama

    # install numpy, matplotlib, pandas, rich, jupyter
    conda install -c conda-forge numpy matplotlib pandas rich jupyterlab ipykernel

%environment
    export PATH="/opt/conda/bin:$PATH"
    . /opt/conda/etc/profile.d/conda.sh
    conda activate
```

Build Singularity container image:

```console
srun --mem 40G singularity build --fakeroot ollama.sif ollama.def
```

1st session:

```console
srun --pty --nodelist=a256-t4-01 singularity shell --nv ollama.sif

Singularity> ollama serve
```

SPØRGSMÅL TIL SVEND: HVORDAN STARTER MAN EN 2ND SESSION I TERMINALEN FREMFOR ET NYT VINDUE?

2nd session:

```console
srun --pty --nodelist=a256-t4-01 singularity shell --nv ollama.sif

ollama run mistral
```
aåt

Bootstrap: docker
From: ollama/ollama:latest
# ollama containers https://github.com/iportilla/ollama-lab

%post
    # Update package lists and install necessary packages
    apt-get -y update
    apt-get install -y wget bzip2

    # Install dependencies
    apt-get install --no-install-recommends -y bc ffmpeg google-perftools libsm6 libxext6 netcat-openbsd pandoc
    apt-get -qq clean
    rm -rf /var/lib/apt/lists/*

    # Install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    export PATH="/opt/conda/bin:$PATH"
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate" >> ~/.bashrc

    # Install pip via conda
    conda install -c conda-forge python=3 pip

    # Configure Conda
    conda config --add channels conda-forge

    # Install Ollama
    pip install ollama

    # Install Python and Jupyter packages
    conda install -c conda-forge numpy matplotlib pandas rich jupyterlab ipykernel

    # Install Node.js, PyTorch, and related packages
    conda install -y nodejs pytorch torchvision torchaudio "pytorch-cuda=${CUDA_VERSION}" -c pytorch -c nvidia -c conda-forge

    # Clean up Conda cache
    conda clean --all -f -y

%environment
    export PATH="/opt/conda/bin:$PATH"
    . /opt/conda/etc/profile.d/conda.sh
    conda activate








Bootstrap: docker
From: ollama/ollama:latest
# ollama containers https://github.com/iportilla/ollama-lab

%post
    # Update package lists and install necessary packages
    apt-get -y update
    apt-get install -y wget bzip2

    # Install dependencies
    apt-get install --no-install-recommends -y bc ffmpeg google-perftools libsm6 libxext6 netcat-openbsd pandoc
    apt-get -qq clean
    rm -rf /var/lib/apt/lists/*

    # Install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    export PATH="/opt/conda/bin:$PATH"
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate" >> ~/.bashrc

    # Install pip via conda
    conda install -c conda-forge python=3 pip

    # Configure Conda
    conda config --add channels conda-forge

    # Install Ollama
    pip install ollama

    # Install Python and Jupyter packages
    conda install -c conda-forge numpy matplotlib pandas rich jupyterlab ipykernel

    # Install Node.js, PyTorch, and related packages
    conda install -y nodejs pytorch torchvision torchaudio "pytorch-cuda=${CUDA_VERSION}" -c pytorch -c nvidia -c conda-forge

    # Clean up Conda cache
    conda clean --all -f -y

%environment
    export PATH="/opt/conda/bin:$PATH"
    . /opt/conda/etc/profile.d/conda.sh
    conda activate




Bootstrap: docker
From: ollama/ollama:latest
# ollama containers https://github.com/iportilla/ollama-lab

%post
    # Update package lists and install necessary packages
    apt-get -y update
    apt-get install -y wget bzip2

    # Install dependencies
    apt-get install --no-install-recommends -y bc ffmpeg google-perftools libsm6 libxext6 netcat-openbsd pandoc
    apt-get -qq clean
    rm -rf /var/lib/apt/lists/*

    # Install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p /opt/conda
    rm ~/miniconda.sh
    export PATH="/opt/conda/bin:$PATH"
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate" >> ~/.bashrc

    # Install pip via conda
    conda install -c conda-forge python=3 pip

    # Configure Conda
    conda config --add channels conda-forge

    # Install Ollama
    pip install ollama

    # Install Python and Jupyter packages
    conda install -c conda-forge numpy matplotlib pandas rich jupyterlab ipykernel

    # Install Node.js, PyTorch, and related packages
    conda install -y nodejs pytorch torchvision torchaudio "pytorch-cuda=${CUDA_VERSION}" -c pytorch -c nvidia -c conda-forge

    # Clean up Conda cache
    conda clean --all -f -y

%environment
    export PATH="/opt/conda/bin:$PATH"
    . /opt/conda/etc/profile.d/conda.sh
    conda activate

