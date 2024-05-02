<div class="tree">
  <ul>
    <li><i class="fa fa-folder-open"></i> Ceph/
      <ul>
        <li><i class="fa fa-folder-open"></i> home
          <ul>
            <li><i class="fa fa-folder-open"></i> doman
              <ul>
                <li><i class="fa fa-folder-open"></i> user
                  <ul>
                    <li><i class="fa fa-code"></i> CSS Files</li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li><i class="fa fa-folder-open"></i> project
          <ul>
             <li><i class="fa fa-folder-open"></i> 1234 <span>project group number</span>
                <ul>
                  <li><i class="fa fa-code"></i> CSS Files</li>
                </ul>
             </li>
          </ul>
        </li>
        <li><i class="fa fa-folder-open"></i> course
          <ul>
              <li><i class="fa fa-folder-open"></i> Course 1. Introduction to TensorFLow
                <ul>
                  <li><i class="fa fa-folder"></i> Images</li>
                  <li><i class="fa fa-code"></i> tensorflow_24.03-tf2-py3.sif</li>
                </ul>
              </li>
              <li><i class="fa fa-folder-open"></i> Course 2. ...
             </li>
          </ul>
        </li>
        <li><i class="fa fa-folder-open"></i> container
          <ul>
            <li><i class="fa fa-code"></i> tensorflow_24.03-tf2-py3.sif</li>
            <li><i class="fa fa-code"></i> ...sif</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</div>

<div class="mt-5 pl-3">
  <strong>Note:</strong> Saw this online and had to create a SASS version for <a href="http://bootadmin.org">BootAdmin.org</a>.
</div>


!!! custom "<span class="custom-callout-icon">:fontawesome-solid-computer: Front-end node</span>"
    You start by logging into a front-end node. This is the gateway to the HPC system. Here, you can manage files, write and edit code, and prepare your computational tasks. The front-end node is *not* for heavy computations but for preparation and interaction with the HPC system.

<span class="arrow-down">:octicons-arrow-down-24:</span>

!!! custom "<span class="custom-callout-icon">:octicons-database-16: File storage</span>"
    AI Lab stores your files in your user directory. Your user directory is stored on a network file system that allows all of the nodes within the platform
    can access your files. This means that if you store or edit a file in your user directory on the front-end node, the compute nodes can see the same file and contents thereof.

<span class="arrow-down">:octicons-arrow-down-24:</span>

!!! custom "<span class="custom-callout-icon">:material-human-queue: Queue system</span>"
    After preparing your computational task, you submit it to AI Labs queue system, [Slurm](/glossery/#slurm). Slurm is like a traffic controller. It receives job submissions from users and decides when and where to run each job based on available resources and the job's requirements. Your job is placed in a queue until resources are available.

<span class="arrow-down">:octicons-arrow-down-24:</span>

!!! custom "<span class="custom-callout-icon">:fontawesome-solid-box-open: Containers</span>"
    One job could be to deploy an applications such as TensorFlow. All applications on AI Lab must be obtained in [containers](/glossery/#containers). Containers are like virtual packages that hold all the stuff your program needs to run smoothly. They bundle up everything – the code, libraries, and settings.

<span class="arrow-down">:octicons-arrow-down-24:</span>

!!! custom "<span class="custom-callout-icon">:octicons-server-24: Compute nodes</span>"
    Once resources are available, Slurm dispatch the submitted job to specific [compute nodes](/glossery/#compute-nodes) within the AI Lab [computing cluster](/glossery/#computing-cluster).

``` mermaid
flowchart LR
  subgraph id1[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 12px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 5px;">Computing cluster</p>]
    direction TB
    A["<span><img src="/assets/img/server.svg"  width='25' height='25' >Compute nodes A256-t4-[01-03]</span>"] ~~~ B["<span><img src="/assets/img/server.svg" width='25' height='25'>Compute nodes A256-t4-[01-03]</span>"] ~~~ C["<span><img src="/assets/img/server.svg" width='25' height='25'>Compute nodes A256-t4-[01-03]</span>"] ~~~ D["<span><img src="/assets/img/server.svg" width='25' height='25'>Compute nodes A256-t4-[01-03]</span>"]
    end

  subgraph id2[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 16px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 10px;">AI Lab</p>]
    direction LR
    G["<span><img src="/assets/img/server.svg" width='25' height='25'>Front-end node (a256-t4-01)</span>"] --> id1 <--> E[<span><img src="/assets/img/database.svg" width='25' height='25'>File storage</span>]
    end

  F[<span><img src="/assets/img/person.svg" width='25' height='25'>User</span>]-- SSH --> G
```
 ==UPDATE TO MATCH AI Lab SYSTEM==


### Overview of compute nodes
AI Lab is a heterogeneous platform with several different types of hardware available in the compute nodes and currently include:

| Node name      | CPU                           | System RAM | GPU                             |
| -------------- | ----------------------------- | ---------- |  ------------------------------ |
| ==a256-t4-01== | ==2x AMD EPYC 7302 16-core==  | ==256GB==  | ==6x NVIDIA T4 GPUs, 16GB RAM== |
| .............. | ............................  | .......... | ............................... |

This diverse selection of different hardware in AI Lab allows for more suitable choice of
specific hardware according to your task. ==MAYBE EXPLAIN EXAMPLES OF WHAT JOBS DIFFERENT NODES WOULD BE FIT FOR==


### List of pre-installed software

```console
SingularityCE 4.1.2
Slurm 23.11
Python 3.9.2
Micro
```

==UPDATE LIST==