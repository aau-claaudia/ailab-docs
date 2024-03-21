Before you start running your computations, simulations, train machine learning algorithms etc, it is important to be aware of AI Student Cloud queueing system [Slurm](https://slurm.schedmd.com/quickstart.html).

## Slurm queue system

??? info "What is Slurm?"
    Slurm Workload Manager is an open-source cluster management and job scheduling system for large and small Linux clusters. Slurm is used to allocate resources, manage user jobs, and provide a framework for job queueing, scheduling, and execution.

Applications can only be run on the compute nodes through Slurm. You
quite literally only have access to the compute nodes when you have a
job allocated on them.

The simplest way to run a job via Slurm is to use the command `srun`, which you have already used when installing containers on AI Student Cloud.

!!! example

    ```console
    srun hostname
    ```
    This runs the command `hostname` as a job in the queue system. When
      run like this with no further parameters specified, Slurm will run the
      command on the first compute node available.  

    The command will return one of these host names. If the command displays
    `srun: job XXXXXX queued and waiting for resources`, this means that all
    compute nodes are fully occupied (by other users' jobs) and your job is
    waiting in queue to be executed when resources become available.

    This was your first Slurm job. You will need this (`srun`) and other
    Slurm commands for most of your work in AI Student Cloud. You will see more
    examples in combination with Singularity in the next section.

### Checking the current state of the compute nodes

It is often desirable to monitor the resource status of the compute nodes when you wish to run a job. 

???+ example annotate

    The `sinfo` command shows basic information about partitions in the
    queue system and what the states of nodes in these partitions are.

        sinfo
          
        PARTITION (1)   AVAIL (2)  TIMELIMIT (3)  NODES (4)  STATE (5) NODELIST (6)
        batch*             up       12:00:00          1        mix     nv-ai-04
        batch*             up       12:00:00          8       idle     a256-t4-[01-02],i256-a10-06,i256-a40-[01-02]...
        prioritized        up     6-00:00:00          8       idle     a256-t4-[01-02],i256-a10-06,i256-a40-[01-02]...

1.  `PARTITION` In the context of the AI Student Cloud, partitions can be understood as distinct categories or groups of compute nodes, essentially serving as separate queues for jobs. Each partition defines a set of conditions under which jobs can access these nodes. It's possible for the same compute node to be a part of multiple partitions, like `batch` and `prioritized`. These will be explained later.
2.  `AVAIL` shows the availability of the partition where "up" is normal, working state where you can submit jobs to it.
3.  `TIMELIMIT` shows the time limit imposed by each partition in `HH:MM:SS` format.
4.  `NODES` shows how many nodes are in the shown state in the specific partition.
5.  `STATE` shows which state the listed nodes are in: `mix` means that the nodes are partially full - some jobs are running on them and they still have available resources; `idle` means that they are completely vacant and have all resources available; `allocated` means that they are completely occupied. Many other states are possible, most of which mean that something is wrong.
6.  `NODELIST` shows the specific compute nodes that is affected by the job.


You can also use the command `scontrol show node` or `scontrol show node <node name>` to show details about all nodes or a specific node, respectively.

???+ example
    ```console
    scontrol show node a256-t4-01

    NodeName=a256-t4-01 Arch=x86_64 CoresPerSocket=16
    CPUAlloc=12 CPUTot=64 CPULoad=0.50
    AvailableFeatures=(null)
    ActiveFeatures=(null)
    Gres=gpu:t4:6
    NodeAddr=172.21.212.130 NodeHostName=a256-t4-01.srv.aau.dk Version=21.08.8-2
    OS=Linux 5.4.0-170-generic #188-Ubuntu SMP Wed Jan 10 09:51:01 UTC 2024
    ...
    ```
The two commands `sinfo` and `scontrol show node` provide information
which is either too little or way too much detail in most
situations. As an alternative, we provide the tool `nodesummary` to
show a hopefully more intuitive overview of the used/available
resources in AI Student Cloud.

![Screenshot of `nodesummary` in use.](/assets/img/nodesummary.png)


### What is in the queue?

When using the cluster, you typically wish to see an overview of what
is currently in the queue. For example to see how many jobs might be
waiting ahead of you or to get an overview of your own jobs.

The command `squeue` can be used to get a general overview:

???+ example annotate

        squeue

        JOBID(1) PARTITION(2)		NAME(3)	 USER(4) ST(5) TIME(6)	NODES(7) NODELIST(REASON)(8)
        31623	     batch		    DRSC xxxxxxxx     R	6:45:14		    1         i256-a10-10
        31693	     batch      singular yyyyyyyy     R	  24:20		    1         i256-a40-01
        31694	     batch      singular yyyyyyyy     R	  24:20		    1         i256-a40-01
        31695	     batch      singular yyyyyyyy     R	  24:20		    1         i256-a40-01
        31696	     batch      singular yyyyyyyy     R	  24:20		    1         i256-a40-01
        31502    prioritiz       runQHGK.zzzzzzzz    PD	   0:00		    1        (Dependency)
        31504    prioritiz       runQHGK.zzzzzzzz    PD	   0:00		    1        (Dependency)

1.  `JOBID` shows the ID number of each job in queue.
2.  `PARTITION` shows which partition each job is running in.
3.  `NAME` is the name of the job which can be specified by the user creating it.
4.  `USER` is the username of the user who created the job.
5.  `ST` is the current state of each job; for example "R" means a job is running and "PD" means pending. There are other states as well - see `man squeue` for more details (under "JOB STATE CODES").
6.  `TIME` shows how long each job has been running. NODES shows how many nodes are involved in each job allocation.
7.  `NODES` shows how many nodes are involved in each job allocation.
8.  `NODELIST` shows which node(s) each job is running on, or alternatively, why it is not running yet.

 
Showing your own jobs only:

???+ example

        squeue --me

`squeue` can show many other details about jobs as well. Run `man
squeue` to see detailed documentation on how to do this.


## Running applications in containers

Now that you are acquainted with [installing applications](/getting-started/installing-applications) and the queue system, we can try running an application. If you followed the example in the [Installing Applications](/getting-started/installing-applications) page, you should now have a container image in your user directory (the file `tensorflow_22.07-tf2-py3.sif`). We can run this container in several ways:

#### 1. Shell
You can open a shell in the container. This basically gives you a command line in the runtime environment inside the container where you can work interactively, i.e. type commands in the command line to run scripts and open applications.   This is good for experimenting with how you wish to run your computations, analyses etc. in the container.

???+ example
       
        srun --pty singularity shell tensorflow_22.07-tf2-py3.sif
    
    The `--pty` parameter is necessary in order to enable typing commands
    into the command line in the job. After opening the shell in the
	container, your command line terminal should display:
	
	    Singularity>
	
	This means that it is ready for you to type in commands. Type `exit`
	and hit ENTER to exit the container and stop the running job.

#### 2. Exec
Execute a specified command (such as running a script) in a container. This is useful if you know exactly which command you wish to run in your container.

???+ example

        srun singularity exec tensorflow_22.07-tf2-py3.sif hostname
	
	Notice here that the `--pty` option is not necessary if the executed
	command does not need keyboard input while running. Here we use
	`hostname` as a toy example of a command that prints out a simple
	piece of information and then exits.

#### 3. Run
Run the default action configured in the container. The container determines what the default action is. This is useful if you have obtained a container constructed to carry out a specific task.

???+ example

        srun --pty singularity run tensorflow_22.07-tf2-py3.sif
	
	In some cases, the default action of a container is to open the shell.
	This is why we use the `--pty` option here.

### Allocating a GPU to your job

The primary role of the AI Student Cloud is to run software that utilises one
or more GPUs for computations.

The final step we need here in order to run applications with a GPU is
to actually allocate a GPU to a job using Slurm. The examples up to
now have all run jobs without a GPU. It is necessary to explicitly ask
Slurm for a GPU in order to be able to use one.

???+ example

    You can allocate a GPU to a job by using the `-G` or `--gres=gpu`
    option for Slurm
	
	    srun -G 1 nvidia-smi
	
	This example allocates 1 GPU to a job running the command
	`nvidia-smi`. This command prints information about the allocated
	GPU and then exits.  
	
	Note that the above example allocate 1 GPU to the job. It is
	possible to allocate more, for example `-G 2` for two GPUs.
	
???+ warning
    Software for computing on GPU is not necessarily able to utilise
    more than one GPU at a time. It is your responsibility to ensure that
    the software you run can indeed utilise as many GPUs as you
    allocate. It is not allowed to allocate more GPUs than your job can
    utilise.


### Using a specific type of GPU

In some cases your work requires a specific type of GPU. It could be,
for example, that you need at least 20 GB of GPU RAM available. In
that case at T4 GPU does not meet the requirement. It could also be
that you know that an A10 GPU would be sufficient for your job, so
there is no need to allocate an A40 GPU to it. Get an overview of the GPUs available in AI Student Cloud [here](/overview/system-overview).

In cases like these, you can specify a specific type of GPU to
allocate to your job. This is done by adding a GPU type *label* to the
`--gres` option to the `srun` command.

???+ example

        sun --gres=gpu:a10:1 my_job_script.sh

  The `--gres` option lets you specify the type of GPU(s) to
	allocate to your job. In this example, the specification `gpu:a10:1`
	means that you are asking for 1 A10 GPU.

	If you merely use `--gres=gpu:1` you will be allocated an arbitrary
	available GPU in the cluster.


### Integrating a GPU with a container

In most cases you probably want to use a GPU in combination with a
Singularity container. In this case, we also need to remember to
enable support for NVIDIA GPUs in Singularity:

???+ example

        srun --gres=gpu:1 singularity exec --nv tensorflow_22.07-tf2-py3.sif nvidia-smi

    The `--nv` option enables NVIDIA GPUs in the container and must always
    be used when running jobs that utilise GPU(s). Otherwise, the GPU(s)
    will not be available inside the container.

These were a few of the most basic details to get started using the AI Student Cloud. Once you have familiarised yourself a bit with the AI Student Cloud, we
suggest you have a closer look at [Application Guides](/application-guides/interactive-tensorflow/) which contains more detailed examples of concrete use cases for the AI Student Cloud.


==TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO==

==Batch / prioritized - vil det være det samme i student cloud?==
==sbatch vs srun? Hvornår skal man bruge sbatch?==
==Prøv at se om checkpointing virker==

## Selecting a partition

??? info "What is a partition?"
    You can think of partitions as different queues for the compute nodes. There are several partitions in the AI Student Cloud and the same nodes can be present in more than one partition.
    For any one node, the different partitions it is present in can for example give access to the node under different conditions. The AI Student Cloud currently has the partitions: batch and prioritized.
  
### The *prioritized* partition

The default partition in AI Student Cloud is *prioritized*. If you submit a
job without specifying a partition, e.g. `sbatch --gres=gpu:1
job_script.sh`, your job automatically gets run in the *prioritized*
partition. All users have access to the *prioritized* partition. This partition has a 6-day time
limit and other jobs cannot cancel jobs in this partition.

### The *batch* partition

The batch partition
has a time limit of 12 hours and furthermore, jobs can get cancelled
(pre-empted) by other jobs running in other partitions. The *batch* partition
is not very interesting to use due to the pre-emption feature.

In order to use the *batch* partition, you must specify it for
your jobs with the "--partition" or "-p" option:

???+ example

    Using the "-p" option to specify a partition for a batch job.

        sbatch -p batch --gres=gpu:1 job_script.sh


## Running longer jobs {#requeueing}

In some cases, you need to run jobs that take longer than the 6 days
which is the maximum run-time of jobs in the *prioritized*
partition. The way to do this is to configure your jobs to be
re-queued if they run out of time. There are two necessary ingredients
to making this work:

1. Instruct Slurm that your job should be requeued if it gets stopped.
2. Program/configure your job workload to use checkpointing of working
   data so that the work can continue from the latest checkpoint when
   it gets the opportunity to start again.

### Instruct Slurm to requeue your job

Note that this only makes sense if you have programmed or configured
your workload to use checkpointing so that it is able to continue from
where it last stopped. If this is not the case, your job would merely
start over from the beginning when requeued and you could end up with
a job that keeps starting over forever but never really finishes.

To instruct Slurm that your job can be requeued if stopped (due to for
example time-out or pre-emption as mentioned above in
[*batch*](#batch)), add the parameter `--requeue` to the `sbatch`
command when submitting your job:

???+ example

        sbatch --requeue --gres=gpu:t4:1 job_script.sh

    Using the "--requeue" option to instruct Slurm that your job can be requeued

We advise that you request a specific type of GPU (for example T4
above) or a specific node when working with requeueable jobs, since we
cannot guarantee what would happen if your job initially started
running with one type of GPU and then subsequently attempted to
continue from a checkpoint with a different type of GPU.

### Use checkpointing {#checkpointing}

Checkpointing means that you configure or program your workload to
store its working data so far to a temporary location on disk at
regular intervals. When the workload starts running, it should first
check if it has an already stored checkpoint on disk, and continue from
there if it finds one.

This way, if your job suddenly gets stopped, you can start it again
and it automatically continues running from its latest saved
checkpoint.

How to implement checkpointing depends on the details of how your
workload has been programmed. If you have programmed your workload
from scratch yourself, the general recipe is to add the following
functionality to your program:

1. Look for an exisiting checkpoint file.
2. If the file exists; load it and continue work from there.
3. If not; start the work from scratch.
4. While working; save the necessary internal data and output data so
   far to a checkpoint file at regular time intervals.
5. When the program completes without errors; save the final output
   data the way you would normally save your output data and delete
   the checkpoint file.

For example, if your program stores a checkpoint every 15 minutes, you
would only risk losing up to 15 minutes of work if the job gets
stopped. All of the prior work is stored in your most recent
checkpoint which your workload can automatically load and continue
from.

Some popular libraries often used in AI Cloud have built-in features
you can use for checkpointing:

- **TensorFlow** provides a [guide
  here](https://www.tensorflow.org/guide/checkpoint) on how to use
  checkpointing in TensorFlow model training.  
  Similarly, the Keras interface also has [this
  mechanism](https://keras.io/api/callbacks/model_checkpoint/) that
  can be used to implement checkpointing.
- **PyTorch** provides a [guide
  here](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html)
  on how to use checkpointing in PyTorch model training.

*You are welcome to suggest additions to this list if you know useful
checkpointing mechanisms for other software that can be used on AI
Cloud.*

