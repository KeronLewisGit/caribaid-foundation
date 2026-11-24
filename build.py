"""Builds the three pages of the Caribaid Foundation preview from one shared header and footer.

    python3 build.py
    python3 -m http.server 8142
"""
from pathlib import Path

WA = '17584860990'
PHONE = '+1 758 486 0990'
EMAIL = 'earl@caribaidfoundation.com'

MARK = '''<svg class="mark" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" stroke-width="3.2"/><circle cx="24" cy="15.5" r="3.6" fill="currentColor"/><path d="M12.5 13.5c3.2 6.5 7 9.3 11.5 9.3s8.300-2.800 11.500-9.300M24 22.800V36" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/></svg>'''

NAV = [('index.html', 'Home'), ('our-work.html', 'Our work'), ('get-involved.html', 'Give &amp; get involved')]


def head(title, desc, page):
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == page else '', t) for h, t in NAV)
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>''' + title + '''</title>
<meta name="description" content="''' + desc + '''">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#2a0f2e">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@400..800&family=Instrument+Serif:ital@1&family=Wix+Madefor+Text:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="util"><div class="wrap">
  <span>Castries, Saint Lucia</span>
  <span class="util-r"><a href="https://wa.me/''' + WA + '''">WhatsApp ''' + PHONE + '''</a><a class="hide-s" href="mailto:''' + EMAIL + '''">''' + EMAIL + '''</a></span>
</div></div>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Caribaid Foundation home">''' + MARK + '''<span><b>Caribaid</b><i>Foundation</i></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
  <nav class="main" id="nav">''' + nav + '''<a class="btn btn-give" href="get-involved.html#give">Give today</a></nav>
</div></header>
<main id="main">
'''


FOOT = '''</main>
<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <a class="brand brand-inv" href="index.html">''' + MARK + '''<span><b>Caribaid</b><i>Foundation</i></span></a>
      <p>A Saint Lucian foundation that helps children and young single mothers with free daycare places, meals, clothes and school supplies.</p>
    </div>
    <div><h3>Find your way</h3><a href="our-work.html">Our work</a><a href="our-work.html#daycare">The daycare we are building</a><a href="get-involved.html#give">Ways to give</a><a href="get-involved.html#volunteer">Volunteer</a></div>
    <div><h3>Talk to us</h3><a href="https://wa.me/''' + WA + '''">WhatsApp ''' + PHONE + '''</a><a href="mailto:''' + EMAIL + '''">''' + EMAIL + '''</a><span>Jeremie Street, Castries, Saint Lucia</span></div>
  </div>
  <div class="wrap foot-base"><span>&copy; <span data-year>2026</span> Caribaid Foundation</span><span>Photos: Wikimedia Commons contributors. <a href="get-involved.html#credits">Credits</a></span></div>
</footer>
<div class="mbar"><a href="get-involved.html#give" class="mbar-give">Give today</a><a href="https://wa.me/''' + WA + '''">WhatsApp us</a></div>
<p class="preview-flag">Preview by Code Canvas · wording and photos to be confirmed with Caribaid</p>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def inner_hero(kicker, title, lede, img, pos='center'):
    return '''<section class="phero">
  <div class="phero-img" style="background-image:url(assets/img/''' + img + ''');background-position:''' + pos + '''"></div>
  <div class="wrap phero-in"><p class="kick">''' + kicker + '''</p><h1>''' + title + '''</h1><p class="lede">''' + lede + '''</p></div>
</section>
'''


ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

TASKS = '''<section class="tasks"><div class="wrap">
  <p class="tasks-k">I&rsquo;d like to&hellip;</p>
  <div class="tasks-row">
    <a class="task" href="get-involved.html#give" data-pick="clothes" data-r><span class="task-n">01</span><b>Give clothes or school supplies</b>''' + ARROW + '''</a>
    <a class="task" href="our-work.html#daycare" data-r><span class="task-n">02</span><b>Help build the daycare</b>''' + ARROW + '''</a>
    <a class="task" href="get-involved.html#volunteer" data-r><span class="task-n">03</span><b>Volunteer my time</b>''' + ARROW + '''</a>
    <a class="task" href="https://wa.me/''' + WA + '''" data-r><span class="task-n">04</span><b>Talk to Earl</b>''' + ARROW + '''</a>
  </div>
</div></section>
'''

