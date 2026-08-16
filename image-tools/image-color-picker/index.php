<?php
$root = '../../';
$page_title = 'Image Color Picker Online Free — Extract Hex & RGB from Photos | Daily1Step';
$page_description = 'Pick exact colors and hex/RGB color codes from any image with an interactive eye-dropper cursor. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Image Color Picker</h1>
      <p>Hover and click anywhere on your image to instantly extract and copy HEX, RGB, and HSL color codes.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 300px; gap:24px; align-items:start;" class="color-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <h4 style="margin:0 0 12px; font-size:.95rem; color:var(--ink);">Click on image to sample color</h4>
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#fff;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:450px; display:block; cursor:crosshair;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:16px;">
          <div style="width:100%; height:80px; border-radius:10px; border:1.5px solid var(--border); box-shadow:var(--shadow-sm);" id="colorSwatch"></div>
          
          <div>
            <label style="display:block; font-weight:700; font-size:.82rem; color:var(--ink-soft); margin-bottom:4px;">HEX CODE</label>
            <div style="display:flex; gap:6px;">
              <input type="text" id="hexVal" readonly style="flex:1; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:700; font-family:monospace; font-size:1.1rem; color:var(--red);">
              <button type="button" class="btn secondary" id="copyHexBtn" style="padding:8px 14px;">Copy</button>
            </div>
          </div>

          <div>
            <label style="display:block; font-weight:700; font-size:.82rem; color:var(--ink-soft); margin-bottom:4px;">RGB CODE</label>
            <div style="display:flex; gap:6px;">
              <input type="text" id="rgbVal" readonly style="flex:1; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:700; font-family:monospace;">
              <button type="button" class="btn secondary" id="copyRgbBtn" style="padding:8px 14px;">Copy</button>
            </div>
          </div>
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
  .color-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/image-color-picker.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
