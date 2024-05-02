It is possible to define and build your own container images with Singularity. Lets try creating a Singularity container image with Python and pip installed. 

First we need to create a [Singularity definition file](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html) (`.def`). This definition file is a blueprint for how Singularity should build the container image. It includes information about the base OS to build, which software to install and several other options.

Lets create an empty text file by using the `nano` command:

```console
nano
```

Now we can enter the blueprint needed to install our application:

```console
Bootstrap: docker
From: ubuntu:20.04

%post
    # This section is where you install additional packages or software
    # Update package list and install the latest Python and pip version
    apt-get update
    apt-get install -y python3 python3-pip

%test
    # Define tests to run after the container is built
    python3 --version
```

In this example we will use `docker` to pull `ubuntu:20.04` as the base OS of our image. 

In the next section,`%post`, we can define commands that will be executed after the base OS has been installed. In this example, we will update the container and install `python3` and `pip`. 

After that we can define commands to run after the container is built in the `%test` section. Lets try with `python3 --version`.

You can find more options to use in definition file in the [Singularity definition file documentation](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html).

To save the file press `CTRL + O` and enter a filename ending with `.def` and hit `ENTER`. In this example, lets call it `python3.def`.
Now, lets build the container image from the definition file with the following command:

```console
srun --mem 40G singularity build --fakeroot python3.sif python3.def
```

`--fakeroot` is added as a parameter as you must be the root user and cannot use `sudo` on AI Lab.
`--mem 40G` is a Slurm command that allows you allocate memory to your process, in this case 40GB of memory. A higher amount of memory than the default is needed for some container builds. 

After some time you should  see the `Python X.X.X` version be printed in the terminal, and you should now have a `python3.sif` image ready to run.

You can find more information about building containers from Singularity definition files [here](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html).