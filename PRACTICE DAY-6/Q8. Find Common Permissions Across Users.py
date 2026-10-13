permissions = {
    'admin': {'read', 'write', 'delete'},
    'operator': {'read', 'write'},
    'auditor': {'read', 'export'}
}
values = list(permissions.values())
common = set.intersection(*values)
all_permissions = set.union(*values)
print("Common permissions:", sorted(common))
print("All permissions:", sorted(all_permissions))
