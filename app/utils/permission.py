class MyPermission:
    def has_permission(self,request,view):
        print(request.user.role.id)
        if request.user.role.id==1:
            print("权限")
            return True
        return False
