from django.contrib import messages
from django.shortcuts import render, redirect
from blog.models import Post,Comment
from django_ratelimit.decorators import ratelimit


# Create your views here.
def index(request):
  allposts = Post.objects.all()
  contents = {'allposts': allposts,'query': 'Minimal Blog'}
  return render(request, 'blog/blogp.html', contents)

@ratelimit(key='ip', rate='3/m', method='ALL', block=True)
def blogpost(request):
  if request.method == "POST":
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    category = request.POST.get('category')
    try:
      # Attempt to save the post
      newpost = Post(title=title,
                     content=content,
                     author=author,
                     category=category)
      newpost.save()

      # If save is successful
      messages.success(request, 'Your post has been submitted successfully!')
      return redirect('blog:blogindex')
    except Exception as e:
      # If an error occurs during save
      messages.error(
          request,
          'Your post has not been submitted! Error: {}'.format(str(e)))
  return render(request, 'blog/blogpost.html')


def singleb(request, b_no):
  post = Post.objects.get(b_no=b_no)
  comments = Comment.objects.filter(post=post, parent = None)
  counts = Comment.objects.filter(post=post).count()
  # Build a dictionary to store replies under their parent comment
  comment_dict = {}
  for comment in comments:
      comment_dict[comment] = Comment.objects.filter(parent=comment)

  contents = {
      'post': post,
      'comment_dict': comment_dict,
      'user': request.user,
      'counts': counts,
  }
  return render(request, 'blog/singleb.html', contents)
  
@ratelimit(key='ip', rate='5/m', method='ALL', block=True)
def postcomment(request):
  if request.method == "POST":
    content = request.POST.get('content')
    user = request.user
    postb_no = request.POST.get('postb_no')
    parentc_no = request.POST.get('parentc_no')
    
    post = Post.objects.get(b_no = postb_no)
    try:
      if parentc_no == '':
        # Attempt to save the comment
        newcomment = Comment(post=post, content=content,user = user)
        newcomment.save()
  
        # If save is successful
        messages.success(request, 'Your comment has been submitted successfully!')
        # return redirect('blog:singleb', b_no=postb_no)
      else:
        parent = Comment.objects.get(c_no = parentc_no)
        newcomment = Comment(post=post, content=content,user = user, parent = parent)
        newcomment.save()
        # If save is successful
        messages.success(request, 'Your reply has been submitted successfully!')
    except Exception as e:
      # If an error occurs during save
      messages.error(
          request,
          'Your comment has not been submitted! Error: {}'.format(str(e)))
    return redirect('blog:singleb', b_no=postb_no)
        
      

def search_posts(request):
  query = request.GET.get('search')
  if query:
    # Apply all filters to the queryset
    results = Post.objects.filter(
        title__icontains=query
    ) | Post.objects.filter(
        author__icontains=query
    ) | Post.objects.filter(
        content__icontains=query
    ) | Post.objects.filter(
        category__icontains=query
    )
  else:
    results = Post.objects.none()

  contents = {'allposts': results, 'query' : "Search Results for: "+query}

  return render(request, 'blog/blogp.html', contents)


def category(request, category_name):
  if category_name:
    results = Post.objects.filter(category=category_name)
  else:
    results = Post.objects.all()
  contents = {'allposts': results, 'query': category_name}
  return render(request, 'blog/blogp.html', contents)
