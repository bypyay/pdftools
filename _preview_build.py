"""
LOCAL PREVIEW ONLY — renders the PHP-templated pages into static HTML
under _preview/ so they can be viewed in a browser without a PHP server.
This is NOT part of the deployed site (the real hosting runs the .php
files directly via PHP). Delete _preview/ and this script before upload.
"""
import os
import re
import shutil
import html as htmlmod

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '_preview')

TOOLS = [
    ('merge', '#e5322d', 'Merge PDF', 'Combine multiple PDFs into one single file.', 'tools/merge-pdf/', True),
    ('split', '#1ba94c', 'Split PDF', 'Extract or split pages into separate PDF files.', 'tools/split-pdf/', True),
    ('compress', '#e58a1c', 'Compress PDF', 'Reduce PDF file size while keeping quality.', 'tools/compress-pdf/', True),
    ('image', '#2b7de9', 'PDF to JPG', 'Convert every PDF page into a JPG image.', 'tools/pdf-to-jpg/', True),
    ('file', '#8a3ee5', 'JPG to PDF', 'Turn your JPG or PNG images into a PDF.', 'tools/jpg-to-pdf/', True),
    ('rotate', '#0aa3a3', 'Rotate PDF', 'Rotate one or all pages of your PDF.', 'tools/rotate-pdf/', True),
    ('lock', '#c81e1e', 'Protect PDF', 'Add a password to secure your PDF.', '#', False),
    ('unlock', '#1ba94c', 'Unlock PDF', 'Remove password protection from a PDF.', 'tools/unlock-pdf/', True),
    ('watermark', '#e5322d', 'Watermark PDF', 'Stamp text or image watermark on pages.', 'tools/watermark-pdf/', True),
    ('word', '#2b5ce9', 'PDF to Word', 'Convert your PDF into an editable DOCX.', 'tools/pdf-to-word/', True),
    ('number', '#e58a1c', 'Page Numbers', 'Add page numbers to your PDF.', 'tools/page-numbers/', True),
    ('trash', '#8a3ee5', 'Delete Pages', 'Remove unwanted pages from a PDF.', 'tools/delete-pages/', True),
]

ICONS = {
    'merge': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3v6a2 2 0 0 0 2 2h6"/><path d="M17 21v-6a2 2 0 0 0-2-2H9"/></svg>',
    'split': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3"/><path d="M21 8V5a2 2 0 0 0-2-2h-3"/><path d="M3 16v3a2 2 0 0 0 2 2h3"/><path d="M16 21h3a2 2 0 0 0 2-2v-3"/></svg>',
    'compress': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3v3a2 2 0 0 1-2 2H3"/><path d="M21 8h-3a2 2 0 0 1-2-2V3"/><path d="M3 16h3a2 2 0 0 1 2 2v3"/><path d="M16 21v-3a2 2 0 0 1 2-2h3"/></svg>',
    'image': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>',
    'file': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>',
    'rotate': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2v6h-6"/><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M3 22v-6h6"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/></svg>',
    'lock': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    'unlock': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>',
    'watermark': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M9 15l6-6M9 9l6 6"/></svg>',
    'word': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M8 13l1.5 5L11 14l1.5 4L14 13"/></svg>',
    'number': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><text x="8" y="18" font-size="8" fill="#fff" stroke="none">12</text></svg>',
    'trash': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>',
}


def header(root, title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmlmod.escape(title)}</title>
<meta name="description" content="{htmlmod.escape(desc)}">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="{root}index.html" class="brand">Daily1Step PDF<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="{root}index.html">All Tools</a>
      <a href="{root}tools/merge-pdf/">Merge PDF</a>
      <a href="{root}tools/split-pdf/">Split PDF</a>
      <a href="{root}tools/compress-pdf/">Compress PDF</a>
      <a href="{root}about.html">About</a>
    </nav>
  </div>
</header>
'''


def footer(root):
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-bottom">Preview build &mdash; Daily1Step PDF</div>
  </div>
</footer>
<script src="{root}assets/js/main.js"></script>
</body>
</html>
'''


