# Add Google Reviews title with i18n to Site_02

with open('Site_02/index.html', 'r', encoding='utf-8') as f:
    s2 = f.read()

# 1. Add title HTML before the StarWall widget
old_html = 'id="testimonials"><div style="text-align:center;padding:20px 10px"><div id="reviews-widget-100">'
new_html = 'id="testimonials"><div style="text-align:center;padding:20px 10px"><h2 class="testimonials-title"data-i18n="google_reviews_title"style="font-size:clamp(1.8rem,3vw,2.5rem);font-weight:700;color:var(--purple-deep);margin-bottom:16px">Google Reviews</h2><div id="reviews-widget-100">'
s2 = s2.replace(old_html, new_html)

# 2. Add PT translation - find the end of PT section and insert before comma+en
# Look for the pattern that ends the PT section and starts EN
old_pt_end = "footer_dev:'Desenvolvido por'},en:"
# But check the actual exact text first
# From the dump: contact_form_msg:"..."},en:{nav_home:"Home"...
# Actually let me find the exact end of pt section
pt_end_start = s2.rfind('"', 0, s2.find('en:{', s2.find('let i18n={')))
# Find the },en:{ pattern
import re
match = re.search(r"'}[^}]*},en:\{", s2[s2.find('let i18n={'):])
# Actually simpler: find the PT section end by searching for },en:{ after the pt section
i18n_start = s2.find('let i18n={')
pt_section = s2[i18n_start:s2.find('en:{', i18n_start)]
# Find last entry before en:{ - look for the pattern "key":"value"
# The pt section ends with ... },en:{
pt_end = s2.find('},en:{', i18n_start)
# The last key-value in PT ends before this },en:{
# We need to find the last complete entry and add after it
# Find the last " before },en:{
last_pt_entry_end = s2.rfind('"', pt_end-5, pt_end-2)
print('PT section ends at', pt_end)

# 3. Add to PT section - insert before },en:{
pt_insert = 'google_reviews_title:"Google Reviews",'
s2 = s2[:pt_end] + pt_insert + s2[pt_end:]

# 4. Add to EN section - find the end of the EN section
# The EN section ends with ... };
en_end = s2.find('};', s2.find('en:{', i18n_start))
en_section_start = s2.find('en:{', i18n_start)
# Find the last entry before the closing };
en_insert_start = en_end
# Find the last " before };
last_en_entry_end = s2.rfind('"', en_end-5, en_end-2)
en_insert = 'google_reviews_title:"Google Reviews",'
s2 = s2[:en_end] + en_insert + s2[en_end:]

with open('Site_02/index.html', 'w', encoding='utf-8') as f:
    f.write(s2)
print('Site_02: OK')
