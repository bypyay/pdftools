<?php
$root = '../../';
$page_title = 'Add Border to Photo Online Free — White & Custom Color Borders | Daily1Step';
$page_description = 'Add white, black, or custom colored borders and frames to photos for Instagram and profile avatars. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Add Border to Photo</h1>
      <p>Add stylish white, black, or custom color photo borders with adjustable thickness.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:880px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 300px; gap:20px; align-items:start;" class="border-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:16px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Border Color</label>
            <input type="color" id="borderColor" value="#ffffff" style="width:100%; height:40px; border:1.5px solid var(--border); border-radius:8px; cursor:pointer;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Border Thickness (% of photo)</label>
            <input type="range" id="borderThickness" min="2" max="25" value="6" style="width:100%;">
          </div>
          <button class="btn" id="downloadBtn" style="margin-top:8px;">Download Photo with Border</button>
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
  .border-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/add-border-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
