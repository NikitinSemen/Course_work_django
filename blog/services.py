from django.core.cache import cache

from config.settings import CACHE_ENABLED
from blog.models import Blog


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Blog.objects.all()
    key = f'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Blog.objects.all()
    cache.set(key, products)
