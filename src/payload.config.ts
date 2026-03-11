import { buildConfig } from 'payload'
import { mongooseAdapter } from '@payloadcms/db-mongodb'
import { lexicalEditor } from '@payloadcms/richtext-lexical'
import { seoPlugin } from '@payloadcms/plugin-seo'
import path from 'path'
import { fileURLToPath } from 'url'

// Collections
import { Users } from './collections/Users'
import { Tenants } from './collections/Tenants'
import { Pages } from './collections/Pages'
import { Media } from './collections/Media'
import { WebsiteSettings } from './globals/WebsiteSettings'

const filename = fileURLToPath(import.meta.url)
const dirname = path.dirname(filename)

export default buildConfig({
  admin: {
    user: Users.slug,
    meta: {
      titleSuffix: ' | ReeveOS CMS',
    },
  },

  collections: [Users, Tenants, Pages, Media],

  globals: [WebsiteSettings],

  editor: lexicalEditor(),

  db: mongooseAdapter({
    url: process.env.DATABASE_URI || 'mongodb://127.0.0.1:27017/reeveos_cms',
  }),

  plugins: [
    seoPlugin({
      collections: ['pages'],
      uploadsCollection: 'media',
      generateTitle: ({ doc }: any) => `${doc?.title} | ReeveOS`,
      generateDescription: ({ doc }: any) => doc?.excerpt || '',
    }),
  ],

  secret: process.env.PAYLOAD_SECRET || 'CHANGE-THIS-SECRET',

  typescript: {
    outputFile: path.resolve(dirname, 'payload-types.ts'),
  },

  upload: {
    limits: {
      fileSize: 5000000, // 5MB max
    },
  },

  serverURL: process.env.NEXT_PUBLIC_SERVER_URL || 'http://localhost:3000',
})
