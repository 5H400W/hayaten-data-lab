import math, random, os, zipfile
OUT="/mnt/user-data/outputs/hayaten-site"; os.makedirs(OUT+"/assets",exist_ok=True)
NAME="HAYATEN Data Lab"; EMAIL="info@yourdomain.com"; PHONE="[add number]"
CSS="""*,*::before,*::after{box-sizing:border-box}html{scroll-behavior:smooth}
:root{--ink:#0a1a5c;--deep:#12308f;--em:#2a5be8;--teal:#4cc9f0;--gold:#5bd6f5;--ivory:#f4f8ff;--text:#0f1f4d;--mute:#56658c;--line:#d8e3f5}
body{margin:0;font:400 17px/1.65 Manrope,system-ui,sans-serif;color:var(--text);background:var(--ivory)}
h1,h2,h3{font-family:Manrope,system-ui,sans-serif;font-weight:800;line-height:1.1;margin:0}a{color:inherit}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
header{position:sticky;top:0;z-index:9;background:rgba(10,26,92,.86);backdrop-filter:blur(14px);border-bottom:1px solid rgba(91,214,245,.18)}
.nav{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font:600 19px Manrope,system-ui,sans-serif}
nav{display:flex;gap:26px;align-items:center}nav a{color:#d4e0ff;text-decoration:none;font-size:15px}nav a:hover{color:#fff}
.btn{display:inline-block;padding:13px 24px;border-radius:999px;font:700 15px Manrope,sans-serif;text-decoration:none;border:0;cursor:pointer;background:linear-gradient(135deg,#8fe3fa,#3fa7f0);color:#0a1a5c;box-shadow:0 10px 30px -12px rgba(91,214,245,.7)}
.btn.ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.35);box-shadow:none}
#m,.burger{display:none}
.hero{color:#fff;padding:92px 0 80px;overflow:hidden;background:url(waves.svg) center/cover no-repeat,radial-gradient(900px 520px at 88% -10%,rgba(76,201,240,.38),transparent 60%),radial-gradient(700px 500px at -5% 105%,rgba(91,214,245,.24),transparent 60%),linear-gradient(160deg,#0a1a5c,#1a3fb0 58%,#0a1a5c)}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:36px;align-items:center}
.hero h1{font-size:clamp(38px,5.6vw,66px);letter-spacing:-.02em}.hero h1 em{font-style:normal;background:linear-gradient(90deg,#8fe3fa,#b4f0ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{font-size:19px;color:#c3d0f5;max-width:34em;margin:22px 0 30px}.cta{display:flex;gap:12px;flex-wrap:wrap}
.hero img{width:100%;height:auto;display:block}.ph{padding:70px 0 56px}.ph .wrap{display:block}.ph h1{font-size:clamp(34px,5vw,54px)}
.eyebrow{font:700 12px Manrope;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
section{padding:78px 0}h2{font-size:clamp(28px,3.8vw,42px);letter-spacing:-.01em;margin-bottom:14px}.lead{color:var(--mute);max-width:42em;margin:0 0 38px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px}
.card{position:relative;background:#fff;border:1px solid var(--line);border-radius:20px;padding:30px 26px;text-decoration:none;display:block;box-shadow:0 22px 44px -30px rgba(10,26,92,.45);transition:transform .25s}
.card::before{content:"";position:absolute;left:26px;right:26px;top:0;height:3px;border-radius:0 0 4px 4px;background:linear-gradient(90deg,var(--gold),var(--teal))}
a.card:hover{transform:translateY(-5px)}.card h3{font-size:22px;margin-bottom:10px}.card p{margin:0;color:var(--mute);font-size:15.5px}.card .go{display:inline-block;margin-top:14px;color:var(--em);font-weight:700;font-size:14px}
.band{color:#fff;background:radial-gradient(700px 400px at 100% 0,rgba(76,201,240,.25),transparent 60%),linear-gradient(135deg,#12308f,#0a1a5c)}.band .lead{color:#b9c8f0}
.band .card{background:rgba(255,255,255,.05);border-color:rgba(91,214,245,.25);box-shadow:none}.band .card p{color:#b9c8f0}
.step b{display:block;font:600 54px Manrope,system-ui,sans-serif;background:linear-gradient(135deg,#8fe3fa,#4cc9f0);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:4px}
ul.tick{list-style:none;padding:0;margin:0}ul.tick li{padding:9px 0 9px 28px;position:relative;border-bottom:1px solid var(--line)}ul.tick li::before{content:"";position:absolute;left:2px;top:17px;width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,var(--gold),var(--teal))}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px}.cband{text-align:center;color:#fff;background:radial-gradient(600px 300px at 50% 0,rgba(91,214,245,.3),transparent 70%),linear-gradient(135deg,#1a3fb0,#0a1a5c)}
.cband p{color:#c3d0f5;max-width:36em;margin:0 auto 26px}
form{display:grid;gap:14px;max-width:560px}label{font-weight:600;font-size:14px}input,textarea,select{width:100%;padding:13px 14px;border-radius:12px;border:1px solid #c3d0ea;background:#fff;font:400 16px Manrope,sans-serif;color:var(--text)}textarea{min-height:130px}
footer{background:#060f3d;color:#aebbe6;padding:56px 0 30px;font-size:14.5px}footer .grid{grid-template-columns:2fr 1fr 1fr 1fr}footer a{display:block;color:#aebbe6;text-decoration:none;padding:3px 0}footer a:hover{color:#fff}footer h3{font:700 13px Manrope;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.fine{border-top:1px solid #1a2a70;margin-top:34px;padding-top:20px;font-size:13px}
@media(max-width:820px){.hero .wrap,.two,footer .grid{grid-template-columns:1fr}.hero{padding:56px 0}section{padding:56px 0}
.burger{display:block;color:#fff;font-size:26px;cursor:pointer}nav{display:none;position:absolute;top:68px;left:0;right:0;flex-direction:column;background:#0a1a5c;padding:18px 22px 24px;align-items:flex-start;gap:16px}#m:checked~nav{display:flex}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}html{scroll-behavior:auto}}"""