WALL = '<div class="wallviz" data-wall aria-hidden="true">' + ''.join('<i style="--i:%d"></i>' % i for i in range(50)) + '</div>'

DAYCARE = '''<section class="build" id="daycare"><div class="wrap build-grid">
  <div class="build-copy">
    <p class="kick kick-l">What we are working towards</p>
    <h2>A free daycare with room for <em>fifty</em> children.</h2>
    <p>Today Caribaid pays for places at private daycares. Our goal is a daycare of our own, free to the families who need it most, so that no young mother has to choose between her child and her schooling.</p>
    <ul class="ticks">
      <li>Building materials: blocks, cement, steel, roofing</li>
      <li>Sponsors, in Saint Lucia or abroad</li>
      <li>Skilled hands: builders, electricians, plumbers</li>
    </ul>
    <a class="btn btn-lime" href="get-involved.html#give" data-pick="building">Help us build it</a>
  </div>
  <div class="build-vis" data-r>
    ''' + WALL + '''
    <p class="wall-cap"><b>50</b> places. One block for each child the daycare will hold.</p>
  </div>
</div></section>
'''

HOME = head('Caribaid Foundation | Free daycare, meals and school supplies for children in Saint Lucia',
            'Caribaid Foundation helps children and young single mothers in Saint Lucia with free daycare places, meals, clothes and school supplies.', 'index.html') + '''
<section class="hero">
  <div class="hero-img"></div>
  <div class="wrap hero-in">
    <p class="kick">Caribaid Foundation · Castries, Saint Lucia</p>
    <h1><span class="ln">Every child in</span> <span class="ln">Saint Lucia deserves</span> <span class="ln">a fair <em>start.<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M4 13c58-9 118-11 176-7 40 2 80 5 116 9" /></svg></em></span></h1>
    <p class="lede">We help children and young single mothers with free daycare places, meals, clothes and school supplies, so that mothers can go back to school and children are cared for.</p>
    <div class="hero-cta"><a class="btn btn-lime" href="get-involved.html#give">Give today</a><a class="btn btn-ghost" href="our-work.html">See our work</a></div>
  </div>
  <div class="hero-note" data-r><span class="dot"></span><p><b>Building now:</b> a free daycare for 50 children. <a href="our-work.html#daycare">How you can help</a></p></div>
</section>
''' + TASKS + '''
<section class="band"><div class="wrap">
  <div class="sec-head"><h2 data-r>Three things we do, <em>every week.</em></h2><p data-r>Caribaid is small and local. What we are given goes to children and mothers we know by name.</p></div>
  <div class="cards">
    <article class="card" data-r><div class="card-img"><img src="assets/img/play.jpg" alt="A small child stacking coloured wooden blocks at a table" loading="lazy"></div><div class="card-b"><span class="tag">Daycare</span><h3>Free daycare places</h3><p>We pay for a child&rsquo;s place at daycare so a young single mother can return to school or work.</p><a href="our-work.html#daycare-places">How it works''' + ARROW + '''</a></div></article>
    <article class="card" data-r><div class="card-img"><img src="assets/img/lunch.jpg" alt="A lunch box packed with apples, tomatoes, peppers and cucumber" loading="lazy"></div><div class="card-b"><span class="tag">Meals</span><h3>A feeding programme</h3><p>A child who has eaten can play, listen and learn. We provide meals for the children in our care.</p><a href="our-work.html#meals">How it works''' + ARROW + '''</a></div></article>
    <article class="card" data-r><div class="card-img"><img src="assets/img/crayons.jpg" alt="A box of crayons on a pile of loose crayons in every colour" loading="lazy"></div><div class="card-b"><span class="tag">Supplies</span><h3>Clothes and school supplies</h3><p>We collect good used clothes, books, bags and stationery and pass them to families who need them.</p><a href="our-work.html#supplies">How it works''' + ARROW + '''</a></div></article>
  </div>
</div></section>
''' + DAYCARE + '''
<section class="band band-paper"><div class="wrap split">
  <div class="split-img" data-r><img src="assets/img/soufriere.jpg" alt="The town of Soufrière and the Pitons seen from the hills, Saint Lucia" loading="lazy"><span class="stamp">Since 2013</span></div>
  <div class="split-copy">
    <p class="kick kick-d">Who we are</p>
    <h2 data-r>Started in Castries by <em>Earl Augustin.</em></h2>
    <p data-r>Caribaid Foundation is a not-for-profit organisation founded by Earl Augustin. When a schoolgirl becomes a mother, her own education usually stops. A free daycare place gives her a way back.</p>
    <p data-r>The work also covers meals, clothing, school supplies and mentoring for young boys, and it is carried by volunteers: fundraisers, cooks, teachers and mentors.</p>
    <a class="link" href="our-work.html" data-r>Read more about our work''' + ARROW + '''</a>
  </div>
</div></section>
<section class="cta"><div class="wrap cta-in">
  <h2 data-r>You do not need much to <em>help.</em></h2>
  <p data-r>A bag of clothes your children have outgrown. A box of exercise books. An afternoon of your time. Tell us what you can give and we will arrange the rest.</p>
  <div class="hero-cta" data-r><a class="btn btn-lime" href="get-involved.html#give">See ways to give</a><a class="btn btn-ghost" href="https://wa.me/''' + WA + '''">WhatsApp Earl</a></div>
</div></section>
''' + FOOT

