import type { CollectionConfig } from 'payload'

export const HelpWalkthroughs: CollectionConfig = {
  slug: 'help-walkthroughs',
  admin: {
    useAsTitle: 'title',
    group: 'Help Centre',
    defaultColumns: ['title', 'stepCount', 'duration', 'sortOrder'],
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
    },
    {
      name: 'description',
      type: 'textarea',
      required: true,
    },
    {
      name: 'thumbnail',
      type: 'upload',
      relationTo: 'help-media',
      admin: { description: 'Screenshot shown on the tour grid card' },
    },
    {
      name: 'stepCount',
      type: 'number',
      required: true,
    },
    {
      name: 'duration',
      type: 'text',
      required: true,
      admin: { description: 'e.g. "2 min", "3 min"' },
    },
    {
      name: 'category',
      type: 'relationship',
      relationTo: 'help-categories',
      admin: { description: 'Which KB category this walkthrough relates to' },
    },
    {
      name: 'sortOrder',
      type: 'number',
      defaultValue: 0,
    },
  ],
  access: {
    read: () => true,
    create: ({ req }) => !!req.user,
    update: ({ req }) => !!req.user,
    delete: ({ req }) => !!req.user,
  },
}
