"""Builds the HTA & Associates pages. Run: python3 build.py  (writes into ./out)"""
import os, json, html, shutil


EMAIL = "htaandassociates@gmail.com"   # swap for the official address in one place
SITE = "https://htaassociates.com/"
GPT = "https://chatgpt.com/g/g-Rf8pxQHPk-hollywood-s-top-attorney"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "docs")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Hanken+Grotesk:wght@400;500;600&display=swap">')

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "HTA & Associates", "url": SITE, "email": EMAIL,
       "logo": SITE + "assets/favicon.svg", "areaServed": ["New York", "Los Angeles"], "sameAs": ["https://www.instagram.com/htaassociates/"],
       "description": "Strategic legal intelligence, advocacy and consulting for media, law and reputation. New York and Los Angeles."}

NAV = [("index.html#divisions", "Divisions"), ("lounge.html", "Legal Lounge"), ("newsroom.html", "Newsroom")]

def head(title, desc, path, css=""):
    d = html.escape(desc)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="HTA &amp; Associates">
<meta property="og:title" content="{title}"><meta property="og:description" content="{d}"><meta property="og:url" content="{SITE}{path}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:image" content="{SITE}assets/lady-justice.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#131110">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="assets/hta.css">
<script type="application/ld+json">{json.dumps(ORG)}</script>
<style>{css}</style>
</head>
<body class="ink">
"""

def bar(current):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="bar"><div class="wrap">
<a class="mark" href="index.html">HTA <i>&amp;</i> Associates</a>
<nav class="nav" aria-label="Main">{links}<a class="nav-cta" href="index.html#consult">Private Consultation</a></nav>
</div></header>
"""

FOOT = f"""<footer class="foot"><div class="wrap">
<p class="foot-name">HTA <i>&amp;</i> Associates</p>
<div class="foot-row">
  <p class="foot-tag">One Team. Two Cities. Limitless Advantage.</p>
  <nav class="foot-links" aria-label="Footer"><a href="lounge.html">Legal Lounge</a><a href="newsroom.html">Newsroom</a><a href="index.html#consult">Private Consultation</a><a href="legal.html">Privacy &amp; Terms</a><a href="https://www.instagram.com/htaassociates/" target="_blank" rel="noopener me">Instagram</a></nav>
</div>
<p class="disclaimer"><strong>HTA &amp; Associates is a strategic legal intelligence, advocacy and consulting organization.</strong>
It is not a law firm and does not provide legal representation or legal advice. Legal services are provided only through independently licensed attorneys where applicable.
Using this site, requesting a consultation or buying a Legal Lounge pass does not create an attorney-client relationship; information you send to HTA is confidential but not protected by attorney-client privilege.</p>
<p class="disclaimer">© 2026 HTA &amp; Associates · New York · Los Angeles · {EMAIL}</p>
</div></footer>
</body>
</html>
"""

