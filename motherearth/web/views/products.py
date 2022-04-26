from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Product


class CreateProductView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Product
    template_name = 'products/product_create.html'
    fields = ('title', 'craft', 'description', 'photo', 'price')
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(Product.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'products': products,
        }
        )

        return context


class EditProductView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Product
    template_name = 'products/product_edit.html'
    fields = ('title', 'craft', 'description', 'photo', 'price')

    def get_success_url(self):
        return reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(Product.objects.filter(owner_id=self.object.owner_id))
        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'products': products,
        }
        )

        return context


class DeleteProductView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'

    def get_success_url(self):
        return reverse_lazy('market')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(Product.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'products': products,
        }
        )

        return context


class MyProductView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'products/my_products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user.profile)
