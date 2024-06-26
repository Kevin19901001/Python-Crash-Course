"""
导入Admin类
"""
import cluster

admin = cluster.Admin('Kevin', 22, '13111111111', 'HubeiWuhan')
admin.privileges.show_privileges(admin)
