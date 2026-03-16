"""
ReeveOS Blog — Full Category Seed
All articles for all categories on reeveos.app/blog
Run: python3 seed_all_articles.py
"""

import os
from datetime import datetime, timezone
from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(MONGO_URI)
db = client['reeveos_cms']

cats_col = db['blog-categories']
posts_col = db['blog-posts']

def now():
    return datetime.now(timezone.utc)

GOLD = '#C9A84C'

CATEGORIES = [
    {'_id': ObjectId(), 'name': 'Salons & Beauty',    'slug': 'salons',        'site': 'reeveos',  'sortOrder': 1},
    {'_id': ObjectId(), 'name': 'Aesthetics Clinics', 'slug': 'aesthetics',    'site': 'reeveos',  'sortOrder': 2},
    {'_id': ObjectId(), 'name': 'Barbers',            'slug': 'barbers',       'site': 'reeveos',  'sortOrder': 3},
    {'_id': ObjectId(), 'name': 'Gyms & Fitness',     'slug': 'gyms',          'site': 'reeveos',  'sortOrder': 4},
    {'_id': ObjectId(), 'name': 'EPOS & Payments',    'slug': 'epos-payments', 'site': 'reeveos',  'sortOrder': 5},
    {'_id': ObjectId(), 'name': 'Marketing & Growth', 'slug': 'marketing',     'site': 'reeveos',  'sortOrder': 6},
    {'_id': ObjectId(), 'name': 'Booking Guides',     'slug': 'booking-guides','site': 'reevenow', 'sortOrder': 1},
    {'_id': ObjectId(), 'name': 'Best Of',            'slug': 'best-of',       'site': 'reevenow', 'sortOrder': 2},
]

def cat(slug):
    return next(c for c in CATEGORIES if c['slug'] == slug)

def post(slug, title, category_slug, site, content_type, priority,
         keyword, meta_desc, excerpt, content, read_time,
         og_image, feat_image, feat_alt, tags,
         faq_items=None, competitor_name=None, related_tool=None,
         cta_text='Start your free trial', cta_url='https://portal.rezvo.app/register',
         secondary_cta_text=None, secondary_cta_url=None):
    return {
        '_id': ObjectId(),
        'title': title,
        'slug': slug,
        'site': site,
        'category': cat(category_slug)['_id'],
        'status': 'published',
        'publishedAt': now(),
        'lastVerifiedAt': datetime(2026, 3, 16, tzinfo=timezone.utc),
        'contentType': content_type,
        'priority': priority,
        'competitorName': competitor_name,
        'relatedTool': related_tool,
        'seo': {
            'targetKeyword': keyword,
            'metaTitle': title[:60],
            'metaDescription': meta_desc,
            'robotsMeta': 'index,follow',
        },
        'social': {
            'ogTitle': title,
            'ogDescription': meta_desc[:150],
            'ogImageUrl': og_image,
            'twitterCard': 'summary_large_image',
        },
        'featuredImageUrl': feat_image,
        'featuredImageAlt': feat_alt,
        'excerpt': excerpt,
        'content': content,
        'readTime': read_time,
        'tags': tags,
        'schema': {'faqItems': faq_items or [], 'breadcrumbs': []},
        'aiOptimisation': {'directAnswer': '', 'keyFacts': []},
        'eeat': {'authorName': 'ReeveOS Team', 'lastUpdatedNote': 'Verified March 2026'},
        'cta': {'text': cta_text, 'url': cta_url, 'secondaryText': secondary_cta_text, 'secondaryUrl': secondary_cta_url},
        'createdAt': now(),
        'updatedAt': now(),
    }


# ════════════════════════════════════════════════════════════════
# SALONS & BEAUTY
# ════════════════════════════════════════════════════════════════

SALON_1 = post(
    slug='fresha-alternatives-uk-2026',
    title="Fresha alternatives UK 2026: 7 platforms that won't charge 20% on every new client",
    category_slug='salons', site='reeveos',
    content_type='competitor-alternative', priority='p1',
    competitor_name='Fresha', related_tool='fresha-cost-calculator',
    keyword='fresha alternative UK',
    meta_desc="Fresha now charges 20% commission on every new client. Here are 7 UK alternatives that let you keep that money.",
    og_image='https://images.unsplash.com/photo-1560066984-138dadb4c035?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1560066984-138dadb4c035?w=1400&h=700&fit=crop',
    feat_alt='UK hair salon interior with styling chairs',
    tags='fresha, fresha alternative, salon booking software, no commission',
    excerpt="Fresha used to be free. Then in 2025 they started charging 20% commission on every new client. For a busy salon, that adds up fast. Here are 7 alternatives.",
    read_time=8,
    cta_text='Calculate your Fresha costs',
    cta_url='https://reeveos.app/tools/fresha-cost-calculator',
    faq_items=[
        {'question': 'Is Fresha still free in 2026?', 'answer': 'No. Fresha now charges £14.95 per staff member per month, 20% commission on new marketplace bookings, and 1.29%+20p per card transaction.'},
        {'question': 'How much does Fresha cost a UK salon per year?', 'answer': 'A 3-staff salon with 30% new clients and £60 average service typically pays £8,000–£11,000 per year in total Fresha fees.'},
        {'question': 'Can I export my clients from Fresha?', 'answer': 'Yes. Fresha lets you export a CSV of your client data. Import it into any alternative platform — ReeveOS accepts CSV imports as part of setup.'},
    ],
    content="""# Fresha alternatives UK 2026: 7 platforms that won't charge 20% on every new client

Let me tell you a story that a lot of salon owners recognise.

You join Fresha because it's free. Your bookings come in. New clients find you on their app. Life is good. Then one day you get an email. Fresha is changing how they charge. From now on, every new client that books through their platform costs you 20% of that appointment's value.

For a £60 appointment, that's £12 gone before you've said hello.

For a busy salon bringing in 40 new clients a month, that's £480 a month. Nearly £6,000 a year. Just to receive bookings.

This is what happened in 2025. Thousands of UK salon owners are now looking for the exit.

## Why Fresha changed

Fresha built their business by being free. That attracted millions of salons worldwide. Now they need to make that back. The 20% new client commission is how.

The more your business grows, the more you pay Fresha. Think about that. Winning new clients now means handing a fifth of that appointment to a platform.

On top of that: £14.95 per staff member per month. Plus 1.29% plus 20p on every card transaction.

For a 3-person salon: £538 a year in subscriptions, up to £7,200 in new client commission, plus £2,400 in transaction fees. That's potentially £10,000+ a year.

## What to look for in an alternative

**Do you own your client data?** With Fresha, your clients also sit in Fresha's database. They can recommend other salons to your clients. With a true alternative, your clients are yours.

**What is the real total cost?** Add up subscription, transaction fees, and any commission. The sticker price is never the full story.

**Does it handle deposits?** No-shows cost UK salons £1.6 billion a year. Any platform worth using makes deposits easy.

**Is it built for UK businesses?** GDPR compliance, GBP pricing, UK bank integrations, UK customer support — these matter.

## The 7 best Fresha alternatives for UK salons

### 1. ReeveOS — best for zero commission, UK-built

No marketplace. No commission. Your clients book through your branded booking page and you keep 100% of every appointment.

Free plan for solo practitioners. Growth plan at £29/month for up to 5 staff includes deposits, automated reminders, and a full CRM. Aesthetics clinics also get digital consent forms — no other platform at this price includes that.

Card payments through Dojo at 0.3% debit / 0.7% credit — substantially cheaper than Fresha's 1.29% + 20p.

**Pricing:** Free to £149/month. Zero commission.

---

### 2. Booksy — best for barbershops and salons wanting a clean app

Strong brand recognition. Clean booking interface clients know how to use. Per-person pricing adds up for larger teams: £29.99/month base + £20 per additional staff member.

**Pricing:** From £29.99/month.

---

### 3. Timely — best for solo practitioners wanting simple booking

New Zealand company. Clean, simple booking tool. No marketplace, no commission. No built-in consultation forms, no EPOS, limited GDPR features.

**Pricing:** From around £20/month per staff.

---

### 4. Phorest — best for larger salons with 5+ staff

20 years in the industry. Sophisticated marketing and retention features. Expensive for smaller operations — most mid-sized salons pay £100/month or more.

**Pricing:** From ~£99/month.

---

### 5. Treatwell — best for filling last-minute slots via marketplace

Consumer marketplace first, management tool second. High commission (20–30%) and the client relationship sits with Treatwell. Works as a secondary channel for filling gaps, not as a primary system.

**Pricing:** 20–30% commission per marketplace booking.

---

### 6. Square Appointments — best for salons already using Square

Integrates with Square card readers. The 1.75% transaction fee becomes expensive at volume. For a salon doing £15,000/month in card sales, that's £262/month in processing fees alone — £3,150/year. Dojo through ReeveOS on the same volume costs around £50/month.

**Pricing:** Free to £69/month + 1.75% per transaction.

---

### 7. Acuity Scheduling — best for freelancers needing a quick setup

Easiest to get started. Very limited for multi-staff salons. American product with minimal UK compliance features.

**Pricing:** £14 to £45/month.

---

## The honest cost comparison

3-staff salon, £60 average, 40 appointments/week, 30% new clients:

| Platform | Annual subscription | Commission | Processing | Total |
|---|---|---|---|---|
| Fresha | £538 | £4,320–£7,200 | £2,400 | £7,258–£10,138 |
| ReeveOS Growth | £348 | £0 | ~£600 | £948 |
| Booksy (3 staff) | £840 | £0 | separate | £840+ |
| Phorest | £1,188 | £0 | separate | £1,188+ |
| Timely (3 staff) | £720 | £0 | separate | £720+ |

## How to leave Fresha

Export your client list from your Fresha dashboard (Reports → Clients → Export). You get a CSV spreadsheet. Import it into your new platform. Update your Instagram bio, Google Business Profile, and any other booking links. Send your regulars a short message with the new link.

The whole process takes about a week. The saving starts from day one.
""".strip()
)

SALON_2 = post(
    slug='how-to-reduce-no-shows-uk-salon',
    title="How to reduce no-shows at your salon: the two things that cut them by 70%",
    category_slug='salons', site='reeveos',
    content_type='cluster', priority='p1',
    related_tool='no-show-calculator',
    keyword='how to reduce no shows salon UK',
    meta_desc="UK salons lose £1.6 billion to no-shows every year. Two things — a booking fee and automated reminders — cut them by up to 70%.",
    og_image='https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=1400&h=700&fit=crop',
    feat_alt='Empty salon styling chair representing missed appointments',
    tags='no-shows, deposits, booking fees, SMS reminders, cancellation policy',
    excerpt="Every empty chair is money you earned but never received. UK salons lose £1.6 billion to no-shows every year. Two simple things cut that by up to 70%.",
    read_time=7,
    cta_text='Calculate your no-show losses',
    cta_url='https://reeveos.app/tools/no-show-calculator',
    faq_items=[
        {'question': 'Is it legal to charge a booking fee in the UK?', 'answer': 'Yes, completely legal. Clearly state your cancellation policy at booking and use the term "booking fee" rather than "deposit" for clarity.'},
        {'question': 'How much should I charge as a booking fee?', 'answer': 'Most UK salons charge 20–50% of the appointment value. For a £60 appointment, that is £12–£30. Any amount upfront significantly reduces no-shows.'},
        {'question': 'How much do automated reminders reduce no-shows?', 'answer': 'Automated SMS reminders sent 24–48 hours before appointments reduce no-shows by 30–40% on their own. Combined with deposits the reduction is 60–70%.'},
    ],
    content="""# How to reduce no-shows at your salon: the two things that cut them by 70%

Picture this. Tuesday morning. Full day booked. You arrive early, get set up, check the diary. At 10am your first client should be in for a cut and colour. At 10:15 she still isn't there. By 11am you know she isn't coming.

That hour and a half is gone. The product prepared is gone. The client you could have booked in that slot — gone too.

Now imagine that happening once or twice a week, every week, all year.

Across all UK salons, this adds up to £1.6 billion in lost revenue every single year. Not turnover. Actually lost money.

The good news is that this is one of the most fixable problems in your business. And you only need two things.

## Why clients no-show

Different reasons need different solutions.

**They forgot.** The most common reason by far. Life is busy, they booked two weeks ago and it slipped their mind. Easy to solve with a reminder.

**They couldn't be bothered to tell you.** They decided not to come but didn't pick up the phone. This is where a booking fee changes behaviour entirely.

**A genuine emergency.** Illness, family crisis, work disaster. You cannot prevent this one, and most salon owners are happy to rearrange for genuine reasons.

The first two reasons account for the vast majority of no-shows. Both are solvable today.

## Tool 1: Automated SMS reminders

Your booking software sends a text to your client 24 or 48 hours before their appointment. You set it up once. It runs by itself from then on.

The message is simple. "Hi Sarah, just a reminder you have an appointment at [Salon Name] tomorrow at 10am. To rearrange please call us on [number]. See you soon."

This catches the forgetters. It also gives the second group — the ones who were going to no-show — one final chance to cancel with enough notice for you to fill the gap.

Automated reminders alone reduce no-shows by 30–40%.

## Tool 2: Booking fees

The terminology matters. "Deposit" legally implies a payment that may be returned under certain conditions. "Booking fee" is clearer — it secures your slot, it is non-refundable if you don't give proper notice. Using the right words protects you if a client ever disputes.

A booking fee is typically 20–50% of the appointment value. For a £60 appointment that's £12–£30. Clients pay when they book online and it comes off the final bill when they arrive.

The psychology is powerful. When someone has paid £20 to book, they are invested. They have a reason to show up. And if they genuinely cannot make it, they are much more likely to call and rearrange because they want the fee transferred, not lost.

Booking fees reduce no-shows by 55–70%.

Combined with automated reminders, salons routinely see 60–70% reductions in no-shows.

## What does a no-show actually cost you?

Say you run a 2-person salon, each doing 8 appointments a day at £55 average. With a 15% no-show rate — roughly average without any protection — that's around 11–12 missed appointments per week.

At £55 average, that's £600–£660 in missed revenue every week. Nearly £32,000 a year.

Solving even half of those with deposits and reminders returns £16,000 per year.

Use our free no-show calculator to put your own numbers in.

## How to introduce booking fees without upsetting regulars

The worry most owners have: "My regulars will hate it."

In practice, regular clients almost always accept booking fees when you explain them properly. They understand the business.

Send regulars a short message before you switch it on: "We're introducing a small booking fee from [date] to protect your appointments. It comes off your bill when you arrive — no change to what you pay overall, just a small deposit upfront."

The clients who react angrily are often the same clients most likely to no-show. You haven't lost a good client. You've protected yourself from a difficult one.

## Your cancellation policy wording

Use this as a starting point:

*"A non-refundable booking fee is required to secure all appointments. This will be deducted from your final bill. Cancellations with less than 24 hours' notice forfeit the booking fee. We understand emergencies happen — please contact us as early as possible and we will always do our best to accommodate you."*

Display it during online booking, in your confirmation message, and visibly in the salon.

## Three things to do this week

**Step 1:** Enable automated SMS reminders in your booking software. Set them for 48 hours before each appointment.

**Step 2:** Write your cancellation policy using the wording above.

**Step 3:** Enable booking fees. Start at 25% of your average appointment value.

Done once. Pays back every week for as long as you run your business.
""".strip()
)