# ---------------------------------------------------------------- HOME
HOME_CSS = """
.hero{padding-block:clamp(40px,6vw,80px) 0}
.hero-top{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;padding-bottom:18px;border-bottom:1px solid var(--ink)}
.words{font-size:clamp(4.6rem,17.5vw,15.5rem);line-height:.84;letter-spacing:-.02em;padding-block:clamp(18px,3vw,36px) clamp(26px,4vw,48px)}
.words span{display:block}
.words .r{color:var(--oxblood)}
.words .r i{font-family:var(--serif);font-weight:500;font-style:italic;letter-spacing:-.01em}
.hero-base{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(28px,5vw,80px);align-items:end;padding-block:30px clamp(56px,8vw,96px)}
.hero-base .acts{display:flex;flex-wrap:wrap;gap:12px;justify-content:flex-end}
@media (max-width:860px){.hero-base{grid-template-columns:1fr}.hero-base .acts{justify-content:flex-start}}

.pillars{display:grid;grid-template-columns:repeat(5,minmax(0,1fr))}
.pillar{display:grid;gap:12px;padding:36px clamp(14px,2vw,28px);border-left:1px solid rgba(238,232,220,.18)}
.pillar:first-child{border-left:0;padding-left:0}
.pillar h3{font-size:clamp(1.6rem,2.4vw,2.2rem)}
.pillar p{color:var(--grey-d);font-size:.95rem}
@media (max-width:900px){.pillars{grid-template-columns:1fr 1fr}.pillar{border-left:0;padding-left:0;border-top:1px solid rgba(238,232,220,.18)}.pillar:last-child{grid-column:1/-1}}

.promise{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,4vw,56px)}
.promise div{display:grid;gap:12px;align-content:start;padding-top:18px;border-top:8px solid var(--oxblood)}
.promise h3{font-size:clamp(2.2rem,3.6vw,3.2rem)}
@media (max-width:860px){.promise{grid-template-columns:1fr}}

.start{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:clamp(28px,5vw,80px);align-items:start}
.chips{display:grid;gap:10px}
.chip{display:flex;justify-content:space-between;align-items:center;gap:14px;width:100%;text-align:left;background:transparent;color:var(--ivory);border:1px solid rgba(238,232,220,.3);padding:18px 20px;font-family:var(--serif);font-size:1.3rem;cursor:pointer;transition:background .2s,border-color .2s}
.chip:after{content:"→";font-family:var(--body);opacity:.5}
.chip:hover{border-color:var(--ivory)}
.chip[aria-pressed="true"]{background:var(--ivory);color:var(--ink);border-color:var(--ivory)}
.chip[aria-pressed="true"]:after{opacity:1}
.answer{position:sticky;top:110px;background:var(--oxblood);padding:clamp(26px,3.4vw,44px);display:grid;gap:18px}
.answer h3{font-size:clamp(2rem,3.4vw,2.8rem)}
.answer ol{margin:0;padding:0;list-style:none;display:grid;gap:14px;counter-reset:m}
.answer li{display:grid;grid-template-columns:40px minmax(0,1fr);gap:10px;counter-increment:m}
.answer li:before{content:counter(m);font-family:var(--display);font-size:2rem;line-height:1;color:var(--brass-hi)}
.answer .btn{justify-self:start;background:var(--ivory);color:var(--ink);border-color:var(--ivory)}
.answer .btn:hover{background:var(--brass-hi);border-color:var(--brass-hi)}
.answer small{color:rgba(238,232,220,.7);font-size:.82rem}
@media (max-width:860px){.start{grid-template-columns:1fr}.answer{position:static}}
.about{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(36px,7vw,110px);align-items:start}
.about dl{margin:0;display:grid}
.about dl div{display:grid;grid-template-columns:170px minmax(0,1fr);gap:22px;padding-block:22px;border-top:1px solid var(--ink)}
.about dt{padding-top:5px}
.about dd{margin:0;font-family:var(--serif);font-size:1.32rem;line-height:1.4}
@media (max-width:860px){.about{grid-template-columns:1fr}.about dl div{grid-template-columns:1fr;gap:6px}}

.divs{display:grid;border-top:3px solid var(--gold-2)}
.div{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(20px,5vw,80px);padding-block:clamp(28px,3.4vw,44px);border-bottom:1px solid rgba(238,232,220,.2);transition:padding .3s}
.div h3{font-size:clamp(2rem,4.2vw,3.6rem)}
.div .tag{font-family:var(--serif);font-style:italic;font-size:1.3rem;color:var(--brass-hi);margin-bottom:8px}
.div p:last-child{color:var(--grey-d)}
.div:hover h3{color:var(--brass-hi)}
@media (max-width:860px){.div{grid-template-columns:1fr;gap:10px}}

.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,4vw,56px)}
.step{display:grid;gap:14px;align-content:start}
.step b{font-family:var(--display);font-weight:400;font-size:clamp(5rem,9vw,8rem);line-height:.8;color:var(--oxblood)}
.step h3{padding-top:14px;border-top:8px solid var(--ink)}
@media (max-width:860px){.steps{grid-template-columns:1fr}}

.cities{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px;background:var(--ivory)}
.city{padding:clamp(36px,5vw,64px) clamp(20px,4vw,48px);display:grid;gap:14px;align-content:start}
.city h3{font-size:clamp(3rem,7vw,6rem)}
.council{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:clamp(24px,5vw,80px);align-items:end;margin-top:clamp(48px,7vw,90px)}
@media (max-width:860px){.cities,.council{grid-template-columns:1fr}}

.consult{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(36px,6vw,90px)}
.consult-copy{display:grid;gap:22px;align-content:start}
.addr{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.addr code{font-family:var(--body);font-weight:600;user-select:all}
.addr button{background:none;border:1px solid currentColor;color:inherit;font:inherit;font-size:.7rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;padding:7px 12px;cursor:pointer}
form{display:grid;grid-template-columns:1fr 1fr;gap:22px 20px}
.f{display:grid;gap:6px;min-width:0}
.f--wide,.check,.form-note,form .btn{grid-column:1/-1}
label{font-size:.7rem;font-weight:600;letter-spacing:.24em;text-transform:uppercase}
input,select,textarea{width:100%;background:transparent;border:0;border-bottom:2px solid rgba(238,232,220,.55);color:var(--ivory);font:inherit;font-size:1.15rem;padding:10px 0;border-radius:0}
select option{color:#131110}
input:focus,select:focus,textarea:focus{border-bottom-color:var(--brass-hi);outline:none}
textarea{min-height:110px;resize:vertical}
.check{display:flex;gap:12px;align-items:flex-start;font-size:.92rem}
.check input{width:18px;height:18px;margin-top:4px;flex:none;accent-color:var(--brass)}
.check label{text-transform:none;letter-spacing:0;font-weight:400;font-size:.92rem}
form .btn{justify-self:start;background:var(--ivory);color:var(--ink);border-color:var(--ivory)}
form .btn:hover{background:var(--brass-hi);border-color:var(--brass-hi)}
.form-note{min-height:1.4em;color:var(--brass-hi)}
@media (max-width:860px){.consult,form{grid-template-columns:1fr}}
"""

DIVISIONS = [
    ("Legal Strategy &amp; Support", "Strategic. Proactive. Protective.",
     "Legal-support strategy, dispute communications and pre-litigation coordination with independent counsel, including cease-and-desist matters, to protect your rights and interests."),
    ("Investigations &amp; Intelligence", "Information. Evidence. Clarity.",
     "In-depth research, open-source intelligence and strategic analysis that bring the facts into focus before you make a move."),
    ("Media &amp; Reputation Protection", "Your reputation. Our priority.",
     "We monitor, analyze and respond to media threats, false narratives and online attacks, safeguarding your brand, credibility and legacy."),
    ("Advocacy &amp; Creator Protection", "Voices matter. We stand with you.",
     "We advocate for creators, entrepreneurs, public figures and individuals facing harassment, defamation or unfair treatment."),
    ("Strategic Affairs &amp; Consulting", "Strategy. Influence. Impact.",
     "Crisis response planning, risk management and executive advisory for complex situations and high-stakes matters."),
    ("Federal Affairs &amp; Government Liaison", "Access. Clarity. Results.",
     "Guidance for navigating federal matters, agency processes and policy issues in complex government environments."),
]

