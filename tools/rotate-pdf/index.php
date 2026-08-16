<?php
$root = '../../';
$page_title = 'Rotate PDF Online Free — Rotate PDF Pages | Daily1Step PDF';
$page_description = 'Rotate all or specific pages of a PDF, free and online. Processed entirely in your browser — no quality loss.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Rotate PDF</h1>
      <p>Rotate individual pages or the whole document. No quality loss — only the page orientation changes.</p>
    </div>

    <div class="handoff-banner" id="handoffBanner">
      <span>&#10003;</span> <span id="handoffBannerText"></span>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="application/pdf">
      <p><strong>Click to select a PDF file</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">One file at a time</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="pageCount"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="margin:14px 0; display:flex; gap:10px;">
        <button class="btn secondary" id="rotateAllLeft">&#8634; Rotate all left</button>
        <button class="btn secondary" id="rotateAllRight">&#8635; Rotate all right</button>
      </div>
      <p style="color:var(--ink-soft); font-size:.82rem; margin-top:-6px;">Or hover a page below and use its own rotate buttons.</p>

      <div class="thumb-grid" id="pageThumbGrid" style="display:none; margin-top:14px;"></div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="rotateBtn">Rotate PDF</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Rotating...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your rotated PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="rotated.pdf">Download rotated.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Rotate another file</button></div>
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
      <h2>How to rotate a PDF</h2>
      <ol>
        <li>Upload your PDF — every page shows as a thumbnail.</li>
        <li>Use "Rotate all" for the whole document, or hover a page and click its own rotate arrows.</li>
        <li>Click <strong>Rotate PDF</strong> and download the result.</li>
      </ol>
    </section>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>vendor/pdf.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/rotate-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
