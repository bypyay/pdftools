<?php
$root = '';
$page_title = 'Daily1Step PDF — Free Online PDF Tools | 22 Browser-Based PDF Tools';
$page_description = 'Every tool you need to work with PDFs in one place: merge, split, compress, sign, organize, crop, and convert PDF files online, 100% free. Processed entirely in your browser.';
include __DIR__ . '/includes/header.php';

$tools = [
  ['icon' => 'merge', 'color' => '#e5322d', 'title' => 'Merge PDF', 'desc' => 'Combine multiple PDFs into one single file.', 'href' => 'tools/merge-pdf/', 'live' => true],
  ['icon' => 'split', 'color' => '#1ba94c', 'title' => 'Split PDF', 'desc' => 'Extract or split pages into separate PDF files.', 'href' => 'tools/split-pdf/', 'live' => true],
  ['icon' => 'compress', 'color' => '#e58a1c', 'title' => 'Compress PDF', 'desc' => 'Reduce PDF file size while keeping quality.', 'href' => 'tools/compress-pdf/', 'live' => true],
  ['icon' => 'sign', 'color' => '#8a3ee5', 'title' => 'Sign PDF', 'desc' => 'Draw, type, or upload your signature to place on any page.', 'href' => 'tools/sign-pdf/', 'live' => true],
  ['icon' => 'organize', 'color' => '#e5322d', 'title' => 'Organize PDF', 'desc' => 'Sort, reorder, rotate, or delete pages visually.', 'href' => 'tools/organize-pdf/', 'live' => true],
  ['icon' => 'extract', 'color' => '#1ba94c', 'title' => 'Extract Pages', 'desc' => 'Extract specific pages or page ranges into a new PDF.', 'href' => 'tools/extract-pages/', 'live' => true],
  ['icon' => 'crop', 'color' => '#0aa3a3', 'title' => 'Crop PDF', 'desc' => 'Trim margins or crop custom areas with interactive box.', 'href' => 'tools/crop-pdf/', 'live' => true],
  ['icon' => 'watermark', 'color' => '#e5322d', 'title' => 'Watermark PDF', 'desc' => 'Stamp text or image watermark with cursor positioning.', 'href' => 'tools/watermark-pdf/', 'live' => true],
  ['icon' => 'image', 'color' => '#2b7de9', 'title' => 'PDF to JPG', 'desc' => 'Convert every PDF page into a high-res JPG image.', 'href' => 'tools/pdf-to-jpg/', 'live' => true],
  ['icon' => 'file', 'color' => '#8a3ee5', 'title' => 'JPG to PDF', 'desc' => 'Turn your JPG or PNG images into a PDF.', 'href' => 'tools/jpg-to-pdf/', 'live' => true],
  ['icon' => 'word', 'color' => '#2b5ce9', 'title' => 'PDF to Word', 'desc' => 'Convert your PDF into an editable DOCX document.', 'href' => 'tools/pdf-to-word/', 'live' => true],
  ['icon' => 'txt', 'color' => '#e58a1c', 'title' => 'PDF to Text', 'desc' => 'Extract clean plain text from your PDF document.', 'href' => 'tools/pdf-to-txt/', 'live' => true],
  ['icon' => 'extract-img', 'color' => '#2b7de9', 'title' => 'Extract Images', 'desc' => 'Extract all embedded photos and graphics to ZIP.', 'href' => 'tools/extract-images/', 'live' => true],
  ['icon' => 'grayscale', 'color' => '#4b5563', 'title' => 'Grayscale PDF', 'desc' => 'Convert color PDF to Black & White to save toner/ink.', 'href' => 'tools/grayscale-pdf/', 'live' => true],
  ['icon' => 'rotate', 'color' => '#0aa3a3', 'title' => 'Rotate PDF', 'desc' => 'Rotate one or all pages of your PDF document.', 'href' => 'tools/rotate-pdf/', 'live' => true],
  ['icon' => 'trash', 'color' => '#8a3ee5', 'title' => 'Delete Pages', 'desc' => 'Remove unwanted pages from a PDF document.', 'href' => 'tools/delete-pages/', 'live' => true],
  ['icon' => 'number', 'color' => '#e58a1c', 'title' => 'Page Numbers', 'desc' => 'Add customized page numbers to your PDF.', 'href' => 'tools/page-numbers/', 'live' => true],
  ['icon' => 'lock', 'color' => '#c81e1e', 'title' => 'Protect PDF', 'desc' => 'Add password encryption to secure your PDF.', 'href' => 'tools/protect-pdf/', 'live' => true],
  ['icon' => 'unlock', 'color' => '#1ba94c', 'title' => 'Unlock PDF', 'desc' => 'Remove password protection and restrictions from PDF.', 'href' => 'tools/unlock-pdf/', 'live' => true],
  ['icon' => 'repair', 'color' => '#e5322d', 'title' => 'Repair PDF', 'desc' => 'Recover damaged and corrupted PDF files.', 'href' => 'tools/repair-pdf/', 'live' => true],
  ['icon' => 'compare', 'color' => '#2b5ce9', 'title' => 'Compare PDF', 'desc' => 'Compare two PDFs side-by-side or with visual diff.', 'href' => 'tools/compare-pdf/', 'live' => true],
  ['icon' => 'html', 'color' => '#0aa3a3', 'title' => 'HTML to PDF', 'desc' => 'Convert HTML code, rich text, or web notes into PDF.', 'href' => 'tools/html-to-pdf/', 'live' => true],
];
?>
<section class="hero">
  <div class="container">
    <h1>Every PDF tool you need, in one place</h1>
    <p>Merge, split, compress, sign, and convert PDF files — 100% free, no signup, and every file is processed right in your browser.</p>
  </div>
