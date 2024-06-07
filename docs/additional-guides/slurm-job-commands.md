Slurm Commands and Arguments Guide

### sbatch
Description: Submit a batch script for execution.
Arguments:
--ntasks=<number>: Number of tasks to be run.
--nodes=<number>: Number of nodes required.
--time=<time>: Maximum runtime for the job.
--partition=<partition>: Specify a partition for the job.
--mem=<memory>: Specify the memory required for the job.
--output=<filename>: Redirect stdout and stderr to the specified file.

1. squeue
Description: View the status of jobs in the queue.
Arguments:
--user=<username>: View jobs of a specific user.
--job=<job_id>: View details of a specific job.
--state=<state>: Filter jobs by state (e.g., pending, running).

1. scancel
Description: Cancel a job.
Arguments:
--user=$USER: Cancel all jobs of a specific user.
--job=<job_id>: Cancel a specific job.

1. scontrol
Description: Control Slurm daemons and configuration.
Arguments:
show config: Display the current Slurm configuration.
reconfigure: Reload the Slurm configuration.
update nodenames: Update node names.

1. sinfo
Description: View information about nodes and partitions.
Arguments:
--nodes: Display node information.
--long: Display detailed information.

1. srun
Description: Run a parallel job or task.
Arguments:
--ntasks=<number>: Number of tasks to run.
--nodes=<number>: Number of nodes to use.
--time=<time>: Maximum runtime for the job.


--gpus-per-node=1
--cpus-per-task=7
--mem-per-gpu=60G
--time=1:00:00