def home():
    pillars = [("Discretion", "Your privacy is our priority."), ("Strategy", "Intelligence-driven legal support."),
               ("Protection", "Safeguarding your interests."), ("Preparation", "Organized. Informed. Always ready."),
               ("Results", "Focused on clarity. Driven by outcomes.")]
    pil = "".join(f'<div class="pillar"><h3>{t}</h3><p>{d}</p></div>' for t, d in pillars)
    divs = "".join(f'<article class="div"><h3>{t}</h3><div><p class="tag">{g}</p><p>{d}</p></div></article>' for t, g, d in DIVISIONS)
    areas = "".join(f"<option>{html.unescape(t)}</option>" for t, _, _ in DIVISIONS)
    return head("HTA &amp; Associates",
                "Strategic legal intelligence for media, law and reputation. New York and Los Angeles. Private consultations by appointment.",
                "", HOME_CSS) + bar("") + f"""
<section class="cine">
  <canvas id="lights" aria-hidden="true"></canvas>

  <div class="wrap">
  <div class="hero-top label"><span>Strategic legal intelligence</span><span>New York · Los Angeles</span><span>By appointment</span></div>
  <figure class="lj"><img src="assets/lady-justice.jpg" width="512" height="512" alt="Lady Justice, blindfolded, holding the scales of justice"></figure>
  <h1 class="words"><span>Media.</span><span>Law.</span><span class="r"><i>Reputation.</i></span></h1>
  <hr class="heavy-rule">
  <div class="hero-base">
    <p class="lede">We fight for people and their rights. A private place to be heard, protected and directed to justice, with discretion and excellence.</p>
    <div class="acts"><a class="btn" href="#consult">Private Consultation</a><a class="btn btn--line" href="lounge.html">The Legal Lounge</a></div>
  </div>
  </div>
</section>
<script>
(function(){{
 var c=document.getElementById('lights'),x=c.getContext('2d'),W,H,mx=-999,my=-999,P=[],S=[],still=matchMedia('(prefers-reduced-motion: reduce)').matches;
 function size(){{var r=devicePixelRatio||1;W=c.offsetWidth;H=c.offsetHeight;c.width=W*r;c.height=H*r;x.setTransform(r,0,0,r,0,0)}}
 function seed(){{
  P=[];for(var i=0;i<90;i++){{var left=Math.random()<.5,u=Math.random();
   P.push({{x:left?u*W*.55:W*.45+u*W*.55,y:Math.random()*H,r:6+Math.random()*Math.random()*46,a:.05+Math.random()*.22,
   h:left?(Math.random()<.6?'200,215,255':'247,227,166'):(Math.random()<.65?'255,176,92':'247,227,166'),v:.04+Math.random()*.18,t:Math.random()*6.28}})}}
  S=[];for(var j=0;j<14;j++)S.push({{y:H*(.72+Math.random()*.26),x:Math.random()*W,l:80+Math.random()*260,v:(Math.random()<.5?-1:1)*(.6+Math.random()*1.8),c:Math.random()<.5?'255,90,60':'255,236,200'}});
 }}
 function draw(){{
  x.clearRect(0,0,W,H);
  var g=x.createRadialGradient(W*.5,H*.35,0,W*.5,H*.35,W*.7);g.addColorStop(0,'rgba(201,162,74,.10)');g.addColorStop(1,'rgba(9,9,11,0)');x.fillStyle=g;x.fillRect(0,0,W,H);
  x.globalCompositeOperation='lighter';
  P.forEach(function(p){{p.y-=p.v;p.t+=.01;if(p.y<-60){{p.y=H+60}}
   var a=p.a*(.75+.25*Math.sin(p.t)),b=x.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r);
   b.addColorStop(0,'rgba('+p.h+','+a+')');b.addColorStop(.6,'rgba('+p.h+','+a*.35+')');b.addColorStop(1,'rgba('+p.h+',0)');
   x.fillStyle=b;x.beginPath();x.arc(p.x,p.y,p.r,0,6.283);x.fill()}});
  S.forEach(function(s){{s.x+=s.v;if(s.x>W+s.l)s.x=-s.l;if(s.x<-s.l)s.x=W+s.l;
   var k=x.createLinearGradient(s.x-s.l,0,s.x,0);k.addColorStop(0,'rgba('+s.c+',0)');k.addColorStop(1,'rgba('+s.c+',.55)');
   x.strokeStyle=k;x.lineWidth=1.4;x.beginPath();x.moveTo(s.x-s.l,s.y);x.lineTo(s.x,s.y);x.stroke()}});
  if(mx>-999){{var m=x.createRadialGradient(mx,my,0,mx,my,260);m.addColorStop(0,'rgba(247,227,166,.16)');m.addColorStop(1,'rgba(247,227,166,0)');x.fillStyle=m;x.fillRect(mx-260,my-260,520,520)}}
  x.globalCompositeOperation='source-over';
  if(!still)requestAnimationFrame(draw);
 }}
 c.parentNode.addEventListener('pointermove',function(e){{var r=c.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top}});c.parentNode.addEventListener('pointerleave',function(){{mx=my=-999}});
 size();seed();draw();addEventListener('resize',function(){{size();seed();if(still)draw()}});
}})();
</script>

<section class="band"><div class="wrap"><div class="pillars">{pil}</div></div></section>

<section class="section heard"><div class="wrap">
  <div class="head"><p class="label">Our promise</p><h2>You will be heard.</h2></div>
  <div class="promise">
    <div><h3>Heard.</h3><p class="muted">A private, confidential conversation, behind closed doors. No judgment. Your story, in full.</p></div>
    <div><h3>Protected.</h3><p class="muted">A plan to stop the damage, secure what is yours and keep your name intact.</p></div>
    <div><h3>Defended.</h3><p class="muted">People in your corner who advocate for you, and independently licensed attorneys whenever the matter calls for one.</p></div>
  </div>
</div></section>

<section class="ink section" id="start"><div class="wrap">
  <div class="head"><p class="label">Start here</p><h2>What's happening?</h2><p class="lede muted">Choose the closest match. We'll show you how HTA would begin. Nothing you click here is sent anywhere.</p></div>
  <div class="start">
    <div class="chips" role="group" aria-label="Situations" id="chips"></div>
    <div class="answer" aria-live="polite">
      <p class="label" id="a-div"></p>
      <h3 id="a-title"></h3>
      <ol id="a-steps"></ol>
      <a class="btn" href="#consult" id="a-go">Talk to us about this</a>
      <small>General information about how we work, not legal advice.</small>
    </div>
  </div>
</div></section>

<section class="section" id="about"><div class="wrap about">
  <div class="head" style="margin:0"><p class="label">About the house</p><h2>Where law, media and strategy meet.</h2><p class="lede muted">Delivering intelligence, clarity and solutions when it matters most.</p></div>
  <dl>
    <div><dt class="label">Who we are</dt><dd>A strategic intelligence firm built at the crossroads of legal, media and reputation advisory.</dd></div>
    <div><dt class="label">What we do</dt><dd>Elite advisory, crisis support, risk management and actionable intelligence.</dd></div>
    <div><dt class="label">Who we serve</dt><dd>Creators, executives, entrepreneurs, public figures, media organizations and businesses worldwide.</dd></div>
    <div><dt class="label">Our approach</dt><dd>Human expertise, sharpened by advanced intelligence systems.</dd></div>
    <div><dt class="label">Our commitment</dt><dd>Discretion. Integrity. Results.</dd></div>
  </dl>
</div></section>

<section class="band section" id="divisions"><div class="wrap">
  <div class="head"><p class="label">The divisions</p><h2>Six divisions.<br>One mission.</h2></div>
  <div class="divs">{divs}</div>
</div></section>

<section class="section" id="process"><div class="wrap">
  <div class="head"><p class="label">How an engagement works</p><h2>Three moves.</h2></div>
  <div class="steps">
    <div class="step"><b>1</b><h3>Private intake</h3><p class="muted">Tell us what is at stake. A short, confidential conversation by appointment.</p></div>
    <div class="step"><b>2</b><h3>Strategy brief</h3><p class="muted">A clear picture: the facts, the risks, the options and the first moves.</p></div>
    <div class="step"><b>3</b><h3>Execution</h3><p class="muted">We carry out the plan with you, and bring in independently licensed attorneys whenever a matter calls for one.</p></div>
  </div>
</div></section>

<section class="ink section" id="council" style="padding-bottom:0"><div class="wrap">
  <div class="head"><p class="label">Two cities</p><h2>By appointment only.</h2></div>
</div>
  <div class="cities">
    <div class="city ink"><p class="label">New York</p><h3>The Bowery</h3><p class="muted">NoHo, Manhattan. Private consultations by appointment.</p></div>
    <div class="city ox"><p class="label">Los Angeles</p><h3>Los Angeles</h3><p>Private consultations by appointment.</p></div>
  </div>
</section>

<section class="section"><div class="wrap council">
  <h2>The Advisory Council.</h2>
  <p class="lede">HTA works alongside a private council of senior legal and media professionals. Their guidance shapes our strategy. Their names stay private.</p>
</div></section>

<section class="ox section" id="consult"><div class="wrap consult">
  <div class="consult-copy">
    <p class="label">Private consultation</p>
    <h2>Request an appointment.</h2>
    <p class="lede">Share the outline of your matter and where you would like to meet. We reply to set a time. Keep sensitive details for the consultation itself.</p>
    <p class="addr">Or write to <code id="addr">{EMAIL}</code> <button type="button" id="copy">Copy</button></p>
  </div>
  <form id="intake" novalidate>
    <div class="f"><label for="nm">Full name</label><input id="nm" name="name" autocomplete="name" required></div>
    <div class="f"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email" required></div>
    <div class="f"><label for="ct">City</label><select id="ct" name="city"><option>New York</option><option>Los Angeles</option><option>Either</option></select></div>
    <div class="f"><label for="ar">Area</label><select id="ar" name="area">{areas}<option>Legal Lounge membership</option><option>Press inquiry</option><option>Something else</option></select></div>
    <div class="f f--wide"><label for="ms">What can we help with?</label><textarea id="ms" name="message" required></textarea></div>
    <div class="check"><input type="checkbox" id="ok" required><label for="ok">I understand HTA &amp; Associates is not a law firm, this request does not create an attorney-client relationship, and what I send is confidential but not privileged.</label></div>
    <button class="btn" type="submit">Send request</button>
    <p class="form-note" id="note" role="status"></p>
  </form>
</div></section>
<script>
(function(){{

  var S=[
   ["Someone is using my name, face or voice","Media & Reputation Protection","Your likeness is yours.",["Save every use you find: screenshots, links and dates.","We map where it appears and who is behind it.","Takedown requests and platform escalation, with a licensed attorney brought in when rights need enforcing."]],
   ["A false story or bad press about me","Media & Reputation Protection","Slow down. Then answer well.",["Hold your reply. A rushed response often spreads a story further.","We assess the story, its reach and who is repeating it.","Correction requests and a response strategy, with counsel for any defamation question."]],
   ["I'm being harassed or attacked online","Advocacy & Creator Protection","You don't have to absorb it.",["Preserve the evidence before anything is deleted.","We report and escalate through each platform's own channels.","A safety and reputation plan, with attorneys or law enforcement where the line has been crossed."]],
   ["A deal or contract went wrong","Legal Strategy & Support","Get the full picture first.",["Gather the contract, the emails and the payment trail.","We lay out the facts, the leverage and the options.","Dispute communications and pre-litigation coordination with independent counsel."]],
   ["Someone made an AI copy of me or my work","Investigations & Intelligence","The new frontier, handled.",["Record where the copy lives and how it is being used.","We trace the source and the platforms involved.","Platform policy claims and rights strategy, with counsel on next steps."]],
   ["A government or agency matter","Federal Affairs & Government Liaison","Navigate it with a map.",["Collect every notice, letter and deadline.","We explain the process and who decides what.","A plan for the road ahead, with licensed professionals where required."]]
  ];
  var C=document.getElementById('chips');
  function show(i){{
    var x=S[i];document.getElementById('a-div').textContent=x[1];document.getElementById('a-title').textContent=x[2];
    document.getElementById('a-steps').innerHTML=x[3].map(function(t){{return '<li><span>'+t+'</span></li>'}}).join('');
    [].forEach.call(C.children,function(b,j){{b.setAttribute('aria-pressed',j===i?'true':'false')}});
    document.getElementById('a-go').onclick=function(){{var a=document.getElementById('ar');[].forEach.call(a.options,function(o){{if(o.text===x[1])a.value=o.value}})}};
  }}
  S.forEach(function(x,i){{var b=document.createElement('button');b.type='button';b.className='chip';b.textContent=x[0];b.onclick=function(){{show(i)}};C.appendChild(b)}});
  show(0);
  var EMAIL="{EMAIL}",f=document.getElementById('intake'),n=document.getElementById('note');
  f.addEventListener('submit',function(e){{
    e.preventDefault();
    var v=function(id){{return document.getElementById(id).value.trim()}};
    if(!v('nm')||!v('em')||!v('ms')){{n.textContent='Please add your name, email and a few lines about your matter.';return}}
    if(!document.getElementById('ok').checked){{n.textContent='Please tick the box to confirm you have read the note above.';return}}
    var body='Name: '+v('nm')+'\\nEmail: '+v('em')+'\\nCity: '+v('ct')+'\\nArea: '+v('ar')+'\\n\\n'+v('ms');
    location.href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Private consultation request: '+v('ar'))+'&body='+encodeURIComponent(body);
    n.textContent='Your email app should open with the request ready to send. If it does not, write to '+EMAIL+'.';
  }});
  document.getElementById('copy').addEventListener('click',function(){{
    var b=this;try{{navigator.clipboard.writeText(EMAIL).then(function(){{b.textContent='Copied'}},sel)}}catch(x){{sel()}}
    function sel(){{var r=document.createRange();r.selectNodeContents(document.getElementById('addr'));var s=getSelection();s.removeAllRanges();s.addRange(r)}}
  }});
}})();
</script>
""" + FOOT

