# File transfer
===+ "Windows"
	For Windows users we recommend using the application [WinSCP](https://winscp.net/eng/docs/lang:da) to transfer files from your local computer to AI Lab. Other popular solutions are [PuTTY](https://www.putty.org/) and [FileZilla](https://filezilla-project.org/). Alternatively, you can install [OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) to be able to use the `scp` command, shown for [Linux/MacOS](/getting-started/file-transfer/#__tabbed_1_2) users.

	When you open WinSCP, you will be welcomed by a 'Login' modal. Follow the instructions in the image above to establish a connection to the server. You can now drag and drop files between your local computer and the AI Lab platform.

	![Screenshot of WinSCP setup](/assets/img/winscp-setup.png)
	
	==Remember to change image with new server address==

	!!! info
		You might want to display hidden files in WinSCP (such as files starting with a dot on Linux systems). Go to Options → Preferences... → Panels and turn on "Show hidden files".

===+ "Linux/MacOS"

	You can transfer files to/from AI Lab using the command line utility
	`scp` from your local computer.

	!!! example

		```console
		scp some-file xxxxxx@student.aau.dk@ai-fe02.srv.aau.dk:~
		```
		
		where '~' means your user directory on AI Lab. 

		You can append directories after that to your destination:

		```console
		scp some-file xxxxxx@student.aau.dk@ai-fe02.srv.aau.dk:~/some-dir/some-sub-dir/
		```

		==CHANGE ai-fe02.srv.aau.dk ADDRESS==


	You can also copy in the opposite direction, e.g. from the AI Lab platform to your local computer with:

	!!! example

		```console
		scp xxxxxx@student.aau.dk@ai-fe02.srv.aau.dk:~/some-folder/some-subfolder/some-file .
		```
		
		where `.` means the current directory you are located in on your local
		computer.
		==CHANGE ai-fe02.srv.aau.dk ADDRESS==

	In general, file transfer tools that can use SSH as protocol should
	work. A common choice is [FileZilla](https://filezilla-project.org/).

Now that you know the basics of file transfer, lets proceed to learn how to <span style="color: var(--md-primary-fg-color); font-weight: 700;"><a href="/getting-started/getting-applications">get applications :octicons-arrow-right-24:</a></span>