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

CATEGORIES = [
    ('all', 'All Tools', '🌟'),
    ('organize', 'Organize PDF', '📁'),
    ('optimize', 'Optimize PDF', '⚡'),
    ('convert-to', 'Convert to PDF', '🔄'),
    ('convert-from', 'Convert from PDF', '📄'),
    ('edit', 'Edit & Stamp', '✍️'),
    ('security', 'Security & Sign', '🔒'),
]

TOOLS = [
    # Organize
    ('organize', 'merge', '#e5322d', 'Merge PDF', 'Combine multiple PDFs into one single file.', 'tools/merge-pdf/', True),
    ('organize', 'split', '#1ba94c', 'Split PDF', 'Extract or split pages into separate PDF files.', 'tools/split-pdf/', True),
    ('organize', 'organize', '#e5322d', 'Organize PDF', 'Sort, reorder, rotate, or delete pages visually.', 'tools/organize-pdf/', True),
    ('organize', 'extract', '#1ba94c', 'Extract Pages', 'Extract specific pages or page ranges into a new PDF.', 'tools/extract-pages/', True),
    ('organize', 'trash', '#8a3ee5', 'Delete Pages', 'Remove unwanted pages from a PDF document.', 'tools/delete-pages/', True),

    # Optimize
    ('optimize', 'compress', '#e58a1c', 'Compress PDF', 'Reduce PDF file size while keeping quality.', 'tools/compress-pdf/', True),
    ('optimize', 'crop', '#0aa3a3', 'Crop PDF', 'Trim margins or crop custom areas with interactive box.', 'tools/crop-pdf/', True),
    ('optimize', 'grayscale', '#4b5563', 'Grayscale PDF', 'Convert color PDF to Black & White to save toner/ink.', 'tools/grayscale-pdf/', True),
    ('optimize', 'repair', '#e5322d', 'Repair PDF', 'Recover damaged and corrupted PDF files.', 'tools/repair-pdf/', True),

    # Convert to PDF
    ('convert-to', 'file', '#8a3ee5', 'JPG to PDF', 'Turn your JPG or PNG images into a PDF.', 'tools/jpg-to-pdf/', True),
    ('convert-to', 'html', '#0aa3a3', 'HTML to PDF', 'Convert HTML code, rich text, or web notes into PDF.', 'tools/html-to-pdf/', True),

    # Convert from PDF
    ('convert-from', 'image', '#2b7de9', 'PDF to JPG', 'Convert every PDF page into a high-res JPG image.', 'tools/pdf-to-jpg/', True),
    ('convert-from', 'word', '#2b5ce9', 'PDF to Word', 'Convert your PDF into an editable DOCX document.', 'tools/pdf-to-word/', True),
    ('convert-from', 'txt', '#e58a1c', 'PDF to Text', 'Extract clean plain text from your PDF document.', 'tools/pdf-to-txt/', True),
    ('convert-from', 'extract-img', '#2b7de9', 'Extract Images', 'Extract all embedded photos and graphics to ZIP.', 'tools/extract-images/', True),

    # Edit & Stamp
    ('edit', 'rotate', '#0aa3a3', 'Rotate PDF', 'Rotate one or all pages of your PDF document.', 'tools/rotate-pdf/', True),
    ('edit', 'watermark', '#e5322d', 'Watermark PDF', 'Stamp text or image watermark with cursor positioning.', 'tools/watermark-pdf/', True),
    ('edit', 'number', '#e58a1c', 'Page Numbers', 'Add customized page numbers to your PDF.', 'tools/page-numbers/', True),

    # Security & Sign
    ('security', 'sign', '#8a3ee5', 'Sign PDF', 'Draw, type, or upload your signature to place on any page.', 'tools/sign-pdf/', True),
    ('security', 'lock', '#c81e1e', 'Protect PDF', 'Add password encryption to secure your PDF.', 'tools/protect-pdf/', True),
    ('security', 'unlock', '#1ba94c', 'Unlock PDF', 'Remove password protection and restrictions from PDF.', 'tools/unlock-pdf/', True),
    ('security', 'compare', '#2b5ce9', 'Compare PDF', 'Compare two PDFs side-by-side or with visual diff.', 'tools/compare-pdf/', True),
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
    <a href="{root}index.html" class="brand">Daily1Step<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="{root}index.html">📄 PDF Tools</a>
      <a href="{root}image-tools/index.html" style="color:var(--red); font-weight:700;">🖼️ Image Tools</a>
      <a href="{root}tools/merge-pdf/">Merge PDF</a>
      <a href="{root}image-tools/compress-image-kb/">Compress in KB</a>
      <a href="{root}image-tools/passport-photo-maker/">Passport Photo</a>
      <a href="{root}about.html">About</a>
    </nav>
  </div>
</header>
'''


def footer(root):
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-bottom">Daily1Step &mdash; 100% Free &amp; Private Browser-Based Tools</div>
  </div>
</footer>
<script src="{root}assets/js/main.js"></script>
</body>
</html>
'''


def build_index():
    tab_html = ''
    for cat_key, cat_title, cat_icon in CATEGORIES:
        count = len(TOOLS) if cat_key == 'all' else len([t for t in TOOLS if t[0] == cat_key])
        active = ' active' if cat_key == 'all' else ''
        tab_html += f'''<button type="button" class="category-tab{active}" data-category="{cat_key}">
          <span>{cat_icon}</span>
          <span>{cat_title}</span>
          <span class="tab-count">{count}</span>
        </button>'''

    cards = ''
    for cat, icon, color, title, desc, href, live in TOOLS:
        cls = 'tool-card' if live else 'tool-card disabled'
        badge = '<span class="badge">Coming soon</span>' if not live else ''
        cards += f'''<a class="{cls}" 
         href="{href.replace('tools/', 'tools/').rstrip('/') + '/' if live else '#'}"
         data-category="{cat}"
         data-title="{title.lower()}"
         data-desc="{desc.lower()}">
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
  <div class="tool-controls-wrap">
    <div class="tool-search-box">
      <span class="search-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" id="toolSearchInput" placeholder="Search PDF tools (e.g. merge, sign, compress)..." autocomplete="off">
    </div>

    <div class="category-tabs" id="categoryTabs">
      {tab_html}
    </div>
  </div>

  <div class="tool-grid" id="mainToolGrid">
    {cards}
  </div>

  <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; color:var(--ink-soft);">
    <p style="font-size:1.4rem; font-weight:700; color:var(--ink); margin-bottom:6px;">No tools found</p>
    <p>Try searching for different keywords like "compress", "sign", "word", or "rotate".</p>
  </div>
</section>

<section class="info-section">
  <h2>Why use Daily1Step?</h2>
  <p>Daily1Step runs entirely in your web browser. Unlike most online tools, your files are <strong>never uploaded to a server</strong> &mdash; everything happens on your own device using client-side JavaScript. That means your documents and photos stay 100% private, and the tools work instantly with no waiting for uploads or downloads.</p>
  <ul>
    <li><strong>22 PDF Tools &amp; 20+ Image Tools</strong> &mdash; comprehensive document and photo utility suite.</li>
    <li><strong>100% Free</strong> &mdash; every tool is free to use, with no hidden limits.</li>
    <li><strong>Private &amp; Secure</strong> &mdash; files are processed locally in your browser and never leave your device.</li>
    <li><strong>Fast &amp; Responsive</strong> &mdash; instant client-side execution with real-time drag-and-drop previews.</li>
    <li><strong>Cross-platform</strong> &mdash; works on Windows, Mac, Linux, Android and iOS, in any modern browser.</li>
  </ul>
</section>

<script>
(function() {{
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var noResults = document.getElementById('noResultsMsg');

  var currentCategory = 'all';

  function filterTools() {{
    var query = (searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    toolCards.forEach(function(card) {{
      var cat = card.getAttribute('data-category');
      var title = card.getAttribute('data-title');
      var desc = card.getAttribute('data-desc');

      var matchesCat = (currentCategory === 'all' || cat === currentCategory);
      var matchesQuery = !query || title.includes(query) || desc.includes(query);

      if (matchesCat && matchesQuery) {{
        card.style.display = 'flex';
        visibleCount++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    if (noResults) {{
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }}
  }}

  categoryTabs.forEach(function(tab) {{
    tab.addEventListener('click', function() {{
      categoryTabs.forEach(function(t) {{ t.classList.remove('active'); }});
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      filterTools();
    }});
  }});

  if (searchInput) {{
    searchInput.addEventListener('input', filterTools);
  }}
}})();
</script>
'''
    return header('', 'Daily1Step — Free Online PDF & Image Tools', 'Every tool you need to work with PDFs and Images in one place. 100% client-side and free.') + body + footer('')


def render_tool_php(php_path, root_rel):
    with open(php_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata
    m_title = re.search(r"\$page_title\s*=\s*'([^']*)'", content)
    title = m_title.group(1) if m_title else 'Daily1Step'
    m_desc = re.search(r"\$page_description\s*=\s*'([^']*)'", content)
    desc = m_desc.group(1) if m_desc else ''

    # Remove PHP blocks and include wrappers
    body = content
    body = re.sub(r'<\?php\s*\$root\s*=.*?\?>', '', body, flags=re.DOTALL)
    body = re.sub(r"<\?php\s*include\s+__DIR__\s*\.\s*'/(\.\./)+includes/header\.php';\s*\?>", '', body)
    body = re.sub(r"<\?php\s*include\s+__DIR__\s*\.\s*'/(\.\./)+includes/footer\.php';\s*\?>", '', body)
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

    # Root index (PDF Tools)
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_index())

    # Build PDF tools
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

IMAGE_CATEGORIES = [
    ('all', 'All Image Tools', '🌟'),
    ('compress', 'Compress in KB', '⚡'),
    ('passport', 'Passport & Exam', '🪪'),
    ('resize', 'Resize & Crop', '📐'),
    ('convert', 'Convert Formats', '🔄'),
    ('edit', 'Edit & Effects', '🎨'),
]

IMAGE_TOOLS = [
    # Compress
    ('compress', 'compress-image-kb', 'Compress Image to KB', 'Reduce JPEG, PNG, or WebP file size to exact KB (20KB, 50KB, 100KB, etc.).', '#e5322d', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 12v9"/><path d="m8 17 4 4 4-4"/></svg>'),
    ('compress', 'increase-image-kb', 'Increase Image Size in KB', 'Safely expand image file size in KB to satisfy minimum upload limits for forms.', '#d97706', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 21v-9"/><path d="m8 16 4-4 4 4"/></svg>'),

    # Passport & Exam
    ('passport', 'passport-photo-maker', 'Passport Photo Maker', 'Create 3.5x4.5cm, 35x45mm, 2x2 inch ID photos with white/blue background & printable sheets.', '#2563eb', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c0-2.5 2.2-4 5-4s5 1.5 5 4"/></svg>'),
    ('passport', 'exam-photo-resizer', 'Govt Exam Photo Resizer', 'Instant 1-click photo and signature specs for SSC, UPSC, PAN Card, Railway, and IBPS.', '#7c3aed', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'),
    ('passport', 'add-name-date-photo', 'Add Name & Date on Photo', 'Stamp candidate Name and Date of Photo (DOP) or DOB at the bottom of exam photos.', '#059669', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="15" x2="17" y2="15"/><line x1="7" y1="18" x2="13" y2="18"/></svg>'),
    ('passport', 'merge-photo-signature', 'Merge Photo & Signature', 'Combine applicant portrait photo and signature into a single uploadable image card.', '#0891b2', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="10" rx="2"/><rect x="3" y="15" width="18" height="6" rx="2"/></svg>'),

    # Resize & Crop
    ('resize', 'resize-image-pixels', 'Resize by Pixels', 'Change image dimensions in width and height pixels with aspect ratio preservation.', '#ea580c', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>'),
    ('resize', 'resize-image-cm-mm', 'Resize in CM / MM / Inches', 'Resize photos to exact real-world print dimensions (cm, mm, inch) with custom DPI.', '#0d9488', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><line x1="6" y1="6" x2="6" y2="10"/><line x1="10" y1="6" x2="10" y2="8"/><line x1="14" y1="6" x2="14" y2="10"/><line x1="18" y1="6" x2="18" y2="8"/></svg>'),
    ('resize', 'crop-image', 'Crop Image', 'Crop JPG, PNG, and WebP pictures with interactive circle, square, or custom boxes.', '#0284c7', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>'),
    ('resize', 'instagram-grid-maker', 'Instagram 3x3 Grid Splitter', 'Slice panoramas into 3x3, 3x2, or 3x1 numbered square tiles and download as a ZIP.', '#c026d3', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>'),
    ('resize', 'bulk-image-resizer', 'Bulk Image Resizer', 'Resize dozens of photos simultaneously to max dimensions and download packaged in ZIP.', '#4f46e5', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="8" width="13" height="13" rx="2"/><path d="M4 16V4a2 2 0 0 1 2-2h12"/></svg>'),

    # Convert
    ('convert', 'png-to-jpg', 'PNG to JPG', 'Convert PNG images to JPG with clean white background fill and quality slider.', '#e11d48', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'),
    ('convert', 'jpg-to-png', 'JPG to PNG', 'Convert JPG pictures to lossless PNG format instantly in your browser.', '#9333ea', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>'),
    ('convert', 'webp-to-jpg', 'WEBP to JPG', 'Convert modern WebP images to universal JPG format online.', '#16a34a', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>'),
    ('convert', 'heic-to-jpg', 'HEIC to JPG', 'Convert Apple iPhone .HEIC & .HEIF photos to standard JPG format.', '#475569', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>'),
    ('convert', 'image-to-jpg', 'Image to JPG', 'Convert any image (PNG, WEBP, GIF, SVG, BMP) to high quality JPG format.', '#e5322d', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'),
    ('convert', 'favicon-generator', 'Favicon Generator', 'Generate multi-size web icon packages (16x16, 32x32, 48x48, Apple Touch Icon) from any logo.', '#ca8a04', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>'),
    ('convert', 'image-to-text-ocr', 'Image to Text (OCR)', 'Extract selectable text from photos, documents, and screenshots using neural OCR.', '#2563eb', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg>'),

    # Edit
    ('edit', 'watermark-image', 'Watermark Image', 'Stamp text or logo image on pictures with interactive click & drag positioning.', '#d97706', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>'),
    ('edit', 'rotate-flip-image', 'Rotate & Flip Image', 'Rotate photos 90, 180, 270 or mirror flip horizontally and vertically in 1 click.', '#10b981', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>'),
    ('edit', 'blur-censor-image', 'Blur & Censor Image', 'Hide sensitive data, pixelate faces, or blackout private documents with interactive brush.', '#ef4444', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>'),
    ('edit', 'grayscale-image', 'Grayscale & Black/White', 'Convert full color photos to aesthetic Black & White or Monochrome tone.', '#475569', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>'),
    ('edit', 'add-border-image', 'Add Border to Photo', 'Add stylish white, black, or custom color photo borders with adjustable thickness.', '#6366f1', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10"/></svg>'),
    ('edit', 'join-images', 'Join Multiple Images', 'Stitch and combine multiple photos side-by-side (horizontally) or stacked (vertically).', '#8b5cf6', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="9" height="16" rx="1"/><rect x="13" y="4" width="9" height="16" rx="1"/></svg>'),
    ('edit', 'split-image', 'Split Image into Pieces', 'Slice pictures into custom rows and columns grid and download pieces in a ZIP.', '#ec4899', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><rect x="2" y="2" width="20" height="20" rx="2"/></svg>'),
    ('edit', 'image-color-picker', 'Image Color Picker', 'Click anywhere on your image to sample and copy HEX, RGB, and HSL color codes.', '#f59e0b', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 2 5 5L8 19l-5 1 1-5 11-13Z"/></svg>'),
    ('edit', 'exif-metadata-remover', 'Remove EXIF Metadata', 'Clean GPS coordinates, camera models, dates, and device tags to protect online privacy.', '#10b981', '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>')
]


def build_image_index():
    tab_html = ''
    for cat_key, cat_title, cat_icon in IMAGE_CATEGORIES:
        count = len(IMAGE_TOOLS) if cat_key == 'all' else len([t for t in IMAGE_TOOLS if t[0] == cat_key])
        active = ' active' if cat_key == 'all' else ''
        tab_html += f'''<button type="button" class="category-tab{active}" data-category="{cat_key}">
          <span>{cat_icon}</span>
          <span>{cat_title}</span>
          <span class="tab-count">{count}</span>
        </button>'''

    cards = ''
    for cat, slug, title, desc, color, icon_svg in IMAGE_TOOLS:
        cards += f'''<a class="tool-card" 
         href="{slug}/"
         data-category="{cat}"
         data-title="{title.lower()}"
         data-desc="{desc.lower()}">
        <span class="icon" style="background:{color}">{icon_svg}</span>
        <h3>{htmlmod.escape(title)}</h3>
        <p>{htmlmod.escape(desc)}</p>
      </a>'''

    body = f'''<section class="hero">
  <div class="container">
    <h1>Every Image tool you need, in one place</h1>
    <p>Compress to exact KB, make passport photos, resize in pixels/cm/mm, crop, watermark, and convert images &mdash; 100% free, no signup, and every photo is processed right in your browser.</p>
  </div>
</section>

<section class="container">
  <div class="tool-controls-wrap">
    <div class="tool-search-box">
      <span class="search-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" id="toolSearchInput" placeholder="Search Image tools (e.g. compress, passport, resize)..." autocomplete="off">
    </div>

    <div class="category-tabs" id="categoryTabs">
      {tab_html}
    </div>
  </div>

  <div class="tool-grid" id="mainToolGrid">
    {cards}
  </div>

  <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; color:var(--ink-soft);">
    <p style="font-size:1.4rem; font-weight:700; color:var(--ink); margin-bottom:6px;">No image tools found</p>
    <p>Try searching for "compress", "passport", "resize", "jpg", or "crop".</p>
  </div>
</section>

<section class="info-section">
  <h2>Why use Daily1Step Image Tools?</h2>
  <p>Daily1Step Image Tools runs entirely in your web browser. Your photos are <strong>never uploaded to any server</strong> &mdash; all compression, resizing, and effects happen locally on your computer or phone using GPU-accelerated HTML5 Canvas.</p>
  <ul>
    <li><strong>Exact KB Targets</strong> &mdash; compress photos to exact 20KB, 50KB, 100KB limits required by govt exam portals.</li>
    <li><strong>Official Exam Specs</strong> &mdash; 1-click photo and signature formatting for SSC, UPSC, PAN Card, and Visa applications.</li>
    <li><strong>100% Free &amp; Unlimited</strong> &mdash; no daily limits, no watermarks, no account registration required.</li>
    <li><strong>Safe &amp; Private</strong> &mdash; photos never leave your device.</li>
  </ul>
</section>

<script>
(function() {{
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var noResults = document.getElementById('noResultsMsg');

  var currentCategory = 'all';

  function filterTools() {{
    var query = (searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    toolCards.forEach(function(card) {{
      var cat = card.getAttribute('data-category');
      var title = card.getAttribute('data-title');
      var desc = card.getAttribute('data-desc');

      var matchesCat = (currentCategory === 'all' || cat === currentCategory);
      var matchesQuery = !query || title.includes(query) || desc.includes(query);

      if (matchesCat && matchesQuery) {{
        card.style.display = 'flex';
        visibleCount++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    if (noResults) {{
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }}
  }}

  categoryTabs.forEach(function(tab) {{
    tab.addEventListener('click', function() {{
      categoryTabs.forEach(function(t) {{ t.classList.remove('active'); }});
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      filterTools();
    }});
  }});

  if (searchInput) {{
    searchInput.addEventListener('input', filterTools);
  }}
}})();
</script>
'''
    return header('../', 'Daily1Step Image Tools — Free Online Image Compress, Resize, Passport Photo & Convert', 'Free online image tools suite. Compress to exact KB, make passport photos, resize, crop, and convert.') + body + footer('../')


def build_all():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # Copy static assets & vendor
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    shutil.copytree(os.path.join(ROOT, 'vendor'), os.path.join(OUT, 'vendor'))

    # Root index (PDF Tools)
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_index())

    # Build PDF tools
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

    # Build Image Tools Hub
    out_img_hub = os.path.join(OUT, 'image-tools')
    os.makedirs(out_img_hub, exist_ok=True)
    with open(os.path.join(out_img_hub, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_image_index())

    # Build each Image tool
    image_tools_dir = os.path.join(ROOT, 'image-tools')
    if os.path.exists(image_tools_dir):
        for tname in os.listdir(image_tools_dir):
            tpath = os.path.join(image_tools_dir, tname)
            if os.path.isdir(tpath):
                php_file = os.path.join(tpath, 'index.php')
                if os.path.exists(php_file):
                    out_tool_dir = os.path.join(OUT, 'image-tools', tname)
                    os.makedirs(out_tool_dir, exist_ok=True)
                    html_content = render_tool_php(php_file, '../../')
                    with open(os.path.join(out_tool_dir, 'index.html'), 'w', encoding='utf-8') as f:
                        f.write(html_content)

    # Simple About page
    about_html = header('', 'About Daily1Step', 'About our private browser-based PDF & Image utility suite.') + '''
    <section class="tool-page"><div class="container">
      <h1>About Daily1Step</h1>
      <p>Daily1Step is a 100% client-side PDF and Image utility suite. All operations run directly in your web browser with zero server uploads.</p>
    </div></section>''' + footer('')
    with open(os.path.join(OUT, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(about_html)

    print(f"Preview built at {OUT}")


if __name__ == '__main__':
    build_all()


