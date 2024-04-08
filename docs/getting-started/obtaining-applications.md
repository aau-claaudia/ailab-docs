# Obtaining Applications
To obtain applications on AI Student Cloud, you must utilize the [container](/glossery/#containers) technology, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html). 

???+ info "What is a container?"
    A container is a stand-alone, executable software package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. Read more about containers [here](/glossery/#containers).

In this section, we will cover how you can obtain a pre-built container that includes all the necessary packages. Additionally, you have the option to [customize a container](/courses/customize-containers) with additional installations, which is covered in [courses](/courses/customize-containers).


## Pre-built containers

The recommended way to obtain containers is to first visit [NVIDIA GPU
Cloud (NGC)](https://catalog.ngc.nvidia.com/) and check whether NVIDIA
already provides a container with the application you need.

![Screenshot of NGC website](/assets/img/ngc.png)

As an example, this could be TensorFlow. You can search on NGC and
find
[TensorFlow](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow). Here
you can choose the desired version from the "Copy image path" dropdown menu:

![Screenshot of NGC TensorFlow page](/assets/img/ngc-tf-detail.png)

==UPDATE IMAGE TO MATCH WITH NEWEST IMAGE==

This copies a link to the container which we will use in the following example.

???+ example

    We need to use Singularity to download the container and in order to run Singularity, we must run it through the Slurm queueing system using the command `srun`. 

    To download the container to your AI Student Cloud instance paste the url to the image like so:

    `srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3`

    NOTE: The container could take ~20 minutes to download. 
    
    The above example consists of the following parts:

    - `srun`: the Slurm command which gets the following command executed
    on a compute node.
    - `mem`: a Slurm command that allows you allocate memory to your
    process, in this case 40GB of memory. A higher amount of memory than the default is needed
    specifically for this TensorFlow container. Please see [Obtaining Memory Consuming Containers](/courses/obtaining-memory-consuming-containers/) page for a better way to
    avoid excessive memory requirements.
    - `singularity pull`: the Singularity command which downloads a
    specified container.
    - `docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3`: this part of the
    command itself consists of two parts. `docker://` tells Singularity
    that we are downloading a Docker container and Singularity
    automatically converts this to a Singularity container upon
    download. `nvcr.io/nvidia/tensorflow:24.03-tf2-py3` is container
    label copied from the NGC webpage which identifies the particular
    container and version that we want.

Once the `singularity pull` command has completed, you should have a
file called `tensorflow_24.03-tf2-py3.sif` in your user directory (use
the command `ls` to see the files in your current directory).

???+ warning "Work-arounds for memory-consuming or slow container builds"

      There is two work-arounds if you have problems installing containers due to excessive memory requirements or very slow container builds.

      1. [Obtaining Memory Consuming Containers](/courses/obtaining-memory-consuming-containers)
      2. [Obtaining Containers Faster](/courses/obtaining-containers-faster)

Now that you know how to obtain applications, let's learn how to <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/running-applications">run applications :octicons-arrow-right-24:</a></span>