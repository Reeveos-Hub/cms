import type { CollectionConfig } from 'payload'

export const BlogPosts: CollectionConfig = {
  slug: 'blog-posts',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'category', 'status', 'contentType', 'priority', 'publishedAt'],
    group: 'Blog',
    preview: (doc: any) => {
      if (doc?.slug && doc?.site) {
        const base = doc.site === 'reeveos' ? 'https://reeveos.app' : 'https://reevenow.com'
        return `${base}/blog/${doc.slug}`
      }
      return null
    },
  },
  versions: {
    drafts: { autosave: { interval: 30000 } },
    maxPerDoc: 20,
  },
  access: {
    read: ({ req }) => {
      if (req.user?.role === 'super_admin' || req.user?.role === 'platform_admin') return true
      return { status: { equals: 'published' } }
    },
    create: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    update: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    delete: ({ req }) => req.user?.role === 'super_admin',
  },
  hooks: {
    beforeChange: [
      ({ data }) => {
        if (data.status === 'published' && !data.publishedAt) {
          data.publishedAt = new Date().toISOString()
        }
        return data
      },
    ],
  },
  fields: [

    // ── IDENTITY ──────────────────────────────────────────────────────────
    {
      name: 'title',
      type: 'text',
      required: true,
      admin: { description: 'The article headline. Include the target keyword. Be specific — vague titles rank poorly.' },
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
      admin: { description: 'URL slug — lowercase, hyphens, no spaces. Under 60 chars. e.g. "fresha-alternatives-uk-2026"' },
    },
    {
      name: 'site',
      type: 'select',
      required: true,
      defaultValue: 'reeveos',
      options: [
        { label: 'reeveos.app — for business owners', value: 'reeveos' },
        { label: 'reevenow.com — for consumers', value: 'reevenow' },
      ],
    },
    {
      name: 'category',
      type: 'relationship',
      relationTo: 'blog-categories',
      required: true,
    },
    {
      name: 'status',
      type: 'select',
      required: true,
      defaultValue: 'draft',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'In Review', value: 'review' },
        { label: 'Published', value: 'published' },
      ],
    },
    {
      name: 'publishedAt',
      type: 'date',
      admin: { description: 'Leave blank — auto-set on first publish' },
    },
    {
      name: 'lastVerifiedAt',
      type: 'date',
      admin: { description: 'When was competitor pricing / factual data last verified? Facts go stale fast.' },
    },

    // ── STRATEGY ──────────────────────────────────────────────────────────
    {
      name: 'contentType',
      type: 'select',
      required: true,
      defaultValue: 'cluster',
      options: [
        { label: 'Pillar Page (3000–5000 words, links to all cluster articles)', value: 'pillar' },
        { label: 'Cluster Article (supports a pillar, 1200–2000 words)', value: 'cluster' },
        { label: 'Competitor Alternative', value: 'competitor-alternative' },
        { label: 'Competitor Comparison (vs ReeveOS)', value: 'competitor-vs' },
        { label: 'Pricing Intel (how much does X cost)', value: 'pricing-intel' },
        { label: 'Case Study', value: 'case-study' },
        { label: 'How-To Tutorial', value: 'tutorial' },
        { label: 'Neighbourhood Guide (reevenow)', value: 'neighbourhood-guide' },
        { label: 'Best Of List (reevenow)', value: 'best-of' },
      ],
    },
    {
      name: 'priority',
      type: 'select',
      defaultValue: 'p2',
      options: [
        { label: 'P1 — Publish immediately', value: 'p1' },
        { label: 'P2 — Within 60 days', value: 'p2' },
        { label: 'P3 — Within 90 days', value: 'p3' },
      ],
    },
    {
      name: 'pillarPage',
      type: 'relationship',
      relationTo: 'blog-posts',
      admin: { description: 'Cluster articles only — link to parent pillar page for internal linking.' },
    },
    {
      name: 'competitorName',
      type: 'text',
      admin: { description: 'e.g. "Fresha", "Booksy". Competitor content only.' },
    },
    {
      name: 'relatedTool',
      type: 'select',
      options: [
        { label: 'Fresha Cost Calculator', value: 'fresha-cost-calculator' },
        { label: 'Booksy Cost Calculator', value: 'booksy-cost-calculator' },
        { label: 'No-Show Cost Calculator', value: 'no-show-calculator' },
        { label: 'EPOS Cost Comparison', value: 'epos-cost-comparison' },
        { label: 'Dojo Card Rate Calculator', value: 'dojo-rate-calculator' },
        { label: 'Business Health Grader', value: 'business-health-grader' },
        { label: 'Mindbody Cost Calculator', value: 'mindbody-cost-calculator' },
      ],
    },

    // ── SEO CORE ──────────────────────────────────────────────────────────
    {
      name: 'seo',
      type: 'group',
      label: 'SEO — Core (Title, Meta, Canonical)',
      fields: [
        {
          name: 'targetKeyword',
          type: 'text',
          required: true,
          admin: { description: 'ONE primary keyword. Use it in: title, H1, first paragraph, at least one H2, image alt text, and naturally throughout body.' },
        },
        {
          name: 'secondaryKeywords',
          type: 'text',
          admin: { description: 'Comma-separated secondary keywords to use naturally in body copy.' },
        },
        {
          name: 'metaTitle',
          type: 'text',
          admin: { description: 'Shown in Google results. 50–60 characters MAX. Target keyword near the front. Leave blank to use article title.' },
        },
        {
          name: 'metaDescription',
          type: 'textarea',
          admin: { description: '150–160 characters. Include target keyword. Write a compelling reason to click — not just a summary.' },
        },
        {
          name: 'canonicalUrl',
          type: 'text',
          admin: { description: 'Only set if this content exists at another URL that should be the official version.' },
        },
        {
          name: 'robotsMeta',
          type: 'select',
          defaultValue: 'index,follow',
          options: [
            { label: 'index,follow — standard for all published articles', value: 'index,follow' },
            { label: 'noindex,nofollow — hide from Google', value: 'noindex,nofollow' },
            { label: 'index,nofollow — index but do not pass link equity', value: 'index,nofollow' },
          ],
        },
      ],
    },

    // ── SEO SOCIAL (Open Graph + Twitter Cards) ───────────────────────────
    {
      name: 'social',
      type: 'group',
      label: 'SEO — Social Sharing (Open Graph + Twitter/X Cards)',
      admin: { description: 'Controls how this article looks when shared on Facebook, LinkedIn, WhatsApp, and Twitter/X. A strong image here dramatically increases click-through.' },
      fields: [
        {
          name: 'ogTitle',
          type: 'text',
          admin: { description: 'Title for social shares. Can be more emotional than the SEO title. Leave blank to use SEO meta title.' },
        },
        {
          name: 'ogDescription',
          type: 'textarea',
          admin: { description: '100–150 characters. Make it human and compelling — this is what shows in the link preview card.' },
        },
        {
          name: 'ogImageUrl',
          type: 'text',
          admin: { description: 'Image URL for social shares. Recommended 1200×630px. Can be an Unsplash CDN URL. This is one of the highest-impact things for social click-through.' },
        },
        {
          name: 'ogImageAlt',
          type: 'text',
          admin: { description: 'Alt text for the OG image. Describe what is literally in the image.' },
        },
        {
          name: 'twitterCard',
          type: 'select',
          defaultValue: 'summary_large_image',
          options: [
            { label: 'summary_large_image — large image preview (recommended)', value: 'summary_large_image' },
            { label: 'summary — small thumbnail', value: 'summary' },
          ],
        },
      ],
    },

    // ── IMAGES ────────────────────────────────────────────────────────────
    {
      name: 'featuredImageUrl',
      type: 'text',
      admin: { description: 'Hero image URL (Unsplash CDN or uploaded). Shown at top of article and on listing pages. Use a real, relevant photo — not a generic stock image.' },
    },
    {
      name: 'featuredImageAlt',
      type: 'text',
      admin: { description: 'Alt text for featured image. Describe what is in the image. Include target keyword if it fits naturally. REQUIRED for accessibility and SEO.' },
    },
    {
      name: 'featuredImageCaption',
      type: 'text',
      admin: { description: 'Optional caption. Captions get read more than body text — use them to reinforce the key point.' },
    },
    {
      name: 'inlineImages',
      type: 'array',
      label: 'Inline Images',
      admin: { description: 'Additional images used within the article. Each must have alt text. Use WebP format where possible for faster loading.' },
      fields: [
        {
          name: 'imageUrl',
          type: 'text',
          required: true,
          admin: { description: 'Image URL' },
        },
        {
          name: 'alt',
          type: 'text',
          required: true,
          admin: { description: 'Alt text — describe the image. Include keyword naturally if it fits.' },
        },
        {
          name: 'caption',
          type: 'text',
        },
        {
          name: 'position',
          type: 'text',
          admin: { description: 'Where in the article does this appear? e.g. "After the comparison table"' },
        },
      ],
    },

    // ── CONTENT ───────────────────────────────────────────────────────────
    {
      name: 'excerpt',
      type: 'textarea',
      required: true,
      admin: { description: '2–3 sentences shown on listing pages and in social previews. What problem does this article solve? Keep under 160 characters.' },
    },
    {
      name: 'content',
      type: 'richText',
      required: true,
      admin: { description: 'Full article. Plain English. Short sentences. Real stories. Specific numbers. One idea per paragraph.' },
    },
    {
      name: 'readTime',
      type: 'number',
      admin: { description: 'Minutes to read (200 words per minute).' },
    },
    {
      name: 'wordCount',
      type: 'number',
      admin: { description: 'Pillar pages: 3000–5000 words. Cluster articles: 1200–2000 words.' },
    },
    {
      name: 'tags',
      type: 'text',
      admin: { description: 'Comma-separated tags for related articles and internal search.' },
    },

    // ── E-E-A-T ───────────────────────────────────────────────────────────
    {
      name: 'eeat',
      type: 'group',
      label: 'E-E-A-T — Experience, Expertise, Authoritativeness, Trust',
      admin: { description: 'Google ranks content higher when it demonstrates real expertise. These fields add trust signals to the article page.' },
      fields: [
        {
          name: 'authorName',
          type: 'text',
          defaultValue: 'ReeveOS Team',
          admin: { description: 'Who wrote or verified this article. Real names build more trust than brand names.' },
        },
        {
          name: 'authorTitle',
          type: 'text',
          admin: { description: 'e.g. "Co-founder, ReeveOS" or "Salon industry specialist"' },
        },
        {
          name: 'authorBio',
          type: 'textarea',
          admin: { description: '1–2 sentences. Why should the reader trust them on this topic?' },
        },
        {
          name: 'reviewedBy',
          type: 'text',
          admin: { description: 'If a real business owner or domain expert reviewed the article, add their name and credentials. e.g. "Reviewed by Natalie, owner of Rejuvenate Skin Experts"' },
        },
        {
          name: 'sources',
          type: 'array',
          label: 'Sources and References',
          admin: { description: 'Link to sources for statistics and claims. Google rewards cited content — industry reports, government data, trade associations.' },
          fields: [
            { name: 'label', type: 'text', required: true, admin: { description: 'e.g. "NHBF UK Hair & Beauty Statistics 2025"' } },
            { name: 'url', type: 'text', required: true },
          ],
        },
        {
          name: 'lastUpdatedNote',
          type: 'text',
          admin: { description: 'Shown to readers — e.g. "Pricing last verified March 2026. Updated quarterly."' },
        },
      ],
    },

    // ── SCHEMA MARKUP ─────────────────────────────────────────────────────
    {
      name: 'schema',
      type: 'group',
      label: 'Schema Markup — Structured Data for Google Rich Results',
      admin: { description: 'Tells Google exactly what type of content this is. FAQ schema creates expandable boxes in search results. HowTo schema shows numbered steps. Both can double your visible search real estate.' },
      fields: [
        {
          name: 'articleType',
          type: 'select',
          defaultValue: 'Article',
          options: [
            { label: 'Article — standard blog post', value: 'Article' },
            { label: 'HowTo — step-by-step guide', value: 'HowTo' },
            { label: 'FAQPage — question and answer format', value: 'FAQPage' },
            { label: 'ReviewNewsArticle — comparing products', value: 'ReviewNewsArticle' },
          ],
        },
        {
          name: 'faqItems',
          type: 'array',
          label: 'FAQ Items — generates FAQ rich results in Google',
          admin: { description: 'Add 3–5 real questions a customer would actually type into Google. Answers in plain English — direct and specific.' },
          fields: [
            { name: 'question', type: 'text', required: true },
            { name: 'answer', type: 'textarea', required: true },
          ],
        },
        {
          name: 'howToSteps',
          type: 'array',
          label: 'How-To Steps — for tutorial articles',
          fields: [
            { name: 'stepNumber', type: 'number', required: true },
            { name: 'stepName', type: 'text', required: true },
            { name: 'stepDescription', type: 'textarea', required: true },
            { name: 'stepImageUrl', type: 'text' },
          ],
        },
        {
          name: 'breadcrumbs',
          type: 'array',
          label: 'Breadcrumb Trail',
          admin: { description: 'Shown above article title and in Google results. e.g. Home > Blog > Salons > This Article' },
          fields: [
            { name: 'label', type: 'text', required: true },
            { name: 'url', type: 'text', required: true },
          ],
        },
      ],
    },

    // ── AI SEARCH OPTIMISATION (2026) ─────────────────────────────────────
    {
      name: 'aiOptimisation',
      type: 'group',
      label: 'AI Search Optimisation — 2026',
      admin: { description: 'Google AI Overviews, Perplexity, and ChatGPT pull answers directly from web pages. These fields help ensure ReeveOS content is cited accurately by AI systems.' },
      fields: [
        {
          name: 'directAnswer',
          type: 'textarea',
          admin: { description: '2–4 sentence direct answer to the article\'s main question. Write so an AI could lift it verbatim and it makes complete sense on its own. Include specific numbers and facts.' },
        },
        {
          name: 'keyFacts',
          type: 'array',
          label: 'Key Facts for AI Citation',
          admin: { description: 'Specific, citable facts. AI systems prefer structured facts they can cite confidently — statistics, prices, percentages, dates, sources.' },
          fields: [
            { name: 'fact', type: 'text', required: true, admin: { description: 'e.g. "UK salons lose £1.6 billion annually to no-shows (Scratch Magazine, 2025)"' } },
          ],
        },
        {
          name: 'llmsSummary',
          type: 'textarea',
          admin: { description: '100–150 word plain-text summary for inclusion in reeveos.app/llms.txt — the file that tells AI tools what is on your site. Factual only, no marketing language.' },
        },
      ],
    },

    // ── CTA ───────────────────────────────────────────────────────────────
    {
      name: 'cta',
      type: 'group',
      label: 'Call to Action',
      fields: [
        { name: 'text', type: 'text', defaultValue: 'Start your free trial' },
        { name: 'url', type: 'text', defaultValue: 'https://portal.rezvo.app/register' },
        { name: 'secondaryText', type: 'text', admin: { description: 'e.g. "Or calculate your savings first"' } },
        { name: 'secondaryUrl', type: 'text' },
      ],
    },

    // ── INTERNAL NOTES ────────────────────────────────────────────────────
    {
      name: 'internalNotes',
      type: 'textarea',
      admin: { description: 'Not shown publicly. Track: competitor pricing check dates, sources to re-verify, update reminders, future content ideas.' },
    },
  ],
}
