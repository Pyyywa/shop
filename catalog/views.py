from django.shortcuts import render
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/material_list.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'{product_item.product_name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'desc', 'image', 'category', 'quantity_per_unit', 'сreation_date', 'last_change_date', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.product_name)
            new_material.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.kwargs.get('pk')])


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'desc', 'image', 'category', 'quantity_per_unit', 'сreation_date', 'last_change_date', 'is_published')
    #success_url = reverse_lazy('catalog:base')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.product_name)
            new_material.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_view', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')