FX=r"""(function(){
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches,M={x:-999,y:-999,on:false},G=document.getElementById('glow'),gx=0,gy=0;
addEventListener('pointermove',function(e){M.x=e.clientX;M.y=e.clientY;M.on=true;if(G)G.style.opacity=1},{passive:true});
document.addEventListener('pointerleave',function(){M.on=false;if(G)G.style.opacity=0});
function Net(host){var c=document.createElement('canvas');c.className='nn';host.prepend(c);var x=c.getContext('2d'),w,h,d,N=[],S=[],vis=true,en=.3,t=0,lx=0,ly=0,story=host.classList.contains('story');
function size(){var r=host.getBoundingClientRect();d=Math.min(window.devicePixelRatio||1,2);w=r.width;h=r.height;c.width=Math.round(w*d);c.height=Math.round(h*d);x.setTransform(d,0,0,d,0,0);
var n=Math.min(story?120:90,Math.round(w*h/13000));N=[];for(var i=0;i<n;i++)N.push({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.28,vy:(Math.random()-.5)*.28,p:Math.random()*6.28,hot:0});if(reduce)draw()}
function draw(){x.clearRect(0,0,w,h);var r=host.getBoundingClientRect(),mx=M.x-r.left,my=M.y-r.top,L=135,i,j,a,b,dx,dy,q,al;
if(story){var p=(innerHeight-r.top)/(r.height+innerHeight);en=Math.max(0,Math.min(1,p))}
for(i=0;i<N.length;i++){a=N[i];if(!reduce){a.x+=a.vx*(1+en*2.2);a.y+=a.vy*(1+en*2.2);if(a.x<0||a.x>w)a.vx*=-1;if(a.y<0||a.y>h)a.vy*=-1}
dx=a.x-mx;dy=a.y-my;q=dx*dx+dy*dy;if(M.on&&q<25600){var f=(1-Math.sqrt(q)/160);a.x+=dx*f*.03;a.y+=dy*f*.03;a.hot=1}else a.hot*=.93}
for(i=0;i<N.length;i++){a=N[i];for(j=i+1;j<N.length;j++){b=N[j];dx=a.x-b.x;dy=a.y-b.y;q=dx*dx+dy*dy;if(q<L*L){al=(1-Math.sqrt(q)/L)*(.2+en*.5+Math.max(a.hot,b.hot)*.45);x.strokeStyle=(a.hot>.2||b.hot>.2)?'rgba(143,227,250,'+al.toFixed(3)+')':'rgba(76,201,240,'+al.toFixed(3)+')';x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke()}}}
for(i=0;i<N.length;i++){a=N[i];al=.45+.4*Math.sin(t*2.2+a.p);x.fillStyle=a.hot>.2?'rgba(143,227,250,'+(.6+a.hot*.4)+')':'rgba(160,225,255,'+al.toFixed(2)+')';x.beginPath();x.arc(a.x,a.y,1.6+a.hot*2.4+en*.8,0,6.283);x.fill()}
if(!reduce){if(M.on&&mx>0&&my>0&&mx<w&&my<h&&(Math.abs(mx-lx)+Math.abs(my-ly))>6){if(S.length<48)S.push({x:mx,y:my,vx:(Math.random()-.5)*1.6,vy:(Math.random()-.5)*1.6,l:1});lx=mx;ly=my}
for(i=S.length-1;i>=0;i--){var s=S[i];s.x+=s.vx;s.y+=s.vy;s.l-=.035;if(s.l<=0){S.splice(i,1);continue}x.fillStyle='rgba(143,227,250,'+(s.l*(.5+.5*Math.random())).toFixed(2)+')';x.beginPath();x.arc(s.x,s.y,1+s.l*2,0,6.283);x.fill()}}}
new ResizeObserver(size).observe(host);new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(host);size();
if(!reduce)(function loop(){requestAnimationFrame(loop);if(!vis||document.hidden)return;t+=.016;draw()})()}
document.querySelectorAll('.fxhost').forEach(Net);
var bar=document.getElementById('bar');
if(!reduce){(function gl(){requestAnimationFrame(gl);if(!G)return;gx+=(M.x-gx)*.14;gy+=(M.y-gy)*.14;G.style.transform='translate3d('+gx+'px,'+gy+'px,0)'})();
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15});
document.querySelectorAll('main h2,.card,.ch>.wrap,.sintro>.wrap,.tick li,.lead').forEach(function(el){el.classList.add('rv');io.observe(el)})}
var tk=false;addEventListener('scroll',function(){if(tk)return;tk=true;requestAnimationFrame(function(){var m=document.documentElement.scrollHeight-innerHeight;if(bar)bar.style.transform='scaleX('+(m>0?scrollY/m:0)+')';tk=false})},{passive:true});
})();"""

