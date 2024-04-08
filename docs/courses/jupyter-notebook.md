´srun --mem 50G singularity pull docker://nvcr.io/nvidia/pytorch:24.03-py3´

´salloc´

´ssh -L 9999:localhost:9999 a256-t4-02´

´srun --pty singularity shell pytorch_24.03-py3.sif´




salloc is a command used in Slurm, a workload manager used in high-performance computing (HPC) environments, to allocate resources for a job before it is executed.

The salloc command is typically used to obtain an interactive shell session or to allocate resources for a specific task without submitting a job script. It allows users to request resources such as CPU cores, memory, GPUs, and time, and interactively run commands or launch applications within the allocated resources.

Here's a basic usage of the salloc command:

bash
Copy code
salloc --nodes=1 --ntasks-per-node=1 --time=1:00:00
In this example, salloc is used to allocate resources for a job on one node with one task per node, and a time limit of 1 hour.

After running salloc, users typically obtain a shell prompt within the allocated resources, where they can interactively execute commands or launch applications. Once the allocated resources are no longer needed, users can exit the session, and the resources will be released back to the Slurm scheduler.