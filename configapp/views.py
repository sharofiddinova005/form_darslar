from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from configapp.models import Category, News
from .forms import NewsForm, CategoryForm


# ==============================================
# NEWS VIEWLARI
# ==============================================

def detail_new(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'detail_new.html', {"new": new})


def update_new(request, pk):
    new = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=new)

    return render(request, 'update_new.html', {"form": form, "new": new})


def del_new(request, pk):
    new = get_object_or_404(News, pk=pk)
    new.delete()
    return redirect('home')  # o'chirishdan keyin index.html ga redirect qilish osonroq


class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = Category.objects.all()  # 'Category.objects.all()' bo'lishi kerak
        return context


# ==============================================
# CATEGORY VIEWLARI
# ==============================================

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(title=name)
        return redirect('home')

    return render(request, 'add_category.html')


def detail_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'detail_category.html', {"category": category})


def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'update_category.html', {"form": form, "category": category})


def del_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('home')


class HomeCategory(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context


def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        "news": news,
        "categories": categories,
        "title": "Home page"
    }
    return render(request, "index.html", context)