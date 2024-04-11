# Running Applications
Now that you are acquainted with [obtaining applications](/getting-started/obtaining-applications) and the [queue system](/getting-started/queue-basics), we can try running an application. If you followed the example in the [Obtaining Applications](/getting-started/obtaining-applications) page, you should now have a container image in your user directory (the file `tensorflow_24.03-tf2-py3.sif`). We can run this container using the `exec` command:

???+ example

    `exec` executes a specified command (such as running a script) in a container. This is useful if you know exactly which command you wish to run in your container.

        srun singularity exec tensorflow_24.03-tf2-py3.sif hostname
	
	Here we use `hostname` as a toy example of a command that prints out a simple piece of information and then exits.

!!! info   
    You can also run a container in interactive mode by using `shell` instead of `exec`. See this [guide](/advanced-guides/running-a-container-in-interactive-mode).

### Allocating a GPU to your job

The primary role of the AI Student Cloud is to run software that utilises one or more GPUs for computations. In order to run applications with a GPU you need to allocate a GPU to a job using Slurm. 

Let's try running a small Python script that performs a simple matrix multiplication of random data to benchmark TensorFlow computing speed:

???+ example
    Download <a href="/assets/scripts/benchmark_tensorflow.py" download="benchmark_tensorflow.py">benchmark_tensorflow.py</a> and copy it from your local computer to your user directory on AI Student Cloud using the `scp` command or `WinSCP` (see [Step 2: File Transfer](/getting-started/file-transfer)):

    #### Execute job without GPU
    Now, lets try executing `benchmark_tensorflow.py` without allocating a GPU:

    ```console
    srun singularity exec tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    After some time (*ignore the warnings*), the terminal should print something like: `Time taken: 21.1207 seconds`. This computation was performed on the CPU.

    #### Execute with GPU
    You can allocate a GPU to a job by using the `-G` or `--gres=gpu` option for Slurm. You also need to add `--nv` to enable NVIDIA GPUs in the container. Lets try allocating 1 arbitrary available GPU to the job by adding `--gres=gpu:1` and notice the time difference:

    ```console
    srun --gres=gpu:1 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    ???+ warning
        Note that the above example allocate 1 GPU to the job. It is possible to allocate more, for example `--gres=gpu:2` for two GPUs. Software for computing on GPU is not necessarily able to utilise more than one GPU at a time. It is your responsibility to ensure that the software you run can indeed utilise as many GPUs as you allocate. It is not allowed to allocate more GPUs than your job can utilise.


    #### Execute with specific GPU
    In some cases your work requires a specific type of GPU. It could be, for example, that you need at least 20 GB of GPU RAM available. In that case at ==T4 GPU== does not meet the requirement. It could also be that you know that an ==A10 GPU== would be sufficient for your job, so there is no need to allocate an ==A40 GPU== to it. Get an overview of the GPUs available in AI Student Cloud [here](/system-overview/#overview-of-compute-nodes).

    You can specify a specific type of GPU to allocate to your job. This is done by adding a *GPU type label* to the `--gres` option. Lets allocate 1 A10 GPU by adding `--gres=gpu:a10:1`:

    ```console
    srun --gres=gpu:a10:1 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
    ```

    ==UPDATE EXAMPLE WITH a10:1 TO MATCH AI STUDENT CLOUD GPU==


<br>
<span style="color: var(--md-primary-fg-color); font-weight: 700;">:material-party-popper: Congratulations! </span>You have now completed the basics of getting started with AI Student Cloud. As you continue your journey, it's important to understand the process of [offboarding](/getting-started/offboarding) from the platform. We also suggest you have a closer look at [Courses](/courses/terminal-basics) which contains more detailed examples of concrete use cases for the AI Student Cloud.

???+ warning
    ==Please ensure you review our [offboarding](/getting-started/offboarding) process, as CLAAUDIA will automatically clear all user information and directories and close any running processes at the end of each semester.==

For all questions and requests, please refer to the [support](/support) page.