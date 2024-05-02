# Getting applications
To obtain applications on AI Lab, you must utilize the container technology, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html). 

!!! info "What is an image?"
    An image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. It serves as a blueprint for creating containers.

!!! info "What is a container?"
    A container is a runtime instance of an image that is executed and managed by Singularity. Containers provide an isolated environment to run applications, ensuring consistency and portability across different systems.

## Pre-downloaded images
The most straightforward method to acquire applications on AI Lab is by accessing pre-downloaded images stored within the platform. The default pre-downloaded images presently include [TensorFlow](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow) and [PyTorch](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch), located at ==PATH TO CLAAUDIA IMAGE DIRECTORY==. We aim to consistently update these images to the latest versions. 

Additionally, you can explore further pre-downloaded images available in the *courses directory* ==PATH TO COURSES DIRECTORY== on AI Lab.

!!! example
    First, let's check out which images exist in ==PATH TO CLAAUDIA IMAGE DIRECTORY==:

    ```console
    ls PATH TO CLAAUDIA IMAGE DIRECTORY
    ```

    Lets copy the `tensorflow_24.03-tf2-py3.sif` image from ==PATH TO CLAAUDIA IMAGE DIRECTORY== to your user directory. <span style="font-weight: 600;">Note! TensorFlow might be newer version at this time.</span>

    To copy a image from the directory, simply execute:

    ```console
    scp INSERT TENSORFLOW PATH xxxxxx@student.aau.dk@ai-fe02.srv.aau.dk:~
    ```

## Download images
Alternatively, you can access a wide array of images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a image for the application you require. Refer to our guide [here](/additional-guides/download-images-from-ngc) for detailed instructions.

## Customize images
You also have the flexibility to create your own images tailored to your specific environment requirements. Refer to our guide on [creating a conda environment](/additional-guides/creating-a-conda-environment).


Now that you know how to obtain applications, let's delve into <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/running-applications">running applications :octicons-arrow-right-24:</a></span>