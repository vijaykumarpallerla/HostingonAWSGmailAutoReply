from django.conf import settings
from django.shortcuts import render

def restrict_email_domain(backend, details, response, *args, **kwargs):
    allowed_domains = getattr(settings, 'ALLOWED_EMAIL_DOMAINS', [])
    allowed_emails = getattr(settings, 'ALLOWED_EMAILS', [])
    
    # If no restrictions are set, allow everyone (or you could default to deny)
    if not allowed_domains and not allowed_emails:
        return

    email = details.get('email', '')
    request = kwargs.get('request')
    
    # Check specific emails
    if email in allowed_emails:
        return

    # Check domains
    if any(email.endswith(domain) for domain in allowed_domains):
        return

    return render(request, 'access_denied.html', status=403)
