<h3>Django CRUD</h3>
<p>The sole purpose of this repository is to practice the developer's knowledge in Django.</p>
<i>Take note: It is STATICFILES_DIRS not STATIC_DIRS</i>

<h3>Mobile Numbers</h3>

<p>The following code below for phone number/s did not work, suggest using the bold captioned sentence. </p>
<i>from django.core.validators import RegexValidator</i>
<i>phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")</i>

<b>Although there is phone number field already available ("pip install django-phonenumber-field"), but size is around 30~40MB (https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models)</b>

<h3>Models</h3>
<i>https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63 ; This teaches how to work with Enum. Keeping it for reference</i>
<b>Only used Django's suggested way in doing Choice. See <a href="https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices">here</a>.</b>