On AI-LAB, we have a ready-to-use [ImageMagick](https://imagemagick.org/index.php) container image. This means that you can quickly access ImageMagick's functionality within the AI-LAB environment without needing to install or configure the software yourself. By utilizing the container image, you can efficiently work with images in your projects, transforming them as needed to suit your applications or experiments.

First, copy the ImageMagick container image from the AI-LAB container directory to your user directory:

```console
scp /container/imagemagick_6.9.10-23.sif ~
```

To verify that everything is functioning as expected, let's use the "mogrify" tool to rotate some images. Begin by copying the following directory containing 100 cat images to your user directory:

```console
scp /course/ailab-docs-files/cats ~
```

Next, create a folder to store the rotated images:

```console
mkdir rotated_images
```

Finally, perform the image rotation by 90 degrees using the mogrify tool:

```console
srun singularity exec imagemagick.sif mogrify -path rotated_images -rotate 90 cats/*.png
```