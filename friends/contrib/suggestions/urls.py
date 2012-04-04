from django.conf.urls.defaults import *


urlpatterns = patterns("friends.contrib.suggestions.views",

    url(r"^suggested_friends/$",
        "suggested_friends",
        name="friends_suggestions_suggested_friends"),

    url(r"^import_contacts/$",
        "import_contacts",
        name="friends_suggestions_import_contacts"),

    url(r'^import_google_contacts/$',
        "import_google_contacts",
        name='friends_suggestions_import_google_contacts'),

)