# ---------------------------------------------------------------- LOUNGE
LOUNGE_CSS = """
.passes{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:2px;background:var(--ink);border:2px solid var(--ink)}
.pass{display:grid;grid-template-rows:auto auto auto 1fr auto;gap:16px;padding:34px 26px;background:var(--ivory)}
.pass--feature{background:var(--ink);color:var(--ivory)}
.pass h3{font-size:2rem}
.price{font-family:var(--display);font-size:clamp(3rem,4.6vw,4.2rem);line-height:1;font-variant-numeric:tabular-nums}
.price small{font-family:var(--body);font-size:.85rem;margin-left:4px;opacity:.7}
.pass ul{list-style:none;margin:0;padding:16px 0 0;border-top:1px solid currentColor;display:grid;gap:10px;font-size:.96rem;align-content:start}
.pass .btn{width:100%}
.pass--feature .btn{background:var(--ivory);color:var(--ink);border-color:var(--ivory)}
.pass--feature .btn:hover{background:var(--brass-hi);border-color:var(--brass-hi)}
.pass--feature .label{color:var(--brass-hi)}
@media (max-width:1000px){.passes{grid-template-columns:1fr 1fr}}
@media (max-width:600px){.passes{grid-template-columns:1fr}}
.note{margin-top:20px}
.inside{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,4vw,56px)}
.inside div{display:grid;gap:12px;padding-top:16px;border-top:8px solid var(--ivory)}
@media (max-width:860px){.inside{grid-template-columns:1fr}}

.mf{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px;background:var(--ink);border:2px solid var(--ink)}
.card{background:var(--ivory);padding:clamp(24px,3vw,40px);display:grid;gap:18px;align-content:start}
.card q{font-family:var(--serif);font-size:1.6rem;line-height:1.3;quotes:"\201C" "\201D"}
.card .pick{display:flex;gap:10px}
.card .pick button{flex:1;padding:14px;background:transparent;border:2px solid var(--ink);font:inherit;font-size:.74rem;font-weight:600;letter-spacing:.24em;text-transform:uppercase;cursor:pointer}
.card .pick button:hover{background:var(--ink);color:var(--ivory)}
.card .verdict{display:grid;gap:8px;border-top:8px solid var(--oxblood);padding-top:14px}
.card .verdict b{font-family:var(--display);font-weight:400;font-size:2rem;color:var(--oxblood)}
.score{margin-top:18px}
@media (max-width:760px){.mf{grid-template-columns:1fr}}
.library{display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(24px,5vw,80px)}
.lib{display:grid;gap:10px;padding-block:30px;border-top:1px solid var(--ink)}
.lib .label{display:flex;justify-content:space-between;gap:12px}
.lib .label em{font-style:normal;color:var(--oxblood)}
@media (max-width:760px){.library{grid-template-columns:1fr}}
.concierge{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:28px;align-items:end}
@media (max-width:760px){.concierge{grid-template-columns:1fr}}
"""