def build_index():
    cards = ''
    for icon, color, title, desc, href, live in TOOLS:
        cls = 'tool-card' if live else 'tool-card disabled'
        badge = '<span class="badge">Coming soon</span>' if not live else ''
        cards += f'''<a class="{cls}" href="{href.replace('tools/', 'tools/').rstrip('/') + '/' if live else '#'}">
        {badge}
        <span class="icon" style="background:{color}">{ICONS[icon]}</span>
        <h3>{htmlmod.escape(title)}</h3>
        <p>{htmlmod.escape(desc)}</p>
      </a>'''

    body = f'''<section class="hero">
  <div class="container">
    <h1>Every PDF tool you need, in one place</h1>
    <p>Merge, split, compress and convert PDF files &mdash; 100% free, no signup, and every file is processed right in your browser.</p>
  </div>
</section>
<section class="container">
  <div class="tool-grid">
    {cards}
  </div>
</section>
<section class="info-section">
  <h2>Why use Daily1Step PDF?</h2>
  <p>Daily1Step PDF runs entirely in your web browser. Your files are never uploaded to a server.</p>
</section>
'''
    html = header('', 'Daily1Step PDF — Free Online PDF Tools', 'Merge, split, compress PDF online free.') + body + footer('')
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


def build_tool_generic(tool_dir):
    """Renders tools/<tool_dir>/index.php into _preview/tools/<tool_dir>/index.html
    by stripping the PHP scaffolding, so the preview always matches the real
    template body instead of a hand-duplicated copy."""
    src_path = os.path.join(ROOT, 'tools', tool_dir, 'index.php')
    with open(src_path, 'r', encoding='utf-8') as f:
        src = f.read()

    title_m = re.search(r"\$page_title = '([^']*)';", src)
    desc_m = re.search(r"\$page_description = '([^']*)';", src)
    title = title_m.group(1) if title_m else tool_dir
    desc = desc_m.group(1) if desc_m else ''

    # Strip the opening <?php ... include header.php; ?> block
    body = re.sub(r"^<\?php.*?include __DIR__ \. '/\.\./\.\./includes/header\.php';\s*\?>", '', src, flags=re.S)
    # Strip the closing <?php include footer.php ?> block
    body = re.sub(r"<\?php include __DIR__ \. '/\.\./\.\./includes/footer\.php'; \?>\s*$", '', body)
    # Resolve the $root PHP echo used for asset links
    body = body.replace("<?php echo $root; ?>", '../../')

    out_dir = os.path.join(OUT, 'tools', tool_dir)
    os.makedirs(out_dir, exist_ok=True)
    html = header('../../', title, desc) + body + footer('../../')
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)


def build_root_page(name):
    """Renders a root-level page like about.php into _preview/<name>.html."""
    src_path = os.path.join(ROOT, name + '.php')
    with open(src_path, 'r', encoding='utf-8') as f:
        src = f.read()

    title_m = re.search(r"\$page_title = '([^']*)';", src)
    desc_m = re.search(r"\$page_description = '([^']*)';", src)
    title = title_m.group(1) if title_m else name
    desc = desc_m.group(1) if desc_m else ''

    body = re.sub(r"^<\?php.*?include __DIR__ \. '/includes/header\.php';\s*\?>", '', src, flags=re.S)
    body = re.sub(r"<\?php include __DIR__ \. '/includes/footer\.php'; \?>\s*$", '', body)
    body = body.replace("<?php echo $root; ?>", '')
    body = re.sub(r"<\?php echo date\('F j, Y'\); \?>", __import__('datetime').date.today().strftime('%B %d, %Y'), body)

    html = header('', title, desc) + body + footer('')
    with open(os.path.join(OUT, name + '.html'), 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copytree(os.path.join(ROOT, 'vendor'), os.path.join(OUT, 'vendor'))
    build_index()
    for tool_dir in ['merge-pdf', 'split-pdf', 'compress-pdf', 'pdf-to-jpg', 'jpg-to-pdf',
                      'rotate-pdf', 'delete-pages', 'watermark-pdf', 'page-numbers', 'unlock-pdf', 'pdf-to-word']:
        php_path = os.path.join(ROOT, 'tools', tool_dir, 'index.php')
        if os.path.exists(php_path):
            build_tool_generic(tool_dir)
    for page in ['about', 'contact', 'privacy-policy', 'terms']:
        if os.path.exists(os.path.join(ROOT, page + '.php')):
            build_root_page(page)
    print('Preview built at', OUT)
