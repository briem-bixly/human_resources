class setup_employee_task_options(NebriOS):
    listens_to = ['setup_employee_task_options']
    # Note that this rule scripts expects a trigger and a list kvp of valid tasks
    # i.e. tasks := "['testing', 'mentoring']"
    # this list will be used for all employees
    # NOTE: if this shared KVP already exists, new tasks will be appended, not overwritten.

    def check(self):
        return self.setup_employee_task_options == True

    def action(self):
        self.setup_employee_task_options = "Ran"
        if not shared.VALID_EMPLOYEE_TASK_OPTIONS:
            shared.VALID_EMPLOYEE_TASK_OPTIONS = []
        for task in self.tasks:
            # first check if the task exists
            if task in [existing_task.value for existing_task in shared.VALID_EMPLOYEE_TASK_OPTIONS]:
                continue
            shared.VALID_EMPLOYEE_TASK_OPTIONS.append({
                'value':task,
                'label':task
            })
