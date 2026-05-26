import os
import urllib.request

# Create assets folder if not exists
assets_dir = 'assets'
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    print(f"Created directory: {assets_dir}")

# Brand colors for SVG vector generator fallbacks (Strict backup recovery only)
PRIMARY_BLUE = "#0078B6"
ACCENT_GREEN = "#8CC63F"
DARK_NAV = "#242424"
LIGHT_BG = "#F5F7F8"

# 1. Custom SVG logo generation
SVG_LOGO_DARK = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="500" height="120">
  <defs>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PRIMARY_BLUE}" />
      <stop offset="100%" stop-color="#005C8A" />
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_GREEN}" />
      <stop offset="100%" stop-color="#7BAE22" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 10)">
    <path d="M 15,30 L 55,10 L 95,30 L 95,70 L 55,90 L 15,70 Z" fill="none" stroke="url(#blueGrad)" stroke-width="6" stroke-linejoin="round" />
    <path d="M 55,25 L 80,38 L 80,62 L 55,75 L 30,62 Z" fill="url(#greenGrad)" opacity="0.85" />
    <path d="M 55,10 L 55,90 M 15,70 L 95,30 M 15,30 L 95,70" stroke="#ffffff" stroke-width="2" opacity="0.3" />
  </g>
  <text x="130" y="58" font-family="'Poppins', sans-serif" font-size="34" font-weight="800" fill="#ffffff" letter-spacing="1.5">ECO SPACE</text>
  <text x="130" y="88" font-family="'Outfit', sans-serif" font-size="16" font-weight="600" fill="{ACCENT_GREEN}" letter-spacing="4.5">PRODUCTS</text>
  <text x="130" y="105" font-family="'Outfit', sans-serif" font-size="10" font-weight="400" fill="#8A8A8A" letter-spacing="2">TRANSFORMING SPACES</text>
</svg>"""

SVG_LOGO_LIGHT = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="500" height="120">
  <defs>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PRIMARY_BLUE}" />
      <stop offset="100%" stop-color="#005C8A" />
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_GREEN}" />
      <stop offset="100%" stop-color="#7BAE22" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 10)">
    <path d="M 15,30 L 55,10 L 95,30 L 95,70 L 55,90 L 15,70 Z" fill="none" stroke="url(#blueGrad)" stroke-width="6" stroke-linejoin="round" />
    <path d="M 55,25 L 80,38 L 80,62 L 55,75 L 30,62 Z" fill="url(#greenGrad)" opacity="0.85" />
    <path d="M 55,10 L 55,90 M 15,70 L 95,30 M 15,30 L 95,70" stroke="#ffffff" stroke-width="2" opacity="0.3" />
  </g>
  <text x="130" y="58" font-family="'Poppins', sans-serif" font-size="34" font-weight="800" fill="{DARK_NAV}" letter-spacing="1.5">ECO SPACE</text>
  <text x="130" y="88" font-family="'Outfit', sans-serif" font-size="16" font-weight="600" fill="{PRIMARY_BLUE}" letter-spacing="4.5">PRODUCTS</text>
  <text x="130" y="105" font-family="'Outfit', sans-serif" font-size="10" font-weight="400" fill="#8A8A8A" letter-spacing="2">TRANSFORMING SPACES</text>
</svg>"""

with open(os.path.join(assets_dir, 'logo.svg'), 'w', encoding='utf-8') as f:
    f.write(SVG_LOGO_DARK)
with open(os.path.join(assets_dir, 'logo-light.svg'), 'w', encoding='utf-8') as f:
    f.write(SVG_LOGO_LIGHT)
print("Created SVG Brand logos.")

