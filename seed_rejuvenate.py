#!/usr/bin/env python3
"""
Seed Rejuvenate Skin Experts into Payload CMS (reeveos_cms database).
Creates: 1 tenant + 4 pages with Puck JSON content.
Run on VPS: python3 /opt/reeveos-cms/seed_rejuvenate.py
"""
from pymongo import MongoClient
from datetime import datetime, timezone
from bson import ObjectId

DB_URI = "mongodb://127.0.0.1:27017"
DB_NAME = "reeveos_cms"

client = MongoClient(DB_URI)
db = client[DB_NAME]

# ═══════════════════════════════════════
# IDs (fixed so we can reference them)
# ═══════════════════════════════════════
TENANT_ID = ObjectId("660000000000000000000001")
PAGE_HOME_ID = ObjectId("660000000000000000000010")
PAGE_BLUE_ID = ObjectId("660000000000000000000011")
PAGE_RED_ID = ObjectId("660000000000000000000012")
PAGE_YELLOW_ID = ObjectId("660000000000000000000013")

now = datetime.now(timezone.utc)

# ═══════════════════════════════════════
# HELPER: Puck block builders
# ═══════════════════════════════════════
def hero_block(eyebrow, heading, subheading, cta_text, cta_url, bg_color="#2C3E2D"):
    return {
        "type": "Hero",
        "props": {
            "eyebrow": eyebrow,
            "heading": heading,
            "subheading": subheading,
            "ctaText": cta_text,
            "ctaUrl": cta_url,
            "bgColor": bg_color,
            "textColor": "#FAF7F2",
            "alignment": "center",
            "paddingY": "large",
        }
    }

def text_block(heading, body, alignment="left"):
    return {
        "type": "TextBlock",
        "props": {
            "heading": heading,
            "body": body,
            "alignment": alignment,
            "paddingY": "medium",
        }
    }

def cards_block(heading, cards, bg_color="#FFFFFF"):
    return {
        "type": "Cards",
        "props": {
            "heading": heading,
            "bgColor": bg_color,
            "cards": cards,
            "paddingY": "large",
        }
    }

def testimonials_block(heading, testimonials, bg_color="#FAF7F2"):
    return {
        "type": "Testimonials",
        "props": {
            "heading": heading,
            "bgColor": bg_color,
            "testimonials": testimonials,
            "paddingY": "large",
        }
    }

def cta_block(heading, subheading, cta_text, cta_url, bg_color="#2C3E2D"):
    return {
        "type": "CTA",
        "props": {
            "heading": heading,
            "subheading": subheading,
            "ctaText": cta_text,
            "ctaUrl": cta_url,
            "bgColor": bg_color,
            "textColor": "#FAF7F2",
            "paddingY": "large",
        }
    }

def services_block(heading, services):
    return {
        "type": "ServiceList",
        "props": {
            "heading": heading,
            "services": services,
            "paddingY": "large",
        }
    }

def team_block(heading, members):
    return {
        "type": "TeamGrid",
        "props": {
            "heading": heading,
            "members": members,
            "paddingY": "large",
        }
    }

def faq_block(heading, faqs):
    return {
        "type": "FAQ",
        "props": {
            "heading": heading,
            "faqs": faqs,
            "paddingY": "large",
        }
    }

def results_block(heading, cases):
    return {
        "type": "BeforeAfter",
        "props": {
            "heading": heading,
            "cases": cases,
            "paddingY": "large",
        }
    }

def journey_block(heading, steps):
    return {
        "type": "Journey",
        "props": {
            "heading": heading,
            "steps": steps,
            "paddingY": "large",
        }
    }

def contact_block(heading, subheading, bg_color="#2C3E2D"):
    return {
        "type": "ContactMap",
        "props": {
            "heading": heading,
            "subheading": subheading,
            "address": "Cardiff Bay, South Wales",
            "phone": "",
            "email": "",
            "bgColor": bg_color,
            "paddingY": "large",
        }
    }