PASSES = [
    ("24 hours", "Day Pass", "49", "", ["The full Legal Lounge library", "Every playbook and checklist", "HTA Concierge, any hour"], False),
    ("7 days", "Week Pass", "129", "", ["Everything in the Day Pass", "One recorded Lounge Briefing", "Saved reading list"], False),
    ("Membership", "Monthly", "199", "/month", ["Everything in the Week Pass", "Live monthly Briefing with open Q&amp;A", "Member rate on private consultations"], False),
    ("Founding", "Annual", "1,500", "/year", ["Everything in Monthly", "Priority scheduling for consultations", "Invitations to member evenings in New York and Los Angeles"], True),
]

LIBRARY = [
    ("AI &amp; copyright", "Can AI-made work be copyrighted?",
     "In the United States, work made entirely by AI has no copyright owner. Work where a person makes real creative choices can be protected. In March 2026 the Supreme Court declined to hear Thaler v. Perlmutter, leaving that rule in place."),
    ("Right of publicity", "Your name, face and voice",
     "California (Civil Code §3344) and New York (Civil Rights Law §§50–51) restrict using a person's name or likeness to sell something without consent. Voice and face clones are the new front line."),
    ("Deals", "Before you sign: the talent-deal checklist",
     "Term, territory, exclusivity, approvals, who owns the work, how you get paid and how you get out."),
    ("Disputes", "What a cease-and-desist letter is, and what it isn't",
     "A demand letter, not a court order. How to read one, how to respond, and when to bring in a licensed attorney."),
]

