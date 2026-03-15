import type { CollectionConfig } from 'payload'

export const HelpCategories: CollectionConfig = {
  slug: 'help-categories',
  admin: {
    useAsTitle: 'title',
    group: 'Help Centre',
    defaultColumns: ['title', 'slug', 'sortOrder'],
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
      unique: true,
      admin: { description: 'URL slug e.g. "calendar", "booking-link"' },
    },
    {
      name: 'description',
      type: 'textarea',
      required: true,
      admin: { description: 'One-sentence description shown on the category card' },
    },
    {
      name: 'icon',
      type: 'text',
      required: true,
      admin: { description: 'Lucide icon name e.g. "Calendar", "Link2", "Users"' },
    },
    {
      name: 'sortOrder',
      type: 'number',
      defaultValue: 0,
      admin: { description: 'Lower = appears first' },
    },
  ],
  access: {
    read: () => true,
    create: ({ req }) => !!req.user,
    update: ({ req }) => !!req.user,
    delete: ({ req }) => !!req.user,
  },
}
