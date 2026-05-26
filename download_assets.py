import os
import urllib.request
import base64

# Create assets folder if not exists
assets_dir = 'assets'
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    print(f"Created directory: {assets_dir}")

# Color constants for fallback styling
PRIMARY_BLUE = "#0074AA"
ACCENT_GREEN = "#8CC63F"
DARK_NAV = "#242424"
LIGHT_BG = "#F5F7F8"

# 1. Custom SVG Logos and graphics generators in case Unsplash fails or for quick local generation
SVG_LOGO = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="500" height="120">
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
  <!-- Logo Icon: Geometric Eco Space blocks -->
  <g transform="translate(10, 10)">
    <!-- Main outer blue structure -->
    <path d="M 15,30 L 55,10 L 95,30 L 95,70 L 55,90 L 15,70 Z" fill="none" stroke="url(#blueGrad)" stroke-width="6" stroke-linejoin="round" />
    <!-- Dynamic green interior eco-leaf/space chevron -->
    <path d="M 55,25 L 80,38 L 80,62 L 55,75 L 30,62 Z" fill="url(#greenGrad)" opacity="0.85" />
    <!-- Inner white space divider -->
    <path d="M 55,10 L 55,90 M 15,70 L 95,30 M 15,30 L 95,70" stroke="#ffffff" stroke-width="2" opacity="0.3" />
  </g>
  <!-- Text Elements -->
  <text x="130" y="58" font-family="'Poppins', 'Montserrat', sans-serif" font-size="34" font-weight="800" fill="#ffffff" letter-spacing="1.5">ECO SPACE</text>
  <text x="130" y="88" font-family="'Outfit', 'Inter', sans-serif" font-size="16" font-weight="600" fill="{ACCENT_GREEN}" letter-spacing="4.5">PRODUCTS</text>
  <!-- Small Elegant tagline -->
  <text x="130" y="105" font-family="'Outfit', 'Inter', sans-serif" font-size="10" font-weight="400" fill="#8A8A8A" letter-spacing="2">TRANSFORMING SPACES</text>
</svg>"""

SVG_LOGO_DARK_BG = SVG_LOGO

SVG_LOGO_LIGHT_BG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="500" height="120">
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
  <text x="130" y="58" font-family="'Poppins', 'Montserrat', sans-serif" font-size="34" font-weight="800" fill="{DARK_NAV}" letter-spacing="1.5">ECO SPACE</text>
  <text x="130" y="88" font-family="'Outfit', 'Inter', sans-serif" font-size="16" font-weight="600" fill="{PRIMARY_BLUE}" letter-spacing="4.5">PRODUCTS</text>
  <text x="130" y="105" font-family="'Outfit', 'Inter', sans-serif" font-size="10" font-weight="400" fill="#8A8A8A" letter-spacing="2">TRANSFORMING SPACES</text>
</svg>"""

# Write custom SVG logo fallback and helper assets directly
with open(os.path.join(assets_dir, 'logo.svg'), 'w', encoding='utf-8') as f:
    f.write(SVG_LOGO_DARK_BG)
with open(os.path.join(assets_dir, 'logo-light.svg'), 'w', encoding='utf-8') as f:
    f.write(SVG_LOGO_LIGHT_BG)
print("Created SVG Brand logos.")

# Create simple placeholder transparent PNG logo by writing a pixel-polished SVG-like fallback
# We will use this logo.svg directly in index.html to maintain absolute modern crispness (best practice),
# but we will download standard logo PNG placeholder for completeness.

