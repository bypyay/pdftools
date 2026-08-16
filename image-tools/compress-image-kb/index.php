<?php
$root = '../../';
$page_title = 'Compress Image to Specific KB Online Free — Reduce Image Size in KB | Daily1Step';
$page_description = 'Reduce image size to exact KB (20KB, 50KB, 100KB, 200KB, etc.) online for free. Perfect for government exam forms, passport applications, and websites. 100% browser-based.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Compress Image to Exact KB</h1>
      <p>Reduce JPEG, PNG, or WebP file size to your exact target KB with intelligent quality optimization.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/jpeg, image/png, image/webp">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Supports JPG, PNG, WEBP</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="fileOriginalSize"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="margin-top:24px; padding:22px; background:var(--bg-soft); border-radius:14px; border:1.5px solid var(--border);">
        <label style="display:block; font-weight:700; font-size:.95rem; margin-bottom:8px; color:var(--ink);">Target File Size</label>
        
        <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin-bottom:14px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <input type="number" id="targetKbInput" value="50" min="5" max="5000" style="width:110px; padding:10px 14px; border:1.5px solid var(--border); border-radius:8px; font-weight:700; font-size:1.1rem; color:var(--red);">
            <span style="font-weight:700; font-size:1rem; color:var(--ink);">KB</span>
          </div>

          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <button type="button" class="preset-chip" data-kb="10">10 KB</button>
            <button type="button" class="preset-chip" data-kb="20">20 KB</button>
            <button type="button" class="preset-chip active" data-kb="50">50 KB</button>
            <button type="button" class="preset-chip" data-kb="100">100 KB</button>
            <button type="button" class="preset-chip" data-kb="200">200 KB</button>
            <button type="button" class="preset-chip" data-kb="500">500 KB</button>
          </div>
        </div>

        <div style="display:flex; justify-content:center; margin-top:16px;">
          <div id="imagePreviewBox" style="max-width:320px; max-height:260px; border-radius:8px; overflow:hidden; border:1.5px solid var(--border); background:#fff; display:flex; align-items:center; justify-content:center;">
            <img id="imgPreview" style="max-width:100%; max-height:240px; object-fit:contain;">
          </div>
        </div>
      </div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="compressBtn">Compress Image</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Optimizing image size...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Image Compressed Successfully!</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="compressed.jpg">Download Compressed Image</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Compress another image</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — compressed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
.preset-chip {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 5px 12px;
  font-size: .8rem;
  font-weight: 600;
  color: var(--ink-soft);
  cursor: pointer;
  transition: all .15s;
}
.preset-chip:hover, .preset-chip.active {
  background: var(--red-light);
  border-color: var(--red);
  color: var(--red);
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/compress-image-kb.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
