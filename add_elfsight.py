# Replace custom Google Reviews carousel with Elfsight widget (real reviews)

# Elfsight widget ID
widget_id = '22341ae8-cb06-4454-b006-6d4d8dcbe591'
platform_url = 'https://static.elfsight.com/platform/platform.js'

# The Elfsight widget HTML
elf_div = '<div class="elfsight-app-' + widget_id + '"></div>'

# Remove all g-* CSS related to our custom carousel
# We need to remove: car_css + s2_css / s1_css classes from <style>
# But keep the rest of the CSS intact.
# Easiest: just remove the specific g-* CSS string we injected

car_css_pattern = '.g-wrap{text-align:center;padding:30px 10px}.g-header{display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:20px;flex-wrap:wrap}.g-header-rating{font-size:28px;font-weight:700;line-height:1}.g-carousel{position:relative;max-width:760px;margin:0 auto;overflow:hidden;padding:4px 0}.g-track{display:flex;transition:transform .5s ease}.g-card{flex:0 0 220px;height:240px;margin:0 8px;padding:20px 16px;border-radius:12px;display:flex;flex-direction:column;justify-content:space-between;text-align:left;box-sizing:border-box}.g-card-text{font-size:13px;line-height:1.5;flex:1;overflow:hidden}.g-card-author{font-size:12px;font-weight:600;margin-top:8px}.g-card-read{font-size:11px;text-decoration:none;display:inline-block;margin-top:4px;border-bottom:1px solid;padding-bottom:1px}.g-dots{display:flex;justify-content:center;gap:8px;margin-top:14px}.g-dot{width:10px;height:10px;border-radius:50%;border:none;cursor:pointer;padding:0;transition:background .3s}.g-see-all{display:inline-block;margin-top:16px;padding:8px 22px;border-radius:24px;font-size:13px;font-weight:600;text-decoration:none;transition:all .3s}'

# Per-site CSS to remove
s2_css_pattern = '.g-card{background:var(--white);box-shadow:0 2px 16px rgba(0,0,0,.07)}.g-card-text{color:var(--black)}.g-card-author{color:var(--purple-deep)}.g-card-read{color:var(--copper);border-color:var(--copper)}.g-dot{background:rgba(74,26,122,.25)}.g-dot.active{background:var(--purple-deep)}.g-header-rating{color:var(--purple-deep)}.g-see-all{background:var(--purple);color:var(--white)}.g-see-all:hover{background:var(--purple-deep);transform:translateY(-1px)}'
s1_css_pattern = '.g-card{background:var(--white);box-shadow:var(--shadow-sm)}.g-card-text{color:var(--text-dark)}.g-card-author{color:var(--purple-deep)}.g-card-read{color:var(--copper);border-color:var(--copper)}.g-dot{background:rgba(74,26,122,.25)}.g-dot.active{background:var(--purple-deep)}.g-header-rating{color:var(--purple-deep)}.g-see-all{background:var(--purple-main);color:var(--white)}.g-see-all:hover{background:var(--purple-deep);transform:translateY(-1px)}'

# JS to remove
car_js_pattern = '<script>function gInit(){'

def remove_carousel_css_js(html, css_overrides_pattern):
    # Remove carousel CSS
    html = html.replace(car_css_pattern, '')
    html = html.replace(css_overrides_pattern, '')
    # Remove carousel JS (find the script block and remove it)
    js_start = html.find('<script>function gInit(){')
    if js_start >= 0:
        js_end = html.find('</script>', js_start) + 9  # len of '</script>'
        html = html[:js_start] + html[js_end:]
    return html

print('=== SITE 02 ===')
with open('Site_02/index.html', 'r', encoding='utf-8') as f:
    s2 = f.read()

# Remove custom carousel CSS and JS
s2 = remove_carousel_css_js(s2, s2_css_pattern)

# Add Elfsight platform script (once, before </head> or before </body>)
# We'll add it just before </body>
be = s2.find('</body>')
if be >= 0:
    elf_script = '<script src="' + platform_url + '" async></script>'
    if elf_script not in s2:
        s2 = s2[:be] + elf_script + s2[be:]

# Replace the inner content of testimonials section with Elfsight div
sec_start = s2.find('<section class="testimonials"id="testimonials">')
if sec_start >= 0:
    sec_content_start = sec_start + len('<section class="testimonials"id="testimonials">')
    sec_end = s2.find('</section>', sec_content_start)
    if sec_end > sec_content_start:
        # Replace everything between section tags with the Elfsight div
        new_content = '<div style="text-align:center;padding:20px 10px">' + elf_div + '</div>'
        s2 = s2[:sec_content_start] + new_content + s2[sec_end:]
        with open('Site_02/index.html', 'w', encoding='utf-8') as f:
            f.write(s2)
        print('Site_02: OK')
    else:
        print('Site_02: could not find section end')
else:
    print('Site_02: testimonials section not found')

print('=== SITE 01 ===')
with open('Site_01/index.html', 'r', encoding='utf-8') as f:
    s1 = f.read()

# Remove custom carousel CSS and JS
s1 = remove_carousel_css_js(s1, s1_css_pattern)

# Add Elfsight platform script
be = s1.find('</body>')
if be >= 0:
    elf_script = '<script src="' + platform_url + '" async></script>'
    if elf_script not in s1:
        s1 = s1[:be] + elf_script + s1[be:]

# Replace the testimonials section content
sec_start = s1.find('<section class="section testimonials"id="testimonials">')
if sec_start >= 0:
    sec_content_start = sec_start + len('<section class="section testimonials"id="testimonials">')
    sec_end = s1.find('</section>', sec_content_start)
    if sec_end > sec_content_start:
        new_content = '<div class="container"><div style="text-align:center;padding:10px 0"><div class="services-header"style="margin-bottom:10px"><div class="section-label">Google Reviews</div><h2 class="section-title">O que dizem <span class="highlight">sobre nos</span></h2></div>' + elf_div + '</div></div>'
        s1 = s1[:sec_content_start] + new_content + s1[sec_end:]
        with open('Site_01/index.html', 'w', encoding='utf-8') as f:
            f.write(s1)
        print('Site_01: OK')
    else:
        print('Site_01: could not find section end')
else:
    print('Site_01: testimonials section not found')

print('Done!')
