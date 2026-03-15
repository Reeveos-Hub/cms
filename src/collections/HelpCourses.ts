import type { CollectionConfig } from 'payload'

export const HelpCourses: CollectionConfig = {
  slug: 'help-courses',
  admin: {
    useAsTitle: 'title',
    group: 'Help Centre',
    defaultColumns: ['title', 'courseNumber'],
  },
  fields: [
    {
      name: 'courseNumber',
      type: 'text',
      required: true,
      admin: { description: 'e.g. "01", "02"' },
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
    },
    {
      name: 'lessons',
      type: 'array',
      admin: { description: 'Ordered list of lessons in this course' },
      fields: [
        {
          name: 'title',
          type: 'text',
          required: true,
        },
        {
          name: 'walkthrough',
          type: 'relationship',
          relationTo: 'help-walkthroughs',
          admin: { description: 'Which walkthrough this lesson plays' },
        },
        {
          name: 'stepIndex',
          type: 'number',
          admin: { description: 'Which step of the walkthrough this lesson starts at (0-indexed)' },
        },
        {
          name: 'duration',
          type: 'text',
          admin: { description: 'e.g. "30 sec", "1 min"' },
        },
      ],
    },
  ],
  access: {
    read: () => true,
    create: ({ req }) => !!req.user,
    update: ({ req }) => !!req.user,
    delete: ({ req }) => !!req.user,
  },
}
