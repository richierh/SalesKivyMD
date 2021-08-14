from kivy.utils import platform

if platform == "android":
    from controllers.social_auth.kivyauth.android.google_auth import (
        initialize_google,
        login_google,
        logout_google,
    )

elif platform != "ios":
    from controllers.social_auth.kivyauth.android.google_auth import (
        initialize_google,
        login_google,
        logout_google,
    )