# ═══════════════════════════════════════
# TENANT: Rejuvenate Skin Experts
# ═══════════════════════════════════════
tenant = {
    "_id": TENANT_ID,
    "name": "Rejuvenate Skin Experts",
    "businessId": "rejuvenate-natalie", # Will be replaced with actual business _id from reeveos_app
    "subdomain": "rejuvenate-skin-experts",
    "customDomains": [],
    "brand": {
        "primaryColor": "#2C3E2D",
        "secondaryColor": "#C4A265",
        "accentColor": "#FAF7F2",
        "fontHeading": "Cormorant Garamond",
        "fontBody": "DM Sans",
        "logo": None,
        "favicon": None,
        "buttonStyle": "pill",
    },
    "navigation": [
        {"label": "Home", "slug": "home", "visible": True, "order": 0},
        {"label": "Book a Facial", "slug": "book-a-facial", "visible": True, "order": 1},
        {"label": "Results", "slug": "results", "visible": True, "order": 2},
        {"label": "Meet Natalie", "slug": "meet-natalie", "visible": True, "order": 3},
    ],
    "footer": {
        "businessName": "Rejuvenate Skin Experts",
        "tagline": "Cardiff's Most-Reviewed Skin Clinic",
        "address": "Cardiff Bay, South Wales",
        "phone": "",
        "email": "",
        "social": {
            "instagram": "rejuvenateskinexperts",
            "facebook": "",
            "tiktok": "",
            "twitter": "",
        },
    },
    "integrations": {
        "ga4Id": "",
        "metaPixelId": "",
        "tiktokPixelId": "",
        "whatsappNumber": "",
        "instagramHandle": "rejuvenateskinexperts",
        "googleReviewUrl": "",
    },
    "seoDefaults": {
        "titleSuffix": " | Rejuvenate Skin Experts Cardiff",
        "defaultOgImage": None,
    },
    "tier": "growth",
    "createdAt": now,
    "updatedAt": now,
}

# ═══════════════════════════════════════
# PAGE 1: HOME (index.html)
# ═══════════════════════════════════════
home_puck = {
    "content": [
        hero_block(
            eyebrow="Cardiff Bay · Est. 2008",
            heading="Cardiff's Most-Reviewed Skin Clinic. Your Move.",
            subheading="Results-driven skincare backed by 17 years of expertise. Whether you know exactly what you want or need guidance — we've got you.",
            cta_text="Book Now",
            cta_url="/book",
        ),
        cards_block(
            heading="Your Gateway to Great Skin",
            cards=[
                {
                    "heading": "Book a Facial. Feel Amazing Tonight.",
                    "body": "You've had a long week. You want glowing skin and an hour of bliss. No consultation needed — just pick a time and we'll do the rest.",
                    "ctaText": "Book Now — From £115",
                    "ctaUrl": "/book-a-facial",
                    "icon": "sparkle",
                },
                {
                    "heading": "Clear, Confident Skin. See the Proof.",
                    "body": "You've tried everything. Products, other clinics, home remedies. You want to see real results and understand the plan before committing.",
                    "ctaText": "See Results & Packages",
                    "ctaUrl": "/results",
                    "icon": "star",
                },
                {
                    "heading": "Meet Natalie. Get Honest Advice.",
                    "body": "You want to know who's treating your skin before you commit. Book a virtual chat or an AI skin scan — no obligation, ever.",
                    "ctaText": "Chat with Natalie",
                    "ctaUrl": "/meet-natalie",
                    "icon": "heart",
                },
            ],
        ),
        testimonials_block(
            heading="What Our Clients Say",
            testimonials=[
                {"quote": "Absolutely hands down the best facial I have ever had. My skin looks incredible.", "name": "Sian", "rating": 5},
                {"quote": "Natalie is a magician. I've never felt so confident in my own skin.", "name": "Katie", "rating": 5},
                {"quote": "I've spent hundreds on skincare that did nothing. One session here changed everything.", "name": "Grace", "rating": 5},
            ],
        ),
        cta_block(
            heading="Ready to Transform Your Skin?",
            subheading="Takes 30 seconds to book · Cardiff Bay · Klarna available",
            cta_text="Book Your Consultation",
            cta_url="/book",
        ),
    ],
    "root": {"props": {}},
}

page_home = {
    "_id": PAGE_HOME_ID,
    "tenant": TENANT_ID,
    "title": "Home",
    "slug": "home",
    "puckData": home_puck,
    "status": "published",
    "publishedAt": now,
    "excerpt": "Cardiff's most-reviewed skin clinic. Results-driven skincare backed by 17 years of expertise.",
    "pageType": "landing",
    "sortOrder": 0,
    "showInNav": True,
    "meta": {
        "title": "Rejuvenate Skin Experts | Cardiff's Premier Skin Clinic",
        "description": "Expert skin treatments in Barry, Cardiff. Microneedling, chemical peels, RF needling and more. 5.0★ from 418+ reviews. Book your consultation today.",
    },
    "createdAt": now,
    "updatedAt": now,
}

