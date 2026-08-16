<?php
$root = '../../';
$page_title = 'Image to JPG Converter Online Free | Daily1Step';
$page_description = 'Convert any image (PNG, WEBP, GIF, SVG, BMP) to high quality JPG format. 100% free and private.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Image to JPG Converter</h1>
      <p>Convert any image (PNG, WEBP, GIF, SVG, BMP) to high quality JPG format.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Fast and 100% private in browser</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="fileSize"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="display:flex; justify-content:center; margin:20px 0;">
        <img id="imgPreview" style="max-width:300px; max-height:240px; border-radius:8px; border:1.5px solid var(--border); background:#fff; object-fit:contain;">
      </div>

      <div class="actions" id="actions">
        <button class="btn" id="convertBtn">Convert Image</button>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Image Processed Successfully!</h3>
      <div style="display:flex; justify-content:center; margin:16px 0;">
        <img id="finalImg" style="max-width:300px; max-height:240px; border-radius:8px; border:1.5px solid var(--border); box-shadow:var(--shadow);">
      </div>
      <a class="btn" id="downloadLink" download="converted.jpg">Download JPG Image</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Process another image</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/image-to-jpg.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
