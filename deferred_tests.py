from twisted.internet.defer import Deferred

def myCallBack(result):
    print(result)
    
    
d = Deferred()
d.addCallback(myCallBack)
d.callback("Triggering callback.")