# ═══════════════════════════════════════
# PAGE 2: BOOK A FACIAL (blue.html)
# ═══════════════════════════════════════
blue_puck = {
    "content": [
        hero_block(
            eyebrow="Instant booking · No consultation needed",
            heading="Your Skin Reset Is 60 Minutes Away.",
            subheading="Long week? Treat yourself. Our luxury lymphatic facial leaves you glowing, lifted and completely reset.",
            cta_text="Book Now — Pick Your Time",
            cta_url="/book",
        ),
        services_block(
            heading="Three Ways to Glow",
            services=[
                {
                    "name": "Luxury Lymphatic Lift",
                    "description": "Instant glow. Breathwork, ozone steaming, therapeutic drainage. The one everyone rebooks.",
                    "price": "From £115",
                    "duration": "45 min",
                    "ctaUrl": "/book",
                },
                {
                    "name": "Microneedling Facial",
                    "description": "Precision renewal for scarring, pigmentation and fine lines. Visible change from session one.",
                    "price": "From £165",
                    "duration": "60 min",
                    "ctaUrl": "/book",
                },
                {
                    "name": "RF Microneedling",
                    "description": "Gold-tipped radiofrequency for deep tightening. Results improve for months after.",
                    "price": "From £295",
                    "duration": "75 min",
                    "ctaUrl": "/book",
                },
            ],
        ),
        testimonials_block(
            heading="Don't Take Our Word For It",
            testimonials=[
                {"quote": "I genuinely cannot stop touching my face. The best facial I've ever had.", "name": "Sarah", "rating": 5},
                {"quote": "Rebooked before I even left. Absolutely incredible experience.", "name": "Emma", "rating": 5},
            ],
        ),
        cta_block(
            heading="Stop Scrolling. Start Glowing.",
            subheading="Takes 30 seconds to book · Cardiff Bay · Klarna available",
            cta_text="Book Now",
            cta_url="/book",
        ),
    ],
    "root": {"props": {}},
}

page_blue = {
    "_id": PAGE_BLUE_ID,
    "tenant": TENANT_ID,
    "title": "Book a Facial",
    "slug": "book-a-facial",
    "puckData": blue_puck,
    "status": "published",
    "publishedAt": now,
    "excerpt": "Your skin reset is 60 minutes away. Luxury lymphatic facials, microneedling and RF treatments in Cardiff Bay.",
    "pageType": "landing",
    "sortOrder": 1,
    "showInNav": True,
    "meta": {
        "title": "Book a Facial | Rejuvenate Skin Experts Cardiff",
        "description": "Luxury lymphatic facials from £115. Microneedling & RF treatments. No consultation needed — book online 24/7. Cardiff Bay.",
    },
    "createdAt": now,
    "updatedAt": now,
}

