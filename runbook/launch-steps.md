# HTA launch steps (Terry)

## 1. GitHub (phone is fine)
1. Reset password if needed: https://github.com/password_reset
2. Create the free organization **HTA-Associates**: https://github.com/organizations/plan
3. Create the **public** repository **htaassociates**: https://github.com/organizations/HTA-Associates/repositories/new
4. Install the Claude app on HTA-Associates: https://github.com/apps/claude/installations/select_target
5. Tell Claude: "repo ready"

## 2. GoDaddy DNS (after Claude says the site is pushed)
https://dcc.godaddy.com/control/portfolio → htaassociates.com → DNS
Delete any existing A record on @ and any "Parked" record. Add:

| Type  | Name | Value                      |
|-------|------|----------------------------|
| A     | @    | 185.199.108.153            |
| A     | @    | 185.199.109.153            |
| A     | @    | 185.199.110.153            |
| A     | @    | 185.199.111.153            |
| CNAME | www  | hta-associates.github.io   |

Then tick **Enforce HTTPS**: https://github.com/HTA-Associates/htaassociates/settings/pages

## 3. Google and Bing (after the site is live)
- Google Search Console: https://search.google.com/search-console → Add property → Domain → htaassociates.com → copy the TXT record into GoDaddy DNS → Verify → Sitemaps → `sitemap.xml`
- Bing Webmaster Tools: https://www.bing.com/webmasters → Import from Google Search Console
- Google Business Profile: https://business.google.com → "HTA & Associates" → service-area business, hide street address, areas New York and Los Angeles

## 4. Claim the same name everywhere (handle: htaassociates)
- YouTube: https://www.youtube.com/create_channel
- Instagram: (existing) put https://htaassociates.com in bio
- TikTok: https://www.tiktok.com/signup
- X: https://x.com/i/flow/signup
- LinkedIn page: https://www.linkedin.com/company/setup/new/
- Facebook page: https://www.facebook.com/pages/create

Bio (paste everywhere):
Strategic legal intelligence for Media. Law. Reputation. New York · Los Angeles. Private consultations by appointment. htaassociates.com

## 5. Send Claude
- Instagram handle
- Official email
- Legal commentators: name, title, one-paragraph bio, headshot, written OK to be named
