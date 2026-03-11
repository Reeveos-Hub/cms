import type { CollectionConfig } from 'payload'

export const Tenants: CollectionConfig = {
  slug: 'tenants',
  admin: {
    useAsTitle: 'name',
  },
  fields: [
    {
      name: 'name',
      type: 'text',
      required: true,
      admin: { description: 'Business name e.g. Rejuvenate Skin Experts' },
    },
    {
      name: 'businessId',
      type: 'text',
      required: true,
      unique: true,
      admin: { description: 'The _id from the businesses collection in reeveos_app database' },
    },
    {
      name: 'subdomain',
      type: 'text',
      required: true,
      unique: true,
      admin: { description: 'e.g. rejuvenate-skin-experts (used for subdomain.reeveos.site)' },
    },
    {
      name: 'customDomains',
      type: 'array',
      fields: [
        { name: 'domain', type: 'text', required: true },
        {
          name: 'status',
          type: 'select',
          defaultValue: 'pending_dns',
          options: [
            { label: 'Pending DNS', value: 'pending_dns' },
            { label: 'DNS Verified', value: 'dns_verified' },
            { label: 'SSL Provisioning', value: 'ssl_provisioning' },
            { label: 'Active', value: 'active' },
            { label: 'Failed', value: 'failed' },
          ],
        },
        { name: 'verifiedAt', type: 'date' },
      ],
    },
    {
      name: 'brand',
      type: 'group',
      fields: [
        { name: 'primaryColor', type: 'text', defaultValue: '#C9A84C' },
        { name: 'secondaryColor', type: 'text', defaultValue: '#111111' },
        { name: 'accentColor', type: 'text', defaultValue: '#FFFFFF' },
        { name: 'fontHeading', type: 'text', defaultValue: 'Figtree' },
        { name: 'fontBody', type: 'text', defaultValue: 'Figtree' },
        { name: 'logo', type: 'upload', relationTo: 'media' },
        { name: 'favicon', type: 'upload', relationTo: 'media' },
        {
          name: 'buttonStyle',
          type: 'select',
          defaultValue: 'rounded',
          options: [
            { label: 'Rounded', value: 'rounded' },
            { label: 'Pill', value: 'pill' },
            { label: 'Square', value: 'square' },
          ],
        },
      ],
    },
    {
      name: 'navigation',
      type: 'array',
      fields: [
        { name: 'label', type: 'text', required: true },
        { name: 'slug', type: 'text', required: true },
        { name: 'visible', type: 'checkbox', defaultValue: true },
        { name: 'order', type: 'number' },
      ],
    },
    {
      name: 'footer',
      type: 'group',
      fields: [
        { name: 'businessName', type: 'text' },
        { name: 'tagline', type: 'text' },
        { name: 'address', type: 'textarea' },
        { name: 'phone', type: 'text' },
        { name: 'email', type: 'email' },
        {
          name: 'social',
          type: 'group',
          fields: [
            { name: 'instagram', type: 'text' },
            { name: 'facebook', type: 'text' },
            { name: 'tiktok', type: 'text' },
            { name: 'twitter', type: 'text' },
          ],
        },
      ],
    },
    {
      name: 'integrations',
      type: 'group',
      fields: [
        { name: 'ga4Id', type: 'text', admin: { description: 'Google Analytics 4 Measurement ID' } },
        { name: 'metaPixelId', type: 'text' },
        { name: 'tiktokPixelId', type: 'text' },
        { name: 'whatsappNumber', type: 'text' },
        { name: 'instagramHandle', type: 'text' },
        { name: 'googleReviewUrl', type: 'text' },
      ],
    },
    {
      name: 'seoDefaults',
      type: 'group',
      fields: [
        { name: 'titleSuffix', type: 'text', admin: { description: 'Appended to all page titles' } },
        { name: 'defaultOgImage', type: 'upload', relationTo: 'media' },
      ],
    },
    {
      name: 'tier',
      type: 'select',
      defaultValue: 'starter',
      options: [
        { label: 'Free', value: 'free' },
        { label: 'Starter', value: 'starter' },
        { label: 'Growth', value: 'growth' },
        { label: 'Scale', value: 'scale' },
        { label: 'Enterprise', value: 'enterprise' },
      ],
    },
  ],
  access: {
    read: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return { id: { equals: req.user?.tenant } }
    },
    create: ({ req }) => req.user?.role === 'super_admin',
    update: ({ req }) => {
      if (req.user?.role === 'super_admin') return true
      return { id: { equals: req.user?.tenant } }
    },
    delete: ({ req }) => req.user?.role === 'super_admin',
  },
}