def lounge():
    cards = ""
    for when, name, price, per, items, feat in PASSES:
        subj = f"Legal Lounge: {name} pass".replace(" ", "%20")
        lis = "".join(f"<li>{i}</li>" for i in items)
        cards += (f'<article class="pass{" pass--feature" if feat else ""}"><p class="label">{when}</p><h3>{name}</h3>'
                  f'<p class="price">${price}<small>{per}</small></p><ul>{lis}</ul>'
                  f'<a class="btn" href="mailto:{EMAIL}?subject={subj}">Request</a></article>')
    lib = "".join(f'<article class="lib"><p class="label">{t}<em>Members</em></p><h3>{h}</h3><p class="muted">{d}</p></article>' for t, h, d in LIBRARY)
    return head("The Legal Lounge | HTA &amp; Associates",
                "The Legal Lounge by HTA & Associates: a private reading room for media, intellectual property, AI and reputation law. Day, week, monthly and annual passes.",
                "lounge.html", LOUNGE_CSS) + bar("lounge.html") + f"""
<section class="page-hero"><div class="wrap">
  <p class="label">HTA &amp; Associates</p>
  <h1>The Legal <i>Lounge.</i></h1>
  <hr class="heavy-rule">
  <p class="lede">A private reading room for media, intellectual property, AI and reputation law. Come in for a day, or stay for the year.</p>
</div></section>

<section style="padding-bottom:clamp(72px,10vw,140px)"><div class="wrap">
  <div class="passes">{cards}</div>
  <p class="note label muted">Founding rates · Secure checkout opens soon · Request a pass and we send your access details</p>
</div></section>

<section class="ink section"><div class="wrap">
  <div class="head"><p class="label">Inside the Lounge</p><h2>Everything you need<br>before the call.</h2></div>
  <div class="inside">
    <div><h3>The Library</h3><p class="muted">Explainers on contracts, copyright, likeness, AI, defamation and online attacks, in plain English.</p></div>
    <div><h3>Playbooks</h3><p class="muted">Step-by-step checklists for deals, disputes, takedowns and press moments.</p></div>
    <div><h3>Briefings</h3><p class="muted">A live monthly session on what changed in media and entertainment law, with open questions at the end.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="head"><p class="label">Play · Myth or Fact?</p><h2>Think you know<br>your rights?</h2></div>
  <div class="mf" id="mf"></div>
  <p class="score label muted" id="score">Four questions. Members get the full set every week.</p>
</div></section>
<script>
(function(){{
 var Q=[
  ["If I bought the song, I can use it in my video.",0,"Buying a copy lets you listen. Putting music in a video needs a license from the people who own the song and the recording."],
  ["Art I made with an AI prompt alone is protected by copyright.",0,"In the U.S., work with no human author has no copyright. Real human creative choices can be protected."],
  ["A cease-and-desist letter is a court order.",0,"It is a demand letter from the other side, not a court order. It still deserves a careful, timely answer."],
  ["A brand needs my permission to use my face in an ad.",1,"California and New York both restrict using a person's name or likeness in advertising without consent."]
 ],n=0,right=0,M=document.getElementById('mf');
 Q.forEach(function(q){{
  var c=document.createElement('article');c.className='card';
  c.innerHTML='<q>'+q[0]+'</q><div class="pick"><button type="button">Myth</button><button type="button">Fact</button></div>';
  [].forEach.call(c.querySelectorAll('button'),function(b,i){{b.onclick=function(){{
    var ok=(i===1)===(q[1]===1);n++;if(ok)right++;
    c.querySelector('.pick').outerHTML='<div class="verdict"><b>'+(q[1]?'Fact.':'Myth.')+'</b><p>'+(ok?'You got it. ':'Not quite. ')+q[2]+'</p></div>';
    document.getElementById('score').textContent='Your score: '+right+' of '+n+(n===Q.length?' · Members get a new set every week.':'');
  }}}});
  M.appendChild(c);
 }});
}})();
</script>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="head"><p class="label">From the Library</p><h2>Now reading.</h2></div>
  <div class="library">{lib}</div>
</div></section>

<section class="ox section"><div class="wrap concierge">
  <div class="head" style="margin:0"><p class="label">HTA Concierge</p><h2>Questions at any hour.</h2><p class="lede">Our automated concierge answers general questions about the Lounge and the topics we cover. General information, not legal advice. Opens in ChatGPT.</p></div>
  <a class="btn" style="background:var(--ivory);color:var(--ink);border-color:var(--ivory)" href="{GPT}" target="_blank" rel="noopener">Ask the Concierge</a>
</div></section>
""" + FOOT

