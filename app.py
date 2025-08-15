from flask import Flask, make_response, redirect, render_template, request, send_from_directory
from flask_compress import Compress
import os
from datetime import datetime
import markdown

app = Flask(__name__, template_folder='templates', static_folder='static')
Compress(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SITE_URL'] = 'https://zymail.pythonanywhere.com'


# Helper functions
def get_current_year():
    return datetime.now().year

def markdown_to_html(md_text):
    return markdown.markdown(md_text)


@app.before_request
def redirect_nonwww():
    if request.host.startswith('www.'):
        return redirect(request.url.replace('www.', '', 1), code=301)
    
    if not request.is_secure:
        return redirect(request.url.replace('http://', 'https://', 1), code=301)
    


@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    return response

# Routes with enhanced SEO
@app.route('/')
def index():
    return render_template('index.html', 
                          year=get_current_year(),
                          meta_title="Free Temporary Email Generator | Disposable Email Addresses - ZyMail",
                          meta_description="Generate free temporary email addresses instantly with ZyMail. Protect your privacy, avoid spam, receive OTPs - no signup required. Best disposable email service 2025.",
                          meta_keywords="temp mail, temporary email, disposable email, free temp mail, email privacy, anonymous email, spam prevention, OTP receiver, email verification, secure email, 10 minute mail, instant email, no signup email, ZyMail",
                          canonical_url="https://zymail.pythonanywhere.com/")

@app.route('/about')
def about():
    return render_template('about.html', 
                          year=get_current_year(),
                          meta_title="About ZyMail | Free Temporary Email Service by Ajmal U K",
                          meta_description="Learn about ZyMail, the best free temporary email service created by Ajmal U K. Discover our mission to provide privacy-focused disposable email solutions for secure online registrations.",
                          meta_keywords="about zymail, temporary email service, disposable email, free temp mail, email privacy, anonymous email, temp email generator, uthakkan, ajmal u k, college of engineering trivandrum",
                          canonical_url="https://zymail.pythonanywhere.com/about")

@app.route('/contact')
def contact():
    return render_template('contact.html', 
                          year=get_current_year(),
                          meta_title="Contact ZyMail | Temporary Email Service Support",
                          meta_description="Have questions about ZyMail's free temporary email service? Contact our support team for assistance with disposable email addresses and privacy protection.",
                          meta_keywords="zymail contact, temporary email contact, disposable email, free temp mail, email privacy, anonymous email, temp email service, uthakkan, ajmal u k, contact temp mail",
                          canonical_url="https://zymail.pythonanywhere.com/contact")

@app.route('/terms')
def terms():
    return render_template('terms.html', 
                          year=get_current_year(),
                          meta_title="Terms of Service | ZyMail Temporary Email Generator",
                          meta_description="Review ZyMail's terms of service for our free temporary email generator. Understand your rights and responsibilities when using disposable email addresses.",
                          meta_keywords="zymail terms, temporary email terms, disposable email, free temp mail, email privacy, anonymous email, user agreement, temp mail terms",
                          canonical_url="https://zymail.pythonanywhere.com/terms")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', 
                          year=get_current_year(),
                          meta_title="Privacy Policy | ZyMail Disposable Email Service",
                          meta_description="Read ZyMail's comprehensive privacy policy. Learn how we protect your data with our free temporary email service and disposable email addresses.",
                          meta_keywords="zymail privacy, temporary email privacy, disposable email, free temp mail, email privacy, anonymous email, data protection, user privacy",
                          canonical_url="https://zymail.pythonanywhere.com/privacy")

@app.route('/faq')
def faq():
    return render_template('faq.html', 
                          year=get_current_year(),
                          meta_title="FAQ | ZyMail Temporary Email Service",
                          meta_description="Find answers to frequently asked questions about ZyMail's free temporary email service. Learn how disposable email addresses protect your privacy.",
                          meta_keywords="zymail faq, temporary email, disposable email, free temp mail, email privacy, anonymous email, temp email service, instant email generator, no registration email, privacy protection, spam-free email, uthakkan, ajmal u k, college of engineering trivandrum, temp mail faq",
                          canonical_url="https://zymail.pythonanywhere.com/faq")

