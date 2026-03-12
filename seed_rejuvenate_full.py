#!/usr/bin/env python3
"""
Seed Rejuvenate Skin Experts — Full 9-Page Site
Seeds into Payload CMS MongoDB (reeveos_cms database)
Run: python3 seed_rejuvenate_full.py
"""

from pymongo import MongoClient
from datetime import datetime, timezone
from bson import ObjectId

DB_NAME = "reeveos_cms"
client = MongoClient("mongodb://127.0.0.1:27017")
db = client[DB_NAME]

now = datetime.now(timezone.utc)

# ─── CLEAN PREVIOUS DATA ────────────────────────────────────────────
print("Cleaning previous Rejuvenate data...")
db.tenants.delete_many({"subdomain": "rejuvenate-skin-experts"})
db.pages.delete_many({"tenant": {"$exists": True}})
print("  Done.")

# ─── TENANT ──────────────────────────────────────────────────────────
tenant_id = ObjectId()
tenant = {
    "_id": tenant_id,
    "name": "Rejuvenate Skin Experts",
    "subdomain": "rejuvenate-skin-experts",
    "customDomain": None,
    "brandColors": {
        "primary": "#2C3E2D",
        "secondary": "#C4A265",
        "background": "#FAF7F2",
        "text": "#2C3E2D",
        "accent": "#C4A265",
    },
    "fonts": {
        "heading": "Cormorant Garamond",
        "body": "DM Sans",
    },
    "logo": "/images/logo.png",
    "favicon": "/images/favicon.ico",
    "navigation": [
        {"label": "Treatments", "href": "/treatments", "order": 1},
        {"label": "Packages", "href": "/packages", "order": 2},
        {"label": "Results", "href": "/results", "order": 3},
        {"label": "Shop", "href": "/shop", "order": 4},
        {"label": "Courses", "href": "/courses", "order": 5},
        {"label": "About", "href": "/about", "order": 6},
        {"label": "Blog", "href": "/blog", "order": 7},
        {"label": "Contact", "href": "/contact", "order": 8},
    ],
    "footer": {
        "businessName": "Rejuvenate Skin Experts",
        "address": "Barry, near Cardiff, South Wales",
        "phone": "07XXX XXXXXX",
        "email": "hello@rejuvenatecardiff.co.uk",
        "hours": "Tue–Sat 9am–6pm",
        "social": {
            "instagram": "https://instagram.com/rejuvenatecardiff",
            "facebook": "https://facebook.com/rejuvenatecardiff",
        },
    },
    "seoDefaults": {
        "titleSuffix": " | Rejuvenate Skin Experts, Cardiff",
        "defaultDescription": "Cardiff's most-reviewed skin clinic. Advanced facials, microneedling, RF treatments, and professional skincare.",
    },
    "integrations": {
        "bookingUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
        "shopApiBase": "https://portal.rezvo.app/api",
        "shopSlug": "rejuvenate-skin-experts",
    },
    "createdAt": now,
    "updatedAt": now,
}

db.tenants.insert_one(tenant)
print(f"✓ Tenant created: {tenant['name']} ({tenant['subdomain']})")

# ─── HELPER ──────────────────────────────────────────────────────────
def make_page(slug, title, seo_title, seo_desc, blocks, order, excerpt=""):
    page_id = ObjectId()
    return {
        "_id": page_id,
        "tenant": tenant_id,
        "title": title,
        "slug": slug,
        "status": "published",
        "puckData": {"content": blocks, "root": {"props": {}}},
        "seo": {
            "title": seo_title,
            "description": seo_desc,
        },
        "excerpt": excerpt,
        "order": order,
        "publishedAt": now,
        "createdAt": now,
        "updatedAt": now,
    }


