<?php
$root = '../../';
$page_title = 'Add Page Numbers to PDF Online Free | Daily1Step PDF';
$page_description = 'Add page numbers to every page of your PDF, free and online. Choose position, format and starting number. Processed entirely in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Add Page Numbers</h1>
      <p>Number every page of your PDF, with the position and format you choose.</p>
    </div>

    <div class="handoff-banner" id="handoffBanner">
      <span>&#10003;</span> <span id="handoffBannerText"></span>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="application/pdf">
      <p><strong>Click to select a PDF file</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">One file at a time</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:520px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="pageCount"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="margin-top:20px;">
        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Position</label>
        <select id="pnPosition" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px; margin-bottom:14px;">
          <option value="bottom-center" selected>Bottom center</option>
          <option value="bottom-right">Bottom right</option>
          <option value="bottom-left">Bottom left</option>
          <option value="top-center">Top center</option>
          <option value="top-right">Top right</option>
          <option value="top-left">Top left</option>
        </select>

        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Format</label>
        <select id="pnFormat" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px; margin-bottom:14px;">
          <option value="n" selected>1, 2, 3&hellip;</option>
          <option value="page-n">Page 1, Page 2&hellip;</option>
          <option value="n-of-total">1 / N</option>
          <option value="page-n-of-total">Page 1 of N</option>
        </select>

        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Start at</label>
        <input type="number" id="pnStart" value="1" min="0" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px; margin-bottom:14px;">

        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Font size</label>
        <input type="number" id="pnSize" value="11" min="6" max="36" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px;">
      </div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="applyBtn">Add Page Numbers</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Working...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your numbered PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="numbered.pdf">Download numbered.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Number another file</button></div>
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
      <h2>How to add page numbers</h2>
      <ol>
        <li>Upload your PDF.</li>
        <li>Choose the position, format and starting number.</li>
        <li>Click <strong>Add Page Numbers</strong> and download the result.</li>
      </ol>
    </section>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/page-numbers.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
