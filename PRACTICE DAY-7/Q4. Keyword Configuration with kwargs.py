'''Q4. Keyword Configuration with **kwargs
Problem Statement: Implement create_device_config(device_id, **kwargs).
 Return a dictionary with device_id and accepted fields baud_rate, parity, timeout_ms and debug. 
 Reject unsupported keys clearly.
Example Input: create_device_config('D01', baud_rate=115200, parity='N', timeout_ms=500)
Example Output: {'device_id': 'D01', 'baud_rate': 115200, 'parity': 'N', 'timeout_ms': 500}'''

def create_device_config(device_id, **kwargs):
    allowed = ["baud_rate", "parity", "timeout_ms", "debug"]
    for key in kwargs:
        if key not in allowed:
            return "Unsupported key: " + key
    config = {"device_id": device_id}
    config.update(kwargs)
    return config
print(create_device_config('D01', baud_rate=115200, parity='N', timeout_ms=500))
