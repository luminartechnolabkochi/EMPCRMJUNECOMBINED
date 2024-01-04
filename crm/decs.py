

def swap_dec(fn):

    def wrapper(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper


def sub(n1,n2):
    
    return n1-n2

def div(n1,n2):
    
    return n1/n2

print(sub(2,10))





def get(request,*args, **kwargs):

    return "some logic"

def sigin_required(fn):

    def wrapper(request,*args, **kwargs):
        if not  request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper




def post(request,*args, **kwargs):
    return "some logic"

def get(request,*args, **kwargs):

    return "some logic"


def post(request,*args, **kwargs):
    return "some logic"