EXTRA="""
.glass{background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.24);border-radius:22px;padding:28px;backdrop-filter:blur(10px)}.glass h3{margin-bottom:10px}.glass ul.tick li{border-color:rgba(255,255,255,.16)}
.pills{display:flex;flex-wrap:wrap;gap:10px}.pills span{padding:9px 16px;border-radius:999px;background:#fff;border:1px solid var(--line);font-weight:700;font-size:14px;color:var(--ink)}
details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 20px;margin-bottom:12px}summary{cursor:pointer;font-weight:700}details p{margin:10px 0 0;color:var(--mute)}

.fxhost{position:relative;overflow:hidden}.fxhost>.wrap{position:relative;z-index:1}
.nn{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
#bar{position:fixed;top:0;left:0;height:3px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,var(--gold),var(--teal));z-index:20}
#glow{position:fixed;left:0;top:0;width:380px;height:380px;margin:-190px 0 0 -190px;border-radius:50%;pointer-events:none;z-index:3;opacity:0;transition:opacity .4s;background:radial-gradient(circle,rgba(91,214,245,.16),rgba(76,201,240,.07) 45%,transparent 70%);will-change:transform}
.rv{opacity:0;transform:translateY(28px);transition:opacity .9s,transform .9s cubic-bezier(.2,.7,.2,1)}.rv.in{opacity:1;transform:none}
.story{color:#fff;padding:0;background:linear-gradient(180deg,#0a1a5c,#12308f 50%,#0a1a5c)}
.sintro{min-height:70vh;display:flex;align-items:center}.ch{min-height:88vh;display:flex;align-items:center}
.story .wrap{position:relative;z-index:1}.ch b{display:block;font:600 clamp(80px,14vw,170px)/1 Manrope,system-ui,sans-serif;background:linear-gradient(135deg,#8fe3fa,#4cc9f0);-webkit-background-clip:text;background-clip:text;color:transparent;opacity:.9}
.ch h2,.sintro h2{font-size:clamp(34px,5.4vw,64px)}.ch p,.sintro p{color:#c3d0f5;font-size:clamp(18px,2.1vw,24px);max-width:30em;margin-top:18px}
@media(hover:none){#glow{display:none}}
"""
open(OUT+"/assets/style.css","w").write(CSS+EXTRA)
open(OUT+"/assets/fx.js","w").write(FX)


