<?php
$root = '../../';
$page_title = 'Watermark Image Online Free — Add Text & Logo to Photos | Daily1Step';
$page_description = 'Add text watermark or logo image to your pictures online. Click and drag watermark with cursor. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Watermark Image</h1>
      <p>Stamp text or your brand logo on pictures with interactive click & drag positioning.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 340px; gap:24px; align-items:start;" class="watermark-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <h4 style="margin:0 0 12px; font-size:.95rem; color:var(--ink);">Click & Drag Watermark on Preview</h4>
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block; cursor:move;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:14px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Watermark Text</label>
            <input type="text" id="wmText" value="CONFIDENTIAL" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Text Color</label>
            <input type="color" id="wmColor" value="#ffffff" style="width:100%; height:40px; border:1.5px solid var(--border); border-radius:8px; cursor:pointer;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Opacity</label>
            <input type="range" id="wmOpacity" min="10" max="100" value="50" style="width:100%;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Font Size</label>
            <input type="range" id="wmSize" min="16" max="100" value="42" style="width:100%;">
          </div>
          <button class="btn" id="downloadBtn" style="margin-top:8px;">Download Watermarked Image</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
@media (max-width: 768px) {
  .watermark-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/watermark-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
