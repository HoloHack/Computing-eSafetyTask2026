import pathlib, re
from html.parser import HTMLParser
root=pathlib.Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
js=(root/'app.js').read_text()
css=(root/'styles.css').read_text()
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.anchors=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and a.get('href','').startswith('#'):self.anchors.append(a['href'][1:])
p=Parser();p.feed(html)
assert len(p.ids)==len(set(p.ids)), 'Duplicate IDs'
assert all(a in p.ids for a in p.anchors), 'Missing anchor'
assert all(x in p.ids for x in re.findall(r'\$\("([^"]+)"\)',js)), 'Missing JS target'
assert len(re.findall(r'data-protection=',html))==5
assert len(re.findall(r'class="game" id=',html))==4
assert len(re.findall(r'\{q:',js))==3
assert 'prefers-reduced-motion' in css
assert 'https://www.esafety.gov.au/young-people/online-gaming' in html
assert 'https://www.esafety.gov.au/industry/basic-online-safety-expectations/online-game-and-gaming-adjacent-services' in html
print('PASS: IDs, anchors, JS references, coverage, sources, reduced motion')
