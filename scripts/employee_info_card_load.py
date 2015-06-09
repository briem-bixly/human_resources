from api.human_resources import find_employee, get_dept_options

import logging

logging.basicConfig(filename='human_resources.log', level=logging.DEBUG)

class employee_info_card_load(NebriOS):
    listens_to = ['employee_info_card_load']

    def check(self):
        return self.employee_info_card_load == True

    def action(self):
        self.employee_info_card_load = "Ran"
        self.tasks_list = shared.VALID_EMPLOYEE_TASK_OPTIONS
        self.departments = get_dept_options(self)
        target_emp, dept = find_employee(self)
        self.editing = False
        if target_emp is not None:
            self.editing = True
            self.first_name = target_emp['first_name']
            self.last_name = target_emp['last_name']
            self.email = target_emp['email']
            self.job_title = target_emp['job_title']
            self.valid_tasks = target_emp['valid_tasks']
            self.is_active = target_emp['is_active']
            self.department = dept
        load_card('employee-info-card')
