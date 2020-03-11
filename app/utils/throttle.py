import time

# BaseThrottle
from rest_framework.throttling import UserRateThrottle, SimpleRateThrottle

# 入口Dispatch 调用 initial调用  check_throttles 调用  get_throttles得到限流类列表
#调用列表每个类的allow_request 所以要实现这个方法

#在SimpleRateThrottle这就是catch
VISIT_RECODE={}

#这里没有继承BaseThrottle 应该是鸭子类型的原因
class MyvisitThrottle(object):
    def __init__(self):
        self.history_visit=[]
        # 10秒内超过5次就限制
        self.time_len=10
        self.rate=5
        print('aaaa')
    def allow_request(self,request,view):
        remote_addr=request.META.get('REMOTE_ADDR')
        print(remote_addr)
        ctime = time.time()
        if remote_addr not in VISIT_RECODE:
            VISIT_RECODE[remote_addr]=[ctime,]
            return True
        history_visit= VISIT_RECODE.get(remote_addr)
        self.history_visit=history_visit
        while history_visit and ctime-history_visit[-1] > self.time_len:
            history_visit.pop()
        if len(history_visit)< self.rate:
            history_visit.insert(0,ctime)
            return True
        return False
    def wait(self):
        ctime = time.time()
        return self.time_len - (ctime - self.history_visit[-1])

# UserRateThrottle,AnonRateThrottle 重写了get_cache_key 方法
# ScopedRateThrottle 重写了get_cache_key 和 allow_request 方法

#这里有个问题 无论用2 3 登陆不登陆都会限制
class MyvisitThrottle2(SimpleRateThrottle):
    """
     匿名用户限制
    """
    scope = "xs"

    # 一般在配置文件的DEFAULT_THROTTLE_RATES中
    THROTTLE_RATES={"xs":"3/m"}

    # 继承SimpleRateThrottle必须重写的一个方法
    # 返回标识 ip或者身份认证或者其他 也就是 HTTP_X_FORWARDED_FOR或者REMOTE_ADDR
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class MyvisitThrottle3(SimpleRateThrottle):
    """
    # 登陆用户限制
    """
    scope = "xs"
    THROTTLE_RATES={"xs":"8/m"}

    # 这里的request 来自allow_request被调用是传入的 最终来自dispatch 属于apiview 继承自View类
    #View类中as_view函数(闭包)中的view调用dispatch并返回出as_view
    def get_cache_key(self, request, view):
        return request.user.username