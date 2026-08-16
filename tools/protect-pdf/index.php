<?php
$root = '../../';
$page_title = 'Protect PDF Online Free — Add Password to PDF | Daily1Step PDF';
$page_description = 'Protect your PDF with a password and encryption, free and online. Set user password and permissions. Processed entirely in your browser — your files never leave your device.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Protect PDF</h1>
      <p>Encrypt your PDF and add password protection to prevent unauthorized access.</p>
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
        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Set password to open PDF</label>
        <input type="password" id="userPw" placeholder="Enter password (e.g. MySecret123)" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px; margin-bottom:14px;">

        <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Confirm password</label>
        <input type="password" id="confirmPw" placeholder="Confirm your password" style="width:100%; padding:10px; border:1px solid var(--border); border-radius:6px; margin-bottom:14px;">

        <p id="pwMismatch" style="color:var(--red); font-size:.82rem; margin-top:-8px; margin-bottom:14px; display:none;">Passwords do not match. Please check and try again.</p>

        <div style="margin-top:10px; padding:12px; background:var(--bg-soft); border-radius:6px; border:1px solid var(--border);">
          <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:8px;">Additional Security Permissions</label>
          <label style="display:flex; align-items:center; gap:8px; font-size:.85rem; margin-bottom:6px; cursor:pointer;">
            <input type="checkbox" id="allowPrinting" checked> Allow printing
          </label>
          <label style="display:flex; align-items:center; gap:8px; font-size:.85rem; margin-bottom:6px; cursor:pointer;">
            <input type="checkbox" id="allowCopying" checked> Allow text & image copying
          </label>
          <label style="display:flex; align-items:center; gap:8px; font-size:.85rem; cursor:pointer;">
            <input type="checkbox" id="allowModifying"> Allow editing / modifying
          </label>
        </div>
      </div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="protectBtn">Protect PDF</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Working...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your protected PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="protected.pdf">Download protected.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Protect another file</button></div>
    </div>

    <div class="continue-box" id="continueBox" style="display:none;">
      <p class="continue-title">Continue to&hellip;</p>
      <div class="continue-grid" id="continueGrid"></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your files and passwords never leave your device — encryption happens 100% locally in your browser.
    </p>

    <section class="info-section">
      <h2>How to password protect a PDF</h2>
      <ol>
        <li>Upload your PDF file.</li>
        <li>Type the password you want to protect the file with, and confirm it.</li>
        <li>Optionally customize printing and copying permissions.</li>
        <li>Click <strong>Protect PDF</strong> and download your encrypted document.</li>
      </ol>
    </section>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib-plus-encrypt.min.js"></script>
<script src="<?php echo $root; ?>vendor/pdf.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/protect-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