# Curated Unsplash IDs for stunning corporate architectures, glass partitions, and clean furniture
UNSPLASH_ASSETS = {
    # Hero images
    'hero-partition.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80',
    'hero-furniture.jpg': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1600&q=80',
    'logo.png': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=400&q=80', # Clean architectural background
    'about-logo.png': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=800&q=80', # Team collaboration

    # Partition images (Alloy)
    'alloy-1.jpg': 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80',
    'alloy-2.jpg': 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80',
    'alloy-3.jpg': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80',
    'alloy-4.jpg': 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=800&q=80',
    'alloy-5.jpg': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80',
    'alloy-6.jpg': 'https://images.unsplash.com/photo-1542744094-3a31f103e35f?auto=format&fit=crop&w=800&q=80',
    'alloy-7.jpg': 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80',
    'alloy-8.jpg': 'https://images.unsplash.com/photo-1568992687947-868a62a9f521?auto=format&fit=crop&w=800&q=80',
    'alloy-9.jpg': 'https://images.unsplash.com/photo-1572021335469-31706a17aaef?auto=format&fit=crop&w=800&q=80',
    'alloy-10.jpg': 'https://images.unsplash.com/photo-1517502884422-41eaaced0168?auto=format&fit=crop&w=800&q=80',
    'alloy-11.jpg': 'https://images.unsplash.com/photo-1531973576160-7125cd663d86?auto=format&fit=crop&w=800&q=80',
    'alloy-12.jpg': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80',

    # Furniture images
    'furniture-1.jpg': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80',
    'furniture-2.jpg': 'https://images.unsplash.com/photo-1554009975-d74653b849f1?auto=format&fit=crop&w=800&q=80',
    'furniture-3.jpg': 'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?auto=format&fit=crop&w=800&q=80',
    'furniture-4.jpg': 'https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?auto=format&fit=crop&w=800&q=80',
    'furniture-5.jpg': 'https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&w=800&q=80',
    'furniture-6.jpg': 'https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=800&q=80',
    'furniture-7.jpg': 'https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=800&q=80',
    'furniture-8.jpg': 'https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&w=800&q=80',

    # Project grid background/previews (Using different premium architectural spaces)
    'project-bcg.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80',
    'project-bosch.jpg': 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=800&q=80',
    'project-cargill.jpg': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80',
    'project-expedia.jpg': 'https://images.unsplash.com/photo-1542744094-3a31f103e35f?auto=format&fit=crop&w=800&q=80',
    'project-hpvogue.jpg': 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80',
    'project-hp.jpg': 'https://images.unsplash.com/photo-1568992687947-868a62a9f521?auto=format&fit=crop&w=800&q=80',
    'project-informatica.jpg': 'https://images.unsplash.com/photo-1572021335469-31706a17aaef?auto=format&fit=crop&w=800&q=80',
    'project-sap.jpg': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80',
    'project-sequoia.jpg': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80',
    'project-thomson.jpg': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80',
    'project-verizon.jpg': 'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?auto=format&fit=crop&w=800&q=80',

    # Contact map and social
    'contact-map.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1200&q=80',
}

# Add sub-project slides for rotation! We will create project slideshow images by appending _1, _2, _3
PROJECT_SLIDES = [
    'bcg', 'bosch', 'cargill', 'expedia', 'hpvogue', 'hp', 'informatica', 'sap', 'sequoia', 'thomson', 'verizon'
]

# We will generate project carousel files locally by linking them or copying them to keep bundle small and fast
# or downloading beautiful variations. To be performant, we can reuse partition and furniture assets as slides,
# which represents a brilliant technique to avoid downloading 33 more files, or we can download standard optimized ones.
# Let's map project slides dynamically to other downloaded high-quality files in JavaScript to minimize disk space,
# keeping it fully relative, OR download a few variations. Let's download a small set or reuse them.
# The JavaScript code can cycle between `assets/alloy-${i}.jpg` and `assets/furniture-${j}.jpg` for the slides,
# which is incredibly smart and saves bandwidth! Let's download the base images and also support direct slide images.

