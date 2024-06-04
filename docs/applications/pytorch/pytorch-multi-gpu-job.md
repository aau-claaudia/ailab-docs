
mnist_ddp.py:
https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp.py

```
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=40GB
#SBATCH --time=0:15:00
#SBATCH --gres=gpu:4

# New way with torchrun
singularity exec --nv pytorch_24.03-py3.sif torchrun --standalone --nnodes=1 --nproc_per_node=4 mnist_ddp.py --epochs=100
```

```
sbatch run-ddp-gpu4.sh
```

```
srun --overlap --pty --jobid=<Job ID> bash
```

```
nvidia-smi
```

```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.171.04             Driver Version: 535.171.04   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A10                     Off | 00000000:4B:00.0 Off |                    0 |
|  0%   43C    P0              64W / 150W |    505MiB / 23028MiB |     15%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA A10                     Off | 00000000:65:00.0 Off |                    0 |
|  0%   44C    P0              66W / 150W |    505MiB / 23028MiB |     37%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA A10                     Off | 00000000:B1:00.0 Off |                    0 |
|  0%   41C    P0              65W / 150W |    505MiB / 23028MiB |     12%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA A10                     Off | 00000000:CA:00.0 Off |                    0 |
|  0%   44C    P0              67W / 150W |    505MiB / 23028MiB |     43%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
```

