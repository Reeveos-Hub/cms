import type { CollectionConfig } from 'payload'

export const HelpMedia: CollectionConfig = {
  slug: 'help-media',
  admin: {
    useAsTitle: 'alt',
    group: 'Help Centre',
    description: 'Screenshots and images for help centre articles',
  },
  upload: {
    staticDir: '../help-media',
    mimeTypes: ['image/jpeg', 'image/png', 'image/webp', 'image/gif'],
    imageSizes: [
      { name: 'thumbnail', width: 400, height: 300, position: 'centre' },
      { name: 'article', width: 1200, height: 800, position: 'centre' },
      { name: 'full', width: 1920, height: 1200, position: 'centre' },
    ],
    adminThumbnail: 'thumbnail',
  },
  fields: [
    {
      name: 'alt',
      type: 'text',
      required: true,
      admin: { description: 'Describe what this screenshot shows' },
    },
    {
      name: 'caption',
      type: 'text',
      admin: { description: 'Optional caption shown below the image' },
    },
    {
      name: 'platform',
      type: 'select',
      options: [
        { label: 'Desktop', value: 'desktop' },
        { label: 'Mobile', value: 'mobile' },
      ],
      admin: { description: 'Is this a desktop or mobile screenshot?' },
    },
  ],
  access: {
    read: () => true,
    create: ({ req }) => !!req.user,
    update: ({ req }) => !!req.user,
    delete: ({ req }) => !!req.user,
  },
}
