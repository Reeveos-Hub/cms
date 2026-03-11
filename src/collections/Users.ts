import type { CollectionConfig } from 'payload'

export const Users: CollectionConfig = {
  slug: 'users',
  auth: true,
  admin: {
    useAsTitle: 'email',
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
    },
    {
      name: 'role',
      type: 'select',
      required: true,
      defaultValue: 'tenant_admin',
      options: [
        { label: 'Super Admin', value: 'super_admin' },
        { label: 'Tenant Admin', value: 'tenant_admin' },
        { label: 'Editor', value: 'editor' },
      ],
    },
    {
      name: 'tenant',
      type: 'relationship',
      relationTo: 'tenants',
      required: true,
      admin: {
        condition: (data) => data?.role !== 'super_admin',
      },
    },
    {
      // Links to the business_id in the main ReeveOS app database
      name: 'businessId',
      type: 'text',
      admin: {
        description: 'The business_id from the main ReeveOS portal (reeveos_app database)',
      },
    },
  ],
  access: {
    // Super admins can see all users, tenant admins see only their tenant
    read: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return { tenant: { equals: req.user?.tenant } }
    },
    create: ({ req }) => req.user?.role === 'super_admin',
    update: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return { tenant: { equals: req.user?.tenant } }
    },
    delete: ({ req }) => req.user?.role === 'super_admin',
  },
}