# ─── PAGE 1: HOME ───────────────────────────────────────────────────
home = make_page(
    slug="home",
    title="Home",
    seo_title="Cardiff's Most-Reviewed Skin Clinic | Rejuvenate Skin Experts",
    seo_desc="Advanced facials, microneedling, RF treatments and Dermalogica skincare. 17+ years experience, 418+ five-star reviews. Barry, near Cardiff.",
    excerpt="Where your skin story begins.",
    order=0,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Cardiff's Most-Reviewed Skin Clinic.",
                "subheading": "Your Move.",
                "ctaText": "Book a Consultation",
                "ctaUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
                "backgroundImage": "/images/hero-home.jpg",
            },
        },
        {
            "type": "GatewayCards",
            "props": {
                "cards": [
                    {"title": "Book a Facial", "description": "Your skin reset is 60 minutes away.", "href": "/treatments", "color": "#F0D9D0"},
                    {"title": "Fix My Skin", "description": "Clear, confident skin in 3 treatments.", "href": "/results", "color": "#EDE6D8"},
                    {"title": "Talk to Natalie", "description": "A skin specialist who actually listens.", "href": "/about", "color": "#E8E0D0"},
                ],
            },
        },
        {
            "type": "TrustStats",
            "props": {
                "stats": [
                    {"value": "17+", "label": "Years Experience"},
                    {"value": "418+", "label": "Five-Star Reviews"},
                    {"value": "5.0", "label": "Average Rating"},
                    {"value": "✓", "label": "Dermalogica Partner"},
                ],
            },
        },
        {
            "type": "Testimonials",
            "props": {
                "heading": "What Our Clients Say",
                "items": [
                    {"text": "Best facial I've ever had. Natalie really knows skin.", "name": "Sarah M.", "rating": 5},
                    {"text": "My acne scarring has genuinely transformed after 4 sessions.", "name": "Rachel D.", "rating": 5},
                    {"text": "The clinic is gorgeous and the results speak for themselves.", "name": "Emma L.", "rating": 5},
                ],
            },
        },
        {
            "type": "CTA",
            "props": {
                "heading": "Ready to Start Your Skin Journey?",
                "text": "Book your consultation today.",
                "buttonText": "Book Now",
                "buttonUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
            },
        },
    ],
)

# ─── PAGE 2: TREATMENTS ─────────────────────────────────────────────
treatments = make_page(
    slug="treatments",
    title="Treatments",
    seo_title="Skin Treatments | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Microneedling, RF Microneedling, Chemical Peels, Lymphatic Lift Facials, Exosome Therapy and more. Advanced skin treatments in Cardiff.",
    excerpt="Advanced treatments for every skin concern.",
    order=1,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Our Treatments",
                "subheading": "Science-led. Results-proven.",
                "backgroundImage": "/images/hero-treatments.jpg",
            },
        },
        {
            "type": "TreatmentList",
            "props": {
                "treatments": [
                    {"name": "Luxury Lymphatic Lift Facial", "price": "From £165", "duration": "75 min", "downtime": "None", "description": "Breathwork, ozone steaming, and therapeutic lymphatic drainage massage. Instant lifted, glowing complexion.", "badge": "Most Relaxing"},
                    {"name": "Microneedling Facial", "price": "From £165", "duration": "60 min", "downtime": "1–2 days", "description": "Precision microneedling creates controlled micro-channels. Gold standard for skin correction."},
                    {"name": "Microneedling Hydration Deluxe", "price": "From £220", "duration": "75 min", "downtime": "1–2 days", "description": "Standard microneedling enhanced with targeted hydration serum infusion."},
                    {"name": "Microneedling with Exosomes", "price": "£315", "duration": "75 min", "downtime": "2–3 days", "description": "Exosome boosters delivered directly into the dermis via microneedling channels.", "badge": "Advanced"},
                    {"name": "RF Microneedling (Face)", "price": "From £295", "duration": "90 min", "downtime": "2–4 days", "description": "Radiofrequency energy via gold-tipped microneedles. Dramatic skin tightening.", "badge": "Premium"},
                    {"name": "RF Microneedling (Body)", "price": "£295", "duration": "90 min", "downtime": "2–4 days", "description": "RF microneedling for body areas. Stretch marks, loose skin, deep collagen remodelling."},
                    {"name": "Ultimate Skin Rejuvenation Ritual", "price": "From £330", "duration": "120 min", "downtime": "2–3 days", "description": "The complete experience. Microneedling, exosomes, LED, lymphatic drainage in one session.", "badge": "Signature"},
                    {"name": "Chemical Face Peel", "price": "From £100", "duration": "45–60 min", "downtime": "3–7 days", "description": "Professional-grade AHA and BHA peels tailored to your skin concern."},
                    {"name": "The Quick Fix Glow Up", "price": "£115", "duration": "45 min", "downtime": "None", "description": "Express lymphatic facial for instant radiance. Perfect pre-event.", "badge": "Express"},
                    {"name": "AI Skin Consultation", "price": "£80", "duration": "60 min", "downtime": "None", "description": "Zemits AI Skin Scanner analyses 12 skin concerns. £40 redeemable against first treatment."},
                    {"name": "Exosome Hair Restoration", "price": "£300 / £1,500 block of 6", "duration": "60 min", "downtime": "24–48 hrs", "description": "Exosomes delivered into the scalp to stimulate dormant follicles and promote regrowth."},
                ],
            },
        },
        {
            "type": "CTA",
            "props": {
                "heading": "Not Sure Which Treatment?",
                "text": "Start with an AI Skin Consultation — £40 redeemable against your first treatment.",
                "buttonText": "Book a Consultation",
                "buttonUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
            },
        },
    ],
)

