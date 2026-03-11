import type { CollectionConfig } from 'payload'

export const Pages: CollectionConfig = {
  slug: 'pages',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'slug', 'status', 'tenant', 'updatedAt'],
  },
  versions: {
    drafts: {
      autosave: {
        interval: 30000, // Auto-save every 30 seconds
      },
    },
    maxPerDoc: 20,
  },
  fields: [
    {
      name: 'tenant',
      type: 'relationship',
      relationTo: 'tenants',
      required: true,
      admin: { description: 'Which business this page belongs to' },
    },
    {
      name: 'title',
      type: 'text',
      required: true,
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      admin: { description: 'URL slug e.g. "home", "about", "treatments"' },
    },
    {
      name: 'puckData',
      type: 'json',
      required: true,
      defaultValue: { content: [], root: {} },
      admin: { description: 'Puck editor JSON data - the visual layout of the page' },
    },
    {
      name: 'status',
      type: 'select',
      defaultValue: 'draft',
      options: [
        { label: 'Draft', value: 'draft' },
        { label: 'Published', value: 'published' },
      ],
    },
    {
      name: 'publishedAt',
      type: 'date',
    },
    {
      name: 'excerpt',
      type: 'textarea',
      admin: { description: 'Short description for SEO and previews' },
    },
    {
      name: 'pageType',
      type: 'select',
      defaultValue: 'page',
      options: [
        { label: 'Page', value: 'page' },
        { label: 'Blog Post', value: 'blog' },
        { label: 'Landing Page', value: 'landing' },
      ],
    },
    {
      name: 'sortOrder',
      type: 'number',
      defaultValue: 0,
      admin: { description: 'Order in navigation (lower = first)' },
    },
    {
      name: 'showInNav',
      type: 'checkbox',
      defaultValue: true,
    },
  ],
  // Compound index for tenant + slug uniqueness
  indexes: [
    {
      fields: { tenant: 1, slug: 1 },
      options: { unique: true },
    },
  ],
  access: {
    read: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      if (!req.user?.tenant) return false
      return { tenant: { equals: req.user?.tenant } }
    },
    create: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return req.user?.role === 'tenant_admin' || req.user?.role === 'editor'
    },
    update: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      if (!req.user?.tenant) return false
      return { tenant: { equals: req.user?.tenant } }
    },
    delete: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return { tenant: { equals: req.user?.tenant } }
    },
  },
  hooks: {
    beforeChange: [
      ({ data, req }) => {
        // Auto-set publishedAt when status changes to published
        if (data.status === 'published' && !data.publishedAt) {
          data.publishedAt = new Date().toISOString()
        }
        return data
      },
    ],
  },
}
