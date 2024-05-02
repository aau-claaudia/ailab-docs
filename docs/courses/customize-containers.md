To customize Singularity containers (.sif files) from sources like NGC, which are read-only, consider the following methods for incorporating additional software:

1. Create a writable sandbox container image
2. Build a new container image file with Cotainr
3. Build a new container image file from a definition file
4. Install Python packages with `pip` or `conda` outside the container

### 1. Create a writable sandbox container image

First create a so-called sandbox container:
```console
srun singularity build --sandbox [sandbox-dir-name] [container image]
```
where you replace `[sandbox-dir-name]` with a name you decide for the
directory that holds your sandbox container, and replace `[container
image]` with the name of a container image you already have in AI Lab
(e.g. `pytorch_23.04-py3.sif`) or the URI of a container to download
(e.g. `docker://nvcr.io/nvidia/pytorch:23.04-py3`).

???+ example

    Start by creating a sandbox container:
    
	```console
	srun singularity build --sandbox pytorch-23.04 docker://nvcr.io/nvidia/pytorch:23.04-py3
    ```
	
    Then when you wish to install additional software in the container, open a shell in the container:

    ```console
    srun singularity shell --writable --fakeroot pytorch-23.04
    ```

    While inside the container, install additional packages using for
    example the `apt` package manager:
    ```console
    Singularity> apt install [package name]
    ```
    or `pip` (for Python):
    ```console
    Singularity> pip install [package name]
    ```

### 2. Build a new container image file with Cotainr

[Cotainr](https://cotainr.readthedocs.io/en/stable/index.html) is a tool developed by [DeiC](https://www.deic.dk/en/om-deic) to ease building of Singularity containers.
It can be used to build custom containers with additional software installable by `conda` and `pip`. This means it is primarily for adding Python packages to a container. 
It works from a base container image that you specify and then build additional Anaconda and Pip packages which you supply as a Conda environment specification.

We begin by downloading the latest release from the [Cotainr repository](https://github.com/DeiC-HPC/cotainr/releases). In the example below we are downloading the latest version as of late 2023. Be sure to check for newer versions at the aforementioned repository. Look for the zip archive "Assets" section, and copy the link.

```console
wget https://github.com/DeiC-HPC/cotainr/archive/refs/tags/2023.11.0.zip
```

You should now have a zip archive, which you can unzip with:
```console
unzip 2023.11.0.zip
```

After this has been done, you should have a directory called `cotainr-2023.11.0`. We should now be able to launch Cotainr and access its commands from within this directory. In a generalised manner the command structure is:
```console
srun [path/to/cotainr] build [name of output file] --base-image=[base image] --conda-env=[name of environment]
```

We use `srun` to ask Slurm to delegate the subsequent command to a compute node. 
We then need to specify the path to `cotainr/bin/cotainr` and call `build`. Then choose a name for your container and replace `[name of output file]` with this newly chosen name. We recommend appending the conventional suffix `.sif` to this name.
After that you will need to specify a `[base image]`, which can be an existing container in your directory or one from a remote source. Finally use the parameter `--conda-env` to specify which Conda environment file you want to use. If you have an existing Conda environment somewhere, you can export this environment `conda env export > my_environemt.yml`.

???+ example
    ```console
    srun ~/cotainr/bin/cotainr build amber.sif --base-image=docker://ubuntu:22.04 --conda-env=amber.yml
    ```

Also don't forget to check out the [offical Cotainr documentation]("https://cotainr.readthedocs.io/en/stable/index.html") for more information.

### 3. Build a new container image file from a definition file

You can also build containers from scratch or from an existing base
image directly with Singularity. This is a somewhat more difficult
approach than the above Cotainr tool, because it requires you to write
the Singularity definition file yourself. The build process can be
lengthy and so, it can take a long time with
trial-and-error to get the definition right and produce a working
container. Please see the [Singularity
documentation](https://docs.sylabs.io/guides/3.8/user-guide/build_a_container.html#building-containers-from-singularityce-definition-files)
for details on how to build containers from definition files.

### 4. Install Python packages with pip or conda outside the container

This is not recommended, as the method is a bit "brittle". It is easy
to set it up wrong and end up in a situation where versions of
packages installed for different container images get mixed up and
cause problems. Consider this a last resort: [Please see this
guide](../examples/pip_in_containers).

