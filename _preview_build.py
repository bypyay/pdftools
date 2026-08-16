"""
LOCAL PREVIEW ONLY — renders the PHP-templated pages into static HTML
under _preview/ so they can be viewed in a browser without a PHP server.
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
    ('sign', '#8a3ee5', 'Sign PDF', 'Draw, type, or upload your signature to place on any page.', 'tools/sign-pdf/', True),
    ('organize', '#e5322d', 'Organize PDF', 'Sort, reorder, rotate, or delete pages visually.', 'tools/organize-pdf/', True),
    ('extract', '#1ba94c', 'Extract Pages', 'Extract specific pages or page ranges into a new PDF.', 'tools/extract-pages/', True),
    ('crop', '#0aa3a3', 'Crop PDF', 'Trim margins or crop custom areas with interactive box.', 'tools/crop-pdf/', True),
    ('watermark', '#e5322d', 'Watermark PDF', 'Stamp text or image watermark with cursor positioning.', 'tools/watermark-pdf/', True),
    ('image', '#2b7de9', 'PDF to JPG', 'Convert every PDF page into a high-res JPG image.', 'tools/pdf-to-jpg/', True),
    ('file', '#8a3ee5', 'JPG to PDF', 'Turn your JPG or PNG images into a PDF.', 'tools/jpg-to-pdf/', True),
    ('word', '#2b5ce9', 'PDF to Word', 'Convert your PDF into an editable DOCX document.', 'tools/pdf-to-word/', True),
    ('txt', '#e58a1c', 'PDF to Text', 'Extract clean plain text from your PDF document.', 'tools/pdf-to-txt/', True),
    ('extract-img', '#2b7de9', 'Extract Images', 'Extract all embedded photos and graphics to ZIP.', 'tools/extract-images/', True),
    ('grayscale', '#4b5563', 'Grayscale PDF', 'Convert color PDF to Black & White to save toner/ink.', 'tools/grayscale-pdf/', True),
    ('rotate', '#0aa3a3', 'Rotate PDF', 'Rotate one or all pages of your PDF document.', 'tools/rotate-pdf/', True),
    ('trash', '#8a3ee5', 'Delete Pages', 'Remove unwanted pages from a PDF document.', 'tools/delete-pages/', True),
    ('number', '#e58a1c', 'Page Numbers', 'Add customized page numbers to your PDF.', 'tools/page-numbers/', True),
    ('lock', '#c81e1e', 'Protect PDF', 'Add password encryption to secure your PDF.', 'tools/protect-pdf/', True),
    ('unlock', '#1ba94c', 'Unlock PDF', 'Remove password protection and restrictions from PDF.', 'tools/unlock-pdf/', True),
    ('repair', '#e5322d', 'Repair PDF', 'Recover damaged and corrupted PDF files.', 'tools/repair-pdf/', True),
    ('compare', '#2b5ce9', 'Compare PDF', 'Compare two PDFs side-by-side or with visual diff.', 'tools/compare-pdf/', True),
    ('html', '#0aa3a3', 'HTML to PDF', 'Convert HTML code, rich text, or web notes into PDF.', 'tools/html-to-pdf/', True),
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
    'organize': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    'extract': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    'crop': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.13 1L6 16a2 2 0 0 0 2 2h15"/><path d="M1 6.13L16 6a2 2 0 0 1 2 2v15"/></svg>',
    'sign': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/></svg>',
    'grayscale': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>',
    'extract-img': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
    'txt': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>',
    'repair': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    'compare': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="8" height="18" rx="2"/><rect x="14" y="3" width="8" height="18" rx="2"/><line x1="10" y1="8" x2="14" y2="8"/><line x1="10" y1="16" x2="14" y2="16"/></svg>',
    'html': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
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
      <a href="{root}tools/sign-pdf/">Sign PDF</a>
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
    <p>Merge, split, compress, sign, and convert PDF files &mdash; 100% free, no signup, and every file is processed right in your browser.</p>
  </div>
</section>

<section class="container">
  <div class="tool-grid">
    {cards}
  </div>
</section>

<section class="info-section">
  <h2>Why use Daily1Step PDF?</h2>
  <p>Daily1Step PDF runs entirely in your web browser. Unlike most online PDF tools, your files are <strong>never uploaded to a server</strong> &mdash; everything happens on your own device using client-side JavaScript. That means your documents stay 100% private, and the tools work instantly with no waiting for uploads or downloads.</p>
  <ul>
    <li><strong>22 Complete Tools</strong> &mdash; everything from merging, splitting, signing, cropping to repairing.</li>
    <li><strong>100% Free</strong> &mdash; every tool is free to use, with no hidden limits.</li>
    <li><strong>Private &amp; Secure</strong> &mdash; files are processed locally in your browser and never leave your device.</li>
    <li><strong>Fast &amp; Responsive</strong> &mdash; instant client-side execution with real-time drag-and-drop previews.</li>
    <li><strong>Cross-platform</strong> &mdash; works on Windows, Mac, Linux, Android and iOS, in any modern browser.</li>
  </ul>
</section>
'''
    return header('', 'Daily1Step PDF — Free Online PDF Tools | 22 Browser-Based PDF Tools', 'Every tool you need to work with PDFs in one place: 22 free client-side PDF tools.') + body + footer('')


def render_tool_php(php_path, root_rel):
    with open(php_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata
    m_title = re.search(r"\$page_title\s*=\s*'([^']*)'", content)
    title = m_title.group(1) if m_title else 'Daily1Step PDF'
    m_desc = re.search(r"\$page_description\s*=\s*'([^']*)'", content)
    desc = m_desc.group(1) if m_desc else ''

    # Remove PHP blocks and include wrappers
    body = content
    body = re.sub(r'<\?php\s*\$root\s*=.*?\?>', '', body, flags=re.DOTALL)
    body = re.sub(r"<\?php\s*include\s+__DIR__\s*\.\s*'/../../includes/header\.php';\s*\?>", '', body)
    body = re.sub(r"<\?php\s*include\s+__DIR__\s*\.\s*'/../../includes/footer\.php';\s*\?>", '', body)
    body = re.sub(r'<\?php\s*echo\s+\$root;\s*\?>', root_rel, body)
    body = re.sub(r'<\?php.*?\?>', '', body, flags=re.DOTALL)

    return header(root_rel, title, desc) + body.strip() + footer(root_rel)


def build_all():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # Copy static assets & vendor
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copytree(os.path.join(ROOT, 'vendor'), os.path.join(OUT, 'vendor'))

    # Root index
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_index())

    # Build tools
    tools_dir = os.path.join(ROOT, 'tools')
    for tname in os.listdir(tools_dir):
        tpath = os.path.join(tools_dir, tname)
        if os.path.isdir(tpath):
            php_file = os.path.join(tpath, 'index.php')
            if os.path.exists(php_file):
                out_tool_dir = os.path.join(OUT, 'tools', tname)
                os.makedirs(out_tool_dir, exist_ok=True)
                html_content = render_tool_php(php_file, '../../')
                with open(os.path.join(out_tool_dir, 'index.html'), 'w', encoding='utf-8') as f:
                    f.write(html_content)

    # Simple About page
    about_html = header('', 'About Daily1Step PDF', 'About our private browser-based PDF suite.') + '''
    <section class="tool-page"><div class="container">
      <h1>About Daily1Step PDF</h1>
      <p>Daily1Step PDF is a 100% client-side PDF utility suite. All operations run directly in your web browser with zero server uploads.</p>
    </div></section>''' + footer('')
    with open(os.path.join(OUT, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(about_html)

    print(f"Preview built at {OUT}")


if __name__ == '__main__':
    build_all()
