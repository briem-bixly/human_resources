import logging

logging.basicConfig(filename="human_resources.log", level=logging.DEBUG)

valid_employee_kvps = ['first_name', 'last_name', 'email', 'tasks', 'job_title', 'valid_tasks', 'is_active']

def get_departments(request):
    logging.debug('****GET DEPARTMENTS****')
    depts = Process.objects.filter(kind="department")
    logging.debug(depts)
    return [dept.as_dict() for dept in depts]
    
def get_dept_options(request):
    depts = Process.objects.filter(kind="department")
    return [{'value':dept.PROCESS_ID, 'label': dept.name} for dept in depts]

def all_employees(request):
    employees = Process.objects.filter(kind="employee", is_active=True)
    return [emp.as_dict() for emp in employees]
    
    
def get_pms(request):
    pms = Process.objects.filter(kind="employee", job_title="Project Manager", is_active=True)
    logging.debug(pms)
    return [pm.as_dict() for pm in pms]
    
    
def get_developers(request):
    emps = Process.objects.filter(kind="employee", is_active=True)
    devs = []
    for e in emps:
        if 'development' in e.valid_tasks:
            devs.append(e)
    return [dev.as_dict() for dev in devs]
    
    
def get_testers(request):
    emps = Process.objects.filter(kind="employee", is_active=True)
    testers = []
    for e in emps:
        if 'testing' in e.valid_tasks:
            emps.append(e)
    return [tester.as_dict() for tester in testers]
    

def find_employee(request):
    try:
        if not isinstance(request, Process) and not isinstance(request, NebriOS):
            if request.FORM is None:
                email = request.BODY.as_dict()['email']
            else:
                email = request.FORM.as_dict()['email']
        else:
            email = request.as_dict()['email']
        employee = Process.objects.get(kind="employee", is_active=True, email=email)
        return employee.as_dict(), employee.PARENT.PROCESS_ID
    except:
        return None, None
            
    
def update_employee(request):
    data = {}
    if request.FORM is not None:
        data = request.FORM.as_dict()
    else:
        data = request.BODY.as_dict()
        
    dept = data['department']
    logging.debug(data)
    # first, let's see if this is a new employee or update
    try:
        emp = Process.objects.get(kind="employee", email=email)
        for key, value in data:
            if key not in valid_employee_kvps:
                continue
            emp[key] = value
        emp.save()
    except:
        # need to create a new employee. let's find the right department.
        department = Process.objects.get(kind='department', PROCESS_ID=dept)
        emp = Process.objects.create(PARENT=department, kind="employee", is_active=True)
        for key, value in data.items():
            if key not in valid_employee_kvps:
                continue
            emp[key] = value
        emp.save()
