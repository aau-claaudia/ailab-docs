===+ "Windows"
	For Windows users we recommend using the application [WinSCP](https://winscp.net/eng/docs/lang:da) to transfer files from your local computer to AI Student Cloud. Other popular solutions are [PuTTY](https://www.putty.org/) and [FileZilla](https://filezilla-project.org/).

	![Screenshot of WinSCP setup](/assets/img/winscp-setup.png)
	
	==Remember to change image with new server address==

	When you open WinSCP, you will be welcomed by a 'Login' modal. Follow the instructions in the image above to establish a connection to the server. You can now drag and drop files between your local computer and the AI Student Cloud platform.

===+ "Linux/MacOS"

	You can transfer files to/from AI Student Cloud using the command line utility
	`scp` from your local computer.

	???+ example

		```console
		scp some-file <aau email>@ai-fe02.srv.aau.dk:~
		```
		
		where '~' means your user directory on AI Student Cloud. You can append
		directories below that to your destination:

		==CHANGE ai-fe02.srv.aau.dk ADDRESS==

	???+ example

		```console
		scp some-file <aau email>@ai-fe02.srv.aau.dk:~/some-dir/some-sub-dir/
		```
		==CHANGE ai-fe02.srv.aau.dk ADDRESS==
	You can also copy in the opposite direction, e.g. from the AI Student Cloud
	pilot platform to your local computer with:

	???+ example

		```console
		scp <aau email>@ai-fe02.srv.aau.dk:~/some-folder/some-subfolder/some-file .
		```
		
		where '.' means the current directory you are located in on your local
		computer.

		==CHANGE ai-fe02.srv.aau.dk ADDRESS==

	In general, file transfer tools that can use SSH as protocol should
	work. A common choice is [FileZilla](https://filezilla-project.org/).