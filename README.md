<h3>Django CRUD</h3>
<p>The sole purpose of this repository is to practice the developer's knowledge in Django.</p>
<i>Take note: It is STATICFILES_DIRS not STATIC_DIRS</i>

<h3>Mobile Numbers</h3>
<p>from django.core.validators import RegexValidator</p>
<p>phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")</p>

<i>Although there is phone number field already available ("pip install django-phonenumber-field"), but size is around 30~40MB (https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models)</i>