# ─── PAGE 3: PACKAGES ───────────────────────────────────────────────
packages = make_page(
    slug="packages",
    title="Packages",
    seo_title="Treatment Packages | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Save on courses of treatments. 18-week intensive plans, lymphatic correction packages, and signature rituals.",
    excerpt="Bundled treatment plans for maximum results.",
    order=2,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Treatment Packages",
                "subheading": "Commit to the journey. Transform the result.",
            },
        },
        {
            "type": "PackageList",
            "props": {
                "packages": [
                    {"name": "18-Week Intensive Correction Plan", "price": "£990", "badge": "Most Popular", "tagline": "The complete skin transformation.", "includes": ["6 × Microneedling Facials", "Customised homecare plan", "Progress photography", "Klarna & Clearpay available"]},
                    {"name": "Lymphatic Correction Package", "price": "POA", "badge": "Holistic", "tagline": "Lymphatic drainage, corrected.", "includes": ["Bespoke lymphatic correction plan", "Multiple lymphatic sessions", "Tailored to your skin goals"]},
                    {"name": "Ultimate Skin Rejuvenation Ritual", "price": "From £330", "badge": "Signature", "tagline": "The full experience, in one session.", "includes": ["Microneedling with Exosome Boosters", "LED Light Therapy", "Lymphatic Drainage", "Advanced Stayve AC Stem Serums"]},
                    {"name": "The Quick Fix Glow Up", "price": "£115", "badge": "Express", "tagline": "Instant radiance when you need it most.", "includes": ["Express Lymphatic Lift Facial", "45 minutes", "Zero downtime"]},
                ],
            },
        },
    ],
)

# ─── PAGE 4: RESULTS ────────────────────────────────────────────────
results = make_page(
    slug="results",
    title="Results",
    seo_title="Before & After Results | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Real client transformations. See microneedling, RF, and chemical peel results from Rejuvenate Skin Experts.",
    excerpt="Real transformations from real clients.",
    order=3,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Clear, Confident Skin in 3 Treatments",
                "subheading": "Real results. Real clients. No filters.",
            },
        },
        {
            "type": "BeforeAfterGallery",
            "props": {
                "heading": "Client Transformations",
                "items": [
                    {"treatment": "Microneedling Course", "sessions": "6 sessions over 18 weeks"},
                    {"treatment": "RF Microneedling", "sessions": "3 sessions"},
                    {"treatment": "Chemical Peel Course", "sessions": "4 sessions"},
                ],
            },
        },
        {
            "type": "CTA",
            "props": {
                "heading": "Ready for Your Transformation?",
                "buttonText": "Book Now",
                "buttonUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
            },
        },
    ],
)

# ─── PAGE 5: SHOP ───────────────────────────────────────────────────
shop = make_page(
    slug="shop",
    title="Shop",
    seo_title="Shop Skincare | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Shop Amatus skincare and Dermalogica professional products. Clinic-tested formulations. Free shipping available.",
    excerpt="Clinic-tested skincare delivered to your door.",
    order=4,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "The Skin Shop",
                "subheading": "Clinic-tested. Dermatologist-approved.",
            },
        },
        {
            "type": "ShopGrid",
            "props": {
                "apiEndpoint": "/api/shop/public/rejuvenate-skin-experts/products",
                "categories": ["Amatus Skincare", "Dermalogica"],
                "products": [
                    {"id": "fp1", "name": "Amatus Gentle 3-Step Routine", "price": 189, "category": "Amatus Skincare", "badge": "Bestseller"},
                    {"id": "fp2", "name": "Amatus Complex 3-Step Routine", "price": 188.95, "category": "Amatus Skincare"},
                    {"id": "fp3", "name": "Amatus Complex Daily Set", "price": 210, "category": "Amatus Skincare", "badge": "New"},
                    {"id": "fp4", "name": "Amatus Complex 1 Serum", "price": 95, "category": "Amatus Skincare"},
                    {"id": "fp5", "name": "Amatus Complex Moisturiser", "price": 85, "category": "Amatus Skincare"},
                    {"id": "fp6", "name": "Amatus Gentle 1 Cleanser", "price": 62, "category": "Amatus Skincare"},
                    {"id": "fp7", "name": "Dermalogica Daily Microfoliant", "price": 72, "category": "Dermalogica", "badge": "Clinic Fave"},
                    {"id": "fp8", "name": "Dermalogica AGE Smart Serum", "price": 98, "category": "Dermalogica"},
                    {"id": "fp9", "name": "Dermalogica Skin Smoothing Cream", "price": 65, "category": "Dermalogica"},
                ],
                "note": "Shop is powered by ReeveOS Shop API — products load dynamically from portal.rezvo.app",
            },
        },
    ],
)

