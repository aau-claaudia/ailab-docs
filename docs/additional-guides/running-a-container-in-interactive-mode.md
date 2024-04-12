You can launch a shell within a Singularity container, allowing you to interact with the container's environment by using the `shell` command:

!!! example
    ```console
    srun --gres=gpu:1 --pty singularity shell --nv tensorflow_24.03-tf2-py3.sif
    ```

    The `--pty` creates a virtual interactive terminal for a command to run within.
    
    You now have shell access

    ```console
    Singularity>
    ```

    Lets try checking the Python version:

    ```console
    python3 --version
    ```

    You can exit the interactive session with:

    ```console
    exit
    ```