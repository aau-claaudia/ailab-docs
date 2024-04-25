!!! custom "`--time` is a useful tool to prevent hangs"
    Sometimes, jobs may get stuck or encounter unforeseen issues, causing them to run indefinitely. Setting a time limit ensures that such jobs are automatically terminated after a certain duration, preventing them from consuming resources unnecessarily.

You can add a `--time` parameter to your Slurm command, e.g. `--time=24:00:00` to run a job for a maximum of 24 hours, or `--time=1-8:00:00` to run a job for maximum 1 day and 8 hours. 

!!! example
    ```console
    srun --time=00:00:10 hostname
    ```