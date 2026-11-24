# Caribaid Foundation: website preview

A three-page preview site for Caribaid Foundation, Castries, Saint Lucia, built by Code Canvas Consultants Ltd.

- `index.html`: home, with the three programmes and the daycare the foundation is working towards
- `our-work.html`: each programme in detail and the 2015 television interview
- `get-involved.html`: a "what can you give" picker that writes a WhatsApp message, volunteer roles, contact details and common questions

## Building

The three pages share a header and footer, kept in `build.py`:

```
python3 build.py
python3 -m http.server 8142
```

No dependencies and no build step beyond that. The site is plain HTML, CSS and JavaScript.

## Content

The wording is a first draft based on what the foundation has said publicly and is to be confirmed with them. No photographs of children are used; the foundation's own photos will be added with consent.

## Credits

Photos are from Wikimedia Commons and are credited at the foot of `get-involved.html`.
