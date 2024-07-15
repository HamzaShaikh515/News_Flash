from django.forms import ValidationError
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
import requests,math
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from .models import Article,Comment,Category,Language,Country,Status


def everything_news(request):
    q = request.GET.get("q")  
    category = request.GET.get("category") 
    country = request.GET.get("country")
    language = request.GET.get("language")
    api_key = "c384de4445624993bef7fac28f71a494"
    query_params = {
        'apiKey' : api_key
    }
    if q:
        query_params["q"] = q
    if category!="":
        query_params["category"] = category
    if country!="":
        query_params["country"] = country
    if language!="":
        query_params["language"] = language

    # newsapi = NewsApiClient(api_key=api_key)
    url = 'https://newsapi.org/v2/everything?'
    
    try:
        # response = newsapi.get_everything(**query_params)
        response = requests.get(url=url,params=query_params) 
        response = response.json()
        articles = response["articles"]
    except Exception as e:
        print(f"Error fetching news: {e}")
        articles = [] 

    context = {"articles": articles}
    return render(request, "everything_news.html", context)

def index(request):
    context = {}
    if request.method=="GET":
        country = request.GET.get('country','in')
        language = request.GET.get('language','en')
        api_key = "c384de4445624993bef7fac28f71a494"
        url = 'https://newsapi.org/v2/top-headlines?'
        params = {
            'apiKey': api_key,
            'country': country,
            'language': language,
            'pageSize': 5,
            }
        response = requests.get(url=url, params=params)
        response = response.json()
        articles = response['articles']

        if country == 'in':
            country_value = 'India'
        if country == 'us':
            country_value = 'United States'
        if country == 'ru':
            country_value = 'Russia'
        if country == 'gb':
            country_value = 'United Kingdom'
        if country == 'cn':
            country_value = 'China'
        if country == 'au':
            country_value = 'Australia'
        if country == 'br':
            country_value = 'Brazil'
        if country == 'de':
            country_value = 'Germany'
        if country == 'at':
            country_value = 'Austria'
        if country == 'be':
            country_value = 'Belgium'
        if country == 'bg':
            country_value = 'Bulgaria'
        if country == 'ca':
            country_value = 'Canada'
        if country == 'ch':
            country_value = 'Switzerland'
        if country == 'co':
            country_value = 'Colombia'
        if country == 'cu':
            country_value = 'Cuba'
        if country == 'cz':
            country_value = 'Czech Republic'
        if country == 'eg':
            country_value = 'Egypt'
        if country == 'fr':
            country_value = 'France'
        if country == 'gr':
            country_value = 'Greece'
        if country == 'hk':
            country_value = 'Hong Kong'
        if country == 'hu':
            country_value = 'Hungary'
        if country == 'id':
            country_value = 'Indonesia'
        if country == 'ie':
            country_value = 'Ireland'
        if country == 'il':
            country_value = 'Israel'
        if country == 'it':
            country_value = 'Italy'
        if country == 'jp':
            country_value = 'Japan'
        if country == 'kr':
            country_value = 'South Korea'
        if country == 'lt':
            country_value = 'Lithuania'
        if country == 'ma':
            country_value = 'Morocco'
        if country == 'mx':
            country_value = 'Mexico'
        if country == 'my':
            country_value = 'Malaysia'
        if country == 'nl':
            country_value = 'Netherlands'
        if country == 'no':
            country_value = 'Norway'
        if country == 'nz':
            country_value = 'New Zealand'
        if country == 'ph':
            country_value = 'Phillippines'
        if country == 'pl':
            country_value = 'Poland'
        if country == 'pt':
            country_value = 'Portugal'
        if country == 'ro':
            country_value = 'Romania'
        if country == 'rs':
            country_value = 'Serbia'
        if country == 'sa':
            country_value = 'Saudi Arabia'
        if country == 'se':
            country_value = 'Sweden'
        if country == 'sg':
            country_value = 'Singapore'
        if country == 'sl':
            country_value = 'Slovenia'
        if country == 'th':
            country_value = 'Thailand'
        if country == 'tr':
            country_value = 'Turkey'
        if country == 'tw':
            country_value = 'Taiwan'
        if country == 'ua':
            country_value = 'Ukraine'
        if country == 've':
            country_value = 'Venezeula'
        if country == 'za':
            country_value = 'South Africa'

        if language == 'en':
            language_value = 'English'
        if language == 'es':
            language_value = 'Spanish'
        if language == 'fr':
            language_value = 'French'
        if language == 'ar':
            language_value = 'Arabic'
        if language == 'de':
            language_value = 'German'
        if language == 'he':
            language_value = 'Hebrew'
        if language == 'it':
            language_value = 'Italian'
        if language == 'nl':
            language_value = 'Dutch'
        if language == 'no':
            language_value = 'Norwegian'
        if language == 'pt':
            language_value = 'Portuguese'
        if language == 'ru':
            language_value = 'Russian'
        if language == 'sv':
            language_value = 'Swedish'
        if language == 'zh':
            language_value = 'Chinese'

        context = {
            'articles' : articles,
            'language'  : language_value,
            'country' : country_value,
        }
    return render(request, 'index.html',context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirmPassword')

        if first_name=="":
            error = 'First Name cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if last_name=="":
            error = 'Last Name cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if username=="":
            error = 'Username cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if email=="":
            error = 'Email cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if password=="":
            error = 'Password cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if confirm=="":
            error = 'Confirm Password cannot be empty!!'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if User.objects.filter(username=username).exists():
            error = "User with this username already exists. Please use another username."
            context = {"error" : error}
            return render(request, "register.html", context)
        
        try :
            EmailValidator(email)
        except ValidationError:
            error = 'Email is invalid. Please use correct email.'
            context = {'error': error}
            return render(request,'register.html',context)
        
        if User.objects.filter(email=email).exists():
            error = "User with this email already registered. Please use another email."
            context = {"error" : error}
            return render(request,"login.html",context)

        if password!=confirm:
            error="Passwords do not match. Please enter the same password in both fields."
            context={"error":error}
            return render(request,"register.html",context)
        
        newuser = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        newuser.save()
        success = 'Registration Successfull! You can now log into your account'
        context ={"success":success}
        return render(request,"register.html",context)
    
    return render(request, "register.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('Home')
        else:
            error = 'Cant Login. Credentials invalid'
            context = {'error': error}
            return render(request,'login.html',context)
    return render(request, "login.html")

def top_headlines(request):
    country = request.GET.get('country')  # Get country from URL parameters
    category = request.GET.get('category')  # Get category from URL parameters
    language = request.GET.get('language')  # Optional: Get language from URL parameters
    q = request.GET.get('q')
            # Ensure articles is defined and empty list if not retrieved
    page = 0
    all_articles={}

    api_key = "c384de4445624993bef7fac28f71a494"
    url = 'https://newsapi.org/v2/top-headlines'

    query_params = {
            'apiKey' : api_key,
    }
    if category != '':
            query_params["category"] = category
    if country != '':
            query_params["country"] = country
    if language != '':
            query_params["language"] = language
    if q != '':
            query_params["q"] = q
    
    while(True):
        page += 1
        query_params['page'] = page
        response = requests.get(url=url, params=query_params)
        response = response.json()
        if response['status'] =='error':
            articles=[]
            total_articles = 0
            break
        articles = response['articles']
        total_articles = response['totalResults']
        total_pages = math.ceil(total_articles / 20)
        all_articles[page] = articles
        if page==total_pages:
            break
    context = {
            "articles": all_articles,
            'totalResults': total_articles,
        }
    return render(request, "top-headlines.html", context)

def user_profile(request):
    articles = Article.objects.filter(author=request.user)
    comments = Comment.objects.filter(commenter_name=request.user)
    context = {
        'articles' : articles,
        'comments' : comments,
    }
    return render(request=request,template_name='profile.html',context=context)
        

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Logout only allowed via POST request.')
    
def add_article_view(request):
    countries = Country.objects.all()
    categories = Category.objects.all()
    languages = Language.objects.all()

    context = {
        'countries' : countries,
        'categories' : categories,
        'languages' : languages,
    }

    if request.method == 'POST':
        category_value = request.POST.get('category')
        language_value = request.POST.get('language')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        content = request.POST.get('article-content')
        author = request.user
        country_value = request.POST.get('country')

        if category_value =='':
            error = '''Please Select the category of the article. You can Select the 'Others' Option if you can't find a suitable category. '''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if language_value =='':
            error = '''Please Select the language of the article. You can Select the 'Others' Option if you can't find a suitable language. '''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if country_value =='':
            error = '''Please Select the Country of the article. You can Select the 'Others' Option if you can't find the Country. '''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if title =='':
            error = '''The title cannot be empty.'''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if summary =='':
            error = '''Please provide the summary of the article. One line will be enough. '''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if content =='':
            error = '''The main content cannot be empty.'''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        if request.method != "GET":
            image = request.FILES.get('images')

        if image is None :
            error = '''Please upload an image. It must be relatable to article.'''
            context['error'] = error
            return render(request, 'add_article.html',context)
        
        category = Category.objects.get(name=category_value)
        language = Language.objects.get(name=language_value)
        country = Country.objects.get(name=country_value)
        
        article = Article.objects.create(category=category,language=language,title=title,author=author,image=image,summary=summary,content=content,country=country)
        success = article.title + ' Article Created Successfully!!'
        context['success'] = success

    return render(request, 'add_article.html',context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user) 
                return redirect('Home')
            else :
                error = 'You are not an admin. Login via user login.'
                context = {'error': error}
                return render(request,'admin_login.html',context)
        else:
            error = 'Cant Login. Credentials invalid'
            context = {'error': error}
            return render(request,'admin_login.html',context)
    return render(request, "admin_login.html")

def user_articles(request):
    categories = Category.objects.all()
    languages = Language.objects.all()
    countries = Country.objects.all()

    context = {
        'categories' : categories,
        'languages' : languages,
        'countries' : countries,
        # 'articles' : articles,
    }

    if request.method=='POST':

        category_value = request.POST.get('category')
        language_value = request.POST.get('language')
        country_value = request.POST.get('country')

        category_obj = Category.objects.get(name=category_value)
        language_obj = Language.objects.get(name=language_value)
        country_obj = Country.objects.get(name=country_value)
        
        status_obj = Status.objects.get(name='Approved')

        articles = Article.objects.filter(category=category_obj,language=language_obj,country=country_obj,status=status_obj)
        for article in articles:
            print(article.image)
        context['articles'] = articles

    return render(request,'user_articles.html',context)

def article_view(request):
    article_id = request.GET.get('article_id')
    
    article = Article.objects.get(unique_id=article_id)
    comments = Comment.objects.filter(article=article).order_by("-created_at")

    print(article.title)
    context = {
        'article' : article,
        'comments' : comments,
    }

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        new_comment = Comment.objects.create(content=comment_text, commenter_name=request.user, article=article)
        return render(request,'article_view.html',context)
    
    return render(request,'article_view.html',context)