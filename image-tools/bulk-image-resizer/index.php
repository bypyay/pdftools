<?php
$root = '../../';
$page_title = 'Bulk Image Resizer Online Free — Resize Multiple Photos to ZIP | Daily1Step';
$page_description = 'Resize multiple JPG, PNG, and WebP images at once in bulk and download all as a ZIP file. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Bulk Image Resizer</h1>
      <p>Resize dozens of photos simultaneously to fixed pixel dimensions or percentage and download as a ZIP.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*" multiple>
      <p><strong>Click to select multiple images</strong> or drag and drop them here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px;">
        <h4 style="margin:0 0 14px; font-size:.95rem; color:var(--ink);" id="fileCountText"></h4>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:18px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Target Max Width (px)</label>
            <input type="number" id="targetWidth" value="1200" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Target Max Height (px)</label>
            <input type="number" id="targetHeight" value="1200" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
        </div>

        <button class="btn" id="bulkProcessBtn" style="width:100%;">Resize All & Download ZIP</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/jszip.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/bulk-image-resizer.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
