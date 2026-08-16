<?php
$root = '../../';
$page_title = 'Resize Image Pixel Online Free — Resize JPG, PNG, WEBP in Pixels | Daily1Step';
$page_description = 'Resize image dimensions by width and height in pixels online. Maintain aspect ratio or set custom width and height. 100% free and client-side.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Resize Image by Pixels</h1>
      <p>Change image resolution and dimensions by width and height in pixels with aspect ratio preservation.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Supports JPG, PNG, WEBP, GIF</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px;">
        <div class="file-row" style="margin-bottom:16px;">
          <span class="name" id="fileName"></span>
          <span class="size" id="fileOriginalDims"></span>
          <button class="remove" id="removeFile" title="Remove">&times;</button>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Width (Pixels)</label>
            <input type="number" id="widthInput" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Height (Pixels)</label>
            <input type="number" id="heightInput" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
        </div>

        <div style="display:flex; align-items:center; gap:8px; margin-bottom:16px;">
          <input type="checkbox" id="lockAspect" checked style="width:18px; height:18px; accent-color:var(--red);">
          <label for="lockAspect" style="font-weight:600; font-size:.88rem; color:var(--ink); cursor:pointer;">Maintain Aspect Ratio</label>
        </div>

        <div style="display:flex; gap:8px; margin-bottom:20px; flex-wrap:wrap;">
          <button type="button" class="preset-chip" data-scale="0.25">25%</button>
          <button type="button" class="preset-chip" data-scale="0.50">50%</button>
          <button type="button" class="preset-chip" data-scale="0.75">75%</button>
          <button type="button" class="preset-chip" data-scale="1.50">150%</button>
          <button type="button" class="preset-chip" data-scale="2.00">200%</button>
        </div>

        <div style="display:flex; justify-content:center; margin-bottom:20px;">
          <img id="imgPreview" style="max-width:280px; max-height:200px; border-radius:8px; border:1.5px solid var(--border); background:#fff; object-fit:contain;">
        </div>

        <button class="btn" id="resizeBtn" style="width:100%;">Resize Image Now</button>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Image Resized Successfully!</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="resized.jpg">Download Resized Image</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Resize another image</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
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
.preset-chip:hover {
  background: var(--red-light);
  border-color: var(--red);
  color: var(--red);
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/resize-image-pixels.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
