The following guidelines are put in place to ensure fair usage of the
system for all users. The following text might be updated from time to
time in order to provide the best possible service for as many users
as possible.

CLAAUDIA work from the following principles for fair usage:

- Good research is the success criterion and CLAAUDIA should lower
  the barrier for allowing this.
- Aim at the most open and unrestricted access model.

Based on these principles we kindly ask that all users consider the
following guidelines:

- Please be mindful of your allocations and refrain from allocating
  many resources without knowing/testing/verifying that you indeed can
  utilise all of the allocated resources.
- Please be mindful and de-allocate the resources when you are no
  longer using them. This enables other users to run their jobs.

If in doubt, you can run:
```console
squeue --me
```
and inspect your own job allocations. If you have allocations you are
not using, then please cancel these resource allocations.

A few key points to remember:

1. Please refrain from allocating jobs that sit idle in order to
   "reserve" ressources for you. For example `srun --pty bash -l`
   opens an interactive (command line) job that keeps running without
   doing anything unless you actively type in commands.  
   *This is unacceptable practice and we will cancel such inactive
   jobs if we encounter them.*
2. There are typically more resources available in the evenings/nights
   and on weekends. If possible, start your job as a batch script
   (`sbatch`) and let it queue and rest while the computer does the
   work. Maybe even better, if the job is not urgent, queue the job to
   run late in the afternoon or use the `-b` or `--begin` option with
   your batch script, e.g. add the line

   ```console
   #SBATCH --begin=18:00:00
   ```

ITS/CLAAUDIA will keep analysing and observing the usage of the system
to make the best use of the available resources based on the above
principles and guidelines. If ITS/CLAAUDIA is in doubt, we will
contact users and ask if the resource allocations are in line with the
above principles and guidelines. We will be more active in periods of
high utilization.