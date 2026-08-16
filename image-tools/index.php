<?php
$root = '../';
$page_title = 'Daily1Step Image Tools — Free Online Image Compress, Resize, Passport Photo & Convert';
$page_description = 'Compress image to exact KB, create passport photos, resize in pixels/cm/mm, crop, watermark, convert PNG/JPG/HEIC/WebP. 100% free and client-side in browser.';
include __DIR__ . '/../includes/header.php';

$image_tools = [
  // 1. Compress
  [
    'slug' => 'compress-image-kb',
    'name' => 'Compress Image to KB',
    'desc' => 'Reduce JPEG, PNG, or WebP file size to exact KB (20KB, 50KB, 100KB, 200KB, etc.).',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 12v9"/><path d="m8 17 4 4 4-4"/></svg>',
    'color' => '#e5322d',
    'category' => 'compress'
  ],
  [
    'slug' => 'increase-image-kb',
    'name' => 'Increase Image Size in KB',
    'desc' => 'Safely expand image file size in KB to satisfy minimum upload limits for application forms.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 21v-9"/><path d="m8 16 4-4 4 4"/></svg>',
    'color' => '#d97706',
    'category' => 'compress'
  ],

  // 2. Passport & Exam
  [
    'slug' => 'passport-photo-maker',
    'name' => 'Passport Photo Maker',
    'desc' => 'Create 3.5×4.5cm, 35×45mm, 2×2 inch ID photos with white/blue background & printable sheets.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c0-2.5 2.2-4 5-4s5 1.5 5 4"/></svg>',
    'color' => '#2563eb',
    'category' => 'passport'
  ],
  [
    'slug' => 'exam-photo-resizer',
    'name' => 'Govt Exam Photo Resizer',
    'desc' => 'Instant 1-click photo and signature specs for SSC, UPSC, PAN Card, Railway, and IBPS.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
    'color' => '#7c3aed',
    'category' => 'passport'
  ],
  [
    'slug' => 'add-name-date-photo',
    'name' => 'Add Name & Date on Photo',
    'desc' => 'Stamp candidate Name and Date of Photo (DOP) or DOB at the bottom of exam photos.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="15" x2="17" y2="15"/><line x1="7" y1="18" x2="13" y2="18"/></svg>',
    'color' => '#059669',
    'category' => 'passport'
  ],
  [
    'slug' => 'merge-photo-signature',
    'name' => 'Merge Photo & Signature',
    'desc' => 'Combine applicant portrait photo and signature into a single uploadable image card.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="10" rx="2"/><rect x="3" y="15" width="18" height="6" rx="2"/></svg>',
    'color' => '#0891b2',
    'category' => 'passport'
  ],

  // 3. Resize & Crop
  [
    'slug' => 'resize-image-pixels',
    'name' => 'Resize by Pixels',
    'desc' => 'Change image dimensions in width and height pixels with aspect ratio preservation.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>',
    'color' => '#ea580c',
    'category' => 'resize'
  ],
  [
    'slug' => 'resize-image-cm-mm',
    'name' => 'Resize in CM / MM / Inches',
    'desc' => 'Resize photos to exact real-world print dimensions (cm, mm, inch) with custom DPI.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><line x1="6" y1="6" x2="6" y2="10"/><line x1="10" y1="6" x2="10" y2="8"/><line x1="14" y1="6" x2="14" y2="10"/><line x1="18" y1="6" x2="18" y2="8"/></svg>',
    'color' => '#0d9488',
    'category' => 'resize'
  ],
  [
    'slug' => 'crop-image',
    'name' => 'Crop Image',
    'desc' => 'Crop JPG, PNG, and WebP pictures with interactive circle, square, or custom boxes.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>',
    'color' => '#0284c7',
    'category' => 'resize'
  ],
  [
    'slug' => 'instagram-grid-maker',
    'name' => 'Instagram 3×3 Grid Splitter',
    'desc' => 'Slice panoramas into 3×3, 3×2, or 3×1 numbered square tiles and download as a ZIP.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>',
    'color' => '#c026d3',
    'category' => 'resize'
  ],
  [
    'slug' => 'bulk-image-resizer',
    'name' => 'Bulk Image Resizer',
    'desc' => 'Resize dozens of photos simultaneously to max dimensions and download packaged in ZIP.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="8" width="13" height="13" rx="2"/><path d="M4 16V4a2 2 0 0 1 2-2h12"/></svg>',
    'color' => '#4f46e5',
    'category' => 'resize'
  ],

  // 4. Convert
  [
    'slug' => 'png-to-jpg',
    'name' => 'PNG to JPG',
    'desc' => 'Convert PNG images to JPG with clean white background fill and quality slider.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
    'color' => '#e11d48',
    'category' => 'convert'
  ],
  [
    'slug' => 'jpg-to-png',
    'name' => 'JPG to PNG',
    'desc' => 'Convert JPG pictures to lossless PNG format instantly in your browser.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    'color' => '#9333ea',
    'category' => 'convert'
  ],
  [
    'slug' => 'webp-to-jpg',
    'name' => 'WEBP to JPG',
    'desc' => 'Convert modern WebP images to universal JPG format online.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>',
    'color' => '#16a34a',
    'category' => 'convert'
  ],
  [
    'slug' => 'heic-to-jpg',
    'name' => 'HEIC to JPG',
    'desc' => 'Convert Apple iPhone .HEIC & .HEIF photos to standard JPG format.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
    'color' => '#475569',
    'category' => 'convert'
  ],
  [
    'slug' => 'image-to-jpg',
    'name' => 'Image to JPG',
    'desc' => 'Convert any image (PNG, WEBP, GIF, SVG, BMP) to high quality JPG format.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    'color' => '#e5322d',
    'category' => 'convert'
  ],
  [
    'slug' => 'favicon-generator',
    'name' => 'Favicon Generator',
    'desc' => 'Generate multi-size web icon packages (16×16, 32×32, 48×48, Apple Touch Icon) from any logo.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>',
    'color' => '#ca8a04',
    'category' => 'convert'
  ],
  [
    'slug' => 'image-to-text-ocr',
    'name' => 'Image to Text (OCR)',
    'desc' => 'Extract selectable text from photos, documents, and screenshots using neural OCR.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg>',
    'color' => '#2563eb',
    'category' => 'convert'
  ],

  // 5. Edit & Effects
  [
    'slug' => 'watermark-image',
    'name' => 'Watermark Image',
    'desc' => 'Stamp text or logo image on pictures with interactive click & drag positioning.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>',
    'color' => '#d97706',
    'category' => 'edit'
  ],
  [
    'slug' => 'rotate-flip-image',
    'name' => 'Rotate & Flip Image',
    'desc' => 'Rotate photos 90°, 180°, 270° or mirror flip horizontally and vertically in 1 click.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>',
    'color' => '#10b981',
    'category' => 'edit'
  ],
  [
    'slug' => 'blur-censor-image',
    'name' => 'Blur & Censor Image',
    'desc' => 'Hide sensitive data, pixelate faces, or blackout private documents with interactive brush.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>',
    'color' => '#ef4444',
    'category' => 'edit'
  ],
  [
    'slug' => 'grayscale-image',
    'name' => 'Grayscale & Black/White',
    'desc' => 'Convert full color photos to aesthetic Black & White or Monochrome tone.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>',
    'color' => '#475569',
    'category' => 'edit'
  ],
  [
    'slug' => 'add-border-image',
    'name' => 'Add Border to Photo',
    'desc' => 'Add stylish white, black, or custom color photo borders with adjustable thickness.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10"/></svg>',
    'color' => '#6366f1',
    'category' => 'edit'
  ],
  [
    'slug' => 'join-images',
    'name' => 'Join Multiple Images',
    'desc' => 'Stitch and combine multiple photos side-by-side (horizontally) or stacked (vertically).',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="9" height="16" rx="1"/><rect x="13" y="4" width="9" height="16" rx="1"/></svg>',
    'color' => '#8b5cf6',
    'category' => 'edit'
  ],
  [
    'slug' => 'split-image',
    'name' => 'Split Image into Pieces',
    'desc' => 'Slice pictures into custom rows and columns grid and download pieces in a ZIP.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><rect x="2" y="2" width="20" height="20" rx="2"/></svg>',
    'color' => '#ec4899',
    'category' => 'edit'
  ],
  [
    'slug' => 'image-color-picker',
    'name' => 'Image Color Picker',
    'desc' => 'Click anywhere on your image to sample and copy HEX, RGB, and HSL color codes.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 2 5 5L8 19l-5 1 1-5 11-13Z"/></svg>',
    'color' => '#f59e0b',
    'category' => 'edit'
  ],
  [
    'slug' => 'exif-metadata-remover',
    'name' => 'Remove EXIF Metadata',
    'desc' => 'Clean GPS coordinates, camera models, dates, and device tags to protect online privacy.',
    'icon' => '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    'color' => '#10b981',
    'category' => 'edit'
  ]
];

