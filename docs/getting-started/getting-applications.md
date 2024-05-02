# Getting applications
To obtain applications on AI-LAB, you must use container images. On AI-LAB we use the container technology, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html)

!!! info "What is an image?"
    An image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. It serves as a blueprint for creating containers.

!!! info "What is a container?"
    A container is a runtime instance of an image that is executed and managed by Singularity. Containers provide an isolated environment to run applications, ensuring consistency and portability across different systems.

## Pre-downloaded images
The most straightforward method to acquire applications on AI-LAB is by accessing pre-downloaded images stored in the `/container` directory. We aim to consistently update these images to the latest versions. You can find a list of the pre-downloaded container images [here](/system-overview/#list-of-pre-download-containers), or you can check which images exist in the `/container` directory on AI-LAB with `ls PATH TO CLAAUDIA IMAGE DIRECTORY`:

!!! example

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