from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


    def clean_email(self):
        data = self.cleaned_data['email']
        is_exists = ShopUser.objects.exclude(pk=self.instance.pk).filter(email=data).exists()


