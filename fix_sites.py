# Google Reviews auto-carousel for both sites

google_url = 'https://maps.app.goo.gl/zs1ntgAKYFbcepaXA'

# Google SVG icon (colorful)
g_svg = '<svg viewBox="0 0 48 48" width="32" height="32"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59A14.5 14.5 0 019.5 24c0-1.59.28-3.14.76-4.59l-7.98-6.19A23.99 23.99 0 000 24c0 3.77.87 7.35 2.56 10.56l7.97-5.97z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 5.97C6.51 42.62 14.62 48 24 48z"/></svg>'

star_y = '<svg viewBox="0 0 24 24" width="18" height="18" fill="#FBBC05"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
stars_5 = star_y * 5

# Carousel CSS — compact, no external deps
car_css = (
  '.g-wrap{text-align:center;padding:30px 10px}'
  '.g-header{display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:20px;flex-wrap:wrap}'
  '.g-header-rating{font-size:28px;font-weight:700;line-height:1}'
  '.g-carousel{position:relative;max-width:760px;margin:0 auto;overflow:hidden;padding:4px 0}'
  '.g-track{display:flex;transition:transform .5s ease}'
  '.g-card{flex:0 0 220px;height:240px;margin:0 8px;padding:20px 16px;border-radius:12px;display:flex;flex-direction:column;justify-content:space-between;text-align:left;box-sizing:border-box}'
  '.g-card-text{font-size:13px;line-height:1.5;flex:1;overflow:hidden}'
  '.g-card-author{font-size:12px;font-weight:600;margin-top:8px}'
  '.g-card-read{font-size:11px;text-decoration:none;display:inline-block;margin-top:4px;border-bottom:1px solid;padding-bottom:1px}'
  '.g-dots{display:flex;justify-content:center;gap:8px;margin-top:14px}'
  '.g-dot{width:10px;height:10px;border-radius:50%;border:none;cursor:pointer;padding:0;transition:background .3s}'
  '.g-see-all{display:inline-block;margin-top:16px;padding:8px 22px;border-radius:24px;font-size:13px;font-weight:600;text-decoration:none;transition:all .3s}'
)

# Per-site theme overrides
s2_css = (
  '.g-card{background:var(--white);box-shadow:0 2px 16px rgba(0,0,0,.07)}'
  '.g-card-text{color:var(--black)}'
  '.g-card-author{color:var(--purple-deep)}'
  '.g-card-read{color:var(--copper);border-color:var(--copper)}'
  '.g-dot{background:rgba(74,26,122,.25)}'
  '.g-dot.active{background:var(--purple-deep)}'
  '.g-header-rating{color:var(--purple-deep)}'
  '.g-see-all{background:var(--purple);color:var(--white)}'
  '.g-see-all:hover{background:var(--purple-deep);transform:translateY(-1px)}'
)
s1_css = (
  '.g-card{background:var(--white);box-shadow:var(--shadow-sm)}'
  '.g-card-text{color:var(--text-dark)}'
  '.g-card-author{color:var(--purple-deep)}'
  '.g-card-read{color:var(--copper);border-color:var(--copper)}'
  '.g-dot{background:rgba(74,26,122,.25)}'
  '.g-dot.active{background:var(--purple-deep)}'
  '.g-header-rating{color:var(--purple-deep)}'
  '.g-see-all{background:var(--purple-main);color:var(--white)}'
  '.g-see-all:hover{background:var(--purple-deep);transform:translateY(-1px)}'
)

# 5 review cards
reviews = [
  ('"Exceptional service! My home has never felt this clean. The team is punctual, polite, and extremely detail-oriented."', 'Maria Silva'),
  ('"We hired them for our office and the difference was immediate. Healthier environment, more productive team."', 'Ricardo Mendes'),
  ('"Post-renovation cleaning was perfect! Everything sparkling, no residue. Super efficient and organized team."', 'Ana Costa'),
  ('"Best cleaning service in Langley! Attention to detail is unmatched. Highly recommend for regular and deep cleaning."', 'Carlos Souza'),
  ('"Our home has never looked better. Trustworthy, reliable, and always goes above and beyond expectations."', 'Juliana Martins'),
]

def make_card(text, author):
    return (
        '<div class="g-card">'
        '<div class="g-card-text">' + text + '</div>'
        '<div class="g-card-author">&mdash; ' + author + '</div>'
        '<a href="' + google_url + '" target="_blank" class="g-card-read">Read on Google &rarr;</a>'
        '</div>'
    )