# ═══════════════════════════════════════
# PAGE 3: RESULTS (red.html)
# ═══════════════════════════════════════
red_puck = {
    "content": [
        hero_block(
            eyebrow="Cardiff Bay · 5.0 ★ · 418+ Reviews",
            heading="Clear, Confident Skin in as Little as 3 Treatments",
            subheading="Tired of spending hundreds on products that don't work? Our unique combination of clinical microneedling and therapeutic repair delivers visible results from session one.",
            cta_text="Book Free Assessment",
            cta_url="/book",
        ),
        text_block(
            heading="You've Tried Everything. Your Skin Still Won't Cooperate.",
            body="You're not lazy. You're not doing it wrong. You've just never had the right combination of treatments working together. Most treatments trigger change but leave skin to heal alone. Our approach pairs clinical microneedling with deep therapeutic repair — so your skin doesn't just react, it rebuilds.",
            alignment="center",
        ),
        results_block(
            heading="Proof, Not Promises — Real Results",
            cases=[
                {"name": "Sian", "condition": "Active Acne Scarring", "treatments": "6 treatments · 20 weeks"},
                {"name": "Katie", "condition": "Rosacea & Congestion", "treatments": "8 treatments · 20 weeks"},
                {"name": "Grace", "condition": "Hormonal Acne", "treatments": "3 treatments · 10 weeks"},
            ],
        ),
        services_block(
            heading="Three Treatments. One Goal: Skin You Love.",
            services=[
                {
                    "name": "Walk Out Glowing From Session One",
                    "description": "Breathwork, ozone steaming and therapeutic drainage. Reduces puffiness and inflammation instantly.",
                    "price": "From £115",
                    "duration": "45 min",
                    "ctaUrl": "/book",
                },
                {
                    "name": "Erase Scars and Pigmentation for Good",
                    "description": "Precision microneedling triggers your skin's own repair. Acne scarring, pigmentation and fine lines fade with each session.",
                    "price": "From £165",
                    "duration": "60 min",
                    "ctaUrl": "/book",
                },
                {
                    "name": "Tighter Skin — No Surgery, No Downtime",
                    "description": "Gold-tipped radiofrequency triggers deep collagen remodelling. Your skin continues tightening for months after.",
                    "price": "From £295",
                    "duration": "75 min",
                    "ctaUrl": "/book",
                },
            ],
        ),
        cards_block(
            heading="The 18-Week Skin Transformation",
            cards=[
                {"heading": "6 × Microneedling Facials", "body": "1 hour each with LED Light Therapy (Red/Blue/Yellow)", "icon": "sparkle"},
                {"heading": "Dermaplaning Every Session", "body": "Smooth canvas for deeper product penetration", "icon": "star"},
                {"heading": "Full-Size Peeliever Kit", "body": "Targeted boosters and home care included", "icon": "heart"},
            ],
            bg_color="#FAF7F2",
        ),
        faq_block(
            heading="Everything You Need to Know",
            faqs=[
                {"q": "Does microneedling hurt?", "a": "Most clients describe it as a mild tingling. We apply numbing cream 20 minutes before so you're completely comfortable."},
                {"q": "How many treatments will I need?", "a": "Most clients see visible results after 1–3 sessions. For deeper concerns like scarring, we typically recommend 6–8 treatments over 18–20 weeks."},
                {"q": "What's the downtime?", "a": "You'll be pink for 24–48 hours, similar to mild sunburn. Most clients return to normal activities the next day."},
                {"q": "Is it safe for all skin types?", "a": "Yes. Natalie personally assesses every client and adjusts needle depth, speed and serums to your exact skin type."},
            ],
        ),
        cta_block(
            heading="Stop Hiding Your Skin. Start Showing It Off.",
            subheading="Book a free skin assessment with Natalie — no obligation, no hard sell.",
            cta_text="Book Free Assessment",
            cta_url="/book",
        ),
    ],
    "root": {"props": {}},
}

page_red = {
    "_id": PAGE_RED_ID,
    "tenant": TENANT_ID,
    "title": "Results & Treatments",
    "slug": "results",
    "puckData": red_puck,
    "status": "published",
    "publishedAt": now,
    "excerpt": "Clear, confident skin in as little as 3 treatments. See real before & after results from our Cardiff clinic.",
    "pageType": "landing",
    "sortOrder": 2,
    "showInNav": True,
    "meta": {
        "title": "Clear Skin in 3 Treatments | Rejuvenate Skin Experts Cardiff",
        "description": "Microneedling, RF treatments & skin transformation packages. Real before & after results. Free skin assessment available. Cardiff Bay.",
    },
    "createdAt": now,
    "updatedAt": now,
}

