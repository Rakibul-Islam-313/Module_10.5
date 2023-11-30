from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    A = {'name' : 'Rakibul Islam', 'id' : 101, 'department' : 'Computer','val': 'mY FIRST jOb', 'lst' : [1,2,3,4],'lsit' : ['rakib', 'airat', 'mahadi'], 'line': ['dog','cat','beer','mankey'],'birthday' : datetime.datetime.now(), 'empty' : "", 'dict' : [
        {
            'name' : 'Abdullah',
            'age' : 17
        },
        {
            'name' : 'zisan',
            'age' : 15
        },
        {
            'name' : 'Khalid',
            'age' : 22
        }
    ], 'lit' : [1,2,3,4], 'lt' : ['i','j','k','l','o','p'], 'tpl': (123456), 'tme' : datetime.datetime.now(), 'var':  ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']], 'value' :('jai is a slug')
    }
    return render(request, 'home.html', context = A)