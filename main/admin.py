from django.contrib import admin

from .models import DemandData, GeoData, SkillsData

# class CsvImportForm(forms.Form):
#     csv_upload = forms.FileField()
#     # csv_upload.label = 'Загрузить csv'
#

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'balance')
#
#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path('upload-csv/', self.upload_csv), ]
#         return new_urls + urls
#
#     def upload_csv(self, request):
#         if request.method == "POST":
#             csv_file = request.FILES["csv_upload"]
#
#             if not csv_file.name.endswith('.csv'):
#                 messages.warning(request, 'Неверный формат')
#                 return HttpResponseRedirect(request.path_info)
#
#             file_data = csv_file.read().decode("utf-8")
#             csv_data = file_data.split("\n")
#
#             for x in csv_data:
#                 fields = x.split(",")
#                 created = Customer.objects.update_or_create(
#                     name=fields[0],
#                     balance=fields[1],
#                 )
#             url = reverse('admin:index')
#             return HttpResponseRedirect(url)
#
#         form = CsvImportForm()
#         data = {"form": form}
#         return render(request, "admin/load_csv.html", data)


# admin.site.register(Customer, CustomerAdmin)

admin.site.register(DemandData)
admin.site.register(GeoData)
admin.site.register(SkillsData)