# ---------------------------------------------------------------- NEWSROOM
NEWS_CSS = """
.news{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:clamp(36px,6vw,90px);align-items:start}
@media (max-width:900px){.news{grid-template-columns:1fr}}
.release{display:grid;gap:18px}
.release h2{font-size:clamp(2.2rem,4.4vw,3.6rem)}
.release p{font-family:var(--serif);font-size:1.3rem;line-height:1.5;max-width:60ch}
.release .label{font-family:var(--body)}
.dateline{font-family:var(--body);font-size:.8rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--oxblood)}
.end{text-align:center;letter-spacing:.5em}
.wire{display:grid;background:var(--ink);color:var(--ivory);padding:clamp(24px,3vw,36px)}
.wire h2{font-size:2.4rem}
.item{display:grid;gap:8px;padding-block:22px;border-top:1px solid rgba(238,232,220,.2)}
.item .label{font-size:.64rem;display:flex;justify-content:space-between;gap:10px;color:var(--brass-hi)}
.item .label em{font-style:normal;color:var(--grey-d)}
.item a{font-family:var(--serif);font-size:1.4rem;line-height:1.25;text-decoration:none}
.item a:hover{text-decoration:underline}
.item p{color:var(--grey-d);font-size:.94rem}
.desk{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:var(--ivory)}
.desk>div{padding:clamp(32px,4vw,56px);display:grid;gap:14px;align-content:start}
@media (max-width:760px){.desk{grid-template-columns:1fr}}
"""

HEADLINES = [
    ("Media rights", "ABC7 New York · AP", "May 4, 2026",
     "https://abc7ny.com/post/ends-us-news-blake-lively-justin-baldoni-end-dispute-settlement-ahead-2026-trial/19038332/",
     "Blake Lively, Justin Baldoni end 'It Ends With Us' dispute in settlement",
     "Settled days before a New York federal trial. Terms were not disclosed."),
    ("Antitrust", "NY1 · AP", "July 28, 2026",
     "https://ny1.com/nyc/all-boroughs/ap-top-news/2026/07/28/former-golden-globes-owners-sue-penske-media-alleging-fraud-in-acquisition-of-awards-show",
     "Former Golden Globes owners sue Penske Media alleging fraud in acquisition of awards show",
     "The Hollywood Foreign Press Association seeks more than $150 million over the 2023 sale."),
    ("AI &amp; copyright", "PetaPixel", "March 4, 2026",
     "https://petapixel.com/2026/03/04/supreme-court-declines-to-hear-ai-image-copyright-case/",
     "Supreme Court Declines to Hear AI Image Copyright Case",
     "Thaler v. Perlmutter ends; work without a human author stays outside U.S. copyright."),
]

