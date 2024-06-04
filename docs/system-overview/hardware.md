The AI-LAB platform is built around several key components, including two front-end nodes for managing tasks and code, and 11 compute nodes equipped with diverse hardware options.

In this overview, you will find a description of each major component of AI-LAB. Below, is a diagram illustrating the architecture of the AI-LAB platform.

``` mermaid
flowchart LR
  subgraph id1[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 12px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 5px;">Computing cluster</p>]
    direction TB
    A["<span><img src="/assets/img/server.svg"  width='25' height='25' >Compute nodes ailab-l4-[01-11]</span>"] ~~~ B["<span><img src="/assets/img/server.svg" width='25' height='25'>Compute nodes vmware[01-04]</span>"]
    end

  subgraph id2[<p style="font-family: Barlow, sans-serif; font-weight: 800; font-size: 16px; text-transform: uppercase; color: #221a52; letter-spacing: 1px; margin: 10px;">AI-LAB</p>]
    direction LR
    G["<span><img src="/assets/img/server.svg" width='25' height='25'>Front-end node (ailab-fe01)</span>"] --> id1 
    H["<span><img src="/assets/img/server.svg" width='25' height='25'>Front-end node (ailab-fe02)</span>"] --> id1 
    id1 <--> E[<span><img src="/assets/img/database.svg" width='25' height='25'>File storage</span>]
    end

  F[<span><img src="/assets/img/person.svg" width='25' height='25'>User</span>]-- SSH --> G
  F[<span><img src="/assets/img/person.svg" width='25' height='25'>User</span>]-- SSH --> H
```

<hr>

## Front-end nodes
You start by logging into a front-end node, either `ailab-fe01` or `ailab-fe02`. These nodes act as the gateway to the HPC system. Here, you can manage files, write and edit code, and prepare your computational tasks. It is important to note that front-end nodes are not intended for heavy computations; they are optimized for task preparation and interaction with the HPC environment.

your computational tasks. The front-end node is *not* for heavy computations but for preparation and interaction with the HPC system.

<hr>

## Compute nodes
AI-LAB currently include the following compute nodes:

| Node name            | CPU model             | Number of CPUs | Number of cores | Number of GPUs | GPU Model | Total Memory (GB) |
| -------------------- | --------------------- | -------------- | --------------- | -------------- | --------- | ----------------- |
| ailab-l4-[01-11]     | AMD EPYC 7543 32-Core | 128            | 64              | 8              | NVIDIA L4 | 500               |