# ═══════════════════════════════════════
# PAGE 4: MEET NATALIE (yellow.html)
# ═══════════════════════════════════════
yellow_puck = {
    "content": [
        hero_block(
            eyebrow="Cardiff Bay · Est. 2008",
            heading="Finally, a Skin Specialist Who Actually Listens",
            subheading="No cookie-cutter protocols. No upselling. Just Natalie — 17 years of clinical expertise, a genuine obsession with skin science, and a clinic built around you.",
            cta_text="Chat with Natalie",
            cta_url="/book",
        ),
        testimonials_block(
            heading="They Came for a Treatment. They Stayed for Her.",
            testimonials=[
                {"quote": "Natalie is a magician. I've never felt so confident in my own skin.", "name": "Katie", "rating": 5},
                {"quote": "She actually listens. Not just to what you want, but what your skin needs.", "name": "Sian", "rating": 5},
                {"quote": "I was so nervous. Natalie made me feel like I was talking to a friend, not a clinician.", "name": "Grace", "rating": 5},
            ],
        ),
        text_block(
            heading="Why Natalie Started Rejuvenate — and Why It's Different",
            body="I started this clinic because I believed in the science of controlled renewal. But the more I worked with clients, the more I realised: great skin isn't just about the right machine or the right serum. It's about someone who actually listens. I travelled internationally to study lymphatic drainage with masters of the technique. I realised microneedling alone wasn't enough — your skin needs therapeutic support to truly heal. Today, I don't follow cookie-cutter protocols. I don't upsell. I assess YOUR skin, create YOUR plan, and adjust every single session based on how YOUR skin responds.",
        ),
        journey_block(
            heading="What Happens When You Get in Touch",
            steps=[
                {"step": "1", "title": "Have a Chat", "body": "Book a virtual call or visit the clinic. Natalie personally assesses your skin and listens to your goals."},
                {"step": "2", "title": "Get Your Plan", "body": "A personalised treatment plan built around your skin, your goals and your budget. No pressure."},
                {"step": "3", "title": "Start Your Treatments", "body": "Your first session includes extra time so we get to know you properly. Every session is adjusted to how your skin responds."},
                {"step": "4", "title": "Join the Family", "body": "You're not just a client — you're part of the Rejuvenate community. Ongoing support, check-ins and honest advice."},
            ],
        ),
        results_block(
            heading="Every Face Has a Story",
            cases=[
                {"name": "Sian", "condition": "Acne Scarring", "treatments": "6 treatments"},
                {"name": "Katie", "condition": "Rosacea", "treatments": "8 treatments"},
                {"name": "Grace", "condition": "Hormonal Acne", "treatments": "3 treatments"},
                {"name": "Sophie", "condition": "Pigmentation", "treatments": "4 treatments"},
            ],
        ),
        cta_block(
            heading="Your Skin Deserves Someone Who Actually Cares",
            subheading="Book a 15-minute virtual chat or an in-person consultation. No obligation, no hard sell — just Natalie.",
            cta_text="Chat with Natalie",
            cta_url="/book",
        ),
    ],
    "root": {"props": {}},
}

page_yellow = {
    "_id": PAGE_YELLOW_ID,
    "tenant": TENANT_ID,
    "title": "Meet Natalie",
    "slug": "meet-natalie",
    "puckData": yellow_puck,
    "status": "published",
    "publishedAt": now,
    "excerpt": "Meet Natalie Price — 17 years of clinical expertise and a genuine obsession with skin science. Book a free consultation.",
    "pageType": "landing",
    "sortOrder": 3,
    "showInNav": True,
    "meta": {
        "title": "Meet Natalie | Rejuvenate Skin Experts Cardiff",
        "description": "17 years of expertise. 418+ five-star reviews. Meet the skin specialist who actually listens. Free virtual consultation available.",
    },
    "createdAt": now,
    "updatedAt": now,
}

# ═══════════════════════════════════════
# SEED IT
# ═══════════════════════════════════════
def seed():
    print("=" * 50)
    print("  Seeding Rejuvenate into reeveos_cms")
    print("=" * 50)

    # Clear existing Rejuvenate data (idempotent)
    db.tenants.delete_many({"subdomain": "rejuvenate-skin-experts"})
    db.pages.delete_many({"tenant": TENANT_ID})
    print("✓ Cleared existing Rejuvenate data")

    # Insert tenant
    db.tenants.insert_one(tenant)
    print(f"✓ Tenant created: {tenant['name']} (ID: {TENANT_ID})")

    # Insert pages
    for page in [page_home, page_blue, page_red, page_yellow]:
        db.pages.insert_one(page)
        print(f"✓ Page created: {page['title']} (/{page['slug']})")

    # Create index
    try:
        db.pages.create_index([("tenant", 1), ("slug", 1)], unique=True)
        print("✓ Index created: tenant + slug (unique)")
    except Exception:
        print("✓ Index already exists")

    print()
    print("=" * 50)
    print(f"  Done! Rejuvenate has {db.pages.count_documents({'tenant': TENANT_ID})} pages")
    print(f"  Subdomain: rejuvenate-skin-experts.reeveos.site")
    print("=" * 50)

    # Verify
    print("\nVerification:")
    for p in db.pages.find({"tenant": TENANT_ID}).sort("sortOrder", 1):
        blocks = len(p.get("puckData", {}).get("content", []))
        print(f"  /{p['slug']:20s} — {p['title']:20s} — {blocks} blocks — {p['status']}")

if __name__ == "__main__":
    seed()
