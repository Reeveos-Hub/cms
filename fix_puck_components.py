#!/usr/bin/env python3
"""
Fix Puck Component Names
========================
Updates seeded page data to use actual Puck component types
registered in WebsiteBuilder.jsx.
"""
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["reeveos_cms"]

def hero_block(heading, subheading="", buttonText="", buttonUrl="#", bgColor="#2C3E2D"):
    return {"type": "HeroBanner", "props": {
        "heading": heading, "subheading": subheading,
        "buttonText": buttonText, "buttonUrl": buttonUrl,
        "bgImage": "", "bgColor": bgColor, "overlayOpacity": "0",
        "minHeight": "400px", "textColor": "#ffffff",
    }}

def heading_block(text, level=2, color="#2C3E2D"):
    return {"type": "Heading", "props": {"text": text, "level": str(level), "align": "center", "color": color}}

def text_block(text, align="center", color="#333"):
    return {"type": "TextBlock", "props": {"text": text, "align": align, "color": color, "fontSize": "1rem"}}

def button_block(text, url, style="primary"):
    return {"type": "Button", "props": {"text": text, "url": url, "style": style, "size": "large", "align": "center"}}

def service_card(title, description, price, duration="", image=""):
    return {"type": "ServiceCard", "props": {"title": title, "description": description, "price": price, "duration": duration, "image": image}}

def testimonial(quote, author, role="Verified Client", rating="5"):
    return {"type": "Testimonial", "props": {"quote": quote, "author": author, "role": role, "rating": rating}}

def team_member(name, role, bio, image=""):
    return {"type": "TeamMember", "props": {"name": name, "role": role, "bio": bio, "image": image}}

def section(children_desc, bgColor="#FAF7F2"):
    return {"type": "Section", "props": {"bgColor": bgColor, "padding": "48px 24px", "maxWidth": "1200px"}}

def contact_form():
    return {"type": "ContactForm", "props": {"heading": "Send Us a Message", "fields": "name,email,phone,message", "submitText": "Send Message", "successMessage": "Thanks! We'll be in touch shortly."}}

def map_block(address):
    return {"type": "Map", "props": {"address": address, "height": "400px", "zoom": "15"}}

def opening_hours(title="Opening Hours"):
    return {"type": "OpeningHours", "props": {
        "title": title,
        "hours": "Monday: Closed\nTuesday: 9am – 6pm\nWednesday: 9am – 6pm\nThursday: 9am – 8pm\nFriday: 9am – 6pm\nSaturday: 9am – 4pm\nSunday: Closed"
    }}

def spacer(height="32px"):
    return {"type": "Spacer", "props": {"height": height}}

# ─── PAGE CONTENT (using real Puck components) ───────────────────────

