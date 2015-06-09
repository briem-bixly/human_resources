# human_resources
Human Resources App for NebriOS

This app is intended for use in a NebriOS instance. Visit https://nebrios.com to sign up for free!

<strong>NOTE</strong> This app has dependencies in https://github.com/briem-bixly/organization_management

<h4>Setup</h4>
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

<h4>Creating/Updating an Employee</h4>
  - running employee_info_card_load from debug mode will trigger a card in interact mode
  
    ```
    employee_info_card_load := True
    ```
  - without any additional arguments, this will load a blank card and allow you to create a new employee
  - in order to update an existing employee, the email argument can be sent as well
  
    ```
    employee_info_card_load := True
    email := person@example.com
    ```
  - this will pre fill the employee info card with the currently set info for that employee
