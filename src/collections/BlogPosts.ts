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
    drafts: {
      autosave: { interval: 30000 },
    },
    maxPerDoc: 20,
  },
  access: {
    // Published posts are fully public — this is SEO content
    read: ({ req, data }) => {
      if (req.user?.role === 'super_admin' || req.user?.role === 'platform_admin') return true
      // Public can only read published posts
      return { status: { equals: 'published' } }
    },
    create: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    update: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    delete: ({ req }) => req.user?.role === 'super_admin',
  },
  hooks: {
    beforeChange: [
      ({ data }) => {
        // Auto-set publishedAt when first published
        if (data.status === 'published' && !data.publishedAt) {
          data.publishedAt = new Date().toISOString()
        }
        return data
      },
    ],
  },
  fields: [
    // ── CONTENT IDENTITY ────────────────────────────────────────────────────
    {
      name: 'title',
      type: 'text',
      required: true,
      admin: { description: 'The article headline — make it clear and specific' },
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
      admin: {
        description: 'URL slug e.g. "fresha-alternatives-uk-2026". Lowercase, hyphens only, no spaces.',
      },
    },
    {
      name: 'site',
      type: 'select',
      required: true,
      defaultValue: 'reeveos',
      options: [
        { label: 'reeveos.app (for business owners)', value: 'reeveos' },
        { label: 'reevenow.com (for consumers)', value: 'reevenow' },
      ],
    },
    {
      name: 'category',
      type: 'relationship',
      relationTo: 'blog-categories',
      required: true,
      admin: { description: 'Primary category e.g. Salons, Barbers, EPOS & Payments' },
    },
    {
      name: 'status',
      type: 'select',
      required: true,
      defaultValue: 'draft',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'Review', value: 'review' },
        { label: 'Published', value: 'published' },
      ],
    },
    {
      name: 'publishedAt',
      type: 'date',
      admin: { description: 'Leave blank — auto-set when first published' },
    },

    // ── CONTENT TYPE & PRIORITY ──────────────────────────────────────────────
    {
      name: 'contentType',
      type: 'select',
      required: true,
      defaultValue: 'cluster',
      options: [
        { label: 'Pillar Page (broad, comprehensive, 3000–5000 words)', value: 'pillar' },
        { label: 'Cluster Article (supports a pillar, 1200–2000 words)', value: 'cluster' },
        { label: 'Competitor Alternative ("X alternatives UK")', value: 'competitor-alternative' },
        { label: 'Competitor Comparison ("X vs ReeveOS")', value: 'competitor-vs' },
        { label: 'Case Study', value: 'case-study' },
        { label: 'How-To Tutorial', value: 'tutorial' },
        { label: 'Pricing Intel ("how much does X cost")', value: 'pricing-intel' },
        { label: 'Neighbourhood Guide (reevenow.com)', value: 'neighbourhood-guide' },
        { label: 'Best Of List (reevenow.com)', value: 'best-of' },
      ],
      admin: { description: 'What type of content is this? Affects internal linking strategy.' },
    },
    {
      name: 'priority',
      type: 'select',
      defaultValue: 'p2',
      options: [
        { label: 'P1 — Publish immediately (highest conversion intent)', value: 'p1' },
        { label: 'P2 — Publish within 60 days', value: 'p2' },
        { label: 'P3 — Publish within 90 days', value: 'p3' },
      ],
    },
    {
      name: 'pillarPage',
      type: 'relationship',
      relationTo: 'blog-posts',
      admin: {
        description: 'If this is a cluster article, link to its parent pillar page here. Critical for internal linking.',
        condition: (data) => data.contentType === 'cluster',
      },
    },
    {
      name: 'competitorName',
      type: 'text',
      admin: {
        description: 'e.g. "Fresha", "Booksy", "EPOS Now". Used for competitor content only.',
        condition: (data) => ['competitor-alternative', 'competitor-vs', 'pricing-intel'].includes(data.contentType),
      },
    },

    // ── SEO FIELDS ───────────────────────────────────────────────────────────
    {
      name: 'seo',
      type: 'group',
      label: 'SEO',
      admin: { description: 'Controls how this page appears in Google search results' },
      fields: [
        {
          name: 'targetKeyword',
          type: 'text',
          required: true,
          admin: { description: 'The ONE primary keyword this article targets e.g. "fresha alternative UK"' },
        },
        {
          name: 'secondaryKeywords',
          type: 'text',
          admin: { description: 'Comma-separated secondary keywords e.g. "fresha pricing UK, salon booking software"' },
        },
        {
          name: 'metaTitle',
          type: 'text',
          admin: {
            description: 'SEO title — shown in Google results. 50–60 characters ideal. Leave blank to use article title.',
          },
        },
        {
          name: 'metaDescription',
          type: 'textarea',
          admin: {
            description: 'SEO description — shown under the title in Google. 150–160 characters ideal. Make it compelling.',
          },
        },
        {
          name: 'canonicalUrl',
          type: 'text',
          admin: { description: 'Only set if this content is published elsewhere first (rare)' },
        },
      ],
    },

    // ── ARTICLE CONTENT ──────────────────────────────────────────────────────
    {
      name: 'excerpt',
      type: 'textarea',
      required: true,
      admin: {
        description: 'A 2–3 sentence summary shown on listing pages and in social shares. Write this like a friendly intro — what problem does this article solve?',
      },
    },
    {
      name: 'featuredImage',
      type: 'upload',
      relationTo: 'media',
      admin: { description: 'Cover image for the article. Will be shown on listing pages and at top of article.' },
    },
    {
      name: 'featuredImageAlt',
      type: 'text',
      admin: { description: 'Alt text for the featured image — describe what is in the image' },
    },
    {
      name: 'content',
      type: 'richText',
      required: true,
      admin: {
        description: 'The full article. Write in plain English — imagine explaining this to someone who has never heard of booking software before. Short sentences. Real stories. Specific numbers.',
      },
    },

    // ── ARTICLE METADATA ─────────────────────────────────────────────────────
    {
      name: 'readTime',
      type: 'number',
      admin: { description: 'Estimated read time in minutes. Roughly 200 words per minute.' },
    },
    {
      name: 'tags',
      type: 'text',
      admin: {
        description: 'Comma-separated tags e.g. "no-shows, deposits, cancellation policy, salon software"',
      },
    },
    {
      name: 'relatedTool',
      type: 'select',
      admin: {
        description: 'Which free tool should be promoted inline in this article?',
      },
      options: [
        { label: 'Fresha Cost Calculator', value: 'fresha-cost-calculator' },
        { label: 'No-Show Cost Calculator', value: 'no-show-calculator' },
        { label: 'EPOS Cost Comparison Tool', value: 'epos-cost-comparison' },
        { label: 'Business Health Grader', value: 'business-health-grader' },
        { label: 'Dojo Card Rate Calculator', value: 'dojo-rate-calculator' },
        { label: 'Mindbody Cost Calculator', value: 'mindbody-cost-calculator' },
      ],
    },
    {
      name: 'ctaText',
      type: 'text',
      admin: {
        description: 'Call-to-action button text at end of article e.g. "Start your free trial" or "Calculate your savings"',
      },
    },
    {
      name: 'ctaUrl',
      type: 'text',
      admin: { description: 'Where the CTA button links to' },
    },

    // ── SCHEMA MARKUP ────────────────────────────────────────────────────────
    {
      name: 'schema',
      type: 'group',
      label: 'Schema Markup (Structured Data)',
      admin: { description: 'Controls Google rich results — FAQ boxes, How-To steps etc.' },
      fields: [
        {
          name: 'faqItems',
          type: 'array',
          label: 'FAQ Items (generates FAQ schema for Google)',
          admin: { description: 'Add 3–5 questions and answers. Google may show these as expandable boxes in search results.' },
          fields: [
            {
              name: 'question',
              type: 'text',
              required: true,
            },
            {
              name: 'answer',
              type: 'textarea',
              required: true,
            },
          ],
        },
        {
          name: 'articleType',
          type: 'select',
          defaultValue: 'Article',
          options: [
            { label: 'Article', value: 'Article' },
            { label: 'How-To Article', value: 'HowTo' },
            { label: 'FAQ Page', value: 'FAQPage' },
            { label: 'Review Article', value: 'ReviewNewsArticle' },
          ],
        },
      ],
    },

    // ── INTERNAL NOTES ───────────────────────────────────────────────────────
    {
      name: 'internalNotes',
      type: 'textarea',
      admin: {
        description: 'Internal notes only — not shown publicly. Use for tracking sources, update reminders, competitor pricing last verified date etc.',
      },
    },
  ],
}