pages_data = {
    "home": [
        hero_block("Cardiff's Most-Reviewed Skin Clinic.", "Your Move.", "Book a Consultation", "https://portal.rezvo.app/book/rejuvenate-skin-experts"),
        spacer(),
        heading_block("Why Rejuvenate?", 2),
        text_block("17+ years experience · 418+ five-star reviews · 5.0 average rating · Dermalogica Partner"),
        spacer(),
        heading_block("What Our Clients Say", 2),
        testimonial("Best facial I've ever had. Natalie really knows skin.", "Sarah M."),
        spacer("16px"),
        testimonial("My acne scarring has genuinely transformed after 4 sessions.", "Rachel D."),
        spacer("16px"),
        testimonial("The clinic is gorgeous and the results speak for themselves.", "Emma L."),
        spacer(),
        hero_block("Ready to Start Your Skin Journey?", "Book your consultation today.", "Book Now", "https://portal.rezvo.app/book/rejuvenate-skin-experts", "#C4A265"),
    ],
    "treatments": [
        hero_block("Our Treatments", "Science-led. Results-proven."),
        spacer(),
        service_card("Luxury Lymphatic Lift Facial", "Breathwork, ozone steaming, and therapeutic lymphatic drainage massage. Instant lifted, glowing complexion.", "From £165", "75 min"),
        spacer("16px"),
        service_card("Microneedling Facial", "Precision microneedling creates controlled micro-channels. Gold standard for skin correction.", "From £165", "60 min"),
        spacer("16px"),
        service_card("Microneedling with Exosomes", "Exosome boosters delivered directly into the dermis via microneedling channels.", "£315", "75 min"),
        spacer("16px"),
        service_card("RF Microneedling (Face)", "Radiofrequency energy via gold-tipped microneedles. Dramatic skin tightening.", "From £295", "90 min"),
        spacer("16px"),
        service_card("RF Microneedling (Body)", "RF microneedling for body areas. Stretch marks, loose skin, deep collagen remodelling.", "£295", "90 min"),
        spacer("16px"),
        service_card("Ultimate Skin Rejuvenation Ritual", "The complete experience. Microneedling, exosomes, LED, lymphatic drainage in one session.", "From £330", "120 min"),
        spacer("16px"),
        service_card("Chemical Face Peel", "Professional-grade AHA and BHA peels tailored to your skin concern.", "From £100", "45–60 min"),
        spacer("16px"),
        service_card("The Quick Fix Glow Up", "Express lymphatic facial for instant radiance. Perfect pre-event.", "£115", "45 min"),
        spacer("16px"),
        service_card("AI Skin Consultation", "Zemits AI Skin Scanner analyses 12 skin concerns. £40 redeemable against first treatment.", "£80", "60 min"),
        spacer("16px"),
        service_card("Exosome Hair Restoration", "Exosomes delivered into the scalp to stimulate dormant follicles and promote regrowth.", "From £300", "60 min"),
        spacer(),
        hero_block("Not Sure Which Treatment?", "Start with an AI Skin Consultation — £40 redeemable.", "Book a Consultation", "https://portal.rezvo.app/book/rejuvenate-skin-experts", "#C4A265"),
    ],
    "packages": [
        hero_block("Treatment Packages", "Commit to the journey. Transform the result."),
        spacer(),
        service_card("18-Week Intensive Correction Plan", "The complete skin transformation. 6 × Microneedling Facials, customised homecare plan, progress photography. Klarna & Clearpay available.", "£990", "18 weeks"),
        spacer("16px"),
        service_card("Lymphatic Correction Package", "Bespoke lymphatic correction plan with multiple sessions tailored to your skin goals.", "POA", "Bespoke"),
        spacer("16px"),
        service_card("Ultimate Skin Rejuvenation Ritual", "Microneedling with Exosome Boosters, LED Light Therapy, Lymphatic Drainage, Advanced Stayve AC Stem Serums.", "From £330", "Single session"),
        spacer("16px"),
        service_card("The Quick Fix Glow Up", "Express Lymphatic Lift Facial. 45 minutes. Zero downtime.", "£115", "45 min"),
    ],
    "results": [
        hero_block("Clear, Confident Skin in 3 Treatments", "Real results. Real clients. No filters."),
        spacer(),
        heading_block("Client Transformations", 2),
        text_block("Our before & after gallery showcases real transformations from microneedling courses, RF treatments, and chemical peel programmes. Every image is unretouched."),
        spacer(),
        hero_block("Ready for Your Transformation?", "", "Book Now", "https://portal.rezvo.app/book/rejuvenate-skin-experts", "#C4A265"),
    ],
    "shop": [
        hero_block("The Skin Shop", "Clinic-tested. Dermatologist-approved."),
        spacer(),
        heading_block("Amatus Skincare", 2),
        service_card("Amatus Gentle 3-Step Routine", "Cleanser, hydrating serum and moisturiser for sensitive, reactive skin.", "£189", "Bestseller"),
        spacer("16px"),
        service_card("Amatus Complex 3-Step Routine", "Triple-action formula combining RF energy with nano-needling for deeper collagen remodelling.", "£188.95", ""),
        spacer("16px"),
        service_card("Amatus Complex Daily Set", "AM brightening serum with PM repair complex for maximum results.", "£210", "New"),
        spacer(),
        heading_block("Dermalogica", 2),
        service_card("Dermalogica Daily Microfoliant", "Iconic enzyme powder exfoliant. Brightens, smooths and refines skin texture.", "£72", "Clinic Fave"),
        spacer("16px"),
        service_card("Dermalogica AGE Smart Serum", "Peptide-rich anti-ageing serum targeting fine lines, firmness and tone.", "£98", ""),
        spacer("16px"),
        service_card("Dermalogica Skin Smoothing Cream", "Rich moisturiser for dry, dehydrated skin. Strengthens the moisture barrier.", "£65", ""),
    ],
    "courses": [
        hero_block("Rejuvenate Academy", "ABT Accredited Training Courses"),
        spacer(),
        service_card("Microneedling Training", "Hands-on microneedling covering skin analysis, needle depth, treatment protocols, aftercare, and contraindications. ABT Accredited.", "£250+", "1 Day"),
        spacer("16px"),
        service_card("Dermaplaning Course", "Master surgical scalpel exfoliation. Safely remove vellus hair and dead skin cells. CPD Certified.", "£249", "1 Day"),
        spacer("16px"),
        service_card("Chemical Face Peel Course", "AHAs, BHAs, combination peels — theory, selection, application, and aftercare. CPD Certified.", "£249", "1 Day"),
        spacer("16px"),
        service_card("Facial Course", "Skin analysis, face mapping, cleansing, facial massage, masking, product selection. Foundation.", "£219", "1 Day"),
        spacer("16px"),
        service_card("Nail Course Package", "Complete nail qualification. Manicure, gel, acrylic, and extensions. ABT Accredited.", "£549", "3 Days"),
    ],
    "about": [
        hero_block("Finally, a Skin Specialist Who Actually Listens"),
        spacer(),
        team_member("Natalie Price", "Founder & Lead Skin Specialist", "With 17 years of industry experience and international training in lymphatic drainage and advanced microneedling techniques, Natalie founded Rejuvenate with one mission: to deliver extraordinary skin results through a combination of clinical science and holistic healing. ABT-accredited, Dermalogica partner."),
        spacer(),
        heading_block("Our Journey", 2),
        text_block("2012 — Introduced microneedling, one of the first clinics in Wales.\n2016 — Natalie travels internationally to study lymphatic drainage.\n2021 — Opened the training academy.\n2024 — 400+ five-star reviews. Cardiff's most-reviewed skin clinic.\n2025 — Official Dermalogica partner. RF Microneedling and Exosome therapy introduced."),
        spacer(),
        hero_block("Start Your Journey With Us", "", "Book a Consultation", "https://portal.rezvo.app/book/rejuvenate-skin-experts", "#C4A265"),
    ],
    "blog": [
        hero_block("The Skin Journal", "Expert advice. Real science. No fluff."),
        spacer(),
        heading_block("Latest Articles", 2),
        text_block("The Truth About Sensitive Skin: What Your Therapist Wants You to Know — Sensitive skin is one of the most misunderstood conditions in beauty."),
        spacer("16px"),
        text_block("AI Skin Consultation in Cardiff: Is It Worth It? — What the Zemits AI Skin Scanner actually analyses and why it's changing treatment plans."),
        spacer("16px"),
        text_block("Calm the Flush: How RF Microneedling is Changing Rosacea Treatment — RF microneedling is rewriting the rosacea story."),
        spacer("16px"),
        text_block("Why Microneedling Is the Best Treatment for Acne Scarring — The science of controlled trauma, and why it outperforms lasers and peels."),
        spacer("16px"),
        text_block("Glow From the Inside Out: The Power of Lymphatic Drainage — Your body's drainage network deserves attention."),
    ],
    "contact": [
        hero_block("Get in Touch", "We'd love to hear from you."),
        spacer(),
        opening_hours(),
        spacer(),
        text_block("Based in Barry, near Cardiff, South Wales\nhello@rejuvenatecardiff.co.uk"),
        spacer(),
        contact_form(),
        spacer(),
        map_block("Rejuvenate Skin Experts, Barry, Cardiff"),
        spacer(),
        button_block("Book Online", "https://portal.rezvo.app/book/rejuvenate-skin-experts"),
    ],
}

# ─── UPDATE MONGODB ──────────────────────────────────────────────────
print("Updating Puck data to use correct component types...")

for slug, blocks in pages_data.items():
    result = db.pages.update_one(
        {"slug": slug},
        {"$set": {
            "puckData": {"content": blocks, "root": {"props": {}}},
        }},
    )
    status = "✓" if result.modified_count else "⚠ not found"
    print(f"  {status} {slug:20s} → {len(blocks)} blocks")

print(f"\nDone. {len(pages_data)} pages updated.")
