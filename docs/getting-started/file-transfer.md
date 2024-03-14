
You can transfer files to/from AI Cloud using the command line utility
`scp` from your local computer (Linux and OS X). *To* AI Cloud:

???+ example

    ```console
	scp some-file <aau email>@ai-fe02.srv.aau.dk:~
	```

    where '~' means your user directory on AI Cloud. You can append
    directories below that to your destination:

???+ example

    ```console
	scp some-file <aau email>@ai-fe02.srv.aau.dk:~/some-dir/some-sub-dir/
	```

You can also copy in the opposite direction, e.g. from the AI Cloud
pilot platform to your local computer with:

???+ example

    ```console
	scp <aau email>@ai-fe02.srv.aau.dk:~/some-folder/some-subfolder/some-file .
	```

    where '.' means the current directory you are located in on your local
	computer.

In general, file transfer tools that can use SSH as protocol should
work. A common choice is [FileZilla](https://filezilla-project.org/)
or the Windows application [WinSCP](https://winscp.net/).