"""
多个模块
创建一个Admin实例并对其调用方法show_privileges()
"""
import another_cluster

admin = another_cluster.Admin('Kevin', 22, '13211111111', 'HubeiWuhan')
admin.privileges.show_privileges(admin)
