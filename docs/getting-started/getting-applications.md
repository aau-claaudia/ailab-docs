# Getting applications
To obtain applications on AI Student Cloud, you must utilize the [container](/glossery/#containers) technology, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html). 

!!! info "What is a container?"
    A container is a stand-alone, executable software package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. Read more about containers [here](/glossery/#containers).

## Pre-downloaded containers
The most straightforward method to acquire applications on AI Student Cloud is by accessing pre-downloaded containers stored within the platform. The default pre-downloaded containers presently include [TensorFlow](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow) and [PyTorch](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch), located at ==PATH TO CLAAUDIA IMAGE DIRECTORY==. We aim to consistently update these containers to the latest versions. 

Additionally, you can explore further pre-downloaded containers available in the *courses directory* ==PATH TO COURSES DIRECTORY== on AI Student Cloud.

!!! example
    First, let's check out which containers exist in ==PATH TO CLAAUDIA IMAGE DIRECTORY==:

    ```console
    ls PATH TO CLAAUDIA IMAGE DIRECTORY
    ```

    Lets copy the `tensorflow_24.03-tf2-py3.sif` container from ==PATH TO CLAAUDIA IMAGE DIRECTORY== to your user directory. <span style="font-weight: 600;">Note! TensorFlow might be newer version at this time.</span>

    To copy a container from the directory, simply execute:

    ```console
    scp INSERT TENSORFLOW PATH xxxxxx@student.aau.dk@ai-fe02.srv.aau.dk:~
    ```

## Download containers
Alternatively, you can access a wide array of containers by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a container for the application you require. Refer to our guide [here](/additional-guides/download-containers-from-ngc) for detailed instructions.

## Customize containers
You also have the flexibility to create your own containers tailored to your specific environment requirements. Refer to our guide on [creating a conda environment](/additional-guides/creating-a-conda-environment).


Now that you know how to obtain applications, let's delve into <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/running-applications">running applications :octicons-arrow-right-24:</a></span>