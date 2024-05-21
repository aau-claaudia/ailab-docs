---
title: FAQ
---

# FAQ

!!! question old "Who manage AI-LAB?"
    AI-LAB is managed by the [CLAAUDIA](https://www.researcher.aau.dk/contact/claaudia) team. CLAAUDIA is a specialized team within ITS at Aalborg University focused on research data support, particularly skilled in leveraging high-performance computing and cloud resources such as AI-LAB. They offer [support](/support) and consultations to help students and researchers navigate through options for utilizing supercomputing resources effectively.

!!! question old "Can I have a graphical user interface (GUI) in AI-LAB?"
    No. As a rule of thumb, you can only operate applications through a command line interface. AI-LAB is best suited for throughput type computing: queue up your job and come back for the result later. If your project could benefit from running on a GPU cluster but demands an interactive graphical interface, we would recommend checking out [UCloud] HPC Platform (https://www.researcher.aau.dk/guides/research-data/high-performance-computing/deic-hpc).

!!! question old "What software can I run in AI-LAB?"
    In principle any software that can run under Linux since the operating system on the servers in AI-LAB is Linux. It is necessary to encapsulate the software in a [container](/glossery/#container) in order to use it.

!!! question old "Am I allowed to work with confidential or sensitive data on AI-LAB?"
    No. In AI-LAB you are only allowed to work with public or internal information according to [AAU’s data classification model](https://www.security.aau.dk/data-classification/the-four-data-types-at-aau) (classified as levels 0 and 1, respectively).
    
    If you need to proces sensitive data, we would recommend checking out [UCloud] HPC Platform (https://www.researcher.aau.dk/guides/research-data/high-performance-computing/deic-hpc).

!!! question old "Why do I get `\r` error when running my .py script?"
    If you encounter an error message like: `/usr/bin/env python3/r: bad interpreter: No such file or directory` while running a .py file, it might be because the file was edited on your local Windows computer before moving it to AI-LAB. Line endings often get converted when files are moved between Linux and Windows. This conversion is a frequent issue as Linux and Unix-like systems use `\n` for line breaks, whereas Windows uses `\r\n` (CRLF, Carriage Return + Line Feed). 
    
    *Solution:* In code editors such as VS Code or PyCharm, you can switch between LF (Linux endings) and CRLF (Windows endings) from the right-hand side of the status bar at the bottom of the window. Therefore, use LF endings if you wish to move a file to AI-LAB.