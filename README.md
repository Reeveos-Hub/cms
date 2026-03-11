# ReeveOS CMS

Website Builder CMS module for ReeveOS platform.

Built with **Payload CMS v3** + **MongoDB** + **Next.js**.

## Architecture

This is a **standalone service** that handles ONLY the website builder functionality.
It does NOT touch the main ReeveOS portal (FastAPI + React).

- **Database**: `reeveos_cms` (separate from `reeveos_app`)
- **Port**: 3000
- **Admin**: `/admin`
- **API**: `/api`

## Setup

```bash
cp .env.example .env
# Edit .env with your MongoDB URI and secret
npm install
npm run build
npm start
```

## Collections

- **Tenants** - Each business is a tenant with brand settings, navigation, domains
- **Pages** - Website pages with Puck JSON data for visual editing
- **Media** - Image uploads with tenant isolation and auto-thumbnails
- **Users** - CMS admin users with role-based access

## Non-Negotiable Rules

1. This service handles ONLY the website builder module
2. All existing FastAPI routes remain UNTOUCHED
3. Full tenant isolation - no business sees another's data
4. HIPAA/ICO/GDPR: EXIF stripping, cookie consent, no PII on public sites
5. Custom domains: SSL via Caddy auto-renewal. No HTTP, ever.
