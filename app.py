from flask import Flask, Response, render_template, send_from_directory, send_file, request, jsonify
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

# Enhanced SEO headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    return response

# Routes with enhanced SEO
@app.route('/')
def index():
    return render_template('index.html', 
                          year=get_current_year(),
                          meta_title="Free Temporary Email Generator | Disposable Email Addresses - ZyMail",
                          meta_description="ZyMail offers free temporary email addresses with instant disposable emails. Protect your privacy, avoid spam, receive OTPs instantly - no signup required. Best temp mail service 2025.")

@app.route('/about')
def about():
    return render_template('about.html', 
                          year=get_current_year(),
                          meta_title="About ZyMail | Free Temporary Email Service",
                          meta_description="Learn about ZyMail, the best free temporary email service created by Ajmal U K. Discover our mission to provide privacy-focused disposable email solutions.")

@app.route('/contact')
def contact():
    return render_template('contact.html', 
                          year=get_current_year(),
                          meta_title="Contact ZyMail | Temporary Email Service Support",
                          meta_description="Have questions about ZyMail's free temporary email service? Contact our support team for assistance with disposable email addresses and privacy protection.")

@app.route('/terms')
def terms():
    return render_template('terms.html', 
                          year=get_current_year(),
                          meta_title="Terms of Service | ZyMail Temporary Email Generator",
                          meta_description="Review ZyMail's terms of service for our free temporary email generator. Understand your rights and responsibilities when using disposable email addresses.")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', 
                          year=get_current_year(),
                          meta_title="Privacy Policy | ZyMail Disposable Email Service",
                          meta_description="Read ZyMail's comprehensive privacy policy. Learn how we protect your data with our free temporary email service and disposable email addresses.")

@app.route('/faq')
def faq():
    return render_template('faq.html', 
                          year=get_current_year(),
                          meta_title="FAQ | ZyMail Temporary Email Service",
                          meta_description="Find answers to frequently asked questions about ZyMail's free temporary email service. Learn how disposable email addresses protect your privacy.")

@app.route('/blog')
def blog():
    return render_template('blog.html', 
                          year=get_current_year(),
                          meta_title="ZyMail Blog | Temporary Email & Privacy Tips",
                          meta_description="Explore the ZyMail blog for expert tips on temporary email services, online privacy, and spam protection. Learn how disposable email addresses can protect you online.")

@app.route('/features')
def features():
    return render_template('features.html', 
                          year=get_current_year(),
                          meta_title="Features | ZyMail Free Temporary Email Generator",
                          meta_description="Discover the powerful features of ZyMail's free temporary email service. Instant disposable emails, privacy protection, and spam prevention - all without signup.")

@app.route('/app')
def app_page():
    return render_template('app.html', 
                          year=get_current_year(),
                          meta_title="ZyMail App | Free Temporary Email Generator",
                          meta_description="Generate free temporary email addresses instantly with ZyMail. Protect your privacy, avoid spam, receive OTPs - no signup required. Best disposable email service.")

# Enhanced sitemap with priority and frequency
@app.route('/sitemap.xml')
def sitemap():
    pages = []
    # Static pages with priority and frequency
    static_pages = [
        ("", "1.0", "daily"),
        ("/about", "0.8", "weekly"),
        ("/contact", "0.7", "monthly"),
        ("/terms", "0.6", "monthly"),
        ("/privacy", "0.7", "monthly"),
        ("/faq", "0.9", "weekly"),
        ("/blog", "0.8", "weekly"),
        ("/features", "0.9", "weekly"),
        ("/app", "0.9", "daily"),
    ]
    
    for path, priority, freq in static_pages:
        pages.append((f"{app.config['SITE_URL']}{path}", priority, freq))
    
    # Blog posts
    blog_posts = [
        ("/blog/why-use-a-temporary-email-service", "0.8", "weekly"),
        ("/blog/how-to-avoid-spam-with-temporary-emails", "0.8", "weekly"),
        ("/blog/protecting-your-online-privacy", "0.8", "weekly")
    ]
    pages.extend([(f"{app.config['SITE_URL']}{post}", priority, freq) for post, priority, freq in blog_posts])
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url, priority, freq in pages:
        sitemap_xml += f"""
        <url>
            <loc>{url}</loc>
            <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
            <changefreq>{freq}</changefreq>
            <priority>{priority}</priority>
        </url>
        """
    
    sitemap_xml += '</urlset>'
    return Response(sitemap_xml, mimetype='application/xml')

# Enhanced robots.txt
@app.route('/robots.txt')
def robots():
    robots_content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/

Sitemap: https://zymail.pythonanywhere.com/sitemap.xml

# Crawl delay
Crawl-delay: 1"""
    return Response(robots_content, mimetype='text/plain')

# Error handlers with SEO-friendly pages
@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', 
                          title='400 Bad Request | ZyMail',
                          year=get_current_year()), 400

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', 
                          title='403 Forbidden | ZyMail',
                          year=get_current_year()), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', 
                          title='404 Not Found | ZyMail',
                          year=get_current_year()), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', 
                          title='500 Internal Server Error | ZyMail',
                          year=get_current_year()), 500

# Asset routes
@app.route('/google83f8616f6a5b1974.html')
def google_verification():
    return send_from_directory('assets', 'google83f8616f6a5b1974.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('assets', 'robots.txt')

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