cards_html = ''.join(make_card(t, a) for t, a in reviews)

# Carousel HTML
carousel_html = (
    '<div class="g-wrap">'
    '<div class="g-header">' + g_svg + '<span class="g-header-rating">5.0</span>' + stars_5 + '</div>'
    '<div class="g-carousel">'
    '<div class="g-track" id="g-track">' + cards_html + '</div>'
    '</div>'
    '<div class="g-dots" id="g-dots"></div>'
    '<a href="' + google_url + '" target="_blank" class="g-see-all">See all reviews &rarr;</a>'
    '</div>'
)

# Carousel JS — auto-play, pause on hover, dot navigation
car_js = (
    '<script>'
    'function gInit(){'
    'var t=document.getElementById("g-track"),c=t.children,d=document.getElementById("g-dots"),l=c.length;'
    'for(var i=0;i<l;i++){'
    'var e=document.createElement("button");'
    'e.className="g-dot";'
    'if(i===0)e.classList.add("active");'
    'e.onclick=(function(idx){return function(){clearInterval(p);p=setInterval(n,3500);o(idx)}})(i);'
    'd.appendChild(e);'
    '}'
    'var s=0,p=setInterval(n,3500);'
    'function o(i){s=i;t.style.transform="translateX(-"+(s*228)+"px)";'
    'var dots=document.querySelectorAll(".g-dot");'
    'for(var j=0;j<dots.length;j++)dots[j].classList.toggle("active",j===s);'
    '}'
    'function n(){o((s+1)%l)}'
    't.parentElement.addEventListener("pointerenter",function(){clearInterval(p);p=null});'
    't.parentElement.addEventListener("pointerleave",function(){if(!p)p=setInterval(n,3500)});'
    '}'
    'document.readyState==="loading"?document.addEventListener("DOMContentLoaded",gInit):gInit();'
    '</script>'
)

print('=== SITE 02 ===')
with open('Site_02/index.html', 'r', encoding='utf-8') as f:
    s2 = f.read()

# Find the testimonials section
s2_start = s2.find('<section class="testimonials"id="testimonials">')
if s2_start >= 0:
    # Find the closing </section> for this section
    s2_end = s2.find('</section>', s2_start) + 10  # len of '</section>'
    new_s2 = (
        '<section class="testimonials"id="testimonials">'
        + carousel_html
        + '</section>'
    )
    s2 = s2[:s2_start] + new_s2 + s2[s2_end:]

    # Add CSS before </style>
    se = s2.find('</style>')
    if se >= 0:
        s2 = s2[:se] + car_css + s2_css + s2[se:]

    # Add JS before </body>
    be = s2.find('</body>')
    if be >= 0:
        s2 = s2[:be] + car_js + s2[be:]

    with open('Site_02/index.html', 'w', encoding='utf-8') as f:
        f.write(s2)
    print('Site_02: OK')
else:
    print('Site_02: testimonials section not found!')

print('=== SITE 01 ===')
with open('Site_01/index.html', 'r', encoding='utf-8') as f:
    s1 = f.read()

# Insert section between about and contact
about_end = s1.find('</section>', s1.find('id="about"'))
contact_start = s1.find('<section class="section contact"', about_end)

if about_end > 0 and contact_start > about_end:
    new_section = (
        '<section class="section testimonials"id="testimonials">'
        '<div class="container">'
        '<div class="services-header"style="margin-bottom:10px">'
        '<div class="section-label">Google Reviews</div>'
        '<h2 class="section-title">O que dizem <span class="highlight">sobre nos</span></h2>'
        '</div>'
        + carousel_html
        + '</div>'
        '</section>'
    )
    # Insert at about_end+10 (right after the closing </section> of about)
    s1 = s1[:about_end + 10] + new_section + s1[about_end + 10:]

    # Add CSS before </style>
    se = s1.find('</style>')
    if se >= 0:
        s1 = s1[:se] + car_css + s1_css + s1[se:]

    # Add JS before </body>
    be = s1.find('</body>')
    if be >= 0:
        s1 = s1[:be] + car_js + s1[be:]

    with open('Site_01/index.html', 'w', encoding='utf-8') as f:
        f.write(s1)
    print('Site_01: OK')
else:
    print('Site_01: insertion point not found')

print('Done!')
