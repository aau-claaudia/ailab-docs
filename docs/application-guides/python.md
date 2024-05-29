# Installing Python and Pip Packages in Singularity Container on AI-LAB

This guide will walk you through the process of creating a Singularity container with Python and pip packages installed, and then running a Python example script within the container on the AI-LAB HPC platform.

### Step 1: Define Singularity Definition File

Create a Singularity definition file (e.g., `python-container.def`) with the necessary instructions to install Python and required packages. 
Here's an example definition file:

```bash
Bootstrap: docker
From: python:latest

%post
    apt-get update && apt-get install -y \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev
    pip install numpy pandas scikit-learn matplotlib # Add any other required packages
```


Type `nano` and press `ENTER` (or use the editor of your choice), and enter the packages of your choice in the editor. In this example we will install the latest python version and `python=3.11.0` and `numpy=1.23.5`:

### Step 2: Build Singularity Image
Build the Singularity image using the definition file:

```console
sudo singularity build python_container.simg container.def
```

This command will create a Singularity image named python_container.simg based on the definition file container.def.

### Step 3: Run Python Script
Write your Python script (e.g., your_script.py) and save it in your working directory. Here's a simple example script:

```python
# your_script.py
import numpy as np

x = np.random.rand(10)
print("Generated random numbers:", x)
```


Submit a job to AI-LAB using Slurm to run your Python script within the Singularity container.

```console
singularity exec python_container.sif python your_script.py
```

This will submit the job to AI-LAB, and the output will be written to output.log.

That's it! You have now installed Python and pip packages in a Singularity container and run a Python script on the AI-LAB HPC platform.

#### Checkpointing
Checkpointing is a technique used to ensure that your computational jobs can be resumed from a previously saved state in case of interruptions or failures. [This guide](/additional-guides/checkpointing/#python-data-checkpointing) demonstrates a basic checkpointing mechanism using the standard Python module [pickle](https://docs.python.org/3/library/pickle.html) to periodically save the data of a process to a file.