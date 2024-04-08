
## Adding a conda environment to a container
Installing a conda environment to a container may be easily done using *cotainr*. 

Cotainr is a tool developed by DeiC to ease building of Singularity containers. It can be used to build custom containers with additional software installable by Conda and Pip. This means it is primarily for adding Python packages to a container. It works from a base container image that you specify and then build additional Anaconda and pip packages which you supply as a conda environment specification.

To begin utilizing *cotainr*, you'll first need to download the latest release from the [Cotainr repository](https://github.com/DeiC-HPC/cotainr/releases) (as of late 2023.11.0) using `wget`:

```console
wget https://github.com/DeiC-HPC/cotainr/archive/refs/tags/2023.11.0.zip
```

You should now have `2023.11.0.zip` in your user directory on AI Student Cloud. Unzip it:

```console
unzip 2023.11.0.zip
```

You can now get access to the *cotainr* command line interface by using the path `cotainr-2023.11.0/bin/cotainr`. But first we will create a conda environment file, `conda_env.yml`, to :


Type `nano`





my_conda_env.yml

channels:
  - conda-forge
dependencies:
  - python=3.11.0
  - numpy=1.23.5


