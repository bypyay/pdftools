<?php
$root = '../../';
$page_title = 'HEIC to JPG Converter Online Free — Convert Apple iPhone Photos | Daily1Step';
$page_description = 'Convert Apple iPhone and iPad HEIC / HEIF photos to high quality JPG images online for free. 100% private and runs locally in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>HEIC to JPG Converter</h1>
      <p>Convert Apple iPhone HEIC & HEIF photos to standard JPG format without uploading files to any server.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept=".heic, .heif, image/heic, image/heif">
      <p><strong>Click to select HEIC photo</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Supports Apple .HEIC & .HEIF files</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="fileSize"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div class="actions" id="actions" style="margin-top:20px;">
        <button class="btn" id="convertBtn">Convert HEIC to JPG</button>
      </div>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Converting HEIC image streams...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>HEIC Converted to JPG Successfully!</h3>
      <div style="display:flex; justify-content:center; margin:16px 0;">
        <img id="convertedPreview" style="max-width:300px; max-height:240px; border-radius:8px; border:1.5px solid var(--border); box-shadow:var(--shadow);">
      </div>
      <a class="btn" id="downloadLink" download="converted.jpg">Download JPG Image</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Convert another HEIC photo</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — converted 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/heic2any.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/heic-to-jpg.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
