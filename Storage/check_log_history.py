# Pure Storage
def check_log_history(events):
    cache = set()
    stack = []
    for idx, event in enumerate(events):
        op, lock_id = event.split()
        if op == 'ACQUIRE':
            if lock_id in cache:
                return idx + 1
            else:
                cache.add(lock_id)
                stack.append(lock_id)
        else:
            if not stack or stack.pop() != lock_id:
                return idx + 1
            else:
                cache.remove(lock_id)
    return 0 if not stack else len(events) + 1


# events = { "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364"}
# events = { "ACQUIRE 364", "ACQUIRE 84", "RELEASE 364", "RELEASE 84"}
# events = { "ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 456"}
# events = { "ACQUIRE 364", "ACQUIRE 84", "ACQUIRE 84", "RELEASE 364"}
events = ("ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 789", "RELEASE 456", "RELEASE 123")
print(check_log_history(events))