@app.route('/blog')
def blog():
    return render_template('blog.html', 
                          year=get_current_year(),
                          meta_title="ZyMail Blog | Temporary Email & Privacy Tips",
                          meta_description="Explore the ZyMail blog for expert tips on temporary email services, online privacy, and spam protection. Learn how disposable email addresses can protect you online.",
                          meta_keywords="zymail blog, temporary email, disposable email, free temp mail, email privacy, anonymous email, temp mail service, uthakkan, ajmal u k, college of engineering trivandrum, temp mail blog",
                          canonical_url="https://zymail.pythonanywhere.com/blog")

@app.route('/features')
def features():
    return render_template('features.html', 
                          year=get_current_year(),
                          meta_title="Features | ZyMail Free Temporary Email Generator",
                          meta_description="Discover the powerful features of ZyMail's free temporary email service. Instant disposable emails, privacy protection, and spam prevention - all without signup.",
                          meta_keywords="zymail features, temporary email, disposable email, free temp mail, email privacy, anonymous email, temp email service, instant email generator, no registration email, privacy protection, spam-free email, uthakkan, ajmal u k, college of engineering trivandrum",
                          canonical_url="https://zymail.pythonanywhere.com/features")

@app.route('/app')
def app_page():
    return render_template('app.html', 
                          year=get_current_year(),
                          meta_title="ZyMail App | Free Temporary Email Generator",
                          meta_description="Generate free temporary email addresses instantly with ZyMail. Protect your privacy, avoid spam, receive OTPs - no signup required. Best disposable email service.",
                          meta_keywords="temp mail, temporary email, disposable email, free temp mail, email privacy, anonymous email, spam prevention, OTP receiver, email verification, secure email, 10 minute mail, instant email, no signup email, ZyMail",
                          canonical_url="https://zymail.pythonanywhere.com/app")



@app.route('/blog/why-use-a-temporary-email-service')
def blog_post_1():
    return render_template('why-use-a-temporary-email-service.html', 
                          year=get_current_year(),
                          meta_title="Why Use a Temporary Email Service? | ZyMail Blog",
                          meta_description="Learn how temporary email services protect your inbox from spam and enhance privacy during online registrations.",
                          canonical_url="https://zymail.pythonanywhere.com/blog/why-use-a-temporary-email-service")
 
@app.route('/blog/protecting-your-online-privacy')
def blog_post_2():
    return render_template('protecting-your-online-privacy.html', 
                          year=get_current_year(),
                          meta_title="Protecting Your Online Privacy in 2025 | ZyMail Blog",
                          meta_description="Essential tips and tools for safeguarding your personal information online with temporary email services.",
                          canonical_url="https://zymail.pythonanywhere.com/blog/protecting-your-online-privacy")
 
@app.route('/blog/how-to-avoid-spam-with-temporary-emails')
def blog_post_3():
    return render_template('how-to-avoid-spam-with-temporary-emails.html', 
                          year=get_current_year(),
                          meta_title="How to Avoid Spam with Temporary Emails | ZyMail Blog",
                          meta_description="Discover effective strategies to prevent spam using disposable email addresses and keep your primary inbox clean.",
                          canonical_url="https://zymail.pythonanywhere.com/blog/how-to-avoid-spam-with-temporary-emails")




