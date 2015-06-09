# human_resources
Human Resources App for NebriOS

This app is intended for use in a NebriOS instance. Visit https://nebrios.com to sign up for free!

Setup:
This app requires very little in terms of setup. Please ensure that all files are placed in the correct places over SFTP.
  - employee_info_card_load.py and setup_employee_task_options.py should be copied to /scripts
  - human_resources.py should be copied to /api
  - employee-info-card.html should be copied to /card_html_files
    
Once all files are in place, setup_employee_task_options needs to be run.
  - in debug mode set setup_employee_task_options and tasks to appropriate values and run
  
    ```
    setup_employee_task_options := True
    tasks := "['development', 'testing', 'mentoring']"
    ```
