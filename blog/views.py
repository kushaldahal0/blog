from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post,Comment
from django_ratelimit.decorators import ratelimit
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def index(request):
  allposts = Post.objects.all().order_by('-created_at')
  paginator = Paginator(allposts, 6)  # Show 6 posts per page
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  contents = {'page_obj': page_obj,'query': 'Minimal Blog'}
  return render(request, 'blog/blogp.html', contents)

@ratelimit(key='ip', rate='3/m', method='ALL', block=True)
def blogpost(request):
  if not request.user.is_authenticated:
    messages.error(request, 'You must be logged in to create a post.')
    return redirect('home:login')
  
  if request.method == "POST":
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.user
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
  return render(request, 'blog/blogpost.html', {'tinymce_api_key': settings.TINYMCE_API_KEY})


def singleb(request, slug):
  post = Post.objects.get(slug=slug)
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
    post_slug = request.POST.get('post_slug')
    parentc_no = request.POST.get('parentc_no')
    
    post = Post.objects.get(slug=post_slug)
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
    return redirect('blog:singleb_slug', slug=post_slug)
        
      

def search_posts(request):
  query = request.GET.get('search')
  if query:
    # Apply all filters to the queryset
    results = Post.objects.filter(
        title__icontains=query
    ) | Post.objects.filter(
        author__username__icontains=query
    ) | Post.objects.filter(
        content__icontains=query
    ) | Post.objects.filter(
        category__icontains=query
    ).order_by('-created_at')
  else:
    results = Post.objects.none()

  paginator = Paginator(results, 6)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  contents = {'page_obj': page_obj, 'query' : "Search Results for: "+query}

  return render(request, 'blog/blogp.html', contents)


def edit_post(request, slug):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to edit posts.')
        return redirect('home:login')
    
    post = get_object_or_404(Post, slug=slug)
    
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('blog:singleb_slug', slug=slug)
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        
        post.title = title
        post.content = content
        post.category = category
        post.save()
        
        messages.success(request, 'Your post has been updated successfully!')
        return redirect('blog:singleb_slug', slug=post.slug)
    
    contents = {'post': post, 'tinymce_api_key': settings.TINYMCE_API_KEY}
    return render(request, 'blog/edit_post.html', contents)


def category(request, category_name):
  if category_name:
    results = Post.objects.filter(category=category_name).order_by('-created_at')
  else:
    results = Post.objects.all().order_by('-created_at')
  
  paginator = Paginator(results, 6)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  contents = {'page_obj': page_obj, 'query': category_name}
  return render(request, 'blog/blogp.html', contents)