$categories = [
  'all' => ['name' => 'All Image Tools', 'icon' => '🌟', 'count' => count($image_tools)],
  'compress' => ['name' => 'Compress in KB', 'icon' => '⚡', 'count' => 2],
  'passport' => ['name' => 'Passport & Exam', 'icon' => '🪪', 'count' => 4],
  'resize' => ['name' => 'Resize & Crop', 'icon' => '📐', 'count' => 5],
  'convert' => ['name' => 'Convert Formats', 'icon' => '🔄', 'count' => 7],
  'edit' => ['name' => 'Edit & Effects', 'icon' => '🎨', 'count' => 8]
];
?>

<section class="hero">
  <div class="container">
    <h1>Every Image tool you need, in one place</h1>
    <p>Compress to exact KB, make passport photos, resize in pixels/cm/mm, crop, watermark, and convert images — 100% free, no signup, and every photo is processed right in your browser.</p>
  </div>
</section>

<section class="tools-section">
  <div class="container">
    <div class="tool-controls-wrap">
      <div class="tool-search-box">
        <span class="search-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </span>
        <input type="text" id="toolSearchInput" placeholder="Search Image tools (e.g. compress, passport, resize)..." autocomplete="off">
      </div>

      <div class="category-tabs" id="categoryTabs">
        <?php foreach ($categories as $cat_key => $cat_info): ?>
          <button class="category-tab <?php echo $cat_key === 'all' ? 'active' : ''; ?>" data-category="<?php echo $cat_key; ?>">
            <span><?php echo $cat_info['icon']; ?> <?php echo $cat_info['name']; ?></span>
            <span class="tab-count"><?php echo $cat_info['count']; ?></span>
          </button>
        <?php endforeach; ?>
      </div>
    </div>

    <div class="tool-grid" id="toolsGrid">
      <?php foreach ($image_tools as $t): ?>
        <a href="<?php echo $t['slug']; ?>/" class="tool-card" data-category="<?php echo $t['category']; ?>" data-name="<?php echo htmlspecialchars(strtolower($t['name'])); ?>" data-desc="<?php echo htmlspecialchars(strtolower($t['desc'])); ?>">
          <div class="icon" style="background: <?php echo $t['color']; ?>;"><?php echo $t['icon']; ?></div>
          <h3><?php echo $t['name']; ?></h3>
          <p><?php echo $t['desc']; ?></p>
        </a>
      <?php endforeach; ?>
    </div>
  </div>
</section>

<script>
(function() {
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var activeCategory = 'all';

  function filterTools() {
    var query = (searchInput.value || '').trim().toLowerCase();

    toolCards.forEach(function(card) {
      var cat = card.getAttribute('data-category');
      var name = card.getAttribute('data-name');
      var desc = card.getAttribute('data-desc');

      var matchesCategory = (activeCategory === 'all' || cat === activeCategory);
      var matchesSearch = (!query || name.indexOf(query) !== -1 || desc.indexOf(query) !== -1);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  searchInput.addEventListener('input', filterTools);

  categoryTabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      categoryTabs.forEach(function(t) { t.classList.remove('active'); });
      tab.classList.add('active');
      activeCategory = tab.getAttribute('data-category');
      filterTools();
    });
  });
})();
</script>

<?php include __DIR__ . '/../includes/footer.php'; ?>
