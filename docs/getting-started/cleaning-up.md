==TODO==


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
