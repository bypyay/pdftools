<?php
$root = '../../';
$page_title = 'Split Image Online Free — Cut Image into Rows & Columns | Daily1Step';
$page_description = 'Cut and split any picture into custom rows and columns. Download all sliced parts in a ZIP archive. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Split Image into Pieces</h1>
      <p>Slice pictures into custom rows and columns grid and download pieces packaged in a ZIP archive.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image to split</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:880px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <div style="display:flex; justify-content:center; gap:16px; margin-bottom:18px;">
          <div>
            <label style="font-weight:700; font-size:.85rem; color:var(--ink);">Columns:</label>
            <input type="number" id="splitCols" value="2" min="1" max="10" style="width:70px; padding:6px; border:1.5px solid var(--border); border-radius:6px; font-weight:700;">
          </div>
          <div>
            <label style="font-weight:700; font-size:.85rem; color:var(--ink);">Rows:</label>
            <input type="number" id="splitRows" value="2" min="1" max="10" style="width:70px; padding:6px; border:1.5px solid var(--border); border-radius:6px; font-weight:700;">
          </div>
        </div>

        <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b; box-shadow:var(--shadow-sm);">
          <canvas id="previewCanvas" style="max-width:100%; max-height:400px; display:block;"></canvas>
        </div>

        <div style="margin-top:20px;">
          <button class="btn" id="downloadZipBtn">Download Sliced Pieces (.ZIP)</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/jszip.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/split-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