def newsroom():
    items = "".join(f'<article class="item"><p class="label">{t}<em>{s} · {d}</em></p><a href="{u}" target="_blank" rel="noopener">{h}</a><p>{n}</p></article>'
                    for t, s, d, u, h, n in HEADLINES)
    return head("Press &amp; Newsroom | HTA &amp; Associates",
                "News, press releases and investigations from HTA & Associates, with a headlines desk on the legal side of media and entertainment.",
                "newsroom.html", NEWS_CSS) + bar("newsroom.html") + f"""
<section class="page-hero"><div class="wrap">
  <p class="label">HTA &amp; Associates</p>
  <h1>Press &amp; <i>Newsroom.</i></h1>
  <hr class="heavy-rule">
</div></section>

<section style="padding-bottom:clamp(72px,10vw,140px)"><div class="wrap news">
  <article class="release" id="lounge-launch">
    <p class="label">Press release · For immediate release</p>
    <h2>HTA &amp; Associates Opens The Legal Lounge and Launches Its Press &amp; Newsroom</h2>
    <p><span class="dateline">New York, Oct. 6, 2026 —</span> HTA &amp; Associates, the strategic legal intelligence, advocacy and consulting organization with teams in New York and Los Angeles, today opened The Legal Lounge, a members' reading room for media, intellectual property, AI and reputation law, and launched its Press &amp; Newsroom.</p>
    <p>The Legal Lounge offers plain-English explainers, playbooks and live monthly briefings, with day, week, monthly and annual passes. The Press &amp; Newsroom will publish HTA announcements, a curated headlines desk on the legal side of entertainment and media, and original investigative reporting.</p>
    <p>Private consultations are available by appointment in New York and Los Angeles at htaassociates.com.</p>
    <p><strong>Media contact:</strong> {EMAIL}</p>
    <p class="end">###</p>
  </article>
  <aside class="wire" aria-label="Headlines desk">
    <h2>Headlines desk</h2>
    <p class="muted" style="margin:8px 0 10px">Their headline, their reporting. Links open the original story.</p>
    {items}
  </aside>
</div></section>

<section class="desk">
  <div class="ink"><p class="label">Investigations desk</p><h3>Original reporting, coming soon.</h3><p class="muted">When a story deserves more than a headline, our investigations desk takes it on. Tips are held in confidence: {EMAIL}</p></div>
  <div class="ox"><p class="label">Media inquiries</p><h3>Press and interviews.</h3><p>For comment, interviews or our releases, write to {EMAIL} with “Press” in the subject line.</p></div>
</section>
""" + FOOT

# ---------------------------------------------------------------- LEGAL
LEGAL_CSS = ".doc{display:grid;gap:16px;max-width:72ch;padding-bottom:clamp(72px,10vw,140px)}.doc h2{font-size:2.2rem;margin-top:26px}.doc p{color:var(--grey)}"

def legal():
    return head("Privacy &amp; Terms | HTA &amp; Associates", "Disclaimer, privacy notice and terms of use for HTA & Associates.", "legal.html", LEGAL_CSS) + bar("legal.html") + f"""
<section class="page-hero"><div class="wrap"><p class="label">Last updated October 6, 2026</p><h1>Privacy &amp; <i>Terms.</i></h1><hr class="heavy-rule"></div></section>
<section><div class="wrap doc">
  <h2>Who we are</h2>
  <p>HTA &amp; Associates is a strategic legal intelligence, advocacy and consulting organization. We are not a law firm, and we do not provide legal representation or legal advice. When a matter needs a lawyer, legal services are provided only by independently licensed attorneys, under their own engagement terms.</p>
  <h2>No attorney-client relationship</h2>
  <p>Reading this site, requesting a consultation, buying a Legal Lounge pass or using the HTA Concierge does not create an attorney-client relationship. Information you send to HTA is kept confidential, but it is not protected by attorney-client privilege. Please do not send sensitive details until we have spoken.</p>
  <h2>Legal Lounge content</h2>
  <p>Legal Lounge explainers, playbooks and briefings are general information for education. They are not legal advice about your situation, and laws change. Consult a licensed attorney before acting on any legal question.</p>
  <h2>HTA Concierge</h2>
  <p>The HTA Concierge is an automated assistant hosted by a third party (OpenAI's ChatGPT). It provides general information only. What you type there is governed by that service's own privacy terms.</p>
  <h2>Privacy</h2>
  <p>This site does not use advertising trackers. The consultation form stores nothing on our servers: it opens an email from your own email app, addressed to us. We use what you send only to respond to you and to provide the services you ask for, and we do not sell personal information. To ask what we hold about you or to have it deleted, write to {EMAIL}.</p>
</div></section>
""" + FOOT

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#131110"/>'
           '<text x="32" y="44" text-anchor="middle" font-family="Didot,Bodoni 72,Georgia,serif" font-weight="700" font-size="30" fill="#eee8dc">H</text>'
           '<rect x="14" y="50" width="36" height="3" fill="#5e1a1d"/></svg>')

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    pages = {"index.html": home(), "lounge.html": lounge(), "newsroom.html": newsroom(), "legal.html": legal()}
    for name, src in pages.items():
        open(os.path.join(OUT, name), "w").write(src)
    open(os.path.join(OUT, "assets", "favicon.svg"), "w").write(FAVICON)
    shutil.copy(os.path.join(HERE, "assets", "hta.css"), os.path.join(OUT, "assets", "hta.css"))
    shutil.copy(os.path.join(HERE, "assets", "lady-justice.jpg"), os.path.join(OUT, "assets", "lady-justice.jpg"))
    print("built", list(pages))