# ─── PAGE 6: COURSES ────────────────────────────────────────────────
courses = make_page(
    slug="courses",
    title="Courses",
    seo_title="Beauty Training Courses | Rejuvenate Skin Academy, Cardiff",
    seo_desc="ABT accredited microneedling, dermaplaning, chemical peel, and nail courses. Hands-on training in Cardiff.",
    excerpt="ABT accredited training courses.",
    order=5,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Rejuvenate Academy",
                "subheading": "ABT Accredited Training Courses",
            },
        },
        {
            "type": "CourseList",
            "props": {
                "courses": [
                    {"name": "Microneedling Training", "price": "£250+", "duration": "1 Day", "level": "Intermediate", "badge": "ABT Accredited", "description": "Hands-on microneedling covering skin analysis, needle depth, treatment protocols, aftercare, and contraindications."},
                    {"name": "Dermaplaning Course", "price": "£249", "duration": "1 Day", "level": "Entry Level", "badge": "CPD Certified", "description": "Master surgical scalpel exfoliation. Safely remove vellus hair and dead skin cells."},
                    {"name": "Chemical Face Peel Course", "price": "£249", "duration": "1 Day", "level": "Intermediate", "badge": "CPD Certified", "description": "AHAs, BHAs, combination peels — theory, selection, application, and aftercare."},
                    {"name": "Facial Course", "price": "£219", "duration": "1 Day", "level": "Entry Level", "badge": "Foundation", "description": "Skin analysis, face mapping, cleansing, facial massage, masking, product selection."},
                    {"name": "Nail Course Package", "price": "£549", "duration": "3 Days", "level": "Beginner", "badge": "ABT Accredited", "description": "Complete nail qualification. Manicure, gel, acrylic, and extensions."},
                ],
            },
        },
    ],
)

# ─── PAGE 7: ABOUT ──────────────────────────────────────────────────
about = make_page(
    slug="about",
    title="About",
    seo_title="Meet Natalie | Rejuvenate Skin Experts, Cardiff",
    seo_desc="17 years of skin expertise. Internationally trained, ABT-accredited. Meet Natalie Price and the Rejuvenate team.",
    excerpt="Finally, a skin specialist who actually listens.",
    order=6,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Finally, a Skin Specialist Who Actually Listens",
                "backgroundImage": "/images/hero-about.jpg",
            },
        },
        {
            "type": "TeamProfile",
            "props": {
                "name": "Natalie Price",
                "role": "Founder & Lead Skin Specialist",
                "bio": "With 17 years of industry experience and international training in lymphatic drainage and advanced microneedling techniques, Natalie founded Rejuvenate with one mission: to deliver extraordinary skin results through a combination of clinical science and holistic healing.",
                "image": "/images/natalie-profile.jpg",
                "credentials": ["ABT Accredited", "Internationally Trained", "Dermalogica Partner", "17+ Years Experience"],
            },
        },
        {
            "type": "Timeline",
            "props": {
                "heading": "Our Journey",
                "events": [
                    {"year": "2012", "event": "Introduced microneedling — one of the first clinics in Wales."},
                    {"year": "2016", "event": "Natalie travels internationally to study lymphatic drainage under world-leading practitioners."},
                    {"year": "2021", "event": "Opened the training academy. First cohort trained in Natalie's techniques."},
                    {"year": "2024", "event": "400+ five-star reviews. Named Cardiff's most-reviewed skin clinic."},
                    {"year": "2025", "event": "Official Dermalogica partner. Introduced RF Microneedling and Exosome therapy."},
                ],
            },
        },
        {
            "type": "CTA",
            "props": {
                "heading": "Start Your Journey With Us",
                "buttonText": "Book a Consultation",
                "buttonUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
            },
        },
    ],
)

