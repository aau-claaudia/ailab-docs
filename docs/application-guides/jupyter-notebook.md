srun singularity exec tensorflow_24.03-tf2-py3.sif jupyter notebook
ssh -L 8888:a256-t4-03:8888 ry90cd@its.aau.dk@ai-fe02.srv.aau.dk

This guide will show you how to start a Jupyter notebook on AI-LAB and access it in your browser.

#### 1. Open a Terminal and Allocate a Compute Node

To begin, open a terminal and run the following command:

```console
srun --pty /bin/bash
```

This command allocates a compute node for you. The --pty /bin/bash part ensures that a pseudo-terminal is created and a bash shell is started on the compute node.

#### 2. Identify Your Compute Node

After the node is allocated, you will see the name of the compute node in the terminal, which will look something like this:

```console
<email>@ailab-l4-01:~$
```
Replace `<email>` with your AAU email address.

In this example, the compute node allocated is `ailab-l4-01`.

#### 3. Connect to the Compute Node

Next, you need to connect to this compute node from another terminal window using SSH, and also set up port forwarding so you can access the notebook from your local computer. We use port 8888 as it is the default port for Jupyter notebooks.

First, open up a new terminal window. Use the following command, replacing `<email>` with your email and `ailab-l4-01` with your compute node name:

```console
ssh -L 8888:localhost:8888 <email>@ailab-l4-01.srv.aau.dk
```

This command logs you into the compute node and sets up a tunnel from port 8888 on your local machine to port 8888 on the compute node, allowing you to access the Jupyter notebook via your local browser.

#### 4. Start a Jupyter Notebook

You can now start a Jupyter notebook. Jupyter is included in the PyTorch and TensorFlow containers found in the container directory on AI-LAB. First, copy the PyTorch container image from the container directory on AI-LAB to your user directory:

```console
cp /ceph/container/pytorch_24.03-py3.sif .
```

Then, run the following command to start a Jupyter notebook:

```console
singularity exec pytorch_24.03-py3.sif jupyter notebook
```

#### 5. Access the Notebook

Open your browser and go to [localhost:8888](http://localhost:8888/). The token required to log in will be displayed in the terminal output.

```console
[I 08:30:06.090 NotebookApp] http://hostname:8888/?token=8db29582846a0a31dfbd5f539f8a5097252011919832d0bb
```

#### 6. Terminate your session

You can run an interactive session for a maximum of 12 hours. For more details, see the [guidelines](/guidelines/#4-jobs-can-run-no-longer-than-12-hours). It is recommended to stop the job as soon as you are done working interactively. Closing the terminal window where you ran `srun --pty /bin/bash` will stop the job.