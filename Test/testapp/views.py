from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login2(request):
    html_content = """username : <input name='username'/>
    password : <input name='username' />
    """
    return HttpResponse(html_content)


def article(request, year, month, article_id):
    print year, month, article_id
    datas = year + month + article_id
    return HttpResponse(datas)

@login_required
def index(request):

    name_info = {
        'name': 'SanJin',
        'age': 20,
        'hobbit': 'show',
        'job': 'stripper',
    }
    return render(request, 'index.html',
                  {'point': 'testpoint', 'n_info': name_info, })

@login_required
def host(request):
    return render(request, 'host.html')

@login_required
def bootstrap(request):
    return render(request, 'bootstrap_index.html')

@login_required
def asset(request):
    return render(request, 'asset.html')

@login_required
def audit(request):
    return render(request, 'audit.html')


def acc_login(request):
    print request
    print request.method
    print request.POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print '--%s  %s--' % (username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login_bootstrap.html', {'login_err': 'Wrong username or password .'})
    else:
        return render(request, 'login_bootstrap.html')

@login_required
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
