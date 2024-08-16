from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django_ratelimit.decorators import ratelimit

def index(request):
    content = {'hello':'hello'}
    return render(request, 'home/index.html',content)

@ratelimit(key='ip', rate='3/m', method='ALL', block=True)
def contact(request):
            content = {'hello': 'hello'}
            if request.method == "POST":  
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                enquiry = request.POST.get('enquiry')

                # Validate the input fields
                if len(name) < 5 or len(email) < 5 or len(phone) < 10 or len(enquiry) < 10:
                    messages.error(request, 'Please enter valid details')
                    return render(request, 'home/contact.html', content)
                else:
                    # Save the contact if validation passes
                    new_contact = Contact(Name=name, Phone=phone, Email=email, Enquiry=enquiry)
                    new_contact.save()
                    messages.success(request, 'Your enquiry has been submitted successfully!')
                    return redirect('home:index')

            return render(request, 'home/contact.html', content)
    
@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
def plogin(request):
    if request.method == "POST":
        inputpassword = request.POST['password']
        inputusername = request.POST['username']
        # inputremember = request.POST['remember']

        user = authenticate(username=inputusername, password=inputpassword)
        if user is not None:
            login(request, user)
            messages.success(request,'You are logged in successfully')
            return redirect('home:index')
        else:
            messages.error(request, 'Invalid username or password')
    content={}
    return render(request,'home/login.html',content)

def validation(request,form):

    if form['password'] != form['c_password']:
        messages.error(request, 'Passwords do not match')
        return False
    if form['terms'] == "off":
        messages.error(request, 'Please accept the terms and conditions')
        return False
    if len(form['password']) < 8:
        messages.error(request, 'Password must be at least 8 characters long')
        return False
    if User.objects.filter(username=form['username']).exists():
        messages.error(request, "Username already exists. Please choose a different one.")
        return False
    if User.objects.filter(email=form['email']).exists():
        messages.error(request, "Email already exists. Please choose a different one.")
        return False
    return True
    
@ratelimit(key='ip', rate='2/m', method='ALL', block=True)
def psignup(request):
    if request.method == "POST":
        inputs = {}
        inputs['password'] = request.POST['password']
        inputs['c_password'] = request.POST["c-password"]
        inputs['username'] = request.POST['username']
        inputs['email'] = request.POST['email']
        inputs['terms'] = request.POST['terms']
        inputs['fname'] = request.POST['fname']
        inputs['lname'] = request.POST['lname']
        
        if validation(request,inputs) == True:
            my_user = User.objects.create_user(username=inputs['username'], email=inputs['email'], password=inputs['password'])
            my_user.first_name = inputs['fname']
            my_user.last_name = inputs['lname']
            my_user.save()
    
            messages.success(request, 'Account created successfully')
            login(request, my_user)
            return redirect('home:index')
    else:
        content={}
        return render(request,'home/signup.html',content)
        
def plogout(request):
    logout(request)
    messages.success(request,"You are logged out successfully")
    return redirect('home:index')

def page_not_found(request,exception):
    return render(request, 'home/missing.html', status = 404)


# adminhaha 12345678

# nav bar previous for boilerplate
# <nav class="dark:bg-gray-900 dark:text-white shadow">
#     <div class="container mx-auto px-4 py-3">
#         <div class="flex justify-between items-center">
#             <a href="{% block header_url %}{% endblock %}" class="text-xl font-bold dark:text-light">{% block header %}{% endblock %}</a>
#             <ul class="flex space-x-4">
#                 <li><a href="{% url 'home:index' %}" class="hover:text-gray-600  dark:hover:text-gray-200 {% block homeactive %}{% endblock %}">Home</a></li>
#                 <li><a href="{% url 'blog:blogindex' %}" class="hover:text-gray-600  dark:hover:text-gray-200 {% block blogactive %}{% endblock %}">Blogs</a></li>
#                 <li><a href="{% url 'home:contact' %}" class="hover:text-gray-600  dark:hover:text-gray-200 {% block contactactive %}{% endblock %}">Contact</a></li>
#                 <li>
#                     {% if user.is_authenticated %}
#                     <div x-data="{ open: false }" class="relative inline-block text-left">
#                       <div>
#                         <button @click="open = !open" type="button" class="inline-flex dark:text-white bg-grey-200 hover:bg-gray-300 border border-gray-900 rounded-lg text-sm px-3 font-medium py-1 inline-block" id="menu-button" aria-expanded="true" aria-haspopup="true">
#                           {{ user.username }}
#                           <svg class="-mr-1 h-5 w-5 text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
#                             <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
#                           </svg>
#                         </button>
#                       </div>

#                       <!-- Dropdown menu -->
#                       <div x-show="open" @click.outside="open = false" class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1" 
#                         x-transition:enter="transition ease-out duration-100 transform"
#                         x-transition:enter-start="opacity-0 scale-95"
#                         x-transition:enter-end="opacity-100 scale-100"
#                         x-transition:leave="transition ease-in duration-75 transform"
#                         x-transition:leave-start="opacity-100 scale-100"
#                         x-transition:leave-end="opacity-0 scale-95">
#                         <div class="py-1" role="none">
#                           <!-- <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="menu-item-0">Account settings</a>
#                           <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="menu-item-1">Support</a>
#                           <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="menu-item-2">License</a> -->
#                             <a href="{% url 'home:logout' %}" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="menu-item-2">Sign Out</a>
#                         </div>
#                       </div>
#                     </div>


#                     {% else %}
#                     <a href="{% url 'home:login' %}" class="text-white bg-blue-700 hover:bg-blue-800 rounded-lg text-sm px-3 font-medium py-1 inline-block">
#                         Sign In
#                     </a>

#                     <!-- Sign Up button -->
#                     <a href="{% url 'home:signup' %}" class="text-white bg-blue-700 hover:bg-blue-800 rounded-lg text-sm px-3 font-medium py-1 inline-block">
#                         Sign Up
#                     </a>
#                     {% endif %}
#                 </li>
#             </ul>
#         </div>
#     </div>
# </nav>