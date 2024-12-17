from django.core.cache import cache

from config.settings import CACHE_ENABLED
from .models import Product, Category


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


class CategoryService:
    @staticmethod
    def get_full_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
