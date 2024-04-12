It is often desirable to monitor the resource status of the compute nodes when you wish to run a job. 

!!! example annotate
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

!!! example
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