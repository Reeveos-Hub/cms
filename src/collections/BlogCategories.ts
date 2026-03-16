import type { CollectionConfig } from 'payload'

export const BlogCategories: CollectionConfig = {
  slug: 'blog-categories',
  admin: {
    useAsTitle: 'name',
    defaultColumns: ['name', 'slug', 'site', 'description'],
    group: 'Blog',
  },
  access: {
    read: () => true, // Public — blog is public
    create: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    update: ({ req }) => req.user?.role === 'super_admin' || req.user?.role === 'platform_admin',
    delete: ({ req }) => req.user?.role === 'super_admin',
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
      admin: { description: 'e.g. "Salons", "Barbers", "EPOS & Payments"' },
    },
    {
      name: 'slug',
      type: 'text',
      required: true,
      unique: true,
      admin: { description: 'URL slug e.g. "salons", "barbers", "epos-payments"' },
    },
    {
      name: 'site',
      type: 'select',
      required: true,
      defaultValue: 'reeveos',
      options: [
        { label: 'reeveos.app (merchant-facing)', value: 'reeveos' },
        { label: 'reevenow.com (consumer-facing)', value: 'reevenow' },
      ],
      admin: { description: 'Which site this category belongs to' },
    },
    {
      name: 'description',
      type: 'textarea',
      admin: { description: 'Short description shown on the category page' },
    },
    {
      name: 'icon',
      type: 'text',
      admin: { description: 'Monochrome SVG icon name from the ReeveOS icon library' },
    },
    {
      name: 'sortOrder',
      type: 'number',
      defaultValue: 0,
      admin: { description: 'Lower number = appears first in navigation' },
    },
  ],
}
