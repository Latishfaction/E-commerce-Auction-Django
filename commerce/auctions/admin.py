from django.contrib import admin

from .models import User,Category,Listing,Comment,Bid,Watchlist,OrderHistory
# Register your models here.

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(OrderHistory)