!!! question "How long can I use AI-LAB for a project"
    ...


!!! question "Can I have a graphical user interface (GUI) in AI-LAB?"
    No. As a rule of thumb, you can only operate applications through a command line interface. AI-LAB is best suited for throughput type computing: queue up your job and come back for the result later. If your project could benefit from running on a GPU cluster but demands an interactive graphical interface, contact CLAAUDIA research support at support@its.aau.dk.

!!! question "What software can I run in AI-LAB?"
    In principle any software that can run under Linux since the operating system on the servers in AI-LAB is Linux. In many cases, it is necessary to encapsulate the software in a container in order to use it. The software must be able to utilise the (NVIDIA) GPUs in the platform. The GPUs cannot automatically accelerate software that was not designed for it.

!!! question "Can I use AI-LAB as a collaborative platform?"
    Yes - it is possible to share files among different users on the cluster.

!!! question "Am I allowed to work with confidential or sensitive data on AI-LAB?"
    ==INDSÆT LINK TIL DATA KLASSIFIKATION==
    No. In AI-LAB you are only allowed to work with public or internal information according to AAU’s data classification model (classified as levels 0 and 1, respectively).
    
    A similar solution for working with confidentoinal or sensitive data (classified as levels 2 and 3) is being developed.

!!! question "Why do I get `\r` error when running my .py script?"
    If you encounter an error message like: `/usr/bin/env python3/r: bad interpreter: No such file or directory` while running a .py file, it might be because the file was edited on your local Windows computer before moving it to AI-LAB. Line endings often get converted when files are moved between Linux and Windows. This conversion is a frequent issue as Linux and Unix-like systems use `\n` for line breaks, whereas Windows uses `\r\n` (CRLF, Carriage Return + Line Feed). 
    
    *Solution:* In code editors such as VS Code or PyCharm, you can switch between LF (Linux endings) and CRLF (Windows endings) from the right-hand side of the status bar at the bottom of the window. Therefore, use LF endings if you wish to move a file to AI-LAB.