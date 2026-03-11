import type { GlobalConfig } from 'payload'

export const WebsiteSettings: GlobalConfig = {
  slug: 'website-settings',
  admin: {
    description: 'Global website builder settings',
  },
  fields: [
    {
      name: 'cookieConsent',
      type: 'group',
      fields: [
        { name: 'enabled', type: 'checkbox', defaultValue: true },
        { name: 'text', type: 'textarea', defaultValue: 'This website uses cookies to ensure you get the best experience.' },
        { name: 'policyUrl', type: 'text' },
        { name: 'autoDetect', type: 'checkbox', defaultValue: true, admin: { description: 'Auto-configure based on enabled integrations' } },
      ],
    },
    {
      name: 'announcementBar',
      type: 'group',
      fields: [
        { name: 'enabled', type: 'checkbox', defaultValue: false },
        { name: 'text', type: 'text' },
        { name: 'link', type: 'text' },
        { name: 'bgColor', type: 'text', defaultValue: '#C9A84C' },
        { name: 'textColor', type: 'text', defaultValue: '#FFFFFF' },
      ],
    },
    {
      name: 'analyticsRetentionDays',
      type: 'number',
      defaultValue: 90,
      admin: { description: 'Auto-delete analytics data after this many days (GDPR)' },
    },
  ],
  access: {
    read: () => true,
    update: ({ req }) => req.user?.role === 'super_admin',
  },
}
