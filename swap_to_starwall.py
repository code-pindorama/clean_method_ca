# Replace Elfsight with StarWall reviews widget + auto-play

starwall_div = '<div id="reviews-widget-100"></div>'
starwall_script = '<script src="https://starwall.io/embed/BhnLL6sHJtDUo9RUZNprvUJ41dxb1Rvx/widget.js" async></script>'

# Auto-play JS — advances carousel every 4s, pauses on hover
autoplay_js = (
    '<script>'
    '(function(){'
    'function a(){'
    'var w=window.ReviewsWidget_100;'
    'if(!w||!w.carouselManager){setTimeout(a,500);return}'
    'var c=w.carouselManager;'
    'var i=setInterval(function(){'
    'c.currentSlide>=c.totalSlides-1?c.goToSlide(0):c.nextSlide()'
    '},4000);'
    'var e=w.container;'
    'if(e){'
    'e.addEventListener("pointerenter",function(){clearInterval(i);i=null});'
    'e.addEventListener("pointerleave",function(){if(!i)i=setInterval(function(){c.currentSlide>=c.totalSlides-1?c.goToSlide(0):c.nextSlide()},4000)});'
    '}'
    '}'
    'a()'
    '})();'
    '</script>'
)

def apply_autoplay(html):
    # Add autoplay JS before </body> (after StarWall script)
    be = html.find('</body>')
    if be >= 0:
        html = html[:be] + autoplay_js + html[be:]
    return html

print('=== SITE 02 ===')
with open('Site_02/index.html', 'r', encoding='utf-8') as f:
    s2 = f.read()

s2 = s2.replace('<script src="https://static.elfsight.com/platform/platform.js" async></script>', '')
s2 = s2.replace(
    '<div class="elfsight-app-22341ae8-cb06-4454-b006-6d4d8dcbe591"></div>',
    starwall_div
)
be = s2.find('</body>')
if be >= 0:
    if starwall_script not in s2:
        s2 = s2[:be] + starwall_script + s2[be:]
s2 = apply_autoplay(s2)

with open('Site_02/index.html', 'w', encoding='utf-8') as f:
    f.write(s2)
print('Site_02: OK')

print('=== SITE 01 ===')
with open('Site_01/index.html', 'r', encoding='utf-8') as f:
    s1 = f.read()

s1 = s1.replace('<script src="https://static.elfsight.com/platform/platform.js" async></script>', '')
s1 = s1.replace(
    '<div class="elfsight-app-22341ae8-cb06-4454-b006-6d4d8dcbe591"></div>',
    starwall_div
)
be = s1.find('</body>')
if be >= 0:
    if starwall_script not in s1:
        s1 = s1[:be] + starwall_script + s1[be:]
s1 = apply_autoplay(s1)

with open('Site_01/index.html', 'w', encoding='utf-8') as f:
    f.write(s1)
print('Site_01: OK')

print('Done!')
