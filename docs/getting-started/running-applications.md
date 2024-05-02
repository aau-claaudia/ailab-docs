# Running applications
Before you start running applications, it is important to be aware of AI Lab queueing system [Slurm](https://slurm.schedmd.com/quickstart.html).

### Slurm queue system
Slurm is a job scheduling system and is used to allocate resources, manage user jobs, and provide a framework for job queueing, scheduling, and execution on AI Lab. Applications on AI Lab can only be run through Slurm. 

The simplest way to run a job via Slurm is to use the command `srun`.

!!! example

    ```console
    srun hostname
    ```

    This runs the command `hostname` as a job in the queue system. When run like this with no further parameters specified, Slurm will run the command on the first compute node available.  

    The command will return one of these host names. If the command displays `srun: job XXXXXX queued and waiting for resources`, this means that all
    compute nodes are fully occupied (by other users' jobs) and your job is waiting in queue to be executed when resources become available.

    This was your first Slurm job. You will need this (`srun`) and other Slurm commands for most of your work in AI Lab.

    !!! info "Checking the queue"
        Before running a job you typically wish to see an overview of what is currently in the queue. For example to see how many jobs might be waiting ahead of you or to get an overview of your own jobs. We recommend looking at our guide [Checking the queue](/additional-guides/checking-the-queue) to get familiar with Slurm queue commands.

### Executing a containerized job

To execute a containerized job, we can use the Singularity command `exec`. Lets try printing "hello world" using Python within the `tensorflow_24.03-tf2-py3.sif` image:

```console
srun singularity exec tensorflow_24.03-tf2-py3.sif python3 -c "print('hello world')"
```

!!! info   
    You can also run an image in interactive mode by using `shell` instead of `exec`. See this [guide](/additional-guides/running-a-container-in-interactive-mode). ==NOT DONE==

### Allocating a GPU to your job

The primary role of AI Lab is to run software that utilises one or more GPUs for computations. In order to run applications with a GPU you need to allocate a GPU to a job using Slurm. 

Let's try running a small Python script that performs a simple matrix multiplication of random data to benchmark TensorFlow computing speed:

!!! example
    Download <a href="/assets/scripts/benchmark_tensorflow.py" download="benchmark_tensorflow.py">benchmark_tensorflow.py</a> and copy it from your local computer to your user directory on AI Lab using the `scp` command or `WinSCP` (see [Step 2: File Transfer](/getting-started/file-transfer)):

    #### Execute job without GPU
    Now, lets first try executing `benchmark_tensorflow.py` without allocating a GPU:

    ```console
    srun singularity exec tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    After some time (*ignore the warnings*), the terminal should print something like: `Time taken: 21.1207 seconds`. This computation was performed on the CPU.

!!! example

    #### Execute with GPU
    You can allocate a GPU to a job by using the `-G` or `--gres=gpu` option for Slurm. You also need to add `--nv` to enable NVIDIA GPUs in the container. Lets try allocating 1 arbitrary available GPU to the job by adding `--gres=gpu:1` and notice the time difference:

    ```console
    srun --gres=gpu:1 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    !!! info "Allocating more than one GPU?"
        Note that the above example allocate 1 GPU to the job. It is possible to allocate more, for example `--gres=gpu:2` for two GPUs. Software for computing on GPU is not necessarily able to utilise more than one GPU at a time. It is your responsibility to ensure that the software you run can indeed utilise as many GPUs as you allocate. It is not allowed to allocate more GPUs than your job can utilise.


!!! example

    #### Execute with specific GPU
    In some cases your work requires a specific type of GPU. It could be, for example, that you need at least 20 GB of GPU RAM available. In that case at ==T4 GPU== does not meet the requirement. It could also be that you know that an ==A10 GPU== would be sufficient for your job, so there is no need to allocate an ==A40 GPU== to it. Get an overview of the GPUs available in AI Lab [here](/system-overview/#overview-of-compute-nodes).

    You can specify a specific type of GPU to allocate to your job. This is done by adding a *GPU type label* to the `--gres` option. Lets allocate 1 A10 GPU by adding `--gres=gpu:a10:1`:

    ```console
    srun --gres=gpu:a10:1 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    !!! info "Checking the status of compute nodes"
        It is often desirable to monitor the resource status of the compute nodes when you wish to run a job on a certain GPU. We recommend looking at our guide [Checking the status of compute nodes](/additional-guides/checking-the-status-of-compute-nodes).


    ==UPDATE EXAMPLE WITH a10:1 TO MATCH AI Lab GPU==


As the last step, it's important to understand the process of <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/offboarding/">Offboarding :octicons-arrow-right-24:</a></span>