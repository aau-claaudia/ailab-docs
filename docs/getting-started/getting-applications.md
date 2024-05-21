# Getting applications
To run applications on AI-LAB, you must use container images. On AI-LAB we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html).

!!! info "What is a container image?"
    A container image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. It serves as a blueprint for creating containers. A container is a runtime instance of an image that is executed and managed by Singularity.

### Pre-downloaded images
The most straightforward method to acquire container images on AI-LAB is by accessing pre-downloaded images stored in the `/container` directory. We aim to consistently update these images to the latest versions. You can find a list of the pre-downloaded container images [here](/system-overview/#list-of-pre-download-containers), or you can check which images exist in the `/container` directory on AI-LAB:

!!! example

    ```console
    ls /ceph/container
    ```

    Lets copy the `tensorflow_24.03-tf2-py3.sif` image from `/ceph/container` to your user directory. <span style="font-weight: 600;">Note! TensorFlow might be newer version at this time.</span>

    To copy the image from the directory, simply execute:

    ```console
    cp /ceph/container/tensorflow_24.03-tf2-py3.sif .
    ```

### Download images
Alternatively, you can access a wide array of images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a image for the application you require. Refer to our guide [here](/additional-guides/download-images-from-ngc) for detailed instructions.

### Customize images
You also have the flexibility to create your own images tailored to your specific environment requirements. Refer to our guide on [building your own container image](/additional-guides/building-your-own-container-image).


Now that you know how to obtain applications, let's delve into <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/running-applications">running applications :octicons-arrow-right-24:</a></span>