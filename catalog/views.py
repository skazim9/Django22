from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from .forms import ProductForm, Category, ProductModeratorForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


from catalog.models import Product


# Create your views here.


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        if self.request.user.has_perm("catalog.remove_any_product"):
            return ProductModeratorForm
        return ProductForm

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "catalog.can_unpublish_product"
        )

    def handle_no_permission(self):
        raise PermissionDenied


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')