def generate_svg_fallback(filepath, label):
    """Generates an extremely sleek geometric CSS/SVG placeholder in case of network issue."""
    width = 1600 if 'hero' in filepath or 'map' in filepath else 800
    height = 1000 if 'hero' in filepath else (600 if 'map' in filepath else 600)
    
    bg_color = DARK_NAV if 'hero' in filepath or 'project' in filepath else LIGHT_BG
    text_color = "#ffffff" if bg_color == DARK_NAV else "#1F2528"
    accent_bar = ACCENT_GREEN
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
      <rect width="100%" height="100%" fill="{bg_color}" />
      <circle cx="{width//2}" cy="{height//2}" r="{min(width, height)//4}" fill="{PRIMARY_BLUE}" opacity="0.05" />
      <path d="M 0,{height//3} Q {width//4},{height//2} {width//2},{height//3} T {width},{height//2}" stroke="{PRIMARY_BLUE}" stroke-width="2" fill="none" opacity="0.1" />
      <path d="M 0,{height*2//3} Q {width*3//4},{height//3} {width//2},{height*2//3} T {width},{height//3}" stroke="{ACCENT_GREEN}" stroke-width="2" fill="none" opacity="0.1" />
      <!-- Minimal Architectural grid lines -->
      <line x1="{width//4}" y1="0" x2="{width//4}" y2="{height}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      <line x1="{width//2}" y1="0" x2="{width//2}" y2="{height}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      <line x1="{width*3//4}" y1="0" x2="{width*3//4}" y2="{height}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      <line x1="0" y1="{height//2}" x2="{width}" y2="{height//2}" stroke="{text_color}" stroke-width="0.5" opacity="0.05" />
      
      <!-- Graphic Focus bracket -->
      <path d="M 40,40 L 40,20 L 20,20 L 20,40" stroke="{accent_bar}" stroke-width="3" fill="none" />
      <path d="M {width-40},40 L {width-40},20 L {width-20},20 L {width-20},40" stroke="{accent_bar}" stroke-width="3" fill="none" />
      <path d="M 40,{height-40} L 40,{height-20} L 20,{height-20} L 20,{height-40}" stroke="{accent_bar}" stroke-width="3" fill="none" />
      <path d="M {width-40},{height-40} L {width-40},{height-20} L {width-20},{height-20} L {width-20},{height-40}" stroke="{accent_bar}" stroke-width="3" fill="none" />
      
      <!-- Label Text -->
      <text x="{width//2}" y="{height//2 - 10}" font-family="'Poppins', 'Montserrat', sans-serif" font-size="28" font-weight="700" fill="{text_color}" text-anchor="middle" letter-spacing="2">ECO SPACE PRODUCTS</text>
      <text x="{width//2}" y="{height//2 + 30}" font-family="'Outfit', 'Inter', sans-serif" font-size="16" font-weight="500" fill="{accent_bar}" text-anchor="middle" letter-spacing="4">{label.upper()}</text>
      <line x1="{width//2 - 60}" y1="{height//2 + 50}" x2="{width//2 + 60}" y2="{height//2 + 50}" stroke="{PRIMARY_BLUE}" stroke-width="2" />
    </svg>"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)

# Loop and download images with high-quality fallbacks
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

print("Starting asset download from Unsplash (optimized sizes)...")
for name, url in UNSPLASH_ASSETS.items():
    filepath = os.path.join(assets_dir, name)
    
    # Check if we should write standard SVG fallback immediately or try to download
    # Logo is better served as crisp SVG logo.svg directly in HTML, but we will download standard backgrounds.
    print(f"Downloading {name}...", end="", flush=True)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(" Success!")
    except Exception as e:
        print(f" Failed ({str(e)}). Generating vector SVG fallback instead...")
        # Save as SVG fallback (named .jpg or .png to keep system links intact!)
        # Web browsers fully support loading SVG markup inside standard <img> tags even if named .jpg!
        # But to be ultra-compatible and standard, we write the SVG code.
        svg_filepath = filepath.replace('.jpg', '.svg').replace('.png', '.svg')
        generate_svg_fallback(svg_filepath, name.split('.')[0].replace('-', ' '))
        # Also copy or rename it or write a clean fallback to the actual requested filename
        generate_svg_fallback(filepath, name.split('.')[0].replace('-', ' '))

# Creating a high-contrast LinkedIn icon locally
SVG_LINKEDIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#8CC63F">
  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
</svg>"""
with open(os.path.join(assets_dir, 'linkedin.svg'), 'w') as f:
    f.write(SVG_LINKEDIN)
with open(os.path.join(assets_dir, 'linkedin.png'), 'w') as f:
    # Just save it as SVG code or raw text fallback so the image is available
    f.write(SVG_LINKEDIN)

print("\nAsset configuration complete!")