import math
_l=[]
for i in range(46):
    y0=40+i*14;a=24+13*math.sin(i*.33);ph=i*.21
    pts=" ".join(f"{x},{y0+a*math.sin(x/200+ph)+13*math.sin(x/75+ph*1.7):.1f}" for x in range(0,1633,32))
    _l.append(f'<polyline points="{pts}" fill="none" stroke="#fff" stroke-opacity="{.05+.12*(.5+.5*math.sin(i*.42)):.3f}"/>')
open(OUT+"/assets/waves.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 700" preserveAspectRatio="xMidYMid slice">'+"".join(_l)+'</svg>')

# generated hero art
random.seed(7); W,H=620,520
pts=[(random.uniform(30,W-30),random.uniform(30,H-30)) for _ in range(46)]
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Abstract data network"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8fe3fa"/><stop offset="1" stop-color="#4cc9f0"/></linearGradient><radialGradient id="r"><stop offset="0" stop-color="#4cc9f0" stop-opacity=".45"/><stop offset="1" stop-color="#4cc9f0" stop-opacity="0"/></radialGradient></defs><circle cx="310" cy="260" r="250" fill="url(#r)"/>']
for i,(x,y) in enumerate(pts):
    near=sorted(pts,key=lambda p:(p[0]-x)**2+(p[1]-y)**2)[1:3]
    for (a,b) in near:
        mx,my=(x+a)/2+(y-b)*.18,(y+b)/2+(a-x)*.18
        s.append(f'<path d="M{x:.0f} {y:.0f} Q{mx:.0f} {my:.0f} {a:.0f} {b:.0f}" stroke="url(#g)" stroke-opacity=".5" stroke-width="1.1" fill="none"/>')
for i,(x,y) in enumerate(pts):
    r=2+(i%5)*1.1; s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r*2.6:.1f}" fill="#4cc9f0" fill-opacity=".12"/><circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="url(#g)"/>')
s.append('</svg>'); open(OUT+"/assets/hero.svg","w").write("".join(s))

LOGO='<svg width="30" height="33" viewBox="0 0 170 185" aria-hidden="true"><polygon points="25,20 62,13 62,160 25,172" fill="#2f5df5"/><polygon points="108,25 145,10 145,165 108,175" fill="#5fd3f7"/><polygon points="8,140 160,62 160,88 8,168" fill="#a9f1ff" fill-opacity=".92"/><rect x="156" y="14" width="9" height="9" fill="#2f5df5"/><rect x="154" y="34" width="12" height="11" fill="#5fd3f7"/></svg>'
NAV=[("services.html","Services"),("engagement-models.html","Engagement"),("how-we-work.html","How we work"),("about.html","About")]
def page(slug,title,desc,body,hero=None):
    nav="".join(f'<a href="{u}">{t}</a>' for u,t in NAV)
    f=lambda items:"".join(f'<a href="{u}">{t}</a>' for u,t in items)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | {NAME}</title><meta name="description" content="{desc}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/style.css"></head><body>