WORK = head('Our work | Caribaid Foundation, Saint Lucia', 'Free daycare places, a feeding programme, clothes and school supplies, and mentoring for boys: what Caribaid Foundation does in Saint Lucia.', 'our-work.html') + inner_hero('Our work', 'Care for the child. A way back to school for the <em>mother.</em>', 'Four programmes, run by volunteers in Saint Lucia.', 'soufriere.jpg', 'center 60%') + '''
<section class="band"><div class="wrap">
  <div class="sec-head"><h2 data-r>How a free daycare place <em>changes things.</em></h2><p data-r>The same three steps, one family at a time.</p></div>
  <ol class="path" data-path>
    <li data-r><span class="path-n">1</span><h3>A young mother reaches us</h3><p>Often she is still of school age, on her own, and has had to leave school to mind her baby.</p></li>
    <li data-r><span class="path-n">2</span><h3>Her child gets a place</h3><p>Caribaid pays for the child&rsquo;s place at a daycare, with meals, at no cost to the family.</p></li>
    <li data-r><span class="path-n">3</span><h3>She goes back to school</h3><p>With her child safe and fed during the day, she can finish her education or take up work.</p></li>
  </ol>
</div></section>
<section class="band band-paper"><div class="wrap">
  <div class="rows">
    <article class="row" id="daycare-places"><div class="row-img" data-r><img src="assets/img/play.jpg" alt="A small child stacking coloured wooden blocks at a table" loading="lazy"></div><div class="row-b"><span class="tag">Programme 01</span><h2 data-r>Free daycare places</h2><p data-r>We pay for daycare places for the children of young single mothers and families who cannot afford the fees. The child is looked after during the day; the mother is free to study or work.</p><ul class="ticks ticks-d" data-r><li>For children of single, low-income mothers</li><li>No cost to the family</li><li>The number of places depends on what we are given</li></ul></div></article>
    <article class="row row-flip" id="meals"><div class="row-img" data-r><img src="assets/img/lunch.jpg" alt="A lunch box packed with apples, tomatoes, peppers and cucumber" loading="lazy"></div><div class="row-b"><span class="tag">Programme 02</span><h2 data-r>The feeding programme</h2><p data-r>A child who has eaten can play, listen and learn. Our feeding programme provides meals for the children we support, with the help of volunteer cooks and donated groceries.</p><ul class="ticks ticks-d" data-r><li>Meals for children at daycare</li><li>Cooked by volunteers</li><li>Dry goods and fresh produce always welcome</li></ul></div></article>
    <article class="row" id="supplies"><div class="row-img" data-r><img src="assets/img/crayons.jpg" alt="A box of crayons on a pile of loose crayons in every colour" loading="lazy"></div><div class="row-b"><span class="tag">Programme 03</span><h2 data-r>Clothes and school supplies</h2><p data-r>Good used clothes, shoes, school bags, exercise books and pencils are collected and passed on to families who need them.</p><ul class="ticks ticks-d" data-r><li>Clean clothes and shoes for babies and children</li><li>Books, bags, pencils and crayons</li><li>Drop off in Castries or ask us to collect</li></ul></div></article>
    <article class="row row-flip" id="mentoring"><div class="row-img" data-r><img src="assets/img/pencils.jpg" alt="A row of sharpened coloured pencils" loading="lazy"></div><div class="row-b"><span class="tag">Programme 04</span><h2 data-r>A boot camp for young boys</h2><p data-r>Boys need steady adults too. Our mentors run a boot camp that gives young boys structure, discipline and someone to talk to.</p><ul class="ticks ticks-d" data-r><li>Led by volunteer mentors</li><li>For school-age boys</li><li>Mentors and special-aid teachers wanted</li></ul></div></article>
  </div>
</div></section>
''' + DAYCARE + '''
<section class="band"><div class="wrap split split-video">
  <div class="split-copy">
    <p class="kick kick-d">In the media</p>
    <h2 data-r>&ldquo;This Foundation <em>Cares.</em>&rdquo;</h2>
    <p data-r>In 2015 Earl Augustin sat down with Delia Dolor on <b>The Dolor Factor</b> to talk about single parents in Saint Lucia and why support works better than blame. The five-part interview is on her YouTube channel.</p>
    <a class="link" href="https://www.youtube.com/watch?v=gLYzexllWoE" target="_blank" rel="noopener" data-r>Watch on YouTube''' + ARROW + '''</a>
  </div>
  <button class="video" data-yt="gLYzexllWoE" aria-label="Play the interview: The Dolor Factor, This Foundation Cares, part 1" data-r>
    <img src="https://i.ytimg.com/vi/gLYzexllWoE/hqdefault.jpg" alt="" loading="lazy">
    <span class="play"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></span>
    <span class="video-cap">The Dolor Factor · Part 1 · Delia Dolor</span>
  </button>
</div></section>
<section class="cta"><div class="wrap cta-in">
  <h2 data-r>Every programme runs on what people <em>give.</em></h2>
  <p data-r>There is no big office and no paid staff. If you can spare clothes, supplies, food, materials or time, it reaches a child.</p>
  <div class="hero-cta" data-r><a class="btn btn-lime" href="get-involved.html#give">See ways to give</a><a class="btn btn-ghost" href="get-involved.html#volunteer">Volunteer</a></div>
</div></section>
''' + FOOT

