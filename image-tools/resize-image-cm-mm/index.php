<?php
$root = '../../';
$page_title = 'Resize Image in CM / MM / Inches Online Free | Daily1Step';
$page_description = 'Resize photos to exact dimensions in Centimeters, Millimeters, or Inches with custom DPI (200, 300, 600 DPI) for official documents. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Resize Image in CM / MM / Inches</h1>
      <p>Convert real-world print dimensions (cm, mm, inch) to exact pixel dimensions with DPI precision.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px;">
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:16px;" class="dim-grid">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Unit</label>
            <select id="unitSelect" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
              <option value="cm">Centimeter (cm)</option>
              <option value="mm">Millimeter (mm)</option>
              <option value="inch">Inches (in)</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Width</label>
            <input type="number" step="0.1" id="widthInput" value="3.5" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Height</label>
            <input type="number" step="0.1" id="heightInput" value="4.5" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
        </div>

        <div style="margin-bottom:18px;">
          <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Resolution (DPI)</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="dpi-btn" data-dpi="150">150 DPI</button>
            <button type="button" class="dpi-btn active" data-dpi="300">300 DPI (Standard)</button>
            <button type="button" class="dpi-btn" data-dpi="600">600 DPI (High Res)</button>
          </div>
        </div>

        <button class="btn" id="resizeBtn" style="width:100%;">Resize & Download</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
.dpi-btn {
  background: var(--bg);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 8px 14px;
  font-weight: 700;
  font-size: .85rem;
  color: var(--ink-soft);
  cursor: pointer;
  flex: 1;
}
.dpi-btn.active {
  background: var(--red-light);
  border-color: var(--red);
  color: var(--red);
}
@media (max-width: 600px) {
  .dim-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/resize-image-cm-mm.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