<header><div class="wrap nav"><a class="logo" href="index.html">{LOGO}{NAME}</a><input type="checkbox" id="m"><label class="burger" for="m" aria-label="Menu">&#9776;</label><nav>{nav}<a class="btn" href="contact.html">Talk to us</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="grid"><div><a class="logo" href="index.html">{LOGO}{NAME}</a><p>Data engineering, AI and software development for businesses worldwide.</p><p>{EMAIL}<br>{PHONE}</p></div>
<div><h3>Services</h3>{f(SVC_LINKS)}</div><div><h3>Company</h3>{f([("engagement-models.html","Engagement models"),("how-we-work.html","How we work"),("about.html","About"),("join-our-bench.html","Join our bench")])}</div><div><h3>Contact</h3>{f([("contact.html","Request a quote"),("privacy.html","Privacy policy")])}</div></div>
<div class="fine">Hayaten Data Labs Private Limited, registered in India. CIN: [add]. &copy; 2026</div></div></footer><div id="glow"></div><div id="bar"></div><script src="assets/fx.js" defer></script></body></html>'''
def phead(t,l): return f'<section class="hero ph fxhost"><div class="wrap"><div><div class="eyebrow">{NAME}</div><h1>{t}</h1><p>{l}</p></div></div></section>'
def cta(t="Tell us what you need",p="Share a few details and we will reply with next steps within two business days."): return f'<section class="cband"><div class="wrap"><h2>{t}</h2><p>{p}</p><a class="btn" href="contact.html">Request a quote</a></div></section>'
def cards(items,link=True):
    return '<div class="grid">'+"".join((f'<a class="card" href="{u}"><h3>{t}</h3><p>{d}</p><span class="go">Learn more &rarr;</span></a>' if link else f'<div class="card"><h3>{t}</h3><p>{d}</p></div>') for t,d,u in items)+'</div>'
def tick(l): return '<ul class="tick">'+"".join(f"<li>{x}</li>" for x in l)+'</ul>'
SV={
"software-development":("Software Development","Custom web and mobile applications, APIs and integrations, built to be maintained by your own team.",["Web and mobile applications","Internal tools that replace spreadsheets and manual workflows","APIs and system integrations","Modernisation of slow or fragile software"],["Clean architecture and code review","Automated tests and written documentation","Small releases with regular demos"]),
"data-engineering":("Data Engineering and Analytics","Bring information from many sources into one reliable place, then turn it into reports people trust.",["Data pipelines (ETL and ELT)","Data warehouses and data lakes","Database design, tuning and migration","BI dashboards and reporting"],["Data-quality checks on every pipeline","Monitoring and alerting as standard","Documented data definitions"]),
"ai-machine-learning":("AI and Machine Learning","Apply AI where it creates measurable value, from first prototype to production.",["Generative AI assistants and document workflows","Forecasting, classification and prediction","Search and summarisation over company knowledge","ML pipelines, evaluation and monitoring"],["Start from the business case and a baseline","Privacy, access control and human review where it matters","Results measured against agreed targets"]),
"hyperautomation":("Hyperautomation","Combine process analysis, workflow tools, RPA and AI to remove repetitive manual work.",["Data entry and reconciliation","Approvals, notifications and hand-offs","Automated report generation","Workflow orchestration across systems"],["Map how work really flows first","Agree a measurable target such as hours saved","Report against it after launch"]),
"cloud-migration":("Cloud Infrastructure and Migration","Robust cloud foundations for data and AI workloads, including careful migration of existing systems.",["Assessment of systems, data and dependencies","Target architecture and phased migration plan","Database and data-platform migration","Cost-aware cloud design"],["Rehearsed cut-over with rollback options","Thorough testing at every stage","Support for AWS, Azure and Google Cloud"]),
"consulting-audits":("Consulting, Architecture and Audits","Clear, independent advice you can act on, whether or not you work with us further.",["Data and solution architecture","Technology roadmaps","Software and data-pipeline audits","Performance, security and cost reviews"],["Findings in plain language","Prioritised recommendations","A fixed scope and fixed fee"])}
SV={k:SV[k] for k in ["ai-machine-learning","data-engineering","software-development","hyperautomation","cloud-migration","consulting-audits"]}
SVC_LINKS=[("services.html","All services")]+[(k+".html",v[0]) for k,v in SV.items()]
SVC_CARDS=[(v[0],v[1],k+".html") for k,v in SV.items()]
def write(slug,*a): open(f"{OUT}/{slug}.html","w").write(page(slug,*a))
MODELS=[("End-to-end project","Fixed price, turnkey delivery. We design, build, test and hand over the complete solution, with payments tied to milestones.",""),("Team augmentation","Specialist engineers join your team on a time-and-material basis and work under your direction.",""),("Scope of work","Milestone-based delivery of a defined piece, such as an audit or one phase of a migration, against clear targets.",""),("Approved vendor","We join your procurement pool as an empanelled supplier, ready for ongoing projects and talent gaps.","")]
STEPS=[("Discover","We learn your data, systems and goals, and agree scope and measures of success."),("Design","We propose an architecture and a delivery plan with fixed milestones."),("Build","Small tested releases with regular demos, so you steer while change is easy."),("Operate","We monitor and improve the system, or hand over cleanly with documentation.")]
steps=lambda:'<div class="grid">'+"".join(f'<div class="card step"><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(STEPS))+'</div>'
STORY='<section class="story fxhost"><div class="sintro"><div class="wrap"><div class="eyebrow">The story</div><h2>How AI is changing the way we work</h2><p>Scroll through five steps, from today\'s manual work to systems that think alongside your team.</p></div></div><div class="ch"><div class="wrap"><b>01</b><h2>Work today</h2><p>Data sits in spreadsheets, old databases and inboxes. People copy, paste and reconcile by hand, and every manual step is a place for delay and error.</p></div></div><div class="ch"><div class="wrap"><b>02</b><h2>Migration</h2><p>Change starts when data moves to modern platforms. With careful assessment, a phased cut-over and rollback plans, legacy data stops being an obstacle and becomes an asset.</p></div></div><div class="ch"><div class="wrap"><b>03</b><h2>Cloud</h2><p>The cloud adds elastic computing, storage and managed services, so you scale with demand and pay for what you use. It is the ground AI needs to run on.</p></div></div><div class="ch"><div class="wrap"><b>04</b><h2>AI</h2><p>Neural networks learn patterns in your data: forecasting, classification, summarising documents, answering questions. Pointed at the right problems, they take repetitive work off people\'s desks.</p></div></div><div class="ch"><div class="wrap"><b>05</b><h2>Engineers</h2><p>AI can draft code and suggest answers, but people must design the architecture, check the results, secure the data and stay accountable. Software engineers turn AI from a demo into a dependable system.</p></div></div><div class="sintro"><div class="wrap"><h2>That is the work we do.</h2><p>We migrate, build and run the systems in every step above.</p><div class="cta" style="margin-top:26px"><a class="btn" href="contact.html">Start a conversation</a></div></div></div></section>'
home=f'''<section class="hero fxhost"><div class="wrap"><div><div class="eyebrow">Data. AI. Software.</div><h1>Systems that turn <em>data into decisions</em></h1><p>We design and build data platforms, AI solutions, automation and custom software for businesses worldwide, with specialists matched to every engagement.</p><div class="cta"><a class="btn" href="contact.html">Request a quote</a><a class="btn ghost" href="services.html">Explore services</a></div></div><img src="assets/hero.svg" alt="Abstract data network"></div></section>
{STORY}<section><div class="wrap"><div class="eyebrow">What we do</div><h2>Six ways we help</h2><p class="lead">One engineering team across data, AI and software, so you do not need separate vendors for each.</p>{cards(SVC_CARDS)}</div></section>
<section class="band"><div class="wrap"><div class="eyebrow">Engagement models</div><h2>Work with us your way</h2><p class="lead">Four models, usable alone or combined as the relationship grows.</p>{cards([(a,b,"engagement-models.html") for a,b,_ in MODELS],False)}</div></section>
<section><div class="wrap"><div class="eyebrow">How a project runs</div><h2>Clear stages, no surprises</h2><p class="lead">The same four stages on every engagement.</p>{steps()}</div></section>{cta()}'''

CH=[("01","Work is changing","AI is taking over routine work such as reading documents, sorting requests, drafting replies and spotting patterns. People move to the parts that need judgement."),
("02","Data is the fuel","AI is only as good as the data beneath it. Clean, connected and well-governed data comes first. Moving old systems to the cloud is one step on that road, not the destination."),
("03","AI inside real workflows","The value is in connecting AI to the systems people already use, with testing, measurement and human review, not in a demo that sits on its own."),
("04","Engineers make it trustworthy","Someone must design the architecture, check the results, secure the data and be accountable when something goes wrong. Software engineers turn AI into a dependable system.")]
STORY='<section class="story fxhost"><div class="sintro"><div class="wrap"><div class="eyebrow">The story</div><h2>How AI is changing the way we work</h2><p>Four steps, from today\'s manual work to systems that think alongside your team.</p></div></div>'+"".join(f'<div class="ch"><div class="wrap"><b>{n}</b><h2>{t}</h2><p>{p}</p></div></div>' for n,t,p in CH)+'<div class="sintro"><div class="wrap"><h2>That is the work we do.</h2><p>We build and run the data, AI and software behind every step above.</p><div class="cta" style="margin-top:26px"><a class="btn" href="contact.html">Start a conversation</a></div></div></div></section>'
TR=[("Scope in writing","Every engagement starts with an agreed scope, milestones and price, so there are no surprises later."),("Confidential from day one","We sign your NDA before you share anything, and limit access to the people on your project."),("You own the work","Custom code and documentation we deliver belong to you once paid, as set out in the agreement."),("Tested and documented","Code is reviewed, pipelines are checked for data quality, and everything is documented for handover."),("Honest advice","If a project is not a good fit, or a simpler option exists, we will tell you."),("Reachable people","You deal directly with the engineers who scope and build your project, not a call centre.")]
FQ=[("Who owns the code?","Custom work delivered to you belongs to you once it is paid for, as set out in the written agreement. We state any open-source or pre-existing components up front."),("Do you sign an NDA?","Yes. We are happy to sign yours before you share any detail, or to provide ours."),("How is pricing set?","Fixed price for well-defined scope, with payments tied to milestones. Time-and-material for team augmentation. Estimates are written and any change is agreed before it affects cost."),("Which time zones do you work in?","We agree working hours that overlap with yours for meetings and decisions, and communicate in clear written English."),("How do we start?","A free 30-minute call, then usually a small fixed-scope first piece such as an audit or pilot, so you can judge our work before committing more.")]
home=f"""<section class="hero fxhost"><div class="wrap"><div><div class="eyebrow">Enterprise data engineering, AI and cloud</div><h1>Data and AI systems <em>you can rely on</em></h1><p>We design, build and run data platforms, AI integrations and cloud infrastructure for businesses that cannot afford guesswork.</p><div class="cta"><a class="btn" href="contact.html">Request a quote</a><a class="btn ghost" href="how-we-work.html">How we work</a></div></div><div class="glass"><h3>What you can expect</h3>{tick(["NDA signed before any detail is shared","Written scope, milestones and price","You own what we build, once paid","Plain updates on a schedule you choose"])}</div></div></section>
<section style="padding:34px 0"><div class="wrap"><div class="pills">{"".join(f"<span>{t}</span>" for t in ["PySpark","Apache Airflow","Snowflake","Python","SQL","AWS","Microsoft Azure","Google Cloud"])}</div></div></section>
{STORY}
<section><div class="wrap"><div class="eyebrow">What we do</div><h2>Six ways we help</h2><p class="lead">One engineering team across AI, data and software, so you do not need a different vendor for each.</p>{cards(SVC_CARDS)}</div></section>
<section class="band"><div class="wrap"><div class="eyebrow">Why trust us</div><h2>How we earn it</h2><p class="lead">No logos or numbers to hide behind. These are the commitments we work to on every engagement.</p>{cards([(a,b,"") for a,b in TR],False)}</div></section>
<section><div class="wrap"><div class="eyebrow">Engagement models</div><h2>Work with us your way</h2><p class="lead">Four models, usable alone or combined.</p>{cards([(a,b,"engagement-models.html") for a,b,_ in MODELS],False)}</div></section>
<section class="band"><div class="wrap"><div class="eyebrow">How a project runs</div><h2>Clear stages, no surprises</h2>{steps()}</div></section>
<section><div class="wrap"><div class="eyebrow">Questions</div><h2>Straight answers</h2><div style="max-width:760px;margin-top:26px">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in FQ)}</div></div></section>{cta()}"""
write("index","Data engineering, AI and software development","Hayaten Data Labs builds data platforms, AI solutions, automation and custom software for businesses worldwide.",home)
write("services","Services","Software development, data engineering, AI, hyperautomation, cloud migration and consulting.",phead("Our services","Six service areas, one engineering team.")+f'<section><div class="wrap">{cards(SVC_CARDS)}<p class="lead" style="margin-top:34px">Also available: managed IT support and specialist developer staffing when a project needs additional capacity.</p></div></section>'+cta())
for k,(t,l,b,a) in SV.items():
    write(k,t,l,phead(t,l)+f'<section><div class="wrap two"><div><h2>What we build</h2>{tick(b)}</div><div><h2>How we deliver</h2>{tick(a)}</div></div></section><section class="band"><div class="wrap"><h2>How a project runs</h2>{steps()}</div></section>'+cta())
write("engagement-models","Engagement models","Fixed-price projects, team augmentation, milestone-based scope of work and approved vendor status.",phead("Engagement models","Different projects need different ways of working. Choose the one that fits.")+f'<section><div class="wrap">{cards(MODELS,False)}</div></section>'+cta())
write("how-we-work","How we work","Our four-stage delivery process and how we communicate.",phead("How we work","A simple, transparent process from first call to handover.")+f'<section><div class="wrap">{steps()}</div></section><section class="band"><div class="wrap two"><div><h2>Governance</h2><p class="lead">Every engagement has a named project lead, a shared plan, regular status updates, scheduled demos and a written change-control process.</p></div><div>{tick(["Weekly or fortnightly demos","Risks raised early and discussed openly","Milestone sign-off against agreed criteria","NDA signed before any detail is shared"])}</div></div></section>'+cta())
write("about","About us","Hayaten Data Labs is an India-registered technology company building data, AI and software systems.",phead("About us","An engineering-led company, built around clarity, quality and ownership.")+f'<section><div class="wrap two"><div><h2>Who we are</h2><p>Hayaten Data Labs Private Limited is registered in India and works with clients around the world. Every engagement is scoped by people who understand the technology and delivered by specialists chosen for the work in front of them.</p></div><div>{tick(["Clarity before code","Data you can trust","Simplicity over complexity","Ownership and transparency"])}</div></div></section>'+cta())
FORM=lambda fields,sub:f'<form id="f">{fields}<button class="btn" type="submit">{sub}</button><p id="n" role="status"></p></form><script>document.getElementById("f").addEventListener("submit",function(e){{e.preventDefault();var b="";this.querySelectorAll("input,textarea,select").forEach(function(x){{b+=x.name+": "+x.value+"\\n"}});location.href="mailto:{EMAIL}?subject="+encodeURIComponent(document.title)+"&body="+encodeURIComponent(b);}});</script>'
fld=lambda n,l,t="input":f'<div><label>{l}</label><{t} name="{l}" required></{t}></div>' if t=="textarea" else f'<div><label>{l}</label><input name="{l}" required></div>'
write("contact","Request a quote","Tell us what you need and we will reply within two business days.",phead("Request a quote","Tell us about your project. We reply within two business days.")+f'<section><div class="wrap">{FORM(fld("a","Name")+fld("b","Work email")+fld("c","Company")+fld("d","What do you need?","textarea"),"Send enquiry")}</div></section>')
write("join-our-bench","Join our bench","Developers and data engineers: tell us about your skills.",phead("Join our bench","Developers and data engineers: tell us about your skills and availability.")+f'<section><div class="wrap">{FORM(fld("a","Name")+fld("b","Email")+fld("c","Core skills")+fld("d","Experience and availability","textarea"),"Send details")}</div></section>')
write("privacy","Privacy policy","How Hayaten Data Labs handles personal information.",phead("Privacy policy","How we handle information you send us.")+f'<section><div class="wrap"><p>[Draft placeholder. Have a lawyer review before launch.] When you contact us we receive the details you submit, such as your name, email address and message. We use them only to respond to you and are not sold to third parties. To ask for your information to be deleted, email {EMAIL}.</p></div></section>')
z=zipfile.ZipFile("/mnt/user-data/outputs/hayaten-site.zip","w",zipfile.ZIP_DEFLATED)
for r,_,fs in os.walk(OUT):
    for f in fs: z.write(os.path.join(r,f),os.path.relpath(os.path.join(r,f),OUT))
z.close(); print(sorted(os.listdir(OUT)))
