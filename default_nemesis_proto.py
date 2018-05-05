import nemesis_pb2
import sys

def default_Task():
    result = nemesis_pb2.Task()
    result.task_id = 0
    result.number_of_groups = 0
    result.gen = False
    result.checker = b''
    result.solution = b''

    if result.IsInitialized() == False:
        print('default_Task isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_Task_Group():
    result = nemesis_pb2.Task.Group()
    result.id = 0
    result.number_of_tests = 0
    
    if result.IsInitialized() == False:
        print('default_Task_Group isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_Task_Group_Test():
    result = nemesis_pb2.Task.Group.Test()
    result.id = 0
    result.time_limit = -1
    result.memory_limit = -1
    result.input = b''
    result.output = b''

    if result.IsInitialized() == False:
        print('default_Task_Group_Test isn\'t initialized', file=sys.stderr)
        return None

    return result


def default_Submit():
    result = nemesis_pb2.Submit()
    result.id = 0
    result.task.CopyFrom(default_Task())
    result.user_id = 0
    result.lang = nemesis_pb2.CXX
    result.code = b''
    result.subsection_id = 0
    result.rejudge = False

    if result.IsInitialized() == False:
        print('default_Submit isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_LogicSubmit():
    result = nemesis_pb2.LogicSubmit()
    result.id = 0
    result.user_id = 0
    result.task_id = 0
    result.lang = nemesis_pb2.CXX
    result.code = b''
    result.subsection_id = 0

    if result.IsInitialized() == False:
        print('default_LogicSubmit isn\'t initialized', file=sys.stderr)
        return None
    
    return result

def default_Status():
    result = nemesis_pb2.Status()
    result.id = 0
    result.task_id = 0
    result.user_id = 0
    result.subsection_id = 0
    result.lang = nemesis_pb2.CXX
    result.number_of_groups = 0
    result.points = 0
    result.acm = False
    result.compiled = False
    result.rejudge = False
    result.compile_log = ''
    result.status = nemesis_pb2.OK

    if result.IsInitialized() == False:
        print('default_Status isn\'t initialized', file=sys.stderr)
        return None

    return result


def default_Status_Group():
    result = nemesis_pb2.Status.Group()
    result.id = 0
    result.number_of_tests = 0
    result.verdict = False
    result.status = nemesis_pb2.OK
    
    if result.IsInitialized() == False:
        print('default_Status_Group isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_Status_Group_Test():
    result = nemesis_pb2.Status.Group.Test()
    result.id = 0
    result.status = nemesis_pb2.OK
    result.verdict = False
    result.time = 0
    result.memory = 0

    if result.IsInitialized() == False:
        print('default_Status_Group_Test isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_CustomInvocation():
    result = nemesis_pb2.CustomInvocation()
    result.id = 0
    result.user_id = 0
    result.lang = nemesis_pb2.CXX
    result.test.CopyFrom(default_Task_Group_Test())
    result.source = b''

    if result.IsInitialized() == False:
        print('default_CustomInvocation isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_CustomInvocationStatus():
    result = nemesis_pb2.CustomInvocationStatus()
    result.id = 0
    result.user_id = 0
    result.time = -1
    result.memory = -1
    result.compiled = False
    result.compile_log = ''
    result.status = nemesis_pb2.OK
    result.out = b''

    if result.IsInitialized() == False:
        print('default_CustomInvocationStatus isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_Job():
    result = nemesis_pb2.Job()
    result.custom = False
    result.custom_job.CopyFrom(default_CustomInvocation())
    result.submit.CopyFrom(default_Submit())

    if result.IsInitialized() == False:
        print('default_Job isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_LogicJob():
    result = nemesis_pb2.LogicJob()
    result.custom = False
    result.custom_job.CopyFrom(default_CustomInvocation())
    result.submit.CopyFrom(default_LogicSubmit())
    
    if result.IsInitialized() == False:
        print('default_LogicJob isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_JobReturn():
    result = nemesis_pb2.JobReturn()
    result.custom = False
    result.custom_status.CopyFrom(default_CustomInvocationStatus())
    result.status.CopyFrom(default_Status())
    result.system_error = False
    
    if result.IsInitialized() == False:
        print('default_JobReturn isn\'t initialized', file=sys.stderr)
        return None

    return result

def default_Heartbeat():
    result = nemesis_pb2.Heartbeat()
    result.id = 0
    result.name = ''
    result.port = ''

    if result.IsInitialized() == False:
        print('default_Heartbeat isn\'t initialized', file=sys.stderr)
        return None

    return result

def main():
    x = default_Task()
    print(x)
    x = default_Task_Group()
    print(x)
    x = default_Task_Group_Test()
    print(x)
    x = default_Submit()
    print(x)
    x = default_LogicSubmit()
    print(x)
    x = default_Status()
    print(x)
    x = default_Status_Group()
    print(x)
    x = default_Status_Group_Test()
    print(x)
    x = default_CustomInvocation()
    print(x)
    x = default_CustomInvocationStatus()
    print(x)
    x = default_Job()
    print(x)
    x = default_LogicJob()
    print(x)
    x = default_JobReturn()
    print(x)
    x = default_Heartbeat()
    print(x)


if __name__ == '__main__':
    main()