SALON_3 = post(
    slug='salon-deposit-policy-uk-law',
    title="Salon deposit policy UK: what the law says, what to charge, and how to enforce it",
    category_slug='salons', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='salon deposit policy UK',
    meta_desc="Everything UK salons need to know about taking deposits legally — the correct wording, how much to charge, and what to do when clients refuse to pay.",
    og_image='https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=1400&h=700&fit=crop',
    feat_alt='Salon receptionist processing a card payment deposit at the front desk',
    tags='salon deposit, booking fee, cancellation policy, UK law, no-shows',
    excerpt="Taking deposits is completely legal for UK salons. But using the right wording and setting a fair policy makes all the difference between protecting your business and losing clients.",
    read_time=6,
    faq_items=[
        {'question': 'Can UK salons legally keep a deposit if a client cancels?', 'answer': 'Yes, provided you clearly communicated your cancellation policy at the time of booking. Use the term "booking fee" and state that it is non-refundable with less than [X] hours notice.'},
        {'question': 'What is the difference between a deposit and a booking fee?', 'answer': 'A deposit legally implies a payment that may be returned when conditions are met. A booking fee is clearer — it secures the appointment and is non-refundable under your stated cancellation terms. Using "booking fee" is safer for UK salons.'},
        {'question': 'How much should a salon charge as a deposit?', 'answer': 'Most UK salons charge 20–50% of the total appointment cost. For high-value treatments (colour, extensions) some charge 50% or even the full amount upfront.'},
    ],
    content="""# Salon deposit policy UK: what the law says, what to charge, and how to enforce it

No-shows. Late cancellations. Colour treatments booked weeks in advance that vanish without a word on the morning.

Every UK salon owner knows the feeling. And most know, in theory, that taking deposits would help. What holds them back is uncertainty about the rules.

Is it legal? Can I actually keep it? What if they dispute it? What wording should I use?

This article answers all of those questions clearly.

## Is it legal for UK salons to take deposits?

Yes. Completely legal.

A UK business can require payment upfront before delivering a service. Salons do this routinely for hair extensions, colour treatments, and bridal bookings. The key requirement is that you communicate your terms clearly before the client confirms their booking.

If a client agrees to your cancellation policy at the time of booking, you are entitled to retain the booking fee if they cancel within the restricted period or simply do not show up.

## Deposit vs booking fee: the wording matters

These two terms are used interchangeably but they mean different things legally.

A **deposit** implies that the money will be returned if certain conditions are met. In consumer law, there is sometimes a presumption that deposits are returnable unless you explicitly state otherwise. This can create disputes.

A **booking fee** is clearer. It secures an appointment slot. It is not a deposit toward the final payment. It is forfeited if the client cancels within your notice period or does not attend. Most solicitors advising salons recommend using "booking fee" rather than "deposit."

## The recommended wording

This is a template you can use directly:

*"A non-refundable booking fee of [£X / X% of the total service cost] is required to confirm your appointment. This will be deducted from your final bill when you attend. Cancellations or rescheduling requests received with less than [24/48/72] hours' notice, or failure to attend, will result in the booking fee being forfeited. We appreciate your understanding — this policy helps us protect appointment availability for all clients."*

Adapt the notice period and amount to your salon. Display this:
- During online booking (before the client confirms)
- In the booking confirmation email or text
- On your website
- Visibly at the front desk for walk-ins

## How much to charge

There is no legal rule on the amount. What works in practice:

- **Standard cuts and blow-dries:** Most salons do not take deposits for these. The appointment time is short and the risk is lower.
- **Colour treatments and longer appointments:** 25–50% of the treatment cost is standard. For a £120 colour, that is £30–£60.
- **Hair extensions and specialist treatments:** Many salons take 50% or even 100% upfront. The investment in products and time is too high to risk.
- **Bridal bookings:** Full payment or 50% minimum is common, with a clear contract.
- **New clients only:** Some salons apply booking fees only to first-time clients and not to established regulars. This is a reasonable middle ground when introducing the policy.

## What to do when clients refuse to pay the booking fee

Some clients will push back. Here is how to handle it.

**Explain the reason clearly.** "We had [X] no-shows last week. This policy protects your appointment slot and allows us to serve all our clients fairly." Most reasonable clients understand once it is explained as a business protection, not a money grab.

**Hold the line on new clients.** If your policy is non-negotiable for new clients, be consistent. Making exceptions immediately undermines the policy.

**Be flexible with longstanding regulars.** You can choose to waive the fee for clients who have been coming for years and have never had a no-show. That is your discretion. But be clear that the waiver is a courtesy, not a right.

**If they dispute a retained fee:** As long as you clearly communicated the policy at booking and the client agreed to it (by completing the booking), you are on solid legal ground. Keep records of your communication.

## What booking software makes this easy

Your booking platform needs to:
- Display the booking fee policy before the client confirms
- Take card payment at the time of booking
- Automatically deduct the fee from the final bill when the client attends
- Handle refunds cleanly if the client gives proper notice

ReeveOS handles all of this from the Growth plan (£29/month). The booking fee amount is configurable per service, the policy is displayed prominently during the booking flow, and the deduction happens automatically at checkout.

## A simple tiered policy to start with

If you have never taken deposits before, start gently:

- **Appointments under 30 minutes:** No deposit required
- **Appointments 30–60 minutes:** £10 booking fee
- **Appointments over 60 minutes:** 25% of service cost
- **Colour and chemical treatments:** 50% of service cost
- **Extensions and specialist treatments:** 50–100% of service cost

Review after 3 months. You will almost certainly find that no-shows have dropped significantly and the pushback from clients was much smaller than you feared.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# AESTHETICS CLINICS
# ════════════════════════════════════════════════════════════════

AESTHETICS_1 = post(
    slug='aesthetics-clinic-software-uk-2026',
    title="Aesthetics clinic software UK 2026: the 5 platforms that handle compliance properly",
    category_slug='aesthetics', site='reeveos',
    content_type='pillar', priority='p1',
    keyword='aesthetics clinic software UK',
    meta_desc="Comparing aesthetics clinic software in the UK for 2026. GDPR consent forms, CQC compliance, booking and deposits — with real GBP pricing.",
    og_image='https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1400&h=700&fit=crop',
    feat_alt='Modern aesthetics clinic treatment room with professional equipment',
    tags='aesthetics clinic software UK, clinic management software, consent forms, GDPR aesthetics',
    excerpt="Most booking platforms weren't built for aesthetics clinics. They don't handle consent forms, medical history, or contraindications. Here are the 5 that actually do.",
    read_time=9,
    faq_items=[
        {'question': 'Do UK aesthetics clinics need digital consent forms?', 'answer': 'Yes. UK GDPR requires informed consent before collecting and processing health data. For aesthetics treatments, digital consent forms that record exactly what was agreed and when are best practice and legally important.'},
        {'question': 'What is CQC and does my aesthetics clinic need to register?', 'answer': 'The Care Quality Commission regulates health and social care in England. Clinics performing certain regulated activities (including some injectable treatments) may need CQC registration. Check the CQC website for your specific treatments.'},
        {'question': 'What software do aesthetics clinics use in the UK?', 'answer': 'The most common platforms are Pabau, Consentz, ReeveOS, Fresha, and Timely. Pabau and ReeveOS are the strongest for compliance features including digital consent forms and contraindication checking.'},
    ],
    content="""# Aesthetics clinic software UK 2026: the 5 platforms that handle compliance properly

Running an aesthetics clinic is not like running a hair salon.

You are dealing with medical history. Contraindications. Consent forms that need to be legally watertight. Before-and-after photographs that must be stored securely under UK GDPR. Clients who may have conditions that make certain treatments unsafe.

Most booking platforms weren't built for any of that. They were built for hair appointments.

This guide covers the five platforms that actually understand what an aesthetics clinic needs — and compares them honestly on price, features, and compliance.

## What aesthetics clinics actually need from software

Before comparing platforms, it's worth being clear about what matters in this specific vertical.

**Digital consent forms.** Every treatment requires informed consent. You need forms that clients can complete digitally, that are stored securely, that record the date and version signed, and that can be retrieved quickly if there's ever a question. Paper forms left in a filing cabinet are not sufficient in 2026.

**Medical history and contraindication checking.** Fillers, Botox, chemical peels, laser — all have contraindications. A client on blood thinners, with a history of cold sores, or with certain autoimmune conditions may not be suitable for specific treatments. Your software should flag these automatically.

**Before-and-after photo management.** Photos must be stored with the client's consent, linked to their record, accessible to you and not to anyone else, and protected under UK GDPR. Cloud storage on a shared drive is not appropriate.

**GDPR compliance.** Client health data is "special category data" under UK GDPR. It requires explicit consent, secure storage, limited access, and the right for clients to request deletion. This is not optional.

**Deposits for aesthetics.** No-show rates in aesthetics clinics can be high. A client who books a Polynucleotide treatment and doesn't show up has cost you the product cost, the room, and your time. Deposits are essential.

## The 5 best platforms for UK aesthetics clinics

### 1. ReeveOS — best for full clinic management plus compliance

ReeveOS was built for UK independent businesses including aesthetics clinics. The Growth plan at £29/month includes:

- Digital consultation forms with 6 sections and around 50 fields
- Contraindication matrix: 20 conditions checked against 5 treatment types with automatic BLOCK, FLAG, or OK logic
- GDPR-compliant storage with audit trail for all form submissions
- Before-and-after photo storage linked to client records
- Deposit collection built into the booking flow
- Automated SMS and email reminders
- Full CRM with treatment history and interaction logging

For a single-practitioner aesthetics clinic, ReeveOS is the only platform offering this level of clinical compliance at sub-£100/month pricing.

**Pricing:** Growth at £29/month. Scale at £59/month for unlimited staff.

---

### 2. Pabau — best for larger clinics needing clinical-grade features

Pabau is the market leader for aesthetics and medical aesthetics in the UK. Genuinely excellent clinical documentation, EMR-grade photo management, AI-assisted note-taking, and strong CQC alignment. The limitation is price — most small clinics find it difficult to justify at £53–£119/month, particularly when they are just getting started.

For a clinic with multiple practitioners or one doing significant volumes of medical aesthetics, Pabau is the professional choice.

**Pricing:** From £53/month.

---

### 3. Consentz — best for consent forms specifically

Consentz was built by an aesthetic doctor specifically for the UK aesthetics industry. The consent form and compliance features are excellent. The limitation is that Consentz focuses on the compliance side — it doesn't offer a full booking system, EPOS, or marketing tools. You would need to use it alongside another platform.

For clinics that already have a booking system and just need better compliance documentation, Consentz fills that gap well.

**Pricing:** Custom pricing on enquiry.

---

### 4. Fresha — has the features but check the cost

Fresha offers digital intake forms and some client medical history features. The compliance tools are less developed than Pabau or Consentz. The bigger concern for aesthetics clinics is the pricing model: 20% commission on every new client booked through the Fresha marketplace can represent significant money for a clinic charging £200–£500 per treatment session.

**Pricing:** £14.95/staff/month + 20% new client commission + 1.29%+20p per transaction.

---

### 5. Timely — acceptable for very small clinics, compliance gaps

Timely handles basic booking and some client intake forms. The UK compliance features are limited — no contraindication checking, no structured medical history forms built specifically for aesthetics. For a sole practitioner doing basic non-invasive treatments who also uses paper forms as a supplement, it works. For anyone doing injectables or regulated treatments, it is not sufficient on its own.

**Pricing:** From ~£20/month per staff member.

---

## What to look for specifically for aesthetics

When evaluating any platform for your clinic, ask these questions:

**Does it have treatment-specific consent forms?** Generic consent forms are not sufficient. You need forms specific to fillers, Botox, chemical peels, laser, and your other specific treatments.

**Does it check contraindications automatically?** Or do you have to read through the form yourself every time and rely on memory?

**How is medical data stored?** Is it encrypted? Is it in UK/EU data centres? What happens to the data if you leave the platform?

**Can clients update their medical history?** Conditions change. A client may develop a new health issue or start a new medication between visits. Your system needs to prompt for updates.

**Does it generate an audit trail?** If there is ever a dispute or a clinical incident, you need to be able to prove exactly what consent was given, when, and by whom.

## The compliance bottom line

UK GDPR classifies health data as special category data. Failing to handle it properly exposes you to fines of up to £17.5 million or 4% of turnover. That is not a theoretical risk — the ICO (Information Commissioner's Office) has taken action against healthcare providers for inadequate data handling.

For an aesthetics clinic, the software you choose is a compliance decision as much as a business decision. Choose a platform that was built with this in mind, not one that added a consent form as an afterthought.
""".strip()
)

AESTHETICS_2 = post(
    slug='digital-consent-forms-aesthetics-uk',
    title="Digital consent forms for UK aesthetics clinics: what GDPR and CQC actually require",
    category_slug='aesthetics', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='aesthetics consent forms UK',
    meta_desc="What UK aesthetics clinics must include in digital consent forms. GDPR requirements, medical history sections, and how to store them securely.",
    og_image='https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=1400&h=700&fit=crop',
    feat_alt='Aesthetics practitioner reviewing digital consent form with client on tablet',
    tags='aesthetics consent forms, GDPR aesthetics, digital consent UK, aesthetics compliance',
    excerpt="Paper consent forms in a filing cabinet are not sufficient in 2026. Here's exactly what UK aesthetics clinics must include in digital consent forms and how to store them.",
    read_time=7,
    faq_items=[
        {'question': 'Are paper consent forms legal for UK aesthetics clinics?', 'answer': 'Paper forms are not illegal, but digital forms are strongly preferable. They create a timestamped, searchable audit trail. Under UK GDPR, you need to prove consent was given — digital records make this far easier.'},
        {'question': 'How long should UK aesthetics clinics keep consent forms?', 'answer': 'Best practice is to retain client records for at least 8 years for adults (longer for minors). This aligns with medical records retention guidelines and covers your liability window.'},
        {'question': 'What happens if I don\'t have proper consent forms?', 'answer': 'Without proper consent, you face both legal liability if a treatment goes wrong and ICO regulatory risk for processing special category health data without explicit consent. Both can be financially significant.'},
    ],
    content="""# Digital consent forms for UK aesthetics clinics: what GDPR and CQC actually require

Most aesthetics practitioners know they need consent forms. Not all are confident they have the right content in them — or that storing them in a folder on the computer or a filing cabinet is actually compliant.

This article explains exactly what UK law requires, what should be in your forms, and how to store everything properly.

## Why this matters more than you might think

Client health data is what UK GDPR calls "special category data." This category — which includes health conditions, medical history, and treatment records — gets the highest level of protection under the law.

Processing special category data without explicit, documented consent exposes you to ICO fines of up to £17.5 million or 4% of global turnover. For a small aesthetics clinic, even a minor breach investigation can be costly in time and stress.

Beyond GDPR, proper consent documentation protects you if a treatment outcome is ever disputed. The burden of proof in a complaint is on you to demonstrate that the client understood and agreed to the treatment, the risks, and the aftercare.

Paper forms in a filing cabinet are not sufficient. They can be lost, they are not searchable, and they don't automatically timestamp when the client signed.

## What must be in your consent forms

Every client consent form for an aesthetics treatment should include these sections.

**Personal details.** Full name, date of birth, contact information. Confirm the client is over 18 (or has parental consent if a minor is receiving a permitted treatment).

**Medical history.** This is the most important section. Include:
- Current medications (including blood thinners, immunosuppressants, retinoids)
- Allergies and sensitivities (particularly to anaesthetics, latex, specific ingredients)
- Skin conditions (eczema, psoriasis, rosacea, active acne)
- Autoimmune conditions
- History of cold sores (relevant for lip fillers)
- Pregnancy or breastfeeding
- Any previous aesthetic treatments and reactions
- Current health conditions relevant to the treatment

**Contraindication acknowledgement.** A specific section confirming the client has declared all relevant medical information and understands that providing false information releases the practitioner from liability.

**Treatment explanation.** What the treatment involves, what results to expect, and the realistic timeline.

**Risk disclosure.** The specific risks of the treatment being performed. Generic "some people experience side effects" is not sufficient. List the actual risks: bruising, swelling, asymmetry, migration (for fillers), paradoxical reactions.

**Aftercare instructions.** What the client should and should not do following the treatment.

**Photography consent.** A separate clear consent for before-and-after photographs, specifying how they will be used (clinical record only / with anonymisation / for marketing). These are separate from the treatment consent and can be declined independently.

**GDPR consent.** How you will store and use their data, their right to access or delete their records, and who has access to their information.

**Signature and date.** The date must be timestamped — not just the day but ideally the time.

## Treatment-specific forms vs one generic form

One generic consent form is not sufficient for a clinic offering multiple treatments.

A client having a chemical peel needs to consent to the specific risks of that treatment. A client having lip fillers needs a form specific to the risks of injectable treatments. A client having laser hair removal needs a different form again.

Best practice is to have:
- A general client health questionnaire (completed on first visit and updated at subsequent visits)
- Treatment-specific consent forms for each category of treatment

The general health questionnaire should be reviewed and re-confirmed at each visit — conditions and medications change.

## How to store consent forms compliantly

**Data must be encrypted at rest and in transit.** Storing forms on an unencrypted laptop or in a shared Dropbox folder is not compliant.

**Access must be restricted.** Only the practitioners who need to see a client's medical records should have access. If you have a receptionist, they should not have access to clinical notes unless there is a legitimate reason.

**Data must be stored in the UK or EEA.** Post-Brexit, UK data must not be transferred to countries without an adequacy agreement.

**Clients must be able to request their data.** Under the right of access, a client can request a copy of all data you hold on them. You must be able to produce this within 30 days.

**Clients must be able to request deletion.** Under the right to erasure, a client can ask you to delete their data. However, this can be refused if you have a legitimate legal obligation to retain records (which you likely do for clinical liability reasons — document your reasoning if you retain records despite a deletion request).

## Using ReeveOS for aesthetics compliance

ReeveOS includes a consultation form system built specifically for aesthetics clinics:

- 6-section consultation form covering all required medical history fields
- Treatment consent forms (2A–2D) with treatment-specific risk disclosure
- Contraindication matrix: 20 conditions × 5 treatments with automatic BLOCK, FLAG, or OK logic
- AES-256-CBC encrypted storage for all form submissions
- GDPR-compliant audit trail with timestamps
- Distribution via link, QR code, automated email, or client portal
- 6-month validity — clients are prompted to re-confirm their health information

The contraindication checking is the feature that matters most in practice. If a client completes their health questionnaire and indicates they are on blood thinners, the system automatically flags this for filler treatments and blocks certain treatments from being booked. This removes the risk of human error in reviewing forms manually.
""".strip()
)

AESTHETICS_3 = post(
    slug='pabau-alternative-uk',
    title="Pabau alternatives UK 2026: aesthetics clinic software that won't cost £1,200 a year",
    category_slug='aesthetics', site='reeveos',
    content_type='competitor-alternative', priority='p1',
    competitor_name='Pabau',
    keyword='pabau alternative UK',
    meta_desc="Pabau costs £53–£119/month. Here are the best UK alternatives for aesthetics clinics that include compliance features at a fraction of the price.",
    og_image='https://images.unsplash.com/photo-1559757175-5700dde675bc?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1559757175-5700dde675bc?w=1400&h=700&fit=crop',
    feat_alt='Aesthetics clinic reception desk with digital booking system',
    tags='pabau alternative, aesthetics software UK, clinic management, consent forms software',
    excerpt="Pabau is excellent but expensive. At £53–£119/month, small and solo aesthetics clinics often pay more than they need to. Here are the alternatives worth considering.",
    read_time=6,
    faq_items=[
        {'question': 'How much does Pabau cost?', 'answer': 'Pabau starts at approximately £53/month for a solo practitioner and goes up to £119/month or more for larger teams. Annual billing reduces the cost slightly.'},
        {'question': 'What is the main difference between Pabau and ReeveOS?', 'answer': 'Pabau is deeper in pure clinical features and is the choice for large multi-practitioner aesthetics businesses. ReeveOS includes consent forms, contraindication checking, and GDPR compliance at a lower price point — the Growth plan is £29/month — making it more accessible for independent clinics.'},
    ],
    content="""# Pabau alternatives UK 2026: aesthetics clinic software that won't cost £1,200 a year

Pabau is genuinely good software. If you run a large aesthetics practice with multiple practitioners, complex clinical documentation needs, and a high volume of treatments, Pabau is probably worth every penny.

But not every aesthetics clinic is a large practice.

Many of the UK's aesthetics practitioners are solo operators or small teams — a clinic owner with one or two employees, working out of a single treatment room, building their business year by year. For those clinics, paying £53–£119/month — up to £1,428 a year — for software that does far more than they need is hard to justify.

Here are the alternatives worth considering.

## What you actually need from aesthetics clinic software

Before looking at alternatives, it's worth being honest about requirements.

A solo aesthetics practitioner with one treatment room needs:
- Online booking with deposit collection
- Digital consultation and consent forms with medical history
- Basic contraindication checking (or at least a prompt to review)
- Secure GDPR-compliant storage of client health data
- Automated appointment reminders
- A CRM to track client treatment history
- Invoicing or basic payment processing

They probably do not need EMR-grade clinical documentation, AI note-taking, or a multi-practitioner workflow system.

The question is which platform covers those actual needs at the right price.

## The best Pabau alternatives for UK aesthetics clinics

### ReeveOS — best value for independent UK clinics

ReeveOS was built for UK independent businesses including aesthetics clinics. The Growth plan at £29/month covers:

- 6-section digital consultation form (about 50 fields covering full medical history)
- Treatment consent forms (specific to Botox, fillers, chemical peels, Polynucleotides, laser)
- Contraindication matrix: 20 medical conditions checked against 5 treatment types with BLOCK/FLAG/OK logic
- AES-256-CBC encrypted storage with full audit trail
- GDPR right-to-access and right-to-erasure tools
- Deposit collection in the booking flow
- Automated SMS and email reminders
- CRM with full client treatment history

For a solo practitioner or small clinic, the saving over Pabau is £288–£1,080 per year. For a business that is still growing, that is significant.

The gap versus Pabau: ReeveOS does not have AI-assisted clinical note-taking or EMR-grade documentation for medically regulated procedures. For a clinic doing Botox, fillers, and peels in an independent setting, this is unlikely to matter. For a clinic doing more complex medical aesthetics alongside a GP or nurse prescriber, Pabau's clinical depth may be worth the premium.

**Pricing:** Growth £29/month. Scale £59/month.

---

### Consentz — for consent forms specifically

Built by an aesthetic doctor for the UK market. Consent forms and compliance features are excellent and purpose-built. The limitation: Consentz focuses on compliance documentation. It is not a full booking system. You would use it alongside a separate booking tool.

For a clinic that already has a booking system and just needs to upgrade their consent form process, Consentz is strong. For a clinic wanting one integrated system, it creates duplication.

**Pricing:** Custom — contact for quote.

---

### Fresha — for clinics prioritising marketplace discovery

Fresha has intake forms and basic client health history. The compliance features are less developed than Pabau or ReeveOS. The main advantage is their consumer marketplace — Fresha can bring new clients to a new or growing clinic.

The cost: 20% commission on every new client booked via the marketplace. For a clinic charging £300 per treatment, that's £60 per new client. At some volume that adds up to more than Pabau's monthly fee.

**Pricing:** £14.95/staff/month + 20% new client commission + processing fees.

---

### Timely — for very small clinics with basic needs

Basic booking and some intake form capability. Not built for the compliance requirements of a UK aesthetics clinic. Reasonable for non-invasive treatments where the clinical risk is low, but not sufficient for injectables or regulated procedures without supplementing with separate compliance documentation.

**Pricing:** From ~£20/month per staff member.

---

## The honest comparison

| Platform | Consent forms | Contraindication checking | Monthly cost | Best for |
|---|---|---|---|---|
| Pabau | Excellent, clinical grade | Yes | £53–£119 | Large/medical practices |
| ReeveOS | Strong, UK-built | Yes (automated) | £29–£59 | Independent clinics |
| Consentz | Excellent, compliance-focused | Partial | Custom | Bolt-on compliance |
| Fresha | Basic | No | £14.95 + commission | Marketplace growth |
| Timely | Basic | No | ~£20/staff | Non-invasive only |

## The bottom line

If you are a solo practitioner or a small aesthetics clinic doing standard treatments (Botox, fillers, peels, non-invasive aesthetics), ReeveOS gives you the compliance features that matter at a third of Pabau's cost.

If you are building a larger medically regulated practice with multiple practitioners and a clinical supervisor, Pabau's depth is likely worth the investment.

The question to ask yourself: what do I actually need right now, and am I paying for features I am not using?
""".strip()
)


# ════════════════════════════════════════════════════════════════
# BARBERS
# ════════════════════════════════════════════════════════════════

BARBER_1 = post(
    slug='walk-in-vs-appointment-barbershop-uk',
    title="Walk-in vs appointment: how UK barbershops manage both without the chaos",
    category_slug='barbers', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='barber walk in appointment management',
    meta_desc="Most UK barbershops run a mix of walk-ins and appointments. Here's how to manage both in the same system without double-booking or frustrated clients.",
    og_image='https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1400&h=700&fit=crop',
    feat_alt='Modern barbershop interior with multiple barber chairs and waiting clients',
    tags='barbershop walk-in management, barber booking system, walk-in queue, appointment booking barber',
    excerpt="Walk-ins or appointments? Most barbershops need both. Managing them together without chaos, double-bookings, or long unexplained waits is a real challenge — here's the system that works.",
    read_time=7,
    faq_items=[
        {'question': 'Should barbershops take appointments or walk-ins?', 'answer': 'Most successful UK barbershops take both. Appointments give predictability; walk-ins fill gaps and serve clients who won\'t plan ahead. A digital queue system lets you manage both in the same view.'},
        {'question': 'How do digital walk-in queues work for barbershops?', 'answer': 'Clients scan a QR code at the door or enter their name on a tablet. They see their position in the queue and an estimated wait time on their phone. They can wait nearby rather than standing in the shop. The barber sees both the walk-in queue and appointment calendar in one view.'},
    ],
    content="""# Walk-in vs appointment: how UK barbershops manage both without the chaos

The classic barbershop debate. Walk-ins or appointments?

The honest answer is: both. And managing both without causing chaos for your clients or your barbers is something most shops handle poorly.

Here's what the problem looks like in practice.

A client walks in on a Saturday morning. Two of your three barbers have appointments booked back-to-back. The third has a gap. But the walk-in client doesn't know this. They see what looks like a full shop. They wait awkwardly for someone to acknowledge them. Meanwhile, a barber finishes a cut and doesn't know who's next.

Or the opposite problem. You have a busy queue of walk-ins. An appointment client arrives. Do you make the walk-ins wait while you see the appointment? Do the walk-ins get annoyed they arrived first?

There is a better way to handle this.

## Why both models exist

**Appointments** give you predictability. You know roughly how busy each hour will be. You can plan product use and staff schedules. Clients with specific requests (colour, specific styles) can ensure they get the right barber. No-show deposits protect your time.

**Walk-ins** serve a fundamental reality about barbershop clients. A significant proportion of men — particularly younger clients — will not plan a haircut two weeks ahead. They decide on a Saturday morning that they need a cut and they want to go now. Refusing walk-ins means losing those clients to the shop down the road.

The goal is a hybrid system that handles both without friction.

## The problem with the current approach

Most barbershops manage this with a combination of:
- A paper appointments book (or basic booking app for booked clients)
- Asking walk-in clients to "just take a seat"
- Verbally updating wait times as best the barbers can estimate

This breaks down when the shop gets busy. Walk-in clients don't know how long they'll wait. They can't go and get a coffee and come back at the right time. Barbers have to manage two separate streams of clients mentally while also doing haircuts.

The result: frustrated clients, stressed barbers, and unnecessary confusion at the busiest moments.

## The digital queue solution

The solution is a system that shows both appointment bookings and walk-in clients in the same view, with estimated wait times that update automatically.

Here's how it works in practice.

A client arrives as a walk-in. At the door they see a small sign: "Add yourself to the queue." They scan a QR code or enter their name on a tablet. The system shows them: "You are 3rd in the walk-in queue. Estimated wait: 25 minutes."

They can go and wait in their car, grab a coffee, or sit in the shop. Their place is held.

The barber's screen shows:
- Next appointment: Sam, 11:15, grade 2 back and sides (confirmed)
- Walk-in queue: 1. Marcus (5 mins), 2. James (12 mins), 3. New arrival (25 mins)

The system blends the two lists automatically, filling appointment gaps with walk-in clients.

When a barber finishes a cut, they tap "next" and the system tells them who is up — appointment or walk-in — based on timing.

## How to set it up

ReeveOS has a dedicated walk-in queue feature built into the Growth plan. Here's the setup:

**Step 1.** Set your appointment booking capacity (how many appointment slots to hold back per hour for booked clients).

**Step 2.** Generate your QR code and display it on a small sign at the door or on your counter.

**Step 3.** Configure your average service times so the estimated wait calculations are accurate.

**Step 4.** Brief your barbers. The system replaces "who's next?" with a clear dashboard view.

## The client experience improvement

When walk-in clients know their estimated wait time, they are significantly less frustrated by it. A 30-minute wait that is transparent and trackable feels very different from a 30-minute wait where the client has no idea if it will be 10 minutes or an hour.

Shops that implement digital queues report that clients are more likely to wait, more likely to return, and more likely to recommend the shop. The wait hasn't changed — the experience has.

## The booking fee question for appointments

For booked appointments, we recommend taking a booking fee for appointments over a certain value (haircuts above £25, for example). Walk-in clients generally don't need a deposit — they're already there.

For booked appointments at peak times — Saturday mornings especially — a £5–£10 booking fee is reasonable and significantly reduces the no-show rate. A £10 deposit on a £25 haircut appointment is a 40% booking fee, which is on the higher side. A flat £5 is more palatable while still being effective.
""".strip()
)

BARBER_2 = post(
    slug='barbershop-marketing-ideas-uk',
    title="7 barbershop marketing ideas that cost nothing and actually work in the UK",
    category_slug='barbers', site='reeveos',
    content_type='cluster', priority='p2',
    keyword='barbershop marketing ideas UK',
    meta_desc="7 practical marketing ideas for UK barbershops that cost little or nothing. Google Business Profile, Instagram, WhatsApp, and referrals — what actually works.",
    og_image='https://images.unsplash.com/photo-1599351431202-1e0f0137899a?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1599351431202-1e0f0137899a?w=1400&h=700&fit=crop',
    feat_alt='Barber showing client the finished haircut in a mirror at a modern barbershop',
    tags='barbershop marketing, barber Instagram, Google Business Profile barber, barber referral programme',
    excerpt="Most barbershops get their best clients through word of mouth. These 7 ideas turn that passive process into something you can actively drive — without a marketing budget.",
    read_time=6,
    content="""# 7 barbershop marketing ideas that cost nothing and actually work in the UK

The best barbershops in the UK have one thing in common: their clients tell other people about them.

Word of mouth is the most powerful marketing channel for a barbershop. The question is how to make that process active rather than passive — how to encourage it, accelerate it, and direct it — without spending money you don't have.

Here are 7 things that actually work.

## 1. Get your Google Business Profile right

This is the highest-return thing you can do this week. It takes 30 minutes and it is free.

Go to business.google.com. Claim or create your profile. Add:
- Correct address, phone number, and hours (including holiday hours)
- At least 10 photos — the exterior, the interior, your barbers working, finished cuts
- Your services with prices
- A link to your booking page

When someone nearby searches "barbers near me" or "barbershop [your town]," your profile is what determines whether they come to you. A profile with photos and reviews beats an empty listing every time.

The most important thing after setting it up: get reviews. More on that in point 3.

## 2. Instagram — show the work

You don't need professional photography. You need your phone, good light, and the habit of photographing your best cuts.

Post two or three times a week. Show the finished cut. Use before-and-after when the client is happy with it (get their permission). Show the shop, your barbers, the atmosphere.

Hashtags: use local ones. #[YourTown]Barber, #[YourCity]Haircut, #UKBarber. These are the ones that reach people who could actually come to you.

The goal is not viral content. The goal is being visible to the people in your postcode who are looking for a new barbershop.

## 3. Ask for Google reviews — but ask at the right moment

The right moment to ask for a Google review is when the client is in the chair, looking in the mirror, and they've just told you they love it.

"Really glad you like it. If you have 30 seconds, a Google review means the world to us — I'll send you the link."

Then send the link via WhatsApp or text immediately while they're still in the shop or just leaving.

Most people who say they'll do it actually will if they get the link immediately. If you wait and send it later, most won't bother.

Ten genuine Google reviews with 5 stars will noticeably increase how many new clients you get from Google searches.

## 4. WhatsApp Business — the best CRM you're not using

Set up a WhatsApp Business account. Create a short message or status update when you have availability — "cancellation today at 2pm, message to book." Share it with your client list.

For regulars who come every 3–4 weeks, send a brief WhatsApp around the time they're likely to be due: "Hey [name], just checking if you want to book in this week? We've got Thursday afternoon free."

This feels personal and it works. People book with barbers they have a relationship with. WhatsApp maintains that relationship without being intrusive.

## 5. A simple referral programme

Tell your existing clients: "If you refer a friend who books with us, your next haircut is £5 off."

Print it on a small card they can give to a friend. Mention it when clients pay. Put it on Instagram.

The economics work well. A new client is worth £25–£40 per month in recurring revenue. Giving a £5 discount to the person who referred them is a very small acquisition cost.

## 6. Local business partnerships

Think about which other local businesses your clients also use. The gym three doors down. The coffee shop across the road. The men's clothing shop in the high street.

Propose a simple arrangement: you'll recommend their business to your clients if they'll recommend yours. Leave some of your cards in their space. Ask if they'll do the same.

This costs nothing and reaches people who already live and work in your area.

## 7. Book the next appointment before they leave

The most overlooked client retention strategy in barbershops.

When a client pays, ask: "Same time in four weeks?"

A significant proportion of clients will say yes. You've just filled a slot in your future diary. You've also made it slightly less likely that they'll drift to a different barbershop next time — because they already have an appointment with you.

For clients on a regular schedule, offer to book them in automatically every 3–4 weeks. They'll appreciate not having to think about it.

---

None of these require a budget. They require consistency and the habit of doing them. The barbershops that grow sustainably are the ones that do these small things regularly, not the ones that run one big marketing campaign and then stop.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# GYMS & FITNESS
# ════════════════════════════════════════════════════════════════

GYMS_1 = post(
    slug='gym-management-software-uk-2026',
    title="Gym management software UK 2026: what independent gym owners actually need",
    category_slug='gyms', site='reeveos',
    content_type='pillar', priority='p1',
    keyword='gym management software UK',
    meta_desc="Comparing gym management software for independent UK gyms in 2026. Real GBP pricing, honest comparison of Mindbody, Glofox, TeamUp, and ReeveOS.",
    og_image='https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400&h=700&fit=crop',
    feat_alt='Independent gym with free weights area and modern equipment',
    tags='gym management software UK, gym software comparison, fitness studio software, gym membership software',
    excerpt="Mindbody is expensive. Glofox has limitations. TeamUp is UK-friendly but class-only. Here's the honest comparison of gym management software for independent UK operators.",
    read_time=9,
    faq_items=[
        {'question': 'What is the best gym management software for small UK gyms?', 'answer': 'For independent UK gyms wanting the best value, TeamUp (from £79/month) and ReeveOS (from £29/month) are the strongest options. TeamUp is class-focused; ReeveOS includes memberships, bookings, EPOS, and broader service management in one platform.'},
        {'question': 'Can I use GoCardless Direct Debit for gym memberships in the UK?', 'answer': 'Yes. GoCardless is the most popular Direct Debit provider for UK gym memberships. ReeveOS integrates with GoCardless so members can pay monthly by Direct Debit automatically without you having to manually chase payments.'},
        {'question': 'How much does Mindbody cost in the UK?', 'answer': 'Mindbody starts at approximately £119/month and goes up to £349/month or more for higher tiers. Annual billing reduces the cost slightly. Many independent UK gyms find this expensive relative to alternatives.'},
    ],
    content="""# Gym management software UK 2026: what independent gym owners actually need

Running an independent gym in the UK is different from running a franchise. You don't have a corporate tech team, a national marketing budget, or 50 locations sharing infrastructure costs. You have one site, a loyal local membership, and a tight margin.

The software you choose needs to reflect that reality.

This guide covers what independent UK gyms actually need, what the main platforms offer, and which ones are worth the monthly fee.

## What matters most for an independent UK gym

**Membership management and Direct Debit.** The financial backbone of any gym. Members need to be able to pay monthly by Direct Debit (GoCardless is the UK standard) and the system needs to handle renewals, pauses, freezes, and cancellations without you manually chasing every payment.

**Class and session booking.** If you run classes, personal training sessions, or any time-based sessions, members need to book online and you need to track attendance.

**Access control integration.** Many independent gyms operate unmanned at certain hours. Your membership software needs to integrate with door access control so only active members can enter.

**Payment processing for extras.** Personal training top-ups, retail products, supplements, day passes. You need a till or EPOS for these that connects to your membership records.

**Retention tools.** Reducing member churn is the single most important thing for gym profitability. Automated win-back messages, attendance tracking, expiring membership alerts — these matter.

**UK-specific features.** Direct Debit via GoCardless. Support in UK timezone. GDPR compliance for member data. Pricing in GBP.

## The main platforms compared

### Mindbody — market leader, but expensive

Mindbody is the biggest name in fitness studio and gym management worldwide. The feature set is comprehensive. The interface is dated in places. The price is the main barrier for independent UK gyms.

At £119/month minimum for the Starter plan and £349/month for the Accelerate plan, you're paying for a platform built for chains and franchises. For an independent gym with 200 members, the cost-to-value ratio is hard to justify.

There's also a specific concern with Mindbody's consumer marketplace: Mindbody has its own client-facing app, and they can and do promote other gyms and studios to your members. Your retention can be affected by the platform itself.

**Pricing:** £119–£349/month.

---

### ABC Glofox — strong for boutique fitness

Glofox is well-regarded for boutique fitness studios — yoga, CrossFit, HIIT. Clean app, good class management, strong onboarding support.

The limitations: it's boutique-fitness focused. If your gym has a free weights area, personal training, or retail, the feature depth outside of classes is limited. Higher tiers for features that feel basic.

**Pricing:** £89–£269/month.

---

### TeamUp — the most UK-friendly option in this tier

TeamUp is popular with UK independent gym owners and PT studios. Genuinely all-features-included pricing (no add-ons), UK-based support, clean interface. Particularly good for class-based businesses.

The limitations: TeamUp is primarily class and session management. If your gym is membership-based with 24/7 access, limited class schedule, and a PT booking element, TeamUp's feature depth outside classes is less impressive. No EPOS. No retail management.

**Pricing:** From £79/month.

---

### ReeveOS — best for all-in-one UK independent gym

ReeveOS covers the full stack for an independent UK gym:

- Membership management with GoCardless Direct Debit integration
- Class booking and session scheduling
- Personal training appointment booking
- EPOS for counter sales, retail, and day passes
- Automated reminders and retention messages
- Member CRM with attendance history
- Staff management and scheduling
- Custom booking domain

For a gym also running personal training, selling retail products, and wanting one system for everything, ReeveOS consolidates what would otherwise be 3–4 separate tools.

The honest limitation versus Mindbody or Glofox: newer platform. The community and ecosystem around those established platforms is larger. If you specifically need a gym-branded consumer app, ReeveOS's consumer directory is newer than Mindbody's.

**Pricing:** Growth £29/month (5 staff). Scale £59/month (unlimited staff).

---

### Gymdesk — worth mentioning, but US-focused

Strong for martial arts gyms, CrossFit boxes, and small functional fitness gyms. US-built, USD pricing, limited UK Direct Debit integration. Not a primary recommendation for UK gyms.

**Pricing:** $75–$150/month USD.

---

## Honest price comparison for a 300-member independent UK gym

| Platform | Monthly cost | Annual cost | GoCardless DD | EPOS | 24/7 access control |
|---|---|---|---|---|---|
| Mindbody Starter | £119 | £1,428 | Via integration | No | Via integration |
| Glofox | £89–£269 | £1,068–£3,228 | Limited | No | Via integration |
| TeamUp | £79+ | £948+ | Yes | No | Via integration |
| ReeveOS Growth | £29 | £348 | Yes | Yes | Via integration |

## Reducing member churn: the most important metric

Software choice matters less than the strategies you use for retention. The gyms that grow are the ones that notice when a member hasn't been in for two weeks and send them a personal message. The ones that offer flexible freeze options so people don't cancel. The ones that build community through events and challenges.

Your software should make retention easier, not just administration faster. Look for:
- Attendance tracking with automated flags for low-attendance members
- Automated win-back messages for lapsing members
- Flexible membership options (monthly, annual, punch cards, day passes)
- Easy membership freeze and pause functionality

## Getting started

If you're currently managing memberships in a spreadsheet, collecting Direct Debits manually, or using three separate tools for bookings, classes, and payments — consolidating onto a single platform will save significant time each week.

The switching cost is lower than most gym owners expect. Most platforms can import a CSV of your current members. GoCardless can migrate existing mandates in many cases. The setup is typically one to two weeks of admin, not months.
""".strip()
)

GYMS_2 = post(
    slug='reduce-gym-member-churn-uk',
    title="How to reduce gym member churn: the retention playbook for independent UK gyms",
    category_slug='gyms', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='reduce gym member churn UK',
    meta_desc="Independent UK gyms lose 30–50% of members annually. Here are the retention strategies that actually work — without expensive loyalty programmes.",
    og_image='https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=1400&h=700&fit=crop',
    feat_alt='Gym member working out with a personal trainer in an independent fitness studio',
    tags='gym member retention, reduce gym churn, gym membership renewal, fitness studio retention',
    excerpt="The average independent UK gym loses 30–50% of members every year. Most of that is preventable. Here's the retention playbook that successful independent gyms use.",
    read_time=7,
    content="""# How to reduce gym member churn: the retention playbook for independent UK gyms

The average independent UK gym has a member churn rate of 30–50% per year. That means replacing a third to half of your entire membership every 12 months just to stand still.

Think about what that costs. If your average member pays £35/month, losing 100 members means losing £42,000 per year in recurring revenue. Replacing those 100 members means spending on marketing, offering joining offers, and investing time in onboarding.

The maths strongly favour retention over acquisition. Keeping a member is worth 5–10 times more than winning a new one.

Here are the retention strategies that actually work.

## Understand why members leave

Before you can fix churn, you need to know its causes. For UK independent gyms, the most common reasons are:

- **They stopped coming.** Members don't cancel because they hate your gym. They cancel because they stopped going, feel guilty about it, and eventually decide to stop paying for something they're not using.
- **Life changes.** New job, new home, new baby, financial pressure. These are harder to prevent but often possible to work with (membership freezes, pauses, reduced memberships).
- **They don't feel part of something.** Independent gyms often have a community advantage over chains — regular members know each other, the owner knows their names. When that feeling fades, so does loyalty.
- **They found something cheaper or more convenient.** Often not about price specifically, but about perceived value relative to cost.

## The attendance drop is the early warning signal

Members who are going to cancel almost always stop coming before they cancel. The pattern is predictable: regular attendance → skipping a week → coming once a fortnight → stopping altogether → cancelling.

The intervention window is between the first attendance drop and the cancellation. Most gyms miss this window entirely because they only notice when the cancellation comes in.

**What to do:** Set up an attendance alert in your gym management software. Any member who hasn't visited in 10–14 days gets a flag. A human (ideally the owner or a coach) contacts them personally.

Not a generic "we miss you" email. A personal message: "Hey [name], haven't seen you in a couple of weeks — everything okay? We've got [class / session / new equipment] you might enjoy."

This single intervention, done consistently, reduces churn significantly. People cancel memberships. They don't cancel people who check in on them.

## The first 30 days are critical

Members who establish a routine in the first 30 days are dramatically more likely to stay long-term. Members who don't are at high risk of churning within 90 days.

Create a structured first-month experience:
- Day 1: Welcome message with their access code, class schedule, and a personal introduction to one staff member
- Day 7: Check-in message — how's it going? Did they find everything?
- Day 14: Invite to a class or challenge relevant to their stated goals
- Day 30: Short progress check-in — what are they enjoying? Is there anything they need?

This doesn't need to be complicated. Four messages over 30 days. But it needs to be personal and consistent.

## Freeze and pause options reduce cancellations

Many member cancellations happen during temporary life disruptions — a month travelling, a new job that makes the commute impossible, a busy period with a new baby.

If your only option is "cancel or keep paying," many members will cancel. If you offer "pause your membership for up to 2 months, then it auto-resumes," many of those members will pause instead.

The economics: a 2-month pause costs you 2 months of membership fees. A cancellation costs you that member potentially forever. Even if only 30% of members who would have cancelled instead pause and return, the freeze option is profitable.

Make this option prominent. Tell members about it when they contact you to cancel. Have your software send it automatically when cancellation is detected.

## Annual memberships improve retention significantly

Members on monthly memberships churn at roughly twice the rate of members on annual memberships. The annual upfront commitment creates a psychological lock-in that monthly payments don't.

The challenge is offering an annual membership that is attractive enough to buy but not so discounted that it undermines your economics.

A common structure: monthly is £35, annual is £350 (equivalent to two months free). The member saves £70, you lock in 12 months of income, and annual churn rates improve dramatically.

Offer annual memberships prominently at sign-up, at the renewal point, and during any promotion period.

## Build community deliberately

Independent gyms have a structural advantage over chains: the owner knows the members. People choose independent gyms partly because they want that sense of community and belonging.

But community doesn't maintain itself passively. It needs active investment.

- Monthly challenges or goals shared among members
- Social media content that features members (with permission)
- End-of-year events or milestone celebrations
- A WhatsApp group for class members or regular attendees
- Personal check-ins from coaches on progress

Members who feel part of something don't cancel. Members who feel like a number on a billing system do.

## The win-back campaign for lapsed members

Even with good retention systems, members will leave. A structured win-back campaign can recover 10–20% of them.

Wait 30–60 days after cancellation. Then send a personal message: "We miss you at [gym name]. We've been making some improvements recently — [specific change: new equipment / new class / new coach]. If you'd like to come back, your first month is on us / here's a reduced rejoining offer."

This works because people often cancel during a difficult period and later regret it. A personal, low-pressure invitation at the right time converts a meaningful proportion.

---

The gyms that grow aren't always the ones with the most equipment or the cheapest membership. They're the ones where members feel seen, supported, and part of something. The software makes the systems easier. The culture makes people stay.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# EPOS & PAYMENTS
# ════════════════════════════════════════════════════════════════

EPOS_1 = post(
    slug='epos-now-alternative-uk-2026',
    title="EPOS Now alternatives UK 2026: cheaper EPOS systems without the hidden fees",
    category_slug='epos-payments', site='reeveos',
    content_type='competitor-alternative', priority='p1',
    competitor_name='EPOS Now',
    keyword='epos now alternative UK',
    meta_desc="EPOS Now charges for basic features as add-ons and locks you into long contracts. Here are the best UK alternatives with transparent pricing.",
    og_image='https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1400&h=700&fit=crop',
    feat_alt='Restaurant EPOS system at counter showing order management screen',
    tags='EPOS Now alternative, EPOS system UK, POS system comparison, cheap EPOS UK',
    excerpt="EPOS Now's headline price looks reasonable until you add the features you actually need. Staff permissions, loyalty, and integrations are all add-ons. Here's what you should use instead.",
    read_time=7,
    faq_items=[
        {'question': 'How much does EPOS Now actually cost?', 'answer': 'EPOS Now starts at £25/month for basic software but most real-world setups cost £50–£100/month once integrations, additional registers, and add-on features are included. Hardware is separate and purchased upfront.'},
        {'question': 'What is the best EPOS system for a small UK restaurant?', 'answer': 'For independent UK restaurants, ReeveOS and Square are the strongest options for all-in-one booking + EPOS + payments. For pure EPOS without booking needs, Square POS and SumUp POS are simpler and cheaper.'},
        {'question': 'Can I use my own card reader with any EPOS system?', 'answer': 'Most cloud EPOS systems require you to use their payment processing. ReeveOS integrates with Dojo, giving you access to 0.3% debit / 0.7% credit rates — significantly cheaper than built-in payment processing on most EPOS platforms.'},
    ],
    content="""# EPOS Now alternatives UK 2026: cheaper EPOS systems without the hidden fees

EPOS Now is one of the most recognisable EPOS brand names in the UK. Their advertising is everywhere and their initial pricing looks reasonable.

The problem is what happens when you start building the system you actually need.

Need multiple staff logins with different permission levels? Add-on. Want a loyalty programme? Add-on. Need the stock management integration? Add-on. Want to connect your booking system? Add-on.

By the time most independent businesses have EPOS Now configured for real-world use, the monthly cost has doubled or tripled from the headline price — and they're locked into a 12 or 24-month contract.

Here are the alternatives that offer transparent, all-in pricing.

## What to look for in an EPOS system

Before comparing platforms, decide what you actually need.

**Minimum requirements for most UK businesses:**
- Process card payments and cash
- Print or email receipts
- Basic sales reporting
- Multiple staff logins

**Common requirements for hospitality and retail:**
- Table management (restaurants)
- Kitchen display or ticket printing (restaurants and cafés)
- Inventory and stock management
- Customer orders and tabs
- Booking system integration

**Nice to have:**
- Loyalty programme
- Online ordering integration
- Accountancy software integration (Xero, Sage)
- Multi-location management

Be clear about which category your requirements fall into before you start comparing. The best system for a coffee shop with two registers is different from the best system for a 30-cover restaurant with a bar.

## The alternatives to EPOS Now

### ReeveOS — best for businesses that also need booking

If you're a restaurant, salon, barber, or any business that takes both bookings and payments, ReeveOS is the only system that genuinely integrates both in a single platform. The EPOS handles counter sales and card payments. The booking system manages appointments and table reservations. The CRM tracks customer history across both.

Card payments through Dojo at 0.3% debit / 0.7% credit — substantially cheaper than EPOS Now's built-in processing.

No long contracts. Cancel any month.

**Pricing:** Growth £29/month. Scale £59/month. No add-ons for basic features.

---

### Square POS — best for simple, low-cost EPOS

Square is genuinely free for basic POS functionality. No monthly software fee. You pay 1.75% per card transaction.

The catch: 1.75% becomes expensive at volume. For a business processing £10,000/month in card sales, that's £175/month in transaction fees. Dojo through ReeveOS on the same volume costs around £35/month.

For a very small business doing under £5,000/month in card sales and needing a simple till with no complex features, Square is difficult to beat on simplicity and setup speed.

**Pricing:** Free software. 1.75% per transaction.

---

### Lightspeed — best for larger retail and restaurants with complex needs

Lightspeed is a comprehensive system with strong inventory management, table management, and reporting. The feature depth is genuine.

The price is enterprise-level: £69–£399/month depending on the tier. Not appropriate for most independent businesses.

**Pricing:** From £69/month.

---

### SumUp POS — best for simple mobile or pop-up trading

SumUp started as a card reader company and their POS is a solid entry-level till for businesses that don't need complexity. Low processing fees (from 0.69%). Limited features — no table management, no kitchen tickets, no complex reporting.

Good for market traders, pop-up food stalls, and small retail.

**Pricing:** Hardware from £99. 0.69–1.69% per transaction.

---

### Zettle by PayPal — viable but watch the fees

Zettle has a clean interface and integrates well with PayPal (useful if you already accept PayPal). The 1.75% processing fee is the same issue as Square — it becomes expensive at volume.

**Pricing:** 1.75% per transaction.

---

## The hidden fee problem with EPOS Now explained

EPOS Now's business model relies on add-on fees for features that other platforms include by default.

Here is a real comparison. Suppose you need:
- 3 staff logins with permission controls
- Basic loyalty programme
- Xero accounting integration
- 1 register

EPOS Now base: £25/month
Add team management features: +£15/month
Add loyalty: +£15/month
Add integrations: +£15/month

**Actual total: £70/month**

ReeveOS Growth at £29/month includes all of the above.

The lesson: always build a full feature list before comparing EPOS systems. Compare the price of the configuration you actually need, not the headline plan price.

## What about hardware?

EPOS Now requires you to purchase their hardware upfront — typically £300–£800 for a complete setup including screen, card reader, and printer.

ReeveOS works on any iPad or Android tablet you already own, or on a standard laptop. You add a Dojo card reader (available on a monthly basis or purchased outright). The hardware cost is significantly lower.

Square and SumUp also work with standard hardware. Their card readers are £20–£50.

## The 3-year cost comparison

For a restaurant doing £15,000/month in card sales, running one till, needing 4 staff logins:

| Platform | Monthly software | Monthly processing | Annual total | 3-year total |
|---|---|---|---|---|
| EPOS Now (full features) | £70 | £225 (1.5%) | £3,540 | £10,620 |
| ReeveOS + Dojo | £29 | £55 (0.3%d/0.7%c) | £1,008 | £3,024 |
| Square POS | £0 | £262 (1.75%) | £3,144 | £9,432 |
| SumUp POS | £0 | £150 (1%) | £1,800 | £5,400 |

Over 3 years, the difference between EPOS Now and ReeveOS is over £7,500.
""".strip()
)

EPOS_2 = post(
    slug='dojo-card-rates-uk-comparison',
    title="Dojo card processing rates UK: how much could you save on card fees?",
    category_slug='epos-payments', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='dojo card rates UK',
    meta_desc="Dojo offers 0.3% debit and 0.7% credit card processing rates. Here's how that compares to Square, Zettle, Stripe, and the UK average — and what it means for your business.",
    og_image='https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1400&h=700&fit=crop',
    feat_alt='Card payment terminal on a counter in a UK high street business',
    tags='dojo card rates, card processing fees UK, dojo vs square, cheapest card reader UK',
    excerpt="Most UK small businesses pay 1.5–2.5% on card transactions. Dojo charges 0.3% debit and 0.7% credit. For a business doing £20,000/month in card sales, that's over £3,000 a year difference.",
    read_time=5,
    faq_items=[
        {'question': 'What are Dojo\'s card processing rates?', 'answer': 'Dojo charges 0.3% on debit card transactions and 0.7% on credit card transactions, plus 2.5p authorisation fee. These rates are available to ReeveOS customers as part of the Dojo reseller partnership.'},
        {'question': 'Is Dojo cheaper than Square?', 'answer': 'For businesses doing more than about £3,000/month in card sales, yes. Square charges a flat 1.75% per transaction. Dojo at 0.3%/0.7% is 50–80% cheaper for most UK businesses.'},
        {'question': 'Does Dojo require a contract?', 'answer': 'Dojo card machine agreements are typically 12-month terms. The card machine itself is available as a one-off purchase (£79+VAT in March 2026) or on a monthly rental basis.'},
    ],
    content="""# Dojo card processing rates UK: how much could you save on card fees?

If your business takes card payments — and in 2026, most UK business revenue comes by card — your processing fees are one of the most controllable costs you have.

Most small businesses simply accept whatever rate they're on. They signed up with Square or Zettle when they were starting out, the percentage seemed small, and they've never looked at it since.

The rate you pay may be costing you thousands of pounds per year more than it needs to.

## The UK card processing landscape

Here are the main options and their current rates:

| Provider | Debit rate | Credit rate | Other fees |
|---|---|---|---|
| Dojo (via ReeveOS) | 0.3% | 0.7% | 2.5p auth fee |
| Square | 1.75% | 1.75% | No monthly fee |
| Zettle by PayPal | 1.75% | 1.75% | No monthly fee |
| SumUp | 0.69–1.69% | 0.69–1.69% | Depending on plan |
| Stripe | 1.5% | 1.5% | +20p per transaction |
| Worldpay | Varies | Varies | Monthly fees + rates |
| UK average (SMEs) | ~0.9–1.2% | ~1.5–2% | Various |

The UK average card processing rate for small businesses is roughly 1–2% depending on card mix. Dojo at 0.3%/0.7% is 50–85% cheaper.

## What this means in pounds

Let's use a real example. A salon doing £8,000/month in card sales with a typical 70/30 debit/credit split.

**On Square (1.75% flat):**
£8,000 × 1.75% = £140/month = £1,680/year

**On Dojo (0.3% debit / 0.7% credit):**
(£5,600 × 0.3%) + (£2,400 × 0.7%) = £16.80 + £16.80 = £33.60/month = £403/year

**Annual saving: £1,277**

Now scale that to a restaurant doing £30,000/month in card sales:

**Square:** £30,000 × 1.75% = £525/month = £6,300/year
**Dojo:** (£21,000 × 0.3%) + (£9,000 × 0.7%) = £63 + £63 = £126/month = £1,512/year

**Annual saving: £4,788**

These are not theoretical numbers. They're the actual difference between the two rates applied to real UK business volumes.

## Why is Dojo so much cheaper?

Dojo operates as a payment facilitator (rather than a full acquiring bank) and passes the interchange savings directly through to merchants at competitive rates. They've built their business model around volume — acquiring large numbers of UK SME merchants at low rates rather than maximising margin per merchant.

The 0.3%/0.7% rates we quote are available through ReeveOS's Dojo reseller partnership. Independent businesses can get Dojo directly but may not always access the same rates.

## The Dojo terminal and agreement

Dojo's card machine (terminal) is a standalone contactless device. Options in March 2026:
- One-off purchase: £79+VAT
- Monthly rental: £10/month+VAT (plus a £10/month platform fee)
- iPhone Tap to Pay: available for contactless-only acceptance

Agreements are typically 12-month terms.

## The real question to ask yourself

Take your last 3 months of card sales. Total them up. Multiply by your current processing rate. That's what you paid in processing fees.

Now multiply the same total by 0.3% (for your debit card portion) and 0.7% (for your credit card portion).

The difference is money your business is paying unnecessarily every month.

For most UK independent businesses processing more than £5,000/month in card sales, switching to Dojo rates pays back the cost of any terminal within the first month.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# MARKETING & GROWTH
# ════════════════════════════════════════════════════════════════

MARKETING_1 = post(
    slug='google-business-profile-uk-small-business',
    title="Google Business Profile: the 30-minute setup guide for UK high street businesses",
    category_slug='marketing', site='reeveos',
    content_type='tutorial', priority='p1',
    keyword='google business profile setup UK',
    meta_desc="A complete step-by-step guide to setting up Google Business Profile for UK salons, restaurants, barbers, and small businesses. Rank on Google Maps in your area.",
    og_image='https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?w=1400&h=700&fit=crop',
    feat_alt='Small business owner updating their Google Business Profile on a laptop',
    tags='Google Business Profile, local SEO UK, Google Maps business, small business Google listing',
    excerpt="When someone searches for a salon, barber, or restaurant near them, Google Business Profile determines whether they find you. 30 minutes now can bring new clients for years.",
    read_time=7,
    faq_items=[
        {'question': 'Is Google Business Profile free?', 'answer': 'Yes, completely free. Creating and managing a Google Business Profile costs nothing. It is separate from Google Ads — you do not need to pay for a listing.'},
        {'question': 'How long does it take to appear on Google after setting up?', 'answer': 'Most businesses appear in Google search results within a few days of completing verification. Full ranking in local searches can take 2–4 weeks as Google indexes the listing.'},
        {'question': 'How do I get more Google reviews for my business?', 'answer': 'Ask at the right moment — when the client is happy, immediately after the service. Send the review link via WhatsApp or text right then. Google provides a short link for your listing you can share directly.'},
    ],
    content="""# Google Business Profile: the 30-minute setup guide for UK high street businesses

When someone in your town types "salon near me" or "best barber [your town]" into Google, what determines whether they find your business?

It is your Google Business Profile.

Not your website. Not your Instagram. Your Google Business Profile is the single most important free marketing tool available to a UK high street business, and it takes 30 minutes to set up properly.

If you already have a profile but set it up years ago and haven't touched it since, this guide covers what you should update. A properly optimised profile in 2026 looks very different from one set up in 2019.

## Why this matters so much

Google's research shows that 76% of people who search for a local business on Google visit one within 24 hours.

When someone searches for your type of business in your area, they see a map with three listings — the "local pack." Businesses in that pack get dramatically more clicks than those below it or in the organic results.

Getting into the local pack comes down to three things:
1. How complete and accurate your Google Business Profile is
2. How many recent, positive reviews you have
3. How close you are to the searcher

You can't control the distance. You can control the first two entirely.

## Step 1: Find or create your profile

Go to business.google.com. Sign in with your Google account.

Search for your business name. If it already exists (Google sometimes creates basic listings automatically), click "Claim this business." If it doesn't exist, click "Add your business."

## Step 2: Fill in every field completely

This is where most business owners stop early. Don't. Complete every field.

**Business name.** Your exact trading name. Do not add keywords (e.g. "Bella's Salon — Best Haircut London" is against Google's guidelines and can get you penalised).

**Category.** Your primary category is the most important. Choose the most specific one available — "Hair Salon," "Barber Shop," "Beauty Salon," "Aesthetics Clinic," "Restaurant." Add secondary categories where they accurately apply.

**Address.** Your exact address as it appears in the Royal Mail database. Consistency matters — if you use "Street" on your website but "St" on your profile, this creates a trust signal discrepancy.

**Phone number.** A local number with your area code, not a 0800 or 0333 number.

**Website.** Link to your homepage or, ideally, to your booking page.

**Hours.** Every day, including different hours for public holidays if applicable. Update these whenever your hours change.

**Description.** A 750-character description of your business. Write naturally. Include your location, your specialisms, and what makes you different. Include your primary keyword once naturally.

## Step 3: Add photos — at least 10

Listings with photos receive significantly more clicks than those without.

Add:
- Your exterior (so people can find you)
- Your interior (showing the atmosphere and standard)
- Your team at work
- Examples of your work (for salons, barbers, aesthetics)
- Your products (for retail, café menus, etc.)

Photos should be well-lit and recent. They don't need to be professional photography — a good phone photo is fine.

Add new photos every few months. Google rewards active profiles.

## Step 4: Set up your booking link

In your profile, find the "Bookings" section. Add the URL of your booking page.

When someone finds you on Google Maps, a "Book" button appears. Removing friction from the booking process directly increases how many of those people actually become clients.

## Step 5: Verify your listing

Google needs to verify that you actually operate from the address you've listed. The standard verification method is a postcard with a code sent to your business address — arrives in 5–7 working days. Enter the code in your profile.

Some businesses now get video verification or phone verification instead. Follow whatever Google presents to you.

## Step 6: Get your review link

In your profile dashboard, find "Get more reviews." Copy the direct review link. Save it on your phone.

This is the link you'll send to happy clients. It takes them directly to the review form without them having to find your profile and navigate to it themselves.

## How to get reviews — the method that actually works

The best time to ask is immediately after a positive interaction, while the client is still physically with you or has just left.

**In person:** "I'm really glad you're happy with it — if you have 30 seconds, a Google review would mean the world to us. I'll send you the link now." Then send it via WhatsApp or text immediately.

**Via your booking confirmation or follow-up:** Include your review link in your automated post-appointment message. "How was your appointment? If you enjoyed it, we'd love a Google review: [link]"

Aim to respond to every review — positive and negative. Responses show potential clients that you're engaged and professional. For negative reviews, a calm, helpful response matters more than the negative review itself.

## After setup: what to do monthly

- Add 2–3 new photos
- Respond to any new reviews
- Update your posts (Google lets you post updates, offers, and events — these appear in your profile)
- Check your insights (Google shows you how many people found you, called you, or visited your website through the profile)

A complete, active Google Business Profile with regular new photos and a steady stream of reviews will consistently bring new clients to your business — for free, indefinitely.
""".strip()
)

MARKETING_2 = post(
    slug='making-tax-digital-uk-small-business-2026',
    title="Making Tax Digital 2026: what every UK high street business owner needs to do now",
    category_slug='marketing', site='reeveos',
    content_type='cluster', priority='p1',
    keyword='making tax digital UK small business',
    meta_desc="Making Tax Digital for Income Tax becomes mandatory in April 2026 for sole traders over £50,000. Here's exactly what you need to do and by when.",
    og_image='https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=1400&h=700&fit=crop',
    feat_alt='Small business owner reviewing financial records on laptop for HMRC digital tax filing',
    tags='making tax digital 2026, MTD income tax, HMRC digital records, sole trader tax UK',
    excerpt="Making Tax Digital for Income Tax is mandatory for sole traders over £50,000 from April 2026. If that includes you, here's what you need to do before the deadline.",
    read_time=6,
    faq_items=[
        {'question': 'Who does Making Tax Digital for Income Tax affect in 2026?', 'answer': 'From April 2026, sole traders and landlords with annual income over £50,000 must keep digital records and submit quarterly updates to HMRC using MTD-compatible software.'},
        {'question': 'What software do I need for Making Tax Digital?', 'answer': 'You need HMRC-recognised MTD-compatible software. Options include Xero, QuickBooks, Sage, and FreeAgent. Some accounting software providers offer free tiers for simple businesses.'},
        {'question': 'What happens if I miss the Making Tax Digital deadline?', 'answer': 'HMRC has indicated a phased approach to penalties initially, but ultimately non-compliance will attract financial penalties. Getting set up before the April 2026 deadline is strongly recommended.'},
    ],
    content="""# Making Tax Digital 2026: what every UK high street business owner needs to do now

If you run a salon, barbershop, aesthetics clinic, restaurant, or any other sole trader business in the UK, and your income is over £50,000 a year — this deadline applies to you.

Making Tax Digital for Income Tax (MTD ITSA) becomes mandatory in April 2026 for sole traders earning over £50,000. A year later, in April 2027, the threshold drops to £30,000.

This is not a small administrative change. It affects how you record your income, how often you report to HMRC, and what software you need to use.

## What Making Tax Digital for Income Tax actually means

Currently, most sole traders submit one Self Assessment tax return per year. Under MTD for Income Tax, you will need to:

1. Keep digital records of your income and expenses throughout the year
2. Submit quarterly updates to HMRC (every 3 months)
3. Submit a final end-of-year declaration confirming your total income

The quarterly updates replace the annual Self Assessment for income tax reporting. You will still complete a Self Assessment for anything outside the scope of MTD.

## Who is affected in April 2026?

**April 2026 (year 1):** Sole traders and landlords with total annual income over £50,000.

**April 2027 (year 2):** Sole traders and landlords with total annual income over £30,000.

Partnerships are expected to follow in a later phase (not yet confirmed).

If your business is a limited company rather than a sole trader structure, MTD for Corporation Tax will come later — this current phase applies to sole traders specifically.

## What you need to do before April 2026

### Step 1: Check if you're affected

Add up your total income for the 2024–25 tax year (the year ending April 2025). If it exceeds £50,000, you are in scope for April 2026.

If you're not sure, check your 2024–25 Self Assessment return once completed, or speak to your accountant.

### Step 2: Choose MTD-compatible software

You must use HMRC-recognised software. The main options for small businesses:

- **Xero** — popular with businesses using an accountant. Good integration with bank feeds.
- **QuickBooks** — has free tier options for simple businesses. Note: Xero and QuickBooks have increased their pricing significantly in 2025–2026.
- **Sage** — Sage has a free API and is competitive on pricing.
- **FreeAgent** — free for businesses with NatWest/RBS banking accounts.

ReeveOS's accounting integrations (Sage via free API, Xero) allow your booking and payment data to flow automatically into your accounting software, reducing manual entry significantly.

### Step 3: Connect your bank feeds

Most MTD software connects directly to your business bank account and imports transactions automatically. Set this up as early as possible — it saves hours of manual bookkeeping.

### Step 4: Understand your quarterly deadlines

Under MTD, your quarterly submission periods will be:
- Q1: 6 April – 5 July (submit by 7 August)
- Q2: 6 July – 5 October (submit by 7 November)
- Q3: 6 October – 5 January (submit by 7 February)
- Q4: 6 January – 5 April (submit by 7 May)

You do not need to pay tax quarterly — just report. Your tax payment schedule remains broadly the same.

### Step 5: Get your bookkeeping habits in order

The biggest practical challenge is keeping records up to date throughout the year rather than pulling everything together once a year. MTD requires contemporaneous digital records — not reconstructing the year from bank statements in January.

For salon and service business owners, this means:
- Using your booking software to record all sales automatically
- Connecting your payment terminal to your accounting software
- Photographing or scanning receipts for expenses as you incur them (apps like Receipt Bank or Dext help here)
- Reconciling your accounts monthly rather than annually

## The honest view on effort required

If you currently do your own bookkeeping for a straightforward sole trader business, MTD will require you to change your habits and invest in software you may not currently use.

If you already use cloud accounting software with bank feeds, the additional work is minimal — you're essentially already doing what MTD requires, just without the quarterly submission step.

If you currently hand your bank statements and a shoebox of receipts to an accountant once a year, you have a bigger transition ahead. The sooner you start, the less painful it will be.

## Finding an accountant for MTD

If you don't currently work with an accountant and are in scope for April 2026, now is the time to find one. Good MTD-aware accountants are busy and many are already booked up for the transition period.

Look for accountants who advertise MTD readiness. HMRC maintains a list of MTD-compatible software, which your accountant should be working with already.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# REEVENOW — BOOKING GUIDES (consumer-facing)
# ════════════════════════════════════════════════════════════════

CONSUMER_1 = post(
    slug='what-to-expect-first-aesthetics-appointment',
    title="What to expect at your first aesthetics appointment in the UK",
    category_slug='booking-guides', site='reevenow',
    content_type='cluster', priority='p1',
    keyword='first aesthetics appointment what to expect',
    meta_desc="Booking your first Botox, filler, or skin treatment appointment? Here's exactly what happens, what questions to ask, and how to find a reputable clinic.",
    og_image='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1400&h=700&fit=crop',
    feat_alt='Client having a consultation with an aesthetics practitioner before a treatment',
    tags='aesthetics appointment, first Botox, filler treatment UK, aesthetics clinic UK',
    excerpt="Never had an aesthetics treatment before? Here's everything that happens from booking to aftercare — and how to make sure you're seeing someone properly qualified.",
    read_time=7,
    faq_items=[
        {'question': 'Do I need a consultation before aesthetics treatments?', 'answer': 'Yes — any reputable aesthetics clinic will require a consultation before your first treatment. This covers your medical history, what you want to achieve, and what\'s realistic. Walk away from any clinic that offers to treat you without a consultation.'},
        {'question': 'How do I know if an aesthetics practitioner is qualified?', 'answer': 'In the UK, practitioners performing injectable treatments should have a healthcare background (nurse, doctor, dentist) and be registered with their professional body. Ask to see their qualifications and check their registration number on the relevant professional register.'},
        {'question': 'What should I not do before an aesthetics appointment?', 'answer': 'Avoid alcohol for 24 hours before, avoid blood-thinning medications and supplements (aspirin, ibuprofen, fish oil) unless prescribed by a doctor, and avoid applying makeup to the treatment area on the day.'},
    ],
    content="""# What to expect at your first aesthetics appointment in the UK

Thinking about your first aesthetics treatment — Botox, fillers, a chemical peel, or something else — but not sure what to expect?

You're not alone. The aesthetics industry has grown enormously in the UK, but many people still book their first appointment with a mix of excitement and uncertainty.

This guide walks you through exactly what happens, from choosing a clinic to aftercare, so you can go in feeling informed rather than anxious.

## Before you book: finding a reputable clinic

Not all aesthetics practitioners are equal. In the UK, the industry is partially regulated — some treatments are restricted to healthcare professionals, others can be performed by anyone with a training certificate.

For injectable treatments (Botox and dermal fillers), look for:

**A healthcare background.** The safest practitioners are doctors, nurses, dentists, or other regulated healthcare professionals. They have the medical training to assess contraindications, manage complications, and understand anatomy properly.

**Professional body registration.** A nurse should be registered with the NMC (Nursing and Midwifery Council). A doctor with the GMC (General Medical Council). Ask for their registration number and check it.

**A physical clinic address.** Be cautious of practitioners offering treatments from temporary venues, people's homes, or at special events. These settings make it harder to follow up if you have a concern after treatment.

**A proper consultation process.** Any reputable clinic will want to have a consultation with you before performing any treatment. This is where they take your medical history, explain the treatment, set realistic expectations, and get your informed consent.

## The consultation

Your first appointment will typically start with a consultation. This might be a separate appointment before the treatment, or it might happen at the beginning of the same appointment.

Expect to be asked about:
- Your medical history, including any chronic conditions
- Current medications (including supplements and over-the-counter pain relief)
- Previous aesthetic treatments and any reactions
- Allergies
- Pregnancy or breastfeeding status
- What you're hoping to achieve

Be completely honest. The practitioner is asking these questions to keep you safe. Conditions like blood disorders, certain skin conditions, and some medications are contraindications for specific treatments.

You'll also be shown before-and-after photographs of similar treatments, given a realistic expectation of results, and told about the recovery and aftercare.

This is also your opportunity to ask questions. Good questions to ask:
- What are the risks of this treatment?
- What does the aftercare involve?
- What happens if I'm not happy with the result?
- How many times have you performed this treatment?
- What would you do in the event of a complication?

A practitioner who answers these questions patiently and honestly is a good sign. One who dismisses your concerns or rushes through the consultation is not.

## The treatment itself

What happens depends entirely on which treatment you're having. Here's a brief overview of the most common ones.

**Anti-wrinkle injections (Botox):** Small injections using a very fine needle into specific facial muscles. Mildly uncomfortable — most people describe it as a sharp pinch. Takes about 15 minutes. Results appear gradually over 2–7 days and typically last 3–4 months.

**Dermal fillers:** Injections of hyaluronic acid gel to add volume or smooth lines. More sensation than anti-wrinkle injections due to the volume being placed. Takes 20–45 minutes. Results are immediate (though there will be some swelling initially).

**Chemical peels:** A solution is applied to the skin that causes controlled exfoliation. Mild peels feel warm and tingly. Stronger peels cause more sensation and require more downtime. Your skin will look red initially.

**Skin boosters and Polynucleotides:** Series of micro-injections into the skin, often over a large area. Can be uncomfortable. Multiple sessions are typically needed.

## Immediately after your treatment

You will likely have some redness, swelling, or small bumps at injection sites. For injectable treatments, this usually resolves within a few hours. You may have minor bruising that takes a few days to clear.

Most people leave looking a little flushed but are fine to go about their day. Your practitioner will tell you what to avoid after your specific treatment.

Common post-treatment advice for injectables:
- Avoid touching or applying pressure to the treatment area
- Stay upright for 4 hours (for anti-wrinkle injections specifically)
- Avoid strenuous exercise for 24 hours
- Avoid alcohol for 24 hours
- Avoid extreme heat (saunas, hot yoga) for 24–48 hours

## Red flags to walk away from

**No consultation required.** A practitioner willing to treat you without a consultation is not following safe practice.

**Pressure to add more treatments.** Reputable clinics don't upsell aggressively in the room.

**Prices dramatically lower than the area average.** Extremely cheap injectable treatments usually mean untrained practitioners, diluted products, or inappropriate settings.

**No aftercare information.** You should leave with clear written information about aftercare and a number to call if you have any concerns.

**They cannot tell you the product or batch number used.** For injectable treatments, the product name and batch number should be recorded in your notes.

If anything feels wrong, it is always better to leave and find a different clinic.

## Finding a clinic you can trust

Look for clinics that require a consultation, take your medical history seriously, and use digital consent forms that record exactly what you agreed to. This is standard practice at well-run clinics and it is also there to protect you.

You can search for rated aesthetics clinics in your area through Reeve Now, where listed practitioners have been reviewed by real clients.
""".strip()
)

CONSUMER_2 = post(
    slug='salon-etiquette-uk-tipping-cancellations',
    title="Salon etiquette UK: tipping, cancellations, and everything you need to know",
    category_slug='booking-guides', site='reevenow',
    content_type='cluster', priority='p2',
    keyword='salon etiquette UK',
    meta_desc="Should you tip your hairdresser in the UK? What happens if you need to cancel? How early should you arrive? The unwritten rules of UK salon visits explained.",
    og_image='https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?w=1400&h=700&fit=crop',
    feat_alt='Client receiving a haircut at a UK salon with stylist working on their hair',
    tags='salon etiquette UK, should I tip hairdresser UK, salon cancellation policy, salon tipping',
    excerpt="Do you tip your hairdresser in the UK? How much notice should you give to cancel? What should you do if you're not happy with the result? Everything explained simply.",
    read_time=5,
    faq_items=[
        {'question': 'Should I tip my hairdresser in the UK?', 'answer': 'Tipping is appreciated but not obligatory in UK salons. If you are happy with your service, 10–15% is a reasonable tip. If the owner cuts your hair, tipping is still appropriate — it is a common misconception that you should not tip business owners.'},
        {'question': 'How much notice should I give to cancel a salon appointment?', 'answer': 'Most UK salons ask for 24–48 hours notice to cancel or rearrange. Check the specific salon\'s policy when booking. Cancelling at the last minute or not showing up may mean you forfeit any booking fee paid.'},
        {'question': 'What do I do if I\'m unhappy with my haircut?', 'answer': 'Tell the stylist at the time if possible — they can often adjust during the appointment. If you only notice when you get home, call or message the salon promptly (within a few days) and explain the issue. Most reputable salons will offer to fix it free of charge.'},
    ],
    content="""# Salon etiquette UK: tipping, cancellations, and what you need to know

UK salon etiquette is a bit of a mystery to many people. Do you tip? How much? What happens if you need to cancel? What should you bring to a colour appointment? What do you do if you hate the result?

These are questions people feel awkward asking out loud. Here's the straightforward guide.

## Do you tip at a UK salon?

Tipping in UK salons is appreciated but not obligatory in the way it is in American culture.

The general guidance:
- **If you're happy with the service:** A tip of 10–15% is appreciated and appropriate.
- **If you're very happy with a longer, more complex service:** Up to 15–20% is reasonable.
- **If you're unhappy:** You're not obligated to tip, and it's better to mention the issue so it can be addressed.

One common misconception: if the business owner cuts your hair, you still tip. It's appropriate regardless of whether the person is an employee or the owner.

How to tip: in cash given directly is most appreciated (the full amount reaches the person). You can also add a tip when paying by card — just ask "can I add a tip to the card?"

## How much notice to cancel

Most UK salons ask for 24–48 hours notice to cancel or rearrange.

If you have paid a booking fee, check the cancellation policy clearly — typically stated during booking. Cancellations within the notice period usually mean the booking fee is not refunded.

If something genuinely urgent comes up (illness, a family emergency), call the salon as soon as you know. Most salons will be understanding about genuine emergencies and will either rebook you or use their discretion about the fee.

Do not just not show up. It wastes the stylist's time and the appointment slot that another client could have filled.

## What to bring to a colour appointment

For hair colour appointments, useful things to bring:
- **Inspiration photos.** Bring several — not just one. Photos help your stylist understand the shade, tone, and finish you have in mind. Be aware that your result may vary from the photo depending on your natural hair colour, condition, and texture.
- **Wear an old or dark top.** Colour processing can splash or drip.
- **Arrive with clean, dry hair unless told otherwise.** Some salons prefer to colour freshly washed hair, others don't. Check when booking.

## What to do if you're not happy with the result

This is the conversation most people dread. But raising it is much better than stewing at home and never going back.

**If you're in the chair and something isn't right:** Say something while you're still in the salon. Stylists are not mind readers and it's much easier to adjust before you've paid and left.

**If you only notice at home:** Call or message the salon within a day or two. Explain what you're unhappy about calmly and specifically. "The colour is more orange than I expected" is more helpful than "I don't like it."

Most reputable salons will offer to correct the issue for free within a reasonable timeframe. This is industry standard practice — it's called a "correction appointment" and good salons do them without a fuss.

## How early to arrive

Arriving 5–10 minutes before your appointment is ideal. Arriving early gives you time to get settled, hang up your coat, and discuss what you want before the stylist's time starts.

If you're running late, phone ahead. Even 5 minutes notice helps the salon manage their diary. If you arrive more than 10–15 minutes late, the stylist may not be able to complete the full service, especially if they have another client directly after.

## Phones during the appointment

This varies by salon. For a cut and blow-dry, a quick look at your phone occasionally is generally fine. For a colour consultation or any service where the stylist needs you to look in the mirror and give feedback, put it away.

If you need to take a call, let the stylist know beforehand.

## Bringing children

Some salons welcome children as clients from a young age. Others have policies about young children accompanying adult clients, particularly if the salon is small or busy.

If in doubt, call ahead and ask. It's a quick question that avoids an awkward moment at the door.

## The consultation for a new service or new stylist

If it's your first time with a stylist, or if you're trying something significantly different, ask for a consultation either before your appointment or at the beginning of it.

Use this time to show your inspiration photos, explain your lifestyle (how much time you spend styling, how often you can come in for maintenance), and ask about realistic outcomes for your specific hair type and condition.

A good consultation sets up a much better result than sitting down and hoping for the best.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# REEVENOW — BEST OF (consumer-facing)
# ════════════════════════════════════════════════════════════════

BESTOF_1 = post(
    slug='best-barbers-sheffield-2026',
    title="The best barbers in Sheffield 2026: where to get a proper cut in the city",
    category_slug='best-of', site='reevenow',
    content_type='best-of', priority='p1',
    keyword='best barbers Sheffield',
    meta_desc="The best independent barbershops in Sheffield in 2026. From the city centre to Kelham Island and beyond — where Sheffield's men go for a great cut.",
    og_image='https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=1400&h=700&fit=crop',
    feat_alt='Interior of a modern independent barbershop in Sheffield with barber chairs and mirrors',
    tags='best barbers Sheffield, Sheffield barbershop, haircut Sheffield, barber near me Sheffield',
    excerpt="Sheffield has a fantastic barbershop scene. From classic wet shaves in the city centre to modern cuts in Kelham Island, here's where to go for a great haircut in the Steel City.",
    read_time=5,
    faq_items=[
        {'question': 'Should I book in advance at Sheffield barbershops?', 'answer': 'For the most popular shops, booking ahead is recommended especially on Fridays and Saturdays. Many Sheffield barbershops also take walk-ins — call ahead to check availability.'},
        {'question': 'How much does a haircut cost in Sheffield?', 'answer': 'A standard cut at a Sheffield independent barbershop typically costs £12–£20. Beard trims add £5–£8. Traditional wet shaves range from £15–£25.'},
    ],
    content="""# The best barbers in Sheffield 2026: where to get a proper cut in the city

Sheffield's barbershop scene is one of the best in the North. The city has always had a strong independent business culture, and that shows in the quality and variety of barbershops across the city.

Whether you want a quick grade 2 on the way to work, a considered fade and skin care consultation, or a traditional hot towel wet shave on a Saturday morning, Sheffield has somewhere for you.

Here's our guide to the independent barbershops worth booking.

## What makes a great barbershop?

Before getting into specific recommendations, it's worth being clear about what we think matters.

**Consistency.** The best shops deliver the same quality regardless of which barber you see or which day you go in. The cut you loved last month should look the same next month.

**Communication.** A good barber asks questions before cutting. They understand what you're asking for, they push back if something won't work with your hair type, and they don't just do what they think looks good.

**Cleanliness.** Tools should be properly sanitised between clients. Capes should be clean. The shop should feel professional.

**A clear booking and queueing system.** Your time matters. A shop that keeps you waiting 45 minutes with no information isn't respecting it.

## Kelham Island and the west side

Kelham Island has become one of Sheffield's most vibrant neighbourhoods, and its barbershops reflect the creative, community-minded character of the area. Independent shops here tend to attract a younger clientele and lean toward modern cuts and contemporary styles.

These shops typically do a good range of textured cuts, fades, and skin fades. They're also typically busy on weekends, so booking ahead is recommended.

## The city centre

The city centre has a mix of traditional and modern barbershops. Traditional shops doing conventional cuts and classic wet shaves have been part of Sheffield high street culture for decades. Alongside them, newer shops have opened offering a wider range of cuts, beard work, and grooming products.

City centre barbershops are convenient for commuters and office workers looking for a lunchtime or post-work cut. Many operate appointment systems alongside walk-ins.

## Sharrow and Broomhall

These diverse neighbourhoods south of the city centre have barbershops catering to a wide range of hair types including Afro-Caribbean and textured hair specialists. If you have 4C hair or need a specialist for textured cuts, this area has excellent options.

## What to expect when you visit

Most Sheffield barbershops welcome both walk-ins and appointments. Calling ahead to check wait times before walking in is good practice, especially on Saturdays.

Prices for a standard cut typically range from £12 to £20 depending on the shop and the service. Beard trims add £5–£8. Hot towel shaves range from £15 to £25.

Tipping is appreciated but not obligatory. £2–£3 on top of a cut is a decent tip if you're happy with the service.

## Book direct and save

Many of Sheffield's best independent barbershops now offer direct booking through Reeve Now. Booking direct means:
- No commission taken from the barbershop (they keep more of what you pay)
- Instant booking confirmation
- Automated reminder so you don't forget
- Easy rescheduling if your plans change

Search for Sheffield barbershops on Reeve Now to find availability and book your slot.

---

*Sheffield's barbershop scene changes regularly — new shops open, recommendations evolve. We update this guide regularly based on new openings and reader recommendations. If we've missed your favourite, let us know.*
""".strip()
)

BESTOF_2 = post(
    slug='best-salons-cardiff-2026',
    title="The best salons in Cardiff and South Wales 2026: where to book your next appointment",
    category_slug='best-of', site='reevenow',
    content_type='best-of', priority='p2',
    keyword='best salons Cardiff',
    meta_desc="The best independent hair salons in Cardiff and South Wales in 2026. City centre, Canton, Pontcanna and beyond — where to get a great haircut or colour treatment.",
    og_image='https://images.unsplash.com/photo-1562322140-8baeececf3df?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1562322140-8baeececf3df?w=1400&h=700&fit=crop',
    feat_alt='Modern hair salon interior in Cardiff with styling chairs and bright mirrors',
    tags='best salons Cardiff, Cardiff hairdresser, hair salon Cardiff, South Wales salon',
    excerpt="Cardiff's independent salon scene is thriving. From city centre blowouts to neighbourhood specialists in Canton and Pontcanna, here's where to book in 2026.",
    read_time=5,
    content="""# The best salons in Cardiff and South Wales 2026

Cardiff's independent salon scene has grown significantly in the past few years. Alongside the established names that have been operating in the city for decades, a newer generation of owner-operated salons has emerged — particularly in the Pontcanna, Canton, and Roath areas.

Whether you're looking for a precision cut, a complex colour transformation, or a relaxed neighbourhood salon for a regular trim, Cardiff has excellent options.

## What to look for in a Cardiff salon

Cardiff salons range from bustling city centre operations to intimate neighbourhood studios with two or three chairs. The city centre salons tend to offer more availability and a wider range of stylists. The neighbourhood salons in Pontcanna and Canton are known for building long-term client relationships and a more personal service.

For colour work, Cardiff has some genuinely talented colourists. Balayage, colour correction, and specialist treatments are well-represented — but research specific stylists before booking for complex colour, not just the salon name.

## The city centre

Cardiff city centre has a concentration of salons catering to shoppers, office workers, and people passing through. These tend to have more appointment slots available and are convenient for those coming into the city anyway.

Prices in the city centre tend to reflect higher overheads — expect to pay city rates for cuts and colour.

## Pontcanna and Canton

These leafy residential areas southwest of the city centre have developed a strong independent business culture. Salons here tend to be smaller, owner-operated, and focused on building a regular local clientele.

The atmosphere is typically more relaxed than the busier city centre salons. These are the kind of places where the stylist remembers your name, your last cut, and what you've been up to.

## Roath and the east side

Roath's eclectic mix of independent businesses includes several good salons catering to the area's diverse community. For Afro-Caribbean hair, textured cuts, and specialist natural hair care, Roath and Cardiff's other diverse neighbourhoods have strong options.

## South Wales beyond Cardiff

If you're in the Vale of Glamorgan, Bridgend, Rhondda, or further afield in South Wales, the same principles apply — look for owner-operated independent salons with a track record in your specific needs.

For aesthetics clinics specifically in South Wales, the area around Barry and the Vale has seen significant growth in high-quality independent aesthetics practitioners.

## Book direct

Many Cardiff and South Wales salons now offer direct online booking through Reeve Now. Direct booking means no waiting on hold, instant confirmation, and automated reminders before your appointment.

Search salons near you on Reeve Now, check availability, and book your slot in under two minutes.

---

*This guide is updated regularly as new salons open and recommendations change. Know a Cardiff salon that belongs here? We want to hear about it.*
""".strip()
)

BESTOF_3 = post(
    slug='best-gyms-nottingham-2026',
    title="The best gyms in Nottingham 2026: independent fitness studios worth joining",
    category_slug='best-of', site='reevenow',
    content_type='best-of', priority='p2',
    keyword='best gyms Nottingham',
    meta_desc="The best independent gyms and fitness studios in Nottingham in 2026. From city centre studios to neighbourhood gyms — alternatives to the big chains worth considering.",
    og_image='https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1200&h=630&fit=crop',
    feat_image='https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1400&h=700&fit=crop',
    feat_alt='Modern independent gym in Nottingham with free weights and training equipment',
    tags='best gyms Nottingham, Nottingham fitness studio, gym near me Nottingham, independent gym Nottingham',
    excerpt="Nottingham has a thriving independent gym scene beyond the big chains. These are the fitness studios worth joining for a more personal, community-focused workout experience.",
    read_time=5,
    content="""# The best gyms in Nottingham 2026: independent fitness studios worth joining

Nottingham's fitness scene has evolved considerably. Alongside the national chains, a growing number of independent gyms and boutique studios have established themselves — particularly in the city centre, Hockley, and the residential neighbourhoods around it.

If you're looking for something more personal than a large chain gym, with people who know your name and programming that actually evolves, Nottingham's independent scene is worth exploring.

## Why independent gyms often win

This isn't anti-chain sentiment — the big chains have their advantages (lots of equipment, multiple locations, often cheaper monthly costs). But independent gyms offer things the chains structurally cannot:

**Community.** In a 200-member independent gym, you know the people you train with. The owner knows your name and your goals. There's a social fabric that a 3,000-member chain gym rarely develops.

**Expertise.** Many independent gym owners are coaches themselves who care deeply about programming and results. They're on the gym floor, not in a regional head office.

**Flexibility.** Membership freezes, pauses, and personal arrangements are far more common at independent gyms. You're a real person, not a direct debit number.

## The city centre and Lace Market

The city centre has several strength and conditioning gyms alongside commercial facilities. For powerlifting, Olympic lifting, or more specialist training, this area has options beyond the standard gym floor.

CrossFit boxes have also established themselves in and around the city centre, offering structured community-based training with experienced coaches.

## Hockley and the creative quarter

Hockley and the area around it has attracted boutique fitness studios — yoga, Pilates, HIIT, boxing and combat sports. These studios tend to be class-based, with strong community atmospheres and members who train together regularly.

Class booking is typically online and spaces fill up quickly for popular sessions. Book in advance.

## Residential neighbourhood gyms

Some of the best independent gyms in Nottingham are the local neighbourhood gyms that have been serving their communities for years. These are the gyms that were there before boutique fitness became a trend and will be there after it. Often cheaper than city centre options, personal service, and genuinely invested in their members' progress.

## What to look for before joining

**Try a free session.** Almost every independent gym will offer a free trial or taster session. Use it. The atmosphere and coaching quality you experience in that session will tell you more than any website.

**Talk to the members.** The people already training there are your best source of honest feedback. Ask how long they've been a member and what keeps them coming back.

**Check the equipment for your specific needs.** A stunning Pilates studio doesn't help if you want to deadlift. Visit in person before committing.

**Understand the cancellation terms.** Before signing any membership agreement, know how much notice you need to give and what happens if you need to pause.

## Book classes and sessions direct

Many Nottingham independent gyms and fitness studios list their classes and availability on Reeve Now. You can search by location, check real-time availability, and book without calling or emailing.

Direct booking also means no commission to a third-party platform — the gym keeps more of what you pay.
""".strip()
)


# ════════════════════════════════════════════════════════════════
# SEED
# ════════════════════════════════════════════════════════════════

ALL_ARTICLES = [
    SALON_1, SALON_2, SALON_3,
    AESTHETICS_1, AESTHETICS_2, AESTHETICS_3,
    BARBER_1, BARBER_2,
    GYMS_1, GYMS_2,
    EPOS_1, EPOS_2,
    MARKETING_1, MARKETING_2,
    CONSUMER_1, CONSUMER_2,
    BESTOF_1, BESTOF_2, BESTOF_3,
]

def seed():
    print("\n📦 ReeveOS Full Category Seed\n")

    # Clear and re-seed categories
    cats_col.delete_many({})
    cats_col.insert_many(CATEGORIES)
    print(f"  {len(CATEGORIES)} categories seeded")

    # Remove any existing articles with same slugs, then insert
    slugs = [a['slug'] for a in ALL_ARTICLES]
    posts_col.delete_many({'slug': {'$in': slugs}})
    posts_col.insert_many(ALL_ARTICLES)
    print(f"  {len(ALL_ARTICLES)} articles seeded")

    print("\n✅ Done\n")
    print("Articles by category:")
    by_cat = {}
    for a in ALL_ARTICLES:
        cat_id = a['category']
        cat_name = next((c['name'] for c in CATEGORIES if c['_id'] == cat_id), 'Unknown')
        by_cat.setdefault(cat_name, []).append(a['slug'])

    for cat_name, slugs in sorted(by_cat.items()):
        print(f"\n  {cat_name} ({len(slugs)} articles):")
        for s in slugs:
            print(f"    - {s}")

    client.close()

if __name__ == '__main__':
    seed()
