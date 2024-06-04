To run applications on AI-LAB, you must use container images. On AI-LAB we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html).

!!! info "What is a container image?"
    A container image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings. It serves as a blueprint for creating containers. A container is a runtime instance of an image that is executed and managed by Singularity.

<hr>

## Pre-downloaded images
The most straightforward method to acquire container images on AI-LAB is by accessing pre-downloaded images stored in the `/ceph/container` directory. We aim to consistently update these images to the latest versions.

You can check which images exist in the `/ceph/container` directory on AI-LAB with `ls`:

```console
ls /ceph/container
```

Lets copy the `tensorflow_24.03-tf2-py3.sif` image from `/ceph/container` to your user directory (**note:** TensorFlow might be newer version at this time).

To copy the image from the directory, simply execute:

```console
cp /ceph/container/tensorflow_24.03-tf2-py3.sif .
```

It may take a few minutes to copy.

<hr>

## Download container images
Alternatively, you can access a wide array of images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a image for the application you require. Refer to our guide [here](/additional-guides/download-images-from-ngc) for detailed instructions.

<hr>

## Build your own container images
You also have the flexibility to create your own images tailored to your specific environment requirements. Refer to our guide on [building your own container image](/additional-guides/building-your-own-container-image).

<br>

Now that you know how to obtain applications, let's delve into [**running jobs :octicons-arrow-right-24:**](/getting-started/running-jobs)