def generate_svg_fallback(filepath, label):
    """Generates an extremely sleek geometric CSS/SVG placeholder in case of network issue."""
    width = 1600 if 'hero' in filepath or 'map' in filepath else 800
    height = 1000 if 'hero' in filepath else (600 if 'map' in filepath else 600)
    
    bg_color = DARK_NAV if 'hero' in filepath or 'alloy' in filepath or 'project' in filepath else LIGHT_BG
    text_color = "#ffffff" if bg_color == DARK_NAV else "#1F2528"
    accent_bar = ACCENT_GREEN
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
      <rect width="100%" height="100%" fill="{bg_color}" />
      <circle cx="{width//2}" cy="{height//2}" r="{min(width, height)//4}" fill="{PRIMARY_BLUE}" opacity="0.05" />
      <path d="M 0,{height//3} Q {width//4},{height//2} {width//2},{height//3} T {width},{height//2}" stroke="{PRIMARY_BLUE}" stroke-width="2" fill="none" opacity="0.1" />
      <path d="M 0,{height*2//3} Q {width*3//4},{height//3} {width//2},{height*2//3} T {width},{height//3}" stroke="{accent_bar}" stroke-width="2" fill="none" opacity="0.1" />
      <line x1="{width//4}" y1="0" x2="{width//4}" y2="{height}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      <line x1="{width//2}" y1="0" x2="{width//2}" y2="{height}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      <text x="{width//2}" y="{height//2 - 10}" font-family="'Poppins', sans-serif" font-size="28" font-weight="700" fill="{text_color}" text-anchor="middle" letter-spacing="2">ECO SPACE PRODUCTS</text>
      <text x="{width//2}" y="{height//2 + 30}" font-family="'Outfit', sans-serif" font-size="16" font-weight="500" fill="{accent_bar}" text-anchor="middle" letter-spacing="4">{label.upper()}</text>
    </svg>"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)

# Highly stable, beautifully-curated high-res corporate interior and real estate asset lists
UNSPLASH_ASSETS = {
    # Brand Preview Illustration
    'about-logo.png': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=600&q=80',

    # Main Banners
    'hero-partition.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80',
    'hero-furniture.jpg': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1600&q=80',

    # Partition Slideshow images (6 high-quality views)
    'alloyss1.jpg': 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80',
    'alloyss2.jpg': 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80',
    'alloyss3.jpg': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80',
    'alloyss4.jpg': 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=800&q=80',
    'alloyss5.jpg': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80',
    'alloyss6.jpg': 'https://images.unsplash.com/photo-1542744094-3a31f103e35f?auto=format&fit=crop&w=800&q=80',

    # Stylized map texture
    'contact-map.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1200&q=80',
}

# Add 20 partition grid assets - using extremely clean, active office partition/glazing photo IDs
partition_photo_ids = [
    'photo-1497366216548-37526070297c', 'photo-1497366754035-f200968a6e72', 'photo-1497366811353-6870744d04b2',
    'photo-1504384308090-c894fdcc538d', 'photo-1497215728101-856f4ea42174', 'photo-1486406146926-c627a92ad1ab',
    'photo-1542744094-3a31f103e35f', 'photo-1556761175-5973dc0f32e7', 'photo-1568992687947-868a62a9f521',
    'photo-1572021335469-31706a17aaef', 'photo-1517502884422-41eaaced0168', 'photo-1531973576160-7125cd663d86',
    'photo-1513694203232-719a280e022f', 'photo-1497366216548-37526070297c', 'photo-1497215728101-856f4ea42174',
    'photo-1504384308090-c894fdcc538d', 'photo-1542744094-3a31f103e35f', 'photo-1556761175-5973dc0f32e7',
    'photo-1568992687947-868a62a9f521', 'photo-1572021335469-31706a17aaef'
]

for i in range(1, 21):
    unsplash_id = partition_photo_ids[(i - 1) % len(partition_photo_ids)]
    # FIXED: Replaced double slash with clean single slash!
    UNSPLASH_ASSETS[f'alloygrid{i}.jpg'] = f'https://images.unsplash.com/{unsplash_id}?auto=format&fit=crop&w=800&q=80'

# Add 8 furniture assets - using highly modern lounge & dynamic office breakout furniture designs
furniture_photo_ids = [
    'photo-1586023492125-27b2c045efd7', 'photo-1505691938895-1758d7feb511', 'photo-1567538096630-e0c55bd6374c',
    'photo-1595515106969-1ce29566ff1c', 'photo-1519641471654-76ce0107ad1b', 'photo-1507089947368-19c1da9775ae',
    'photo-1540518614846-7eded433c457', 'photo-1586023492125-27b2c045efd7'
]

for j in range(1, 9):
    unsplash_id = furniture_photo_ids[(j - 1) % len(furniture_photo_ids)]
    UNSPLASH_ASSETS[f'furniture-{j}.jpg'] = f'https://images.unsplash.com/{unsplash_id}?auto=format&fit=crop&w=800&q=80'

# Add 11 Client Project background slides
project_names = ['bcg', 'bosch', 'cargill', 'expedia', 'hpvogue', 'hp', 'informatica', 'sap', 'sequoia', 'thomson', 'verizon']
for proj in project_names:
    for slide in range(1, 3):
        proj_ids = [
            'photo-1497366216548-37526070297c', 'photo-1497215728101-856f4ea42174', 'photo-1504384308090-c894fdcc538d',
            'photo-1542744094-3a31f103e35f', 'photo-1556761175-5973dc0f32e7', 'photo-1568992687947-868a62a9f521',
            'photo-1572021335469-31706a17aaef', 'photo-1524758631624-e2822e304c36', 'photo-1513694203232-719a280e022f'
        ]
        unsplash_id = proj_ids[(slide - 1) % len(proj_ids)]
        UNSPLASH_ASSETS[f'project-{proj}-{slide}.jpg'] = f'https://images.unsplash.com/{unsplash_id}?auto=format&fit=crop&w=800&q=80'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

print("Starting expanded, fixed asset download from Unsplash (widescreen JPEGs)...")
for name, url in UNSPLASH_ASSETS.items():
    filepath = os.path.join(assets_dir, name)
    print(f"Downloading {name}...", end="", flush=True)
    try:
        # FIXED: Set higher timeout limit to 15 seconds to completely prevent connection resets
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(" Success!")
    except Exception as e:
        print(f" Failed. Generating brand vector SVG fallback...")
        generate_svg_fallback(filepath, name.split('.')[0].replace('-', ' '))

# Generate stylized LinkedIn brand PNG
SVG_LINKEDIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#8CC63F">
  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
</svg>"""
with open(os.path.join(assets_dir, 'linkedin.svg'), 'w') as f:
    f.write(SVG_LINKEDIN)
with open(os.path.join(assets_dir, 'linkedin.png'), 'w') as f:
    f.write(SVG_LINKEDIN)

print("\nAsset configuration complete!")
