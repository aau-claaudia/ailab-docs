### What is AI Student Cloud
The AI Student Cloud is designed exclusively for students at Aalborg University, offering [high-performance computing (HPC)](https://www.researcher.aau.dk/guides/research-data/high-performance-computing/introduction-to-hpc) right at your fingertips. Think of it as a mini supercomputer, packed with GPUs, making it a perfect playground for training [deep learning](#) models, running simulations, and performing high-speed data analysis.

This platform is home to an extensive collection of [GPU resources](/overview/#system-overview), tailored specifically for machine learning tasks. Whether you're working on image recognition, deep learning tasks, or data processing, AI Student Cloud is equipped to handle vast processes that benefit from [parallel computing](#).

### What is the purpose of AI Student Cloud?
AI Student Cloud isn't just about providing hardware; it's about opening the door to high-performance computing for students, with an educational twist. From simulations to deep learning, it supports a large number of [applications](/tutorials/matlab), all while fostering an environment where students can experiment, learn, and grow their computational skills. We advocate reading the [Usage policy](/usage-policy/) of AI Student Cloud before getting started.

### How to access?
First you need to fill out an [application form](#)==CHANGE LINK== to request for access. After getting approval, you can access AI Student Cloud using a terminal application from your computer to log into the [front-end node](#). This is where you'll manage files and submit jobs to be processed on the GPU nodes. It's a shared resource, emphasizing learning how to navigate a queueing mechanism and understand containerization. We will guide you through all this in [Getting started](/getting-started/login).

### Who manage AI Student Cloud
AI Student Cloud is a facility at Aalborg University managed by the [CLAAUDIA](https://www.researcher.aau.dk/contact/claaudia) team.


## System overview
AI Student Cloud consists of a front-end node (ai-fe02.srv.aau.dk) and a number of compute nodes. AI Student Cloud is a heterogeneous platform with several different
types of hardware available in the compute nodes.

The compute nodes of the AI Student Cloud currently include: 

| Node name  | CPU                       | System RAM | GPU                         |
| ---------- | ------------------------- | ---------- |  -------------------------- |
| a256-t4-01 | 2x AMD EPYC 7302 16-core  | 256GB      | 6x NVIDIA T4 GPUs, 16GB RAM |
| ==PUT IN NEW AI STUDENT CLOUD NODES== | ........................  | .......... | ........................... |
| .......... | ........................  | .......... | ........................... |

This diverse selection of
different hardware in the AI Student Cloud allows for more suitable choice of
specific hardware according to your task. For example, the DGX-2
compute nodes are better suited for the
comutationally intensive training of deep neural networks, while the
compute nodes with T4 GPUs are better suited for inference tasks using
an already trained model.

``` mermaid
flowchart LR
  subgraph id1[ ]
    direction LR
    B[<img src='/assets/img/desktop-tower.svg' width='25' height='25' /> Front-end node ai-fe-02];
    B -.-> C["<img src='/assets/img/desktop-tower.svg' width='25' height='25' /> Compute nodes a256-t4-[01-03]"];
    B -.-> D["<img src='/assets/img/desktop-tower.svg' width='25' height='25' /> Compute nodes  a256-t4-[01-03]"];
    B -.-> E["<img src='/assets/img/desktop-tower.svg' width='25' height='25' /> Compute nodes  a256-t4-[01-03]"];
    B -.-> F["<img src='/assets/img/desktop-tower.svg' width='25' height='25' /> Compute nodes  a256-t4-[01-03]"];
  end
  subgraph id2[AI Student Cloud]
    direction TB
     G["<img src='/assets/img/database-arrow-up-outline.svg' width='25' height='25' /> User directory on CephFS network drive "] <--> id1
  end
  A[<img src='/assets/img/laptop.svg' width='25' height='25' /> Your computer] -->|SSH| id2
```
 ==UPDATE TO MATCH AI STUDENT CLOUD SYSTEM==

### Front-end node
The front-end node is used for logging into the platform, accessing your files, and starting jobs on the compute nodes. The front-end node
is a relatively small server which is *not* meant for performing heavy
computations; only light-weight operations such as transferring files
to and from AI Student Cloud and defining and launching job scripts.

### File storage
The AI Student Cloud stores your
files in your user directory. Your user directory is stored on a
network file system that allows all of the nodes within the platform
can access your files. This means that if you store or edit a file in
your user directory on the front-end node, the compute nodes
can see the same file and contents thereof. The nodes
access the network file system in a shared manner, so there is nothing
you need to do to synchronise the files between the nodes.

The details of defining and running jobs are described in the
[Getting Started](/getting-started/getting-access) section.
