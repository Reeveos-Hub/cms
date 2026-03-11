import type { CollectionConfig } from 'payload'

export const Media: CollectionConfig = {
  slug: 'media',
  admin: {
    useAsTitle: 'filename',
  },
  upload: {
    staticDir: '../media',
    mimeTypes: ['image/jpeg', 'image/png', 'image/webp', 'image/svg+xml', 'image/gif'],
    imageSizes: [
      { name: 'thumbnail', width: 200, height: 200, position: 'centre' },
      { name: 'card', width: 400, height: 300, position: 'centre' },
      { name: 'hero', width: 1200, height: 600, position: 'centre' },
    ],
    adminThumbnail: 'thumbnail',
    // EXIF stripping is handled by sharp (included in Payload) - GDPR compliant
  },
  fields: [
    {
      name: 'tenant',
      type: 'relationship',
      relationTo: 'tenants',
      required: true,
      admin: { description: 'Which business this image belongs to' },
    },
    {
      name: 'alt',
      type: 'text',
      admin: { description: 'Alt text for accessibility and SEO (required for published pages)' },
    },
    {
      name: 'caption',
      type: 'text',
    },
  ],
  access: {
    // Public read for published website images
    read: () => true,
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
}
