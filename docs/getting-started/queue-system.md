# Queue System
Before you start running your computations, simulations, train machine learning algorithms etc, it is important to be aware of AI Student Cloud queueing system [Slurm](https://slurm.schedmd.com/quickstart.html).

???+ info "What is Slurm?"
    Slurm Workload Manager is an open-source cluster management and job scheduling system for large and small Linux clusters. Slurm is used to allocate resources, manage user jobs, and provide a framework for job queueing, scheduling, and execution.

Applications can only be run on the compute nodes through Slurm. You
quite literally only have access to the compute nodes when you have a
job allocated on them.

The simplest way to run a job via Slurm is to use the command `srun`.

!!! example

    ```console
    srun hostname
    ```

    This runs the command `hostname` as a job in the queue system. When run like this with no further parameters specified, Slurm will run the command on the first compute node available.  

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
    ==NEED TO BE UPDATED TO AI STUDENT CLOUD SPECIFICS==
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
    ==NEED TO BE UPDATED TO AI STUDENT CLOUD SPECIFICS==
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

==SCREENSHOT NEED TO BE UPDATED TO AI STUDENT CLOUD SPECIFICS==
![Screenshot of `nodesummary` in use.](/assets/img/nodesummary.png)


### What is in the queue?

When using the cluster, you typically wish to see an overview of what
is currently in the queue. For example to see how many jobs might be
waiting ahead of you or to get an overview of your own jobs.

The command `squeue` can be used to get a general overview:

???+ example annotate
    ==NEED TO BE UPDATED TO AI STUDENT CLOUD SPECIFICS==

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

Now that you know the basics of the queueing system, lets proceed to learn about how to <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/obtaining-applications">obtain applications :octicons-arrow-right-24:</a></span>