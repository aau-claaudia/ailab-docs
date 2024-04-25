You can download a large range of containers by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and check whether NVIDIA provides a container with the application you need.

![Screenshot of NGC website](/assets/img/ngc.png)

As an example, this could be TensorFlow. You can search on NGC and find [TensorFlow](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow). Here you can choose the desired version from the "Copy image path" dropdown menu:

![Screenshot of NGC TensorFlow page](/assets/img/ngc-tf-detail.png)

This copies a link to the container which we will use in the following example.

!!! example

    We need to use Singularity to download the container and in order to run Singularity, we must run it through the Slurm queueing system using the command `srun`. 

    To download the container to your AI Student Cloud instance paste the url to the image like so:

    `srun --mem 40G singularity pull docker://nvcr.io/nvidia/tensorflow:24.03-tf2-py3`

    NOTE: The container could take ~20 minutes to download. 
    
    The above example consists of the following parts:

    - `srun`: the Slurm command which gets the following command executed
    on a compute node.
    - `mem`: a Slurm command that allows you allocate memory to your
    process, in this case 40GB of memory. A higher amount of memory than the default is needed
    specifically for this TensorFlow container. Please see [Download memory consuming containers](/additional-guides/download-memory-consuming-containers/) page for a better way to
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

!!! warning "Work-around for memory-consuming downloads"

      There is a workaround if you have problems downloading containers due to excessive memory requirements. See out guide: [Download memory consuming containers](/additional-guides/download-memory-consuming-containers).