OPTS = [('clothes', 'Clothes'), ('supplies', 'School supplies'), ('food', 'Food'), ('building', 'Building materials'), ('money', 'Money'), ('time', 'My time')]

GIVE = head('Give and get involved | Caribaid Foundation, Saint Lucia', 'Give clothes, school supplies, food, building materials, money or your time to Caribaid Foundation in Saint Lucia.', 'get-involved.html') + inner_hero('Give &amp; get involved', 'Tell us what you can give. We will do the <em>rest.</em>', 'Pick what you have. We reply on WhatsApp, usually the same day.', 'harbour.jpg', 'center 45%') + '''
<section class="band" id="give"><div class="wrap">
  <div class="sec-head"><h2 data-r>What would you like to <em>give?</em></h2><p data-r>Choose one or more. The message to Earl writes itself.</p></div>
  <div class="picker" data-picker>
    <div class="chips" role="group" aria-label="What I can give">''' + ''.join('<button type="button" class="chip" data-k="%s" aria-pressed="false">%s</button>' % o for o in OPTS) + '''</div>
    <div class="picker-grid">
      <div class="advice" aria-live="polite"><p class="advice-empty">Pick something above to see what helps most.</p></div>
      <form class="send" novalidate>
        <label>Your name<input name="name" autocomplete="name" required></label>
        <label>Where are you?<select name="where"><option>In Saint Lucia</option><option>Overseas</option></select></label>
        <label>Anything we should know <span>(optional)</span><textarea name="note" rows="3"></textarea></label>
        <p class="send-prev" data-preview></p>
        <button class="btn btn-give btn-wide" type="submit">Send on WhatsApp</button>
        <p class="send-alt">Prefer email? <a href="mailto:''' + EMAIL + '''" data-mail>Send the same message by email</a></p>
        <p class="send-err" role="alert" hidden>Please add your name and pick at least one thing to give.</p>
      </form>
    </div>
  </div>
</div></section>
<section class="band band-paper" id="volunteer"><div class="wrap">
  <div class="sec-head"><h2 data-r>Give an afternoon. <em>Volunteer.</em></h2><p data-r>Caribaid is run entirely by volunteers. These are the hands we need most.</p></div>
  <div class="roles">
    <div class="role" data-r><span>01</span><h3>Cooks</h3><p>Help prepare meals for the children in the feeding programme.</p></div>
    <div class="role" data-r><span>02</span><h3>Mentors</h3><p>Spend time with boys in the boot camp. Be the steady adult.</p></div>
    <div class="role" data-r><span>03</span><h3>Special-aid teachers</h3><p>Support children who need extra help with reading, numbers or speech.</p></div>
    <div class="role" data-r><span>04</span><h3>Fundraisers</h3><p>Organise a collection at your workplace, church, school or club.</p></div>
  </div>
  <p class="roles-cta" data-r><a class="btn btn-give" href="#give" data-pick="time">I can volunteer</a></p>
</div></section>
<section class="band" id="contact"><div class="wrap split split-map">
  <div class="split-copy">
    <p class="kick kick-d">Find us</p>
    <h2 data-r>Jeremie Street, <em>Castries.</em></h2>
    <dl class="facts" data-r>
      <div><dt>WhatsApp or call</dt><dd><a href="https://wa.me/''' + WA + '''">''' + PHONE + '''</a></dd></div>
      <div><dt>Email</dt><dd><a href="mailto:''' + EMAIL + '''">''' + EMAIL + '''</a></dd></div>
      <div><dt>Drop-off</dt><dd>Jeremie Street, Castries. Please message first so someone is there to receive you.</dd></div>
      <div><dt>Overseas</dt><dd>Sending a barrel or a parcel? Message us and we will give you the delivery details.</dd></div>
    </dl>
  </div>
  <div class="mapbox" data-r>
    <img src="assets/img/jeremie-street.jpg" alt="Castries Central Market seen from Jeremie Street" loading="lazy">
    <a class="btn btn-lime" href="https://www.google.com/maps/search/?api=1&query=Jeremie+Street+Castries+Saint+Lucia" target="_blank" rel="noopener">Open in Google Maps</a>
  </div>
</div></section>
<section class="band band-paper faq"><div class="wrap narrow">
  <h2 data-r>Common <em>questions</em></h2>
  <details data-r><summary>What condition should clothes be in?</summary><p>Clean and wearable: something you would be happy to see your own child in. Baby and children&rsquo;s sizes are needed most.</p></details>
  <details data-r><summary>Can I give from overseas?</summary><p>Yes. Many Saint Lucians abroad send barrels or parcels. Message us first and we will tell you where to send them and what is needed that month.</p></details>
  <details data-r><summary>Can my company or church sponsor a child&rsquo;s daycare place?</summary><p>Yes. Tell us how many places and for how long, and we will explain how it works and report back to you.</p></details>
  <details data-r><summary>How do I get help for my own child?</summary><p>Message Earl on WhatsApp or come and see us in Castries. Everything you tell us is kept private.</p></details>
  <p class="credits" id="credits">Photo credits (Wikimedia Commons): Castries harbour by P. Hughes, CC BY 4.0. Soufrière and the Pitons by DavidMPyle, CC BY 4.0. Castries Market from Jeremie Street by Gene93k, CC BY-SA 3.0. Building blocks by Shixart1985, CC BY 2.0. Crayons by Conrad 7, CC0. Lunch box by Hay Kranen, CC0. Coloured pencils by Dietmar Rabich, CC BY-SA 4.0.</p>
</div></section>
''' + FOOT

root = Path(__file__).parent
for name, html in (('index.html', HOME), ('our-work.html', WORK), ('get-involved.html', GIVE)):
    (root / name).write_text(html)
(root / 'assets/favicon.svg').write_text(MARK.replace('class="mark"', 'xmlns="http://www.w3.org/2000/svg" style="color:#a8156f"').replace(' aria-hidden="true"', ''))
print('built 3 pages')
