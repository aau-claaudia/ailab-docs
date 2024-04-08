You can use `shell` command to open a shell in the container. This basically gives you a command line in the runtime environment inside the container where you can work interactively, i.e. type commands in the command line to run scripts and open applications. This is good for experimenting with how you wish to run your computations, analyses etc. in the container.

???+ example
       
        srun --pty singularity shell tensorflow_22.07-tf2-py3.sif
    
    The `--pty` parameter is necessary in order to enable typing commands
    into the command line in the job. After opening the shell in the
	container, your command line terminal should display:
	
	    Singularity>
	
	This means that it is ready for you to type in commands. Type `exit`
	and hit ENTER to exit the container and stop the running job.
