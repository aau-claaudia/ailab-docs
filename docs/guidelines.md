---
title: Guidelines
---

# Guidelines

AI-LAB is a service made available to all AAU students. The platform consists of shared hardware, and this only works if the users use the platform as intended. This is why we ask you to consider the following use guidelines.


#### 1. Data deletion and extension policies
Every year at 1. August, all data and user information will be automatically removed from the AI-LAB platform. You will receive email notifications 2 months, 1 month, 14 days, and 2 day prior to the deletion date. It is important to ensure that you transfer any desired files from AI-LAB to your local computer before the deletion date.

Should you wish to keep your data on AI-LAB and use the platform for another semester, you can submit an extension request through the [application form](https://forms.office.com/e/caEhCRmqVN) for AI-LAB. Alternatively, you can apply for a new project.

#### 2. Not for confidential or sensitive data
In AI-LAB you are only allowed to work with public or internal information according to [AAU’s data classification model](https://www.security.aau.dk/data-classification) (classified as levels 0 and 1, respectively).

If you would like to work with confidential or sensitive data (classified as levels 2 and 3), then we support another HPC platform called [UCloud](https://www.researcher.aau.dk/guides/research-data/high-performance-computing/deic-hpc/procedure-projects-on-ucloud-deic-interactive-hpc).

#### 3. Data Management best practices
Effective data management is crucial for maximizing the value of your research and ensuring its integrity. Organize your data in a clear and structured manner, labeling files and directories appropriately. Regularly back up your data to prevent loss in case of unexpected events. Additionally, adhere to any data sharing and privacy regulations applicable to your field. Get more guidance about data management [here](https://www.researcher.aau.dk/guides/research-data/data-management/introduction-to-data-management).

#### 4. Jobs can run no longer than 12 hours
AI-LAB is designed primarily for data processing, not storage. Our High-Performance Computing (HPC) platform supports complex data analysis and simulation tasks efficiently. This focus ensures our resources are distributed optimally among users.

#### 5. Not intended for CPU processing
The platform excels in tasks requiring parallel processing capabilities, such as training deep learning models, image and video analysis, and other GPU-accelerated computational work. However, it's not intended for applications that only need CPU processing.

#### 6. Allocating the right amount of resources
Please be mindful of your allocations and refrain from allocating many resources without knowing/testing/verifying that you indeed can utilise all of the allocated resources. 

Please be mindful and de-allocate the resources when you are no longer using them. This enables other users to run their jobs.

#### 7. Focus on data processing, not storage
AI-LAB is designed primarily for data processing, not storage. Our High-Performance Computing (HPC) platform supports complex data analysis and simulation tasks efficiently. This focus ensures our resources are distributed optimally among users.

    
<!--
!!! aau "Working interactively"
    AI-LAB is optimized for high-performance computing tasks, requiring significant computational resources. Interactive sessions, such as Jupyter notebook sessions, can lead to inefficient resource use and reduce availability for users running intensive data processing tasks. To ensure optimal utilization of our platform, we recommend performing interactive data writing and testing on your local computer, reserving AI-LAB exclusively for executing the heavy-duty processing part of your projects.
-->

#### 8. Scheduled maintenance
On specific dates, scheduled maintenance will be conducted on AI-LAB. The routine maintenance will occur between <span style="font-weight: bold;">00:01 and 23:59</span>. AI-LAB will be unavailable throughout most of that day. You can still submit new jobs until the beginning of the service window. For jobs that may exceed the service window, please ensure to set a maximum runtime using the parameter `--time` that concludes before <span style="font-weight: bold;">23:59</span> the day preceding the service window. Read more about the `--time` parameter [here](/additional-guides/setting-a-time-limit). Otherwise, these jobs will not be able to start until after the maintenance period. You will receive email notifications ==1 month, 14 days, and 1 day== prior to the scheduled maintenance window.