</section>

<section class="container">
  <div class="tool-grid">
    <?php foreach ($tools as $t): ?>
      <a class="tool-card<?php echo $t['live'] ? '' : ' disabled'; ?>" href="<?php echo $t['href']; ?>">
        <?php if (!$t['live']): ?><span class="badge">Coming soon</span><?php endif; ?>
        <span class="icon" style="background:<?php echo $t['color']; ?>"><?php echo icon_svg($t['icon']); ?></span>
        <h3><?php echo htmlspecialchars($t['title']); ?></h3>
        <p><?php echo htmlspecialchars($t['desc']); ?></p>
      </a>
    <?php endforeach; ?>
  </div>
</section>

<section class="info-section">
  <h2>Why use Daily1Step PDF?</h2>
  <p>Daily1Step PDF runs entirely in your web browser. Unlike most online PDF tools, your files are <strong>never uploaded to a server</strong> — everything happens on your own device using client-side JavaScript. That means your documents stay 100% private, and the tools work instantly with no waiting for uploads or downloads.</p>
  <ul>
    <li><strong>22 Complete Tools</strong> — everything from merging, splitting, signing, cropping to repairing.</li>
    <li><strong>100% Free</strong> — every tool is free to use with no hidden watermarks or limits.</li>
    <li><strong>Private &amp; Secure</strong> — files are processed locally in your browser and never leave your device.</li>
    <li><strong>Fast &amp; Responsive</strong> — instant client-side execution with real-time drag-and-drop previews.</li>
    <li><strong>Cross-Platform</strong> — works on Windows, Mac, Linux, Android, and iPhone in any modern browser.</li>
  </ul>
</section>
<?php
include __DIR__ . '/includes/footer.php';

function icon_svg($name) {
  $icons = [
    'merge' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3v6a2 2 0 0 0 2 2h6"/><path d="M17 21v-6a2 2 0 0 0-2-2H9"/></svg>',
    'split' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3"/><path d="M21 8V5a2 2 0 0 0-2-2h-3"/><path d="M3 16v3a2 2 0 0 0 2 2h3"/><path d="M16 21h3a2 2 0 0 0 2-2v-3"/></svg>',
    'compress' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3v3a2 2 0 0 1-2 2H3"/><path d="M21 8h-3a2 2 0 0 1-2-2V3"/><path d="M3 16h3a2 2 0 0 1 2 2v3"/><path d="M16 21v-3a2 2 0 0 1 2-2h3"/></svg>',
    'image' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>',
    'file' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>',
    'rotate' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2v6h-6"/><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M3 22v-6h6"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/></svg>',
    'lock' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    'unlock' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>',
    'watermark' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M9 15l6-6M9 9l6 6"/></svg>',
    'word' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M8 13l1.5 5L11 14l1.5 4L14 13"/></svg>',
    'number' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><text x="8" y="18" font-size="8" fill="#fff" stroke="none">12</text></svg>',
    'trash' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>',
    'organize' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    'extract' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    'crop' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.13 1L6 16a2 2 0 0 0 2 2h15"/><path d="M1 6.13L16 6a2 2 0 0 1 2 2v15"/></svg>',
    'sign' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/></svg>',
    'grayscale' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>',
    'extract-img' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
    'txt' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>',
    'repair' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    'compare' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="8" height="18" rx="2"/><rect x="14" y="3" width="8" height="18" rx="2"/><line x1="10" y1="8" x2="14" y2="8"/><line x1="10" y1="16" x2="14" y2="16"/></svg>',
    'html' => '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
  ];
  return $icons[$name] ?? '';
}
?>
