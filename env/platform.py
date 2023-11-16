class Cloud:
    # 默认存储无上限
    def __init__(self, task_queue, service_list, cpu, mem):
        self.task_queue = task_queue
        self.service_list = service_list
        self.cpu = cpu  # [10,15]GHz
        self.mem = mem  # GB


class Node:
    def __init__(self, task_queue, service_list, cpu, mem, storage):
        self.cpu = cpu
        self.mem = mem
        self.storage = storage
        self.service_list = service_list
        self.task_queue = task_queue


class Master:
    def __init__(self, cpu, mem, storage, node_list, all_task):
        self.cpu = cpu
        self.mem = mem
        self.storage = storage
        self.node_list = node_list
        self.all_task = all_task


class Docker:
    def __init__(self, mem, cpu, storage, available_time, type, running_task):
        self.mem = mem
        self.cpu = cpu
        self.storage = storage
        self.available_time = available_time
        self.type = type
        self.running_task = running_task

