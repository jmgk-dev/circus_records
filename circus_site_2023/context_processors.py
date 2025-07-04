from django.conf import settings

def global_ids(request):
    """
    Makes global IDs/configs available in all templates.
    """
    return {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'MAILERLITE_ACCOUNT_ID': settings.MAILERLITE_ACCOUNT_ID,
        'META_PIXEL_ID': settings.META_PIXEL_ID,
        'TERMLY_UUID': settings.TERMLY_UUID,
        'GOOGLE_SITE_VERIFICATION': settings.GOOGLE_SITE_VERIFICATION,
        'TERMS_POLICY_UUID': settings.TERMS_POLICY_UUID,
        'PRIVACY_POLICY_UUID': settings.PRIVACY_POLICY_UUID,
    }