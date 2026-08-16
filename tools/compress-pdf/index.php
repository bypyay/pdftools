<?php
$root = '../../';
$page_title = 'Compress PDF Online Free — Reduce PDF File Size | Daily1Step PDF';
$page_description = 'Reduce the file size of your PDF online, free. Choose a compression level and download a smaller PDF. Processed entirely in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Compress PDF</h1>
      <p>Shrink your PDF file size. Best results on scanned or image-heavy PDFs.</p>
    </div>

    <div class="handoff-banner" id="handoffBanner">
      <span>&#10003;</span> <span id="handoffBannerText"></span>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="application/pdf">
      <p><strong>Click to select a PDF file</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">One file at a time</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:720px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="fileSize"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="margin-top:20px;">
        <label style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <input type="radio" name="level" value="low"> Low compression — best quality, smaller size reduction
        </label>
        <label style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <input type="radio" name="level" value="recommended" checked> Recommended compression — good quality, good size reduction
        </label>
        <label style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
          <input type="radio" name="level" value="high"> High compression — smallest size, lower quality
        </label>
        <label style="display:flex; align-items:center; gap:8px;">
          <input type="radio" name="level" value="target"> Custom target size
        </label>
        <div id="targetSizeWrap" style="display:none; margin-top:10px; margin-left:26px;">
          <input type="number" id="targetSizeInput" min="1" step="1" placeholder="e.g. 200" style="width:120px; padding:8px; border:1px solid var(--border); border-radius:6px; font-size:.95rem;"> <span id="targetUnitLabel">KB</span>
          <p style="color:var(--ink-soft); font-size:.8rem; margin-top:6px;">We'll search for the highest quality that fits under this size. Very small targets may not be reachable while keeping pages readable — you'll get the smallest size we could manage instead.</p>
        </div>
      </div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="compressBtn">Compress PDF</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Compressing...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your compressed PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="compressed.pdf">Download compressed.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Compress another file</button></div>
    </div>

    <div class="continue-box" id="continueBox" style="display:none;">
      <p class="continue-title">Continue to&hellip;</p>
      <div class="continue-grid" id="continueGrid"></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your files never leave your device — everything is processed locally in your browser.
    </p>

    <section class="info-section">
      <h2>How PDF compression works here</h2>
      <p>This tool re-renders each page as an optimized image and rebuilds the PDF around it, which is very effective at shrinking scanned documents and image-heavy PDFs. Because of this, text in the compressed file will no longer be selectable or searchable — if you need to keep editable/searchable text, use a lighter compression level or skip compression for text-only documents.</p>
    </section>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>vendor/pdf.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/compress-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
