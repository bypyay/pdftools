<?php
$root = '';
$page_title = 'Daily1Step PDF — Free Online PDF Tools | Merge, Split, Compress PDF';
$page_description = 'Every tool you need to work with PDFs in one place: merge, split, compress, and convert PDF files online, free. 100% browser-based — your files never leave your device.';
include __DIR__ . '/includes/header.php';

$tools = [
  ['icon' => 'merge', 'color' => '#e5322d', 'title' => 'Merge PDF', 'desc' => 'Combine multiple PDFs into one single file.', 'href' => 'tools/merge-pdf/', 'live' => true],
  ['icon' => 'split', 'color' => '#1ba94c', 'title' => 'Split PDF', 'desc' => 'Extract or split pages into separate PDF files.', 'href' => 'tools/split-pdf/', 'live' => true],
  ['icon' => 'compress', 'color' => '#e58a1c', 'title' => 'Compress PDF', 'desc' => 'Reduce PDF file size while keeping quality.', 'href' => 'tools/compress-pdf/', 'live' => true],
  ['icon' => 'image', 'color' => '#2b7de9', 'title' => 'PDF to JPG', 'desc' => 'Convert every PDF page into a JPG image.', 'href' => 'tools/pdf-to-jpg/', 'live' => true],
  ['icon' => 'file', 'color' => '#8a3ee5', 'title' => 'JPG to PDF', 'desc' => 'Turn your JPG or PNG images into a PDF.', 'href' => 'tools/jpg-to-pdf/', 'live' => true],
  ['icon' => 'rotate', 'color' => '#0aa3a3', 'title' => 'Rotate PDF', 'desc' => 'Rotate one or all pages of your PDF.', 'href' => 'tools/rotate-pdf/', 'live' => true],
  ['icon' => 'trash', 'color' => '#8a3ee5', 'title' => 'Delete Pages', 'desc' => 'Remove unwanted pages from a PDF.', 'href' => 'tools/delete-pages/', 'live' => true],
  ['icon' => 'watermark', 'color' => '#e5322d', 'title' => 'Watermark PDF', 'desc' => 'Stamp text across every page of a PDF.', 'href' => 'tools/watermark-pdf/', 'live' => true],
  ['icon' => 'number', 'color' => '#e58a1c', 'title' => 'Page Numbers', 'desc' => 'Add page numbers to your PDF.', 'href' => 'tools/page-numbers/', 'live' => true],
  ['icon' => 'unlock', 'color' => '#1ba94c', 'title' => 'Unlock PDF', 'desc' => 'Remove password protection from a PDF.', 'href' => 'tools/unlock-pdf/', 'live' => true],
  ['icon' => 'word', 'color' => '#2b5ce9', 'title' => 'PDF to Word', 'desc' => 'Convert your PDF into an editable DOCX.', 'href' => 'tools/pdf-to-word/', 'live' => true],
  ['icon' => 'lock', 'color' => '#c81e1e', 'title' => 'Protect PDF', 'desc' => 'Add a password to secure your PDF.', 'href' => '#', 'live' => false],
];
?>
<section class="hero">
  <div class="container">
    <h1>Every PDF tool you need, in one place</h1>
    <p>Merge, split, compress and convert PDF files — 100% free, no signup, and every file is processed right in your browser.</p>
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
  <p>Daily1Step PDF runs entirely in your web browser. Unlike most online PDF tools, your files are <strong>never uploaded to a server</strong> — everything happens on your own device using JavaScript. That means your documents stay private, and the tools work instantly with no waiting for uploads or downloads.</p>
  <ul>
    <li><strong>Free</strong> — every tool is free to use, with no hidden limits.</li>
    <li><strong>Private</strong> — files are processed locally in your browser and never leave your device.</li>
    <li><strong>Fast</strong> — no upload/download round-trip to a server.</li>
    <li><strong>Cross-platform</strong> — works on Windows, Mac, Linux, Android and iOS, in any modern browser.</li>
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
  ];
  return $icons[$name] ?? '';
}
