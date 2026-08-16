<?php
$root = '../../';
$page_title = 'JPG to PDF Online Free — Convert Images to PDF | Daily1Step PDF';
$page_description = 'Combine JPG or PNG images into a single PDF file, free and online. Reorder images before converting. Processed entirely in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>JPG to PDF</h1>
      <p>Combine your images into a single PDF, in the order you choose.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/jpeg,image/png" multiple>
      <p><strong>Click to select images</strong> or drag and drop them here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">JPG or PNG, multiple files supported</p>
    </div>

    <div class="thumb-grid" id="thumbGrid" style="display:none;"></div>
    <p class="thumb-hint" id="thumbHint" style="display:none;">Drag the images to reorder them before converting.</p>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="convertBtn">Convert to PDF</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Converting...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="images.pdf">Download images.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Convert more images</button></div>
    </div>

    <div class="continue-box" id="continueBox" style="display:none;">
      <p class="continue-title">Continue to&hellip;</p>
      <div class="continue-grid" id="continueGrid"></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your files never leave your device — everything is processed locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/jpg-to-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