# ─── PAGE 8: BLOG ───────────────────────────────────────────────────
blog = make_page(
    slug="blog",
    title="Blog",
    seo_title="Skin Journal | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Expert skin advice, treatment guides, and industry insights from Rejuvenate Skin Experts.",
    excerpt="Expert skin advice and treatment insights.",
    order=7,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "The Skin Journal",
                "subheading": "Expert advice. Real science. No fluff.",
            },
        },
        {
            "type": "BlogList",
            "props": {
                "posts": [
                    {"title": "The Truth About Sensitive Skin: What Your Therapist Wants You to Know", "slug": "sensitive-skin-truth", "excerpt": "Sensitive skin is one of the most misunderstood conditions in beauty."},
                    {"title": "AI Skin Consultation in Cardiff: Is It Worth It?", "slug": "ai-skin-consultation", "excerpt": "What the Zemits AI Skin Scanner actually analyses and why it's changing treatment plans."},
                    {"title": "Calm the Flush: How RF Microneedling is Changing Rosacea Treatment", "slug": "rosacea-rf-microneedling", "excerpt": "Rosacea used to be considered unresponsive. RF microneedling is rewriting that story."},
                    {"title": "Why Microneedling Is the Best Treatment for Acne Scarring", "slug": "microneedling-acne-scarring", "excerpt": "The science of controlled trauma, and why it outperforms lasers and peels."},
                    {"title": "Glow From the Inside Out: The Power of Lymphatic Drainage", "slug": "lymphatic-drainage-glow", "excerpt": "The lymphatic system is your body's drainage network — and most of us never think about it."},
                ],
            },
        },
    ],
)

# ─── PAGE 9: CONTACT ────────────────────────────────────────────────
contact = make_page(
    slug="contact",
    title="Contact",
    seo_title="Contact Us | Rejuvenate Skin Experts, Cardiff",
    seo_desc="Get in touch with Rejuvenate Skin Experts. Based in Barry, near Cardiff. Book online or call us.",
    excerpt="Get in touch.",
    order=8,
    blocks=[
        {
            "type": "Hero",
            "props": {
                "heading": "Get in Touch",
                "subheading": "We'd love to hear from you.",
            },
        },
        {
            "type": "ContactInfo",
            "props": {
                "address": "Barry, near Cardiff, South Wales",
                "phone": "07XXX XXXXXX",
                "email": "hello@rejuvenatecardiff.co.uk",
                "hours": {
                    "Monday": "Closed",
                    "Tuesday": "9am – 6pm",
                    "Wednesday": "9am – 6pm",
                    "Thursday": "9am – 8pm",
                    "Friday": "9am – 6pm",
                    "Saturday": "9am – 4pm",
                    "Sunday": "Closed",
                },
                "bookingUrl": "https://portal.rezvo.app/book/rejuvenate-skin-experts",
            },
        },
        {
            "type": "ContactForm",
            "props": {
                "fields": ["name", "email", "phone", "message"],
                "submitText": "Send Message",
            },
        },
        {
            "type": "Map",
            "props": {
                "location": "Rejuvenate Skin Experts, Barry, Cardiff",
            },
        },
    ],
)

# ─── INSERT ALL PAGES ────────────────────────────────────────────────
all_pages = [home, treatments, packages, results, shop, courses, about, blog, contact]
result = db.pages.insert_many(all_pages)
print(f"\n✓ {len(result.inserted_ids)} pages seeded:")
for p in all_pages:
    block_count = len(p["puckData"]["content"])
    print(f"  {p['title']:20s}  /{p['slug']:20s}  {block_count} blocks  [{p['status']}]")

# ─── VERIFY ──────────────────────────────────────────────────────────
print(f"\n✓ Tenant count:  {db.tenants.count_documents({})}")
print(f"✓ Page count:    {db.pages.count_documents({})}")
print(f"\n✓ Rejuvenate Skin Experts — 9 pages seeded into {DB_NAME}")
print(f"  Subdomain: rejuvenate-skin-experts.reeveos.site")
print(f"  Shop API:  portal.rezvo.app/api/shop/public/rejuvenate-skin-experts/products")
print(f"\nDone.")