@app.route('/sitemap.xml')
def sitemap():
    pages = [
        {'loc': 'https://zymail.pythonanywhere.com/', 'priority': '1.0'},
        {'loc': 'https://zymail.pythonanywhere.com/about', 'priority': '0.8'},
        {'loc': 'https://zymail.pythonanywhere.com/app', 'priority': '0.9'},
        {'loc': 'https://zymail.pythonanywhere.com/blog', 'priority': '0.7'},
        {'loc': 'https://zymail.pythonanywhere.com/blog/why-use-a-temporary-email-service', 'priority': '0.6'},
        {'loc': 'https://zymail.pythonanywhere.com/blog/protecting-your-online-privacy', 'priority': '0.6'},
        {'loc': 'https://zymail.pythonanywhere.com/blog/how-to-avoid-spam-with-temporary-emails', 'priority': '0.6'},
        {'loc': 'https://zymail.pythonanywhere.com/contact', 'priority': '0.7'},
        {'loc': 'https://zymail.pythonanywhere.com/faq', 'priority': '0.8'},
        {'loc': 'https://zymail.pythonanywhere.com/features', 'priority': '0.8'},
        {'loc': 'https://zymail.pythonanywhere.com/privacy', 'priority': '0.7'},
        {'loc': 'https://zymail.pythonanywhere.com/terms', 'priority': '0.7'}
    ]
    
    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response


# Error handlers with SEO
@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', 
                          title='400 Bad Request | ZyMail',
                          meta_title="400 Bad Request | ZyMail Temporary Email Service",
                          meta_description="The request could not be understood by ZyMail. Please check your input and try again.",
                          year=get_current_year()), 400

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', 
                          title='403 Forbidden | ZyMail',
                          meta_title="403 Forbidden | ZyMail Temporary Email Service",
                          meta_description="You don't have permission to access this resource on ZyMail. Please contact support if you believe this is an error.",
                          year=get_current_year()), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', 
                          title='404 Not Found | ZyMail',
                          meta_title="404 Not Found | ZyMail Temporary Email Service",
                          meta_description="The page you requested could not be found on ZyMail. Try our homepage or use the search function.",
                          year=get_current_year()), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', 
                          title='500 Internal Server Error | ZyMail',
                          meta_title="500 Internal Server Error | ZyMail Temporary Email Service",
                          meta_description="We're experiencing technical difficulties on ZyMail. Our team has been notified and is working to resolve the issue.",
                          year=get_current_year()), 500

# Asset routes
@app.route('/google83f8616f6a5b1974.html')
def google_verification():
    return send_from_directory('assets', 'google83f8616f6a5b1974.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('assets', 'robots.txt')

@app.route('/llms.txt')
def llms():
    return send_from_directory('assets', 'llms.txt')

@app.route('/ads.txt')
def ads():
    return send_from_directory('assets', 'ads.txt')

@app.route('/logo.png')
def logo():
    return send_from_directory('assets', 'logo.png')

@app.route('/og-image.jpg')
def og_image():
    return send_from_directory('assets', 'og-image.jpg')

@app.route('/twitter-image.jpg')
def twitter_image():
    return send_from_directory('assets', 'twitter-image.jpg')

# Favicon routes
@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory('assets/favicon', 'favicon.ico')

@app.route('/favicon.svg')
def favicon_svg():
    return send_from_directory('assets/favicon', 'favicon.svg')

@app.route('/favicon-96x96.png')
def favicon_96():
    return send_from_directory('assets/favicon', 'favicon-96x96.png')

@app.route('/web-app-manifest-192x192.png')
def web_app_manifest_192():
    return send_from_directory('assets/favicon', 'web-app-manifest-192x192.png')

@app.route('/web-app-manifest-512x512.png')
def web_app_manifest_512():
    return send_from_directory('assets/favicon', 'web-app-manifest-512x512.png')

@app.route('/apple-touch-icon.png')
def apple_icon():
    return send_from_directory('assets/favicon', 'apple-touch-icon.png')

@app.route('/site.webmanifest')
def webmanifest():
    return send_from_directory('assets/favicon', 'site.webmanifest')

if __name__ == '__main__':
    app.run(debug=False, threaded=True, host='0.0.0.0', port=5000)