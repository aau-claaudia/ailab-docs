<div id="service-window-warning" style="display: none;" markdown>
!!! warning "<span id="time-to-window"></span> to the next service window"

    We will be performing a scheduled maintenance on AI Lab. The routine maintenance will take place <span id="service-date" style="font-weight: bold;"></span> between <span style="font-weight: bold;">00:01 and 23:59</span>. AI Lab will be unavailable throughout most of the day. You can still submit new jobs until the beginning of the service window. For jobs that may exceed the service window, please ensure to set a maximum runtime using the parameter `--time` that concludes before <span style="font-weight: bold;">23:59</span> the day preceding the service window. Read more about the `--time` parameter [here](/additional-guides/setting-a-time-limit). Otherwise, these jobs will not be able to start until after the maintenance period. You will receive email notifications ==1 month, 14 days, and 1 day== prior to the scheduled maintenance window.
 
    If you have any further questions please refer your question to CLAAUDIA through the [AAU service portal](https://www.serviceportal.aau.dk/).

</div>

# Welcome to AI Lab documentation

Welcome to the AI Lab documentation, a guide designed to help Aalborg University students delve into powerful computing projects using AI Lab. Before [getting started](getting-started/preperation.md) we recommend getting an [overview](system-overview.md) of the system behind AI Lab and reading our [Guidelines](guidelines.md).

<br>

<div class="grid cards" markdown>

-   :octicons-server-24:{ .lg .middle } __System overview__

    ---

    The Architecture of AI Lab

    [:octicons-arrow-right-24: System overview](/system-overview)

-   :material-scale-balance:{ .lg .middle } __Guidelines__

    ---

    Best practices for using AI Lab

    [:octicons-arrow-right-24: Guidelines](/guidelines)

-   :octicons-rocket-24:{ .lg .middle } __Getting Started__

    ---

    Step-by-step guide to AI Lab

    [:octicons-arrow-right-24: Getting Started](/getting-started/preperation)

-   :material-lightbulb-outline:{ .lg .middle } __Courses__

    ---

    AI Lab applications courses

    [:octicons-arrow-right-24: Courses](/courses/==UPDATE LINK==)

</div>

<br>

### What is AI Lab?
AI Lab is designed exclusively for students at Aalborg University, offering [high-performance computing (HPC)](https://www.researcher.aau.dk/guides/research-data/high-performance-computing/introduction-to-hpc) right at your fingertips. Think of it as a mini supercomputer, packed with GPUs, making it a perfect playground for training [deep learning](/glossery/#deep-learning) models, running simulations, and performing high-speed data analysis.

This platform is home to an extensive collection of [GPU resources](/system-overview/#overview-of-compute-nodes), tailored specifically for machine learning tasks. Whether you're working on image recognition, deep learning tasks, or data processing, AI Lab is equipped to handle vast processes that benefit from [parallel computing](/glossery/#parallel-computing).

!!! custom "<span class="custom-callout-icon">:octicons-goal-24: Purpose</span>"
    AI Lab isn't just about providing hardware; it's about opening the door to high-performance computing for students, with an educational twist. From simulations to deep learning, it supports a large number of applications, all while fostering an environment where students can experiment, learn, and grow their computational skills.

!!! custom "<span class="custom-callout-icon">:octicons-lock-24: How to access</span>"
    First you need to fill out an [application form](https://forms.office.com/e/caEhCRmqVN) to request for access. After getting approval, you can access AI Lab using a terminal application from your local computer. We will guide you through all this in [Getting Started](/getting-started/preperation).

!!! custom "<span class="custom-callout-icon">:octicons-people-24: Who manage AI Lab</span>"
    AI Lab is managed by the [CLAAUDIA](https://www.researcher.aau.dk/contact/claaudia) team. CLAAUDIA is a specialized team within ITS at Aalborg University focused on research data support, particularly skilled in leveraging high-performance computing and cloud resources such as AI Lab. They offer [support](/support) and consultations to help students and researchers navigate through options for utilizing supercomputing resources effectively.

<script src="javascripts/serviceWindow.js"></script>