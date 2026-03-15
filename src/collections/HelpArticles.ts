import type { CollectionConfig } from 'payload'

export const HelpArticles: CollectionConfig = {
  slug: 'help-articles',
  admin: {
    useAsTitle: 'title',
    group: 'Help Centre',
    defaultColumns: ['title', 'category', 'status', 'updatedAt'],
  },
  versions: {
    drafts: { autosave: { interval: 30000 } },
    maxPerDoc: 10,
  },
  fields: [
    {
      name: 'title',
      type: 'text',
      required: true,
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      admin: { description: 'URL slug — auto-generated from title if left blank' },
    },
    {
      name: 'category',
      type: 'relationship',
      relationTo: 'help-categories',
      required: true,
    },
    {
      name: 'description',
      type: 'textarea',
      required: true,
      admin: { description: 'Shows in search results and at top of article. 1-2 sentences.' },
    },
    {
      name: 'status',
      type: 'select',
      defaultValue: 'published',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'Published', value: 'published' },
      ],
    },
    // --- TABLE OF CONTENTS ---
    {
      name: 'tableOfContents',
      type: 'array',
      admin: { description: '"In this article" links — one per section' },
      fields: [
        {
          name: 'anchorId',
          type: 'text',
          required: true,
          admin: { description: 'Anchor ID e.g. "create-booking"' },
        },
        {
          name: 'label',
          type: 'text',
          required: true,
          admin: { description: 'Display text e.g. "Create a booking"' },
        },
      ],
    },
    // --- SECTIONS (the main content) ---
    {
      name: 'sections',
      type: 'array',
      admin: { description: 'Article sections. Each has a title with desktop and mobile step-by-step instructions.' },
      fields: [
        {
          name: 'sectionId',
          type: 'text',
          required: true,
          admin: { description: 'Must match a tableOfContents anchorId' },
        },
        {
          name: 'sectionTitle',
          type: 'text',
          required: true,
        },
        // --- DESKTOP STEPS ---
        {
          name: 'desktopSteps',
          type: 'array',
          admin: { description: 'Step-by-step instructions for DESKTOP users' },
          fields: [
            {
              name: 'text',
              type: 'richText',
              required: true,
              admin: { description: 'Use **bold** for button names and UI elements' },
            },
            {
              name: 'screenshot',
              type: 'upload',
              relationTo: 'help-media',
              admin: { description: 'Screenshot showing this step (upload in Pass 2)' },
            },
            {
              name: 'screenshotCaption',
              type: 'text',
              admin: { description: 'Optional caption below the screenshot' },
            },
          ],
        },
        // --- MOBILE STEPS ---
        {
          name: 'mobileSteps',
          type: 'array',
          admin: { description: 'Step-by-step instructions for MOBILE. Leave empty if same as desktop.' },
          fields: [
            {
              name: 'text',
              type: 'richText',
              required: true,
            },
            {
              name: 'screenshot',
              type: 'upload',
              relationTo: 'help-media',
            },
            {
              name: 'screenshotCaption',
              type: 'text',
            },
          ],
        },
        // --- SECTION NOTE ---
        {
          name: 'note',
          type: 'textarea',
          admin: { description: 'Optional tip/note shown after the steps in this section' },
        },
      ],
    },
    // --- FAQs ---
    {
      name: 'faqs',
      type: 'array',
      admin: { description: 'Frequently asked questions shown at the bottom of the article' },
      fields: [
        { name: 'question', type: 'text', required: true },
        { name: 'answer', type: 'textarea', required: true },
      ],
    },
    // --- RELATED CONTENT ---
    {
      name: 'relatedArticles',
      type: 'relationship',
      relationTo: 'help-articles',
      hasMany: true,
      admin: { description: 'Related articles shown in the sidebar' },
    },
    {
      name: 'relatedWalkthrough',
      type: 'relationship',
      relationTo: 'help-walkthroughs',
      admin: { description: 'Related walkthrough — shows "See this in action" card' },
    },
    {
      name: 'relatedCourse',
      type: 'relationship',
      relationTo: 'help-courses',
      admin: { description: 'Related academy course shown at bottom' },
    },
  ],
  access: {
    read: () => true,
    create: ({ req }) => !!req.user,
    update: ({ req }) => !!req.user,
    delete: ({ req }) => !!req.user,
  },
  hooks: {
    beforeChange: [
      ({ data }) => {
        if (data && data.title && !data.slug) {
          data.slug = data.title
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, '-')
            .replace(/^-|-$/g, '')
        }
        return data
      },
    